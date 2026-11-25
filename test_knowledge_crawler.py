"""Automated verification tests for coursera_knowledge_crawler.py."""

import json
import tempfile
from pathlib import Path
from playwright.sync_api import sync_playwright

import coursera_knowledge_crawler as k


def test_url_filters_and_title_cleaning():
    slug = "developing-applications-with-sql-databases-and-django"
    assert k.is_knowledge_url(f"https://www.coursera.org/learn/{slug}/lecture/abc12/intro", slug)
    assert k.is_knowledge_url(f"https://www.coursera.org/learn/{slug}/supplement/def34/summary", slug)
    assert not k.is_knowledge_url(f"https://www.coursera.org/learn/{slug}/assignment-submission/xyz/quiz", slug)
    assert not k.is_knowledge_url(f"https://www.coursera.org/learn/{slug}/quiz/xyz/practice", slug)
    assert not k.is_knowledge_url(f"https://www.coursera.org/learn/{slug}/ungradedLti/xyz/lab", slug)
    assert not k.is_knowledge_url(f"https://www.coursera.org/learn/{slug}/peer/xyz/final-project", slug)

    cleaned = k.clean_item_title("Relational Databases Video . Duration: 7 minutes 7 min", "https://x/y")
    assert cleaned == "Relational Databases", cleaned


def test_vtt_parser():
    vtt = """WEBVTT

1
00:00:00.000 --> 00:00:03.000
Welcome to Django Application Development.

2
00:00:03.000 --> 00:00:06.000
In this video, we learn about <i>ORM</i>.
"""
    txt = k.parse_vtt_to_text(vtt)
    assert "Welcome to Django Application Development." in txt
    assert "In this video, we learn about ORM." in txt
    assert "-->" not in txt


def test_dom_extractors_and_outputs():
    video_html = """
    <html><body><main>
      <h1 class="video-name">Relational Databases</h1>
      <div class="rc-Transcript">
        <div class="rc-Paragraph">
          <span class="timestamp">0:00</span>
          <span class="rc-Phrase">Welcome to this video on relational databases.</span>
          <span class="rc-Phrase">A relational database stores data in tables.</span>
        </div>
        <div class="rc-Paragraph">
          <span class="timestamp">0:15</span>
          <span class="rc-Phrase">Each table consists of rows and columns.</span>
        </div>
      </div>
    </main></body></html>
    """

    reading_html = """
    <html><body><main>
      <div class="rc-ReadingItem">
        <h1>Module 1 Cheat Sheet</h1>
        <div class="rc-CML">
          <h2>Basic SQL Commands</h2>
          <p>Use <code>SELECT</code> to query rows from a table.</p>
          <pre>SELECT * FROM students WHERE id = 1;</pre>
          <ul>
            <li>INSERT adds rows</li>
            <li>UPDATE modifies rows</li>
          </ul>
          <table>
            <tr><th>Command</th><th>Purpose</th></tr>
            <tr><td>CREATE</td><td>Create a table</td></tr>
          </table>
        </div>
      </div>
    </main></body></html>
    """

    with sync_playwright() as p:
        browser = p.chromium.launch(channel="msedge", headless=True)
        page = browser.new_page()

        page.set_content(video_html)
        v_res = k.extract_video_transcript(page)
        assert v_res["extraction_method"] == "dom_transcript"
        assert "Welcome to this video on relational databases." in v_res["content"]
        assert "Each table consists of rows and columns." in v_res["content"]

        page.set_content(reading_html)
        r_res = k.extract_reading_content(page)
        assert r_res["extraction_method"] == "dom_reading_cml"
        assert "### Basic SQL Commands" in r_res["content"]
        assert "SELECT * FROM students WHERE id = 1;" in r_res["content"]
        assert "| Command | Purpose |" in r_res["content"]

        browser.close()

    with tempfile.TemporaryDirectory() as tmp:
        out_dir = Path(tmp)
        jp, mp = k.save_knowledge_outputs(
            out_dir,
            {"key": "coursera1", **k.COURSES["coursera1"]},
            [
                {
                    "module_number": 1,
                    "module_title": "Getting Started with SQL",
                    "type": "video",
                    "title": "Relational Databases",
                    "url": "https://www.coursera.org/learn/developing-applications-with-sql-databases-and-django/lecture/abc/relational",
                    "page_title": v_res["page_title"],
                    "extraction_method": v_res["extraction_method"],
                    "char_count": len(v_res["content"]),
                    "content": v_res["content"],
                },
                {
                    "module_number": 1,
                    "module_title": "Getting Started with SQL",
                    "type": "reading",
                    "title": "Module 1 Cheat Sheet",
                    "url": "https://www.coursera.org/learn/developing-applications-with-sql-databases-and-django/supplement/def/cheat-sheet",
                    "page_title": r_res["page_title"],
                    "extraction_method": r_res["extraction_method"],
                    "char_count": len(r_res["content"]),
                    "content": r_res["content"],
                },
            ],
        )
        assert jp.exists() and mp.exists()
        assert (out_dir / "modules" / "module_01.md").exists()
        data = json.loads(jp.read_text(encoding="utf-8"))
        assert data["total_items_extracted"] == 2
        assert data["total_videos"] == 1
        assert data["total_readings"] == 1


if __name__ == "__main__":
    test_url_filters_and_title_cleaning()
    test_vtt_parser()
    test_dom_extractors_and_outputs()
    print("ALL KNOWLEDGE CRAWLER TESTS PASSED!")

"""Automated verification tests for coursera_quiz_crawler.py."""

import json
import tempfile
from pathlib import Path
from playwright.sync_api import sync_playwright

import coursera_quiz_crawler as c


def test_courses_catalog():
    assert len(c.COURSES) == 7
    assert c.COURSES["coursera1"]["slug"] == "developing-applications-with-sql-databases-and-django"


def test_url_filtering_and_normalization():
    slug = "developing-applications-with-sql-databases-and-django"
    assert c.is_candidate_quiz_url(f"https://www.coursera.org/learn/{slug}/quiz/abc12/practice-quiz", slug)
    assert c.is_candidate_quiz_url(f"https://www.coursera.org/learn/{slug}/exam/def34/graded-exam", slug)
    assert c.is_candidate_quiz_url(
        f"https://www.coursera.org/learn/{slug}/assignment-submission/E0uwq/graded-quiz/attempt", slug
    )
    assert not c.is_candidate_quiz_url(f"https://www.coursera.org/learn/{slug}/lecture/xyz/video", slug)
    assert not c.is_candidate_quiz_url(f"https://www.coursera.org/learn/{slug}/supplement/xyz/reading", slug)
    assert not c.is_candidate_quiz_url(f"https://www.coursera.org/learn/{slug}/ungradedLti/xyz/lab", slug)
    assert not c.is_candidate_quiz_url(f"https://www.coursera.org/learn/{slug}/peer/xyz/project", slug)

    norm = c.normalize_quiz_url(
        f"https://www.coursera.org/learn/{slug}/assignment-submission/E0uwq/graded-quiz/attempt?foo=bar"
    )
    assert norm == f"https://www.coursera.org/learn/{slug}/assignment-submission/E0uwq/graded-quiz"


def test_dom_extraction_and_output():
    standard_html = """
    <html><body><main>
    <h1>Graded Quiz: Introduction to Databases</h1>
    <div data-testid="part-Submission_MultipleChoiceQuestion">
      <div data-testid="cml-viewer">1. Which of the following best describes the role of a database?</div>
      <div role="radiogroup">
        <label><input type="radio" name="q1"> A physical device for storing data</label>
        <label><input type="radio" name="q1" checked> A collection of related tables</label>
        <label><input type="radio" name="q1"> A programming language</label>
      </div>
    </div>
    <div data-testid="part-Submission_CheckboxQuestion">
      <div data-testid="cml-viewer">2. Select all ACID properties.</div>
      <div role="group">
        <label><input type="checkbox" name="q2"> Atomicity</label>
        <label><input type="checkbox" name="q2"> Consistency</label>
        <label><input type="checkbox" name="q2"> Rendering</label>
      </div>
    </div>
    <label><input type="checkbox"> I understand that submitting work that is not my own (Honor Code)</label>
    </main></body></html>
    """

    aria_html = """
    <html><body><main>
    <h1>Practice Quiz: ARIA Format</h1>
    <div role="radiogroup">
      <p>1. What does SQL stand for?</p>
      <div role="radio" aria-checked="true">Structured Query Language</div>
      <div role="radio" aria-checked="false">Simple Queue Language</div>
    </div>
    </main></body></html>
    """

    non_mc_html = """
    <html><body><main>
    <h1>Peer-Graded Assignment</h1>
    <p>Upload your GitHub repository URL below.</p>
    <textarea></textarea>
    </main></body></html>
    """

    with sync_playwright() as p:
        browser = p.chromium.launch(channel="msedge", headless=True)
        page = browser.new_page()

        # Standard Coursera DOM
        page.set_content(standard_html)
        res1 = c.extract_mc_questions(page)
        assert res1["question_count"] == 2
        assert res1["questions"][0]["question_type"] == "single_choice"
        assert res1["questions"][0]["options"][1]["checked"] is True
        assert res1["questions"][1]["question_type"] == "multiple_select"
        assert len(res1["questions"][1]["options"]) == 3

        # ARIA fallback DOM
        page.set_content(aria_html)
        res2 = c.extract_mc_questions(page)
        assert res2["question_count"] == 1
        assert res2["questions"][0]["options"][0]["checked"] is True

        # Non-MC page
        page.set_content(non_mc_html)
        res3 = c.extract_mc_questions(page)
        assert res3["question_count"] == 0

        browser.close()

    # Verify JSON + TXT output generation
    with tempfile.TemporaryDirectory() as tmp:
        out_dir = Path(tmp)
        json_path, txt_path = c.save_outputs(
            out_dir,
            {"key": "coursera1", **c.COURSES["coursera1"]},
            [
                {
                    "title": "Graded Quiz: Introduction to Databases",
                    "source": "Module 1",
                    "kind": "graded_quiz",
                    "url": "https://www.coursera.org/learn/developing-applications-with-sql-databases-and-django/assignment-submission/E0uwq/graded-quiz",
                    "final_url": "https://www.coursera.org/learn/developing-applications-with-sql-databases-and-django/assignment-submission/E0uwq/graded-quiz/attempt",
                    "status": "opened_via_button",
                    "question_count": res1["question_count"],
                    "questions": res1["questions"],
                    "raw_page_text": res1["raw_page_text"],
                }
            ],
        )
        assert json_path.exists() and txt_path.exists()
        data = json.loads(json_path.read_text(encoding="utf-8"))
        assert data["total_mc_questions"] == 2
        txt = txt_path.read_text(encoding="utf-8")
        assert "A collection of related tables" in txt
        assert "Atomicity" in txt


if __name__ == "__main__":
    test_courses_catalog()
    test_url_filtering_and_normalization()
    test_dom_extraction_and_output()
    print("ALL CRAWLER VERIFICATION TESTS PASSED!")

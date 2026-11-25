"""
Exports the entire DWP301c Knowledge Codex (all 7 courses, 35 Synthesized Module
Study Guides, and 55 Practice Quizzes / 381 questions) into a standard EPUB 3.0
ebook (`DWP301c_Codex.epub`) for Apple Books on iPhone 7 Plus (100% offline, zero JS).
"""

from __future__ import annotations

import html
import json
import re
import uuid
import zipfile
from pathlib import Path
from typing import Any

from db import DB_PATH, get_connection

APP_DIR = Path(__file__).resolve().parent
DEFAULT_EPUB = APP_DIR / "DWP301c_Codex.epub"

EPUB_CSS = """
body {
  font-family: -apple-system, BlinkMacSystemFont, "Helvetica Neue", sans-serif;
  font-size: 1rem;
  line-height: 1.65;
  margin: 0;
  padding: 0 4px;
}
h1 {
  font-family: Georgia, serif;
  font-size: 1.6em;
  line-height: 1.25;
  margin: 0.4em 0 0.6em;
  border-bottom: 2px solid #1f5bb5;
  padding-bottom: 0.3em;
}
h2 {
  font-family: Georgia, serif;
  font-size: 1.28em;
  margin: 1.4em 0 0.5em;
  color: #1f5bb5;
}
h3 {
  font-size: 1.08em;
  margin: 1.1em 0 0.4em;
}
h4 {
  font-size: 0.98em;
  margin: 0.9em 0 0.3em;
}
blockquote {
  margin: 0.8em 0 1.2em;
  padding: 10px 14px;
  background: #eaf1fc;
  border-left: 3px solid #1f5bb5;
  border-radius: 4px;
}
code {
  font-family: Menlo, Consolas, monospace;
  font-size: 0.86em;
  background: #f1f4f8;
  padding: 1px 4px;
  border-radius: 3px;
}
pre {
  font-family: Menlo, Consolas, monospace;
  font-size: 0.82em;
  line-height: 1.45;
  background: #181d27;
  color: #e8ecf4;
  padding: 10px 12px;
  border-radius: 6px;
  overflow-x: auto;
  white-space: pre-wrap;
  word-break: break-word;
}
pre code {
  background: transparent;
  color: inherit;
  padding: 0;
}
table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.88em;
  margin: 1em 0;
}
th, td {
  border: 1px solid #d7dde6;
  padding: 6px 8px;
  text-align: left;
  vertical-align: top;
}
th {
  background: #f3f5f8;
  font-weight: 700;
}
ul, ol {
  padding-left: 1.3em;
  margin: 0.4em 0 1em;
}
li {
  margin-bottom: 0.35em;
}
.quiz-card {
  border: 1px solid #d7dde6;
  border-radius: 6px;
  padding: 10px 12px;
  margin-bottom: 12px;
}
.quiz-prompt {
  font-weight: 700;
  margin: 0 0 6px;
}
.quiz-ans {
  margin-top: 6px;
  font-size: 0.9em;
  color: #1d7a4c;
  font-weight: 600;
}
.meta {
  font-size: 0.85em;
  color: #5d6778;
  margin-bottom: 1em;
}
"""


def md_inline_to_xhtml(text: str) -> str:
    slots: list[str] = []

    def stash(m: re.Match[str]) -> str:
        slots.append(f"<code>{html.escape(m.group(1))}</code>")
        return f"\x00CODE{len(slots) - 1}\x00"

    protected = re.sub(r"`([^`]+)`", stash, text or "")
    out = html.escape(protected)
    out = re.sub(r"&lt;br\s*/?&gt;", "<br/>", out, flags=re.IGNORECASE)
    out = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", out)
    out = re.sub(r"(^|[^*])\*([^*]+)\*", r"\1<em>\2</em>", out)
    out = re.sub(r"\x00CODE(\d+)\x00", lambda m: slots[int(m.group(1))], out)
    return out


def md_to_xhtml(md: str) -> str:
    lines = (md or "").replace("\r\n", "\n").split("\n")
    out: list[str] = []
    i = 0
    n = len(lines)

    while i < n:
        line = lines[i]
        stripped = line.strip()

        if stripped.startswith("```"):
            code_lines = []
            i += 1
            while i < n and not lines[i].strip().startswith("```"):
                code_lines.append(lines[i])
                i += 1
            i += 1
            out.append(f"<pre><code>{html.escape(chr(10).join(code_lines))}</code></pre>")
            continue

        if stripped.startswith("|") and i + 1 < n and re.match(r"^\|\s*[-:]+", lines[i + 1].strip()):
            def split_row(r: str) -> list[str]:
                return [md_inline_to_xhtml(c.strip()) for c in r.strip().strip("|").split("|")]

            headers = split_row(line)
            i += 2
            rows = []
            while i < n and lines[i].strip().startswith("|"):
                rows.append(split_row(lines[i]))
                i += 1
            th_html = "".join(f"<th>{c}</th>" for c in headers)
            tb_html = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
            out.append(f"<table><thead><tr>{th_html}</tr></thead><tbody>{tb_html}</tbody></table>")
            continue

        h_m = re.match(r"^(#{1,4})\s+(.+)$", stripped)
        if h_m:
            lvl = min(4, len(h_m.group(1)))
            out.append(f"<h{lvl}>{md_inline_to_xhtml(h_m.group(2).strip())}</h{lvl}>")
            i += 1
            continue

        if stripped.startswith(">"):
            q_lines = []
            while i < n and lines[i].strip().startswith(">"):
                q_lines.append(lines[i].strip().lstrip(">").strip())
                i += 1
            out.append(f"<blockquote><p>{md_inline_to_xhtml(' '.join(q_lines))}</p></blockquote>")
            continue

        if re.match(r"^\s*[-*]\s+", line):
            items = []
            while i < n and re.match(r"^\s*[-*]\s+", lines[i]):
                items.append(f"<li>{md_inline_to_xhtml(re.sub(r'^\s*[-*]\s+', '', lines[i]))}</li>")
                i += 1
            out.append(f"<ul>{''.join(items)}</ul>")
            continue

        if re.match(r"^\s*\d+\.\s+", line):
            items = []
            while i < n and re.match(r"^\s*\d+\.\s+", lines[i]):
                items.append(f"<li>{md_inline_to_xhtml(re.sub(r'^\s*\d+\.\s+', '', lines[i]))}</li>")
                i += 1
            out.append(f"<ol>{''.join(items)}</ol>")
            continue

        if not stripped:
            i += 1
            continue

        para = []
        while (
            i < n
            and lines[i].strip()
            and not lines[i].strip().startswith(("```", "|", ">"))
            and not re.match(r"^(#{1,4}\s+|[-*]\s+|\d+\.\s+)", lines[i].strip())
        ):
            para.append(lines[i].strip())
            i += 1
        out.append(f"<p>{md_inline_to_xhtml(' '.join(para))}</p>")

    return "\n".join(out)


def wrap_xhtml(title: str, body_html: str) -> str:
    return f"""<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" lang="vi">
<head>
  <meta charset="utf-8"/>
  <title>{html.escape(title)}</title>
  <link rel="stylesheet" type="text/css" href="styles.css"/>
</head>
<body>
{body_html}
</body>
</html>
"""


def export_epub(output_path: Path | None = None) -> Path:
    out_file = output_path or DEFAULT_EPUB
    conn = get_connection(DB_PATH)
    book_uuid = str(uuid.uuid5(uuid.NAMESPACE_URL, "https://github.com/carwynetic/DWP-source-from-coursera"))

    chapters: list[tuple[str, str, str]] = []  # (filename, title, xhtml_str)
    toc_tree: list[dict[str, Any]] = []

    try:
        courses = conn.execute("SELECT * FROM courses ORDER BY course_order ASC").fetchall()

        # Cover / Intro page
        intro_rows = "".join(
            f"<li><strong>Course {c['course_order']}:</strong> {html.escape(c['name'])} "
            f"({c['total_modules']} modules · {c['total_questions']} quiz Qs)</li>"
            for c in courses
        )
        intro_html = (
            "<h1>DWP301c Codex — Full 7-Course Study Guide</h1>"
            "<p class='meta'>Web Development with Python (FPT University AI · IBM Full Stack Developer)</p>"
            "<p>Tổng hợp đầy đủ 35 Module Study Guides và 381 câu hỏi ôn tập trắc nghiệm từ 7 khóa học Coursera.</p>"
            f"<ul>{intro_rows}</ul>"
        )
        chapters.append(("intro.xhtml", "DWP301c Codex — Overview", wrap_xhtml("Overview", intro_html)))

        for c in courses:
            cid = c["id"]
            c_num = c["course_order"]
            c_title = f"Course {c_num}: {c['short_name']}"
            c_node: dict[str, Any] = {"title": f"Course {c_num}: {c['name']}", "href": "", "children": []}

            mods = conn.execute(
                "SELECT * FROM modules WHERE course_id = ? ORDER BY module_number ASC",
                (cid,),
            ).fetchall()

            for m in mods:
                m_num = m["module_number"]
                fname = f"c{c_num}_m{m_num}.xhtml"
                if not c_node["href"]:
                    c_node["href"] = fname
                m_title = f"Module {m_num}: {m['title']}"
                body = (
                    f"<p class='meta'>{html.escape(c_title)}</p>"
                    + md_to_xhtml(m["guide_md"])
                )
                chapters.append((fname, m_title, wrap_xhtml(m_title, body)))
                c_node["children"].append({"title": m_title, "href": fname})

            # Quizzes chapter for this course
            qz_rows = conn.execute(
                "SELECT * FROM quizzes WHERE course_id = ? ORDER BY module_number ASC, id ASC",
                (cid,),
            ).fetchall()
            if qz_rows:
                q_fname = f"c{c_num}_quizzes.xhtml"
                q_parts = [f"<p class='meta'>{html.escape(c_title)}</p>", "<h1>Practice &amp; Graded Quizzes</h1>"]
                for qz in qz_rows:
                    q_parts.append(f"<h2>{html.escape(qz['title'])} (Module {qz['module_number']})</h2>")
                    qs = conn.execute(
                        "SELECT * FROM quiz_questions WHERE quiz_id = ? ORDER BY q_index ASC",
                        (qz["id"],),
                    ).fetchall()
                    for q in qs:
                        opts = json.loads(q["options_json"])
                        opt_lis = []
                        correct_letters = []
                        for idx, o in enumerate(opts):
                            letter = chr(65 + idx)
                            opt_lis.append(f"<li><strong>{letter}.</strong> {html.escape(o.get('text', ''))}</li>")
                            if o.get("checked"):
                                correct_letters.append(letter)
                        ans_html = (
                            f"<p class='quiz-ans'>Đáp án tham khảo: {', '.join(correct_letters)}</p>"
                            if correct_letters
                            else ""
                        )
                        q_parts.append(
                            "<div class='quiz-card'>"
                            f"<p class='quiz-prompt'>{q['q_index']}. {html.escape(q['prompt_text'])}</p>"
                            f"<ul style='list-style:none;padding-left:0.4em'>{''.join(opt_lis)}</ul>"
                            f"{ans_html}"
                            "</div>"
                        )
                q_title = f"Course {c_num} Quizzes ({c['total_questions']} Qs)"
                chapters.append((q_fname, q_title, wrap_xhtml(q_title, "\n".join(q_parts))))
                c_node["children"].append({"title": f"Quizzes ({c['total_questions']} Qs)", "href": q_fname})

            toc_tree.append(c_node)
    finally:
        conn.close()

    # Build EPUB 3 nav.xhtml
    nav_items = ["<li><a href='intro.xhtml'>Overview</a></li>"]
    for cn in toc_tree:
        sub = "".join(f"<li><a href='{ch['href']}'>{html.escape(ch['title'])}</a></li>" for ch in cn["children"])
        nav_items.append(f"<li><a href='{cn['href']}'>{html.escape(cn['title'])}</a><ol>{sub}</ol></li>")
    nav_xhtml = wrap_xhtml(
        "Table of Contents",
        f"<nav epub:type='toc' id='toc'><h1>Mục lục DWP301c</h1><ol>{''.join(nav_items)}</ol></nav>",
    )

    # Build OPF manifest & spine
    manifest_items = [
        "<item id='css' href='styles.css' media-type='text/css'/>",
        "<item id='nav' href='nav.xhtml' media-type='application/xhtml+xml' properties='nav'/>",
    ]
    spine_items = []
    for idx, (fname, _, _) in enumerate(chapters):
        cid = f"chap_{idx}"
        manifest_items.append(f"<item id='{cid}' href='{fname}' media-type='application/xhtml+xml'/>")
        spine_items.append(f"<itemref idref='{cid}'/>")

    content_opf = f"""<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="BookId">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:identifier id="BookId">urn:uuid:{book_uuid}</dc:identifier>
    <dc:title>DWP301c Codex — Full 7-Course Study Guide</dc:title>
    <dc:language>vi</dc:language>
    <dc:creator>Carwyn Nguyen</dc:creator>
    <meta property="dcterms:modified">2026-11-25T00:00:00Z</meta>
  </metadata>
  <manifest>
    {''.join(manifest_items)}
  </manifest>
  <spine>
    {''.join(spine_items)}
  </spine>
</package>
"""

    container_xml = """<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles>
    <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
  </rootfiles>
</container>
"""

    with zipfile.ZipFile(out_file, "w") as zf:
        zf.writestr("mimetype", "application/epub+zip", compress_type=zipfile.ZIP_STORED)
        zf.writestr("META-INF/container.xml", container_xml, compress_type=zipfile.ZIP_DEFLATED)
        zf.writestr("OEBPS/styles.css", EPUB_CSS, compress_type=zipfile.ZIP_DEFLATED)
        zf.writestr("OEBPS/content.opf", content_opf, compress_type=zipfile.ZIP_DEFLATED)
        zf.writestr("OEBPS/nav.xhtml", nav_xhtml, compress_type=zipfile.ZIP_DEFLATED)
        for fname, _, xhtml_str in chapters:
            zf.writestr(f"OEBPS/{fname}", xhtml_str, compress_type=zipfile.ZIP_DEFLATED)

    return out_file


if __name__ == "__main__":
    p = export_epub()
    print(f"Exported EPUB: {p} ({p.stat().st_size / 1024:.1f} KB)")

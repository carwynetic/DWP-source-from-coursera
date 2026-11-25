"""
Seeds the SQLite3 + FTS5 database from crawled Coursera knowledge/ and output_question/ folders
along with structured module-by-module Study Guides from web_app/synthesized/.
By default seeds all 7 courses (or pass --course coursera1 ... to seed a subset).
"""

from __future__ import annotations

import argparse
import json
import math
import re
from pathlib import Path

from db import DB_PATH, get_connection, init_db

COURSE_CATALOG = [
    {
        "key": "coursera1",
        "order": 1,
        "slug": "developing-applications-with-sql-databases-and-django",
        "name": "Django Application Development with SQL and Databases",
        "short_name": "SQL & Django",
        "url": "https://www.coursera.org/learn/developing-applications-with-sql-databases-and-django",
    },
    {
        "key": "coursera2",
        "order": 2,
        "slug": "introduction-html-css-javascript",
        "name": "Introduction to HTML, CSS, & JavaScript",
        "short_name": "HTML, CSS & JS",
        "url": "https://www.coursera.org/learn/introduction-html-css-javascript",
    },
    {
        "key": "coursera3",
        "order": 3,
        "slug": "getting-started-with-git-and-github",
        "name": "Getting Started with Git and GitHub",
        "short_name": "Git & GitHub",
        "url": "https://www.coursera.org/learn/getting-started-with-git-and-github",
    },
    {
        "key": "coursera4",
        "order": 4,
        "slug": "developing-frontend-apps-with-react",
        "name": "Developing Front-End Apps with React",
        "short_name": "React & Redux",
        "url": "https://www.coursera.org/learn/developing-frontend-apps-with-react",
    },
    {
        "key": "coursera5",
        "order": 5,
        "slug": "ibm-containers-docker-kubernetes-openshift",
        "name": "Introduction to Containers w/ Docker, Kubernetes & OpenShift",
        "short_name": "Docker & K8s",
        "url": "https://www.coursera.org/learn/ibm-containers-docker-kubernetes-openshift",
    },
    {
        "key": "coursera6",
        "order": 6,
        "slug": "applications-development-microservices-serverless-openshift",
        "name": "Application Development using Microservices and Serverless",
        "short_name": "Microservices",
        "url": "https://www.coursera.org/learn/applications-development-microservices-serverless-openshift",
    },
    {
        "key": "coursera7",
        "order": 7,
        "slug": "ibm-cloud-native-full-stack-development-capstone",
        "name": "Full Stack Application Development Capstone Project",
        "short_name": "Capstone",
        "url": "https://www.coursera.org/learn/ibm-cloud-native-full-stack-development-capstone",
    },
]


def clean_title(raw: str) -> str:
    t = re.sub(r"\s+", " ", (raw or "")).strip()
    t = re.sub(
        r"\s*(Video|Reading|Practice Assignment|Graded Assignment)\s*[•·].*$",
        "",
        t,
        flags=re.IGNORECASE,
    ).strip()
    t = re.sub(r"\s*Grade:\s*.*$", "", t, flags=re.IGNORECASE).strip()
    return t or raw.strip()


def classify_lesson(title: str, item_type: str) -> str:
    low = title.lower()
    if "cheat sheet" in low:
        return "cheat_sheet"
    if "summary" in low or "glossary" in low:
        return "summary"
    return item_type


def is_honor_code_noise(question: dict) -> bool:
    opts = question.get("options", [])
    prompt = (question.get("prompt_text") or "").strip()
    if not prompt and len(opts) == 1:
        txt = (opts[0].get("text") or "").lower()
        if "understand and agree" in txt or "honor code" in txt:
            return True
    return False


def parse_module_num(source_label: str) -> int:
    m = re.search(r"(\d+)", source_label or "")
    return int(m.group(1)) if m else 0


def extract_guide_summary(md: str) -> str:
    """Extract the core takeaway blockquote from a synthesized module guide."""
    for line in md.splitlines():
        s = line.strip()
        if s.startswith(">"):
            cleaned = re.sub(r"^>\s*(\*\*[^*]+\*\*\s*)?", "", s).strip()
            if cleaned:
                return cleaned
    return ""


def normalize_q_key(course_key: str, module_num: int, prompt_text: str) -> str:
    clean = re.sub(r"\s+", " ", (prompt_text or "").replace("\u200b", "").replace("\u00a0", " ")).strip().lower()
    return f"{course_key}|{module_num}|{clean[:180]}"


def seed_database(target_courses: list[str], db_path: Path | None = None) -> None:
    app_dir = Path(__file__).resolve().parent
    source_root = app_dir.parent
    knowledge_root = source_root / "knowledge"
    quiz_root = (
        source_root / "output_question"
        if (source_root / "output_question").exists()
        else source_root / "output"
    )
    synthesized_root = app_dir / "synthesized"

    enhancements_file = app_dir / "quiz_enhancements.json"
    enhancements: dict[str, dict] = {}
    if enhancements_file.exists():
        enhancements = json.loads(enhancements_file.read_text(encoding="utf-8"))

    # Drop and recreate schema cleanly so new columns always exist
    target_db = db_path or DB_PATH
    if target_db.exists():
        target_db.unlink()
    init_db(db_path)
    conn = get_connection(db_path)

    try:
        conn.execute("DELETE FROM lessons_fts;")
        conn.execute("DELETE FROM quiz_questions;")
        conn.execute("DELETE FROM quizzes;")
        conn.execute("DELETE FROM lessons;")
        conn.execute("DELETE FROM modules;")
        conn.execute("DELETE FROM courses;")

        for meta in COURSE_CATALOG:
            cur = conn.execute(
                """
                INSERT INTO courses (key, slug, name, short_name, course_order, url, is_seeded)
                VALUES (?, ?, ?, ?, ?, ?, 0)
                """,
                (meta["key"], meta["slug"], meta["name"], meta["short_name"], meta["order"], meta["url"]),
            )
            course_id = cur.lastrowid

            if meta["key"] not in target_courses:
                continue

            folder_name = f"{meta['key']}_{meta['slug']}"
            k_file = knowledge_root / folder_name / "knowledge.json"
            q_file = quiz_root / folder_name / "raw_quizzes.json"

            total_videos = 0
            total_readings = 0
            total_chars = 0
            module_map: dict[int, int] = {}

            if k_file.exists():
                k_data = json.loads(k_file.read_text(encoding="utf-8"))
                items = k_data.get("items", [])

                for idx, it in enumerate(items, 1):
                    m_num = int(it.get("module_number", 1))
                    m_title = (it.get("module_title") or f"Module {m_num}").strip()
                    if m_num not in module_map:
                        guide_file = synthesized_root / meta["key"] / f"module_{m_num:02d}.md"
                        guide_md = guide_file.read_text(encoding="utf-8").strip() if guide_file.exists() else ""
                        guide_summary = extract_guide_summary(guide_md)
                        guide_chars = len(guide_md)
                        guide_mins = max(1, math.ceil(guide_chars / 1000)) if guide_chars > 0 else 0

                        m_cur = conn.execute(
                            """
                            INSERT INTO modules (course_id, module_number, title, guide_md, guide_summary, guide_chars, guide_read_minutes)
                            VALUES (?, ?, ?, ?, ?, ?, ?)
                            """,
                            (course_id, m_num, m_title, guide_md, guide_summary, guide_chars, guide_mins),
                        )
                        module_map[m_num] = m_cur.lastrowid

                        if guide_md:
                            conn.execute(
                                """
                                INSERT INTO lessons_fts (title, content_md, course_key, lesson_id, module_number, item_type)
                                VALUES (?, ?, ?, ?, ?, ?)
                                """,
                                (f"Module {m_num} Study Guide: {m_title}", guide_md, meta["key"], "0", str(m_num), "guide"),
                            )

                    item_type = it.get("type", "reading")
                    title = clean_title(it.get("title", f"Lesson {idx}"))
                    content = (it.get("content") or "").replace("\u200b", "").strip()
                    char_cnt = len(content)
                    read_min = max(1, math.ceil(char_cnt / 1100))
                    category = classify_lesson(title, item_type)

                    l_cur = conn.execute(
                        """
                        INSERT INTO lessons (
                            course_id, module_id, module_number, item_order,
                            item_type, category, title, url, content_md,
                            char_count, read_minutes
                        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                        """,
                        (
                            course_id,
                            module_map[m_num],
                            m_num,
                            idx,
                            item_type,
                            category,
                            title,
                            it.get("url", ""),
                            content,
                            char_cnt,
                            read_min,
                        ),
                    )
                    lesson_id = l_cur.lastrowid

                    conn.execute(
                        """
                        INSERT INTO lessons_fts (title, content_md, course_key, lesson_id, module_number, item_type)
                        VALUES (?, ?, ?, ?, ?, ?)
                        """,
                        (title, content, meta["key"], str(lesson_id), str(m_num), item_type),
                    )

                    if item_type == "video":
                        total_videos += 1
                    else:
                        total_readings += 1
                    total_chars += char_cnt

            total_quizzes = 0
            total_questions = 0
            if q_file.exists():
                q_data = json.loads(q_file.read_text(encoding="utf-8"))
                for qz in q_data.get("quizzes", []):
                    clean_qs = [q for q in qz.get("questions", []) if not is_honor_code_noise(q)]
                    if not clean_qs:
                        continue
                    m_num = parse_module_num(qz.get("source", ""))
                    qz_cur = conn.execute(
                        """
                        INSERT INTO quizzes (course_id, module_number, source_label, kind, title, url, question_count)
                        VALUES (?, ?, ?, ?, ?, ?, ?)
                        """,
                        (
                            course_id,
                            m_num,
                            qz.get("source", ""),
                            qz.get("kind", "practice_quiz"),
                            clean_title(qz.get("title", "Quiz")),
                            qz.get("url", ""),
                            len(clean_qs),
                        ),
                    )
                    quiz_id = qz_cur.lastrowid
                    for qi, q_item in enumerate(clean_qs, 1):
                        prompt_clean = (q_item.get("prompt_text") or "").replace("\u200b", "").strip()
                        opts = [dict(o) for o in q_item.get("options", [])]
                        q_key = normalize_q_key(meta["key"], m_num, prompt_clean)
                        enh = enhancements.get(q_key, {})
                        if "correct_indices" in enh and enh["correct_indices"]:
                            valid_idx = set(enh["correct_indices"])
                            for oi, opt in enumerate(opts):
                                opt["checked"] = oi in valid_idx
                        explanation = (enh.get("explanation") or "").strip()

                        conn.execute(
                            """
                            INSERT INTO quiz_questions (quiz_id, q_index, question_type, prompt_text, options_json, explanation)
                            VALUES (?, ?, ?, ?, ?, ?)
                            """,
                            (
                                quiz_id,
                                qi,
                                q_item.get("question_type", "single_choice"),
                                prompt_clean,
                                json.dumps(opts, ensure_ascii=False),
                                explanation,
                            ),
                        )
                    total_quizzes += 1
                    total_questions += len(clean_qs)

            conn.execute(
                """
                UPDATE courses
                SET is_seeded = 1,
                    total_modules = ?,
                    total_lessons = ?,
                    total_videos = ?,
                    total_readings = ?,
                    total_quizzes = ?,
                    total_questions = ?,
                    total_chars = ?
                WHERE id = ?
                """,
                (
                    len(module_map),
                    total_videos + total_readings,
                    total_videos,
                    total_readings,
                    total_quizzes,
                    total_questions,
                    total_chars,
                    course_id,
                ),
            )
            print(
                f"Seeded {meta['key']}: {len(module_map)} modules, "
                f"{total_videos + total_readings} lessons ({total_videos}v/{total_readings}r), "
                f"{total_quizzes} quizzes ({total_questions} questions), {total_chars:,} chars"
            )

        conn.commit()
    finally:
        conn.close()


def main() -> None:
    parser = argparse.ArgumentParser(description="Seed DWP301c Knowledge Hub SQLite database")
    parser.add_argument("--course", nargs="+", default=None, help="Course keys to seed (default: all 7 courses)")
    parser.add_argument("--all", action="store_true", help="Seed all 7 courses")
    args = parser.parse_args()

    targets = [c["key"] for c in COURSE_CATALOG] if (args.all or not args.course) else args.course
    seed_database(targets)
    print(f"Database ready at: {DB_PATH}")


if __name__ == "__main__":
    main()

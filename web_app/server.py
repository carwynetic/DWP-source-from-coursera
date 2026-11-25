"""
FastAPI backend for the DWP301c Knowledge Codex web application.
"""

from __future__ import annotations

import html
import json
import re
from pathlib import Path
from typing import Any

from fastapi import FastAPI, HTTPException, Query, Request
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from db import DB_PATH, get_connection, init_db, rows_to_dicts

APP_DIR = Path(__file__).resolve().parent
STATIC_DIR = APP_DIR / "static"

app = FastAPI(
    title="DWP301c Knowledge Codex API",
    version="1.0.0",
    description="Structured knowledge hub and study workbench for DWP301c (7 Coursera IBM courses).",
)


@app.middleware("http")
async def security_headers_middleware(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "SAMEORIGIN"
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    return response


class LessonStatePatch(BaseModel):
    is_completed: bool | None = None
    is_bookmarked: bool | None = None


@app.on_event("startup")
def on_startup() -> None:
    if not DB_PATH.exists():
        init_db()


@app.get("/api/health")
def health_check() -> dict[str, Any]:
    conn = get_connection()
    try:
        courses_seeded = conn.execute("SELECT COUNT(*) FROM courses WHERE is_seeded = 1").fetchone()[0]
        total_lessons = conn.execute("SELECT COUNT(*) FROM lessons").fetchone()[0]
        total_questions = conn.execute("SELECT COUNT(*) FROM quiz_questions").fetchone()[0]
        return {
            "status": "ok",
            "courses_seeded": courses_seeded,
            "total_lessons": total_lessons,
            "total_questions": total_questions,
        }
    finally:
        conn.close()


@app.get("/api/courses")
def list_courses() -> dict[str, Any]:
    conn = get_connection()
    try:
        rows = conn.execute(
            """
            SELECT c.*,
                   COALESCE((SELECT COUNT(*) FROM lessons l WHERE l.course_id = c.id AND l.is_completed = 1), 0) AS completed_lessons,
                   COALESCE((SELECT COUNT(*) FROM lessons l WHERE l.course_id = c.id AND l.is_bookmarked = 1), 0) AS bookmarked_lessons
            FROM courses c
            ORDER BY c.course_order ASC
            """
        ).fetchall()
        return {"courses": rows_to_dicts(rows)}
    finally:
        conn.close()


@app.get("/api/courses/{course_key}")
def get_course_detail(course_key: str) -> dict[str, Any]:
    conn = get_connection()
    try:
        course_row = conn.execute(
            """
            SELECT c.*,
                   COALESCE((SELECT COUNT(*) FROM lessons l WHERE l.course_id = c.id AND l.is_completed = 1), 0) AS completed_lessons,
                   COALESCE((SELECT COUNT(*) FROM lessons l WHERE l.course_id = c.id AND l.is_bookmarked = 1), 0) AS bookmarked_lessons
            FROM courses c
            WHERE c.key = ?
            """,
            (course_key,),
        ).fetchone()
        if not course_row:
            raise HTTPException(status_code=404, detail=f"Course '{course_key}' not found.")

        course = dict(course_row)
        module_rows = conn.execute(
            """
            SELECT id, module_number, title, guide_summary, guide_chars, guide_read_minutes,
                   CASE WHEN length(guide_md) > 0 THEN 1 ELSE 0 END AS has_guide
            FROM modules
            WHERE course_id = ?
            ORDER BY module_number ASC
            """,
            (course["id"],),
        ).fetchall()

        lesson_rows = conn.execute(
            """
            SELECT id, module_id, module_number, item_order, item_type, category,
                   title, url, char_count, read_minutes, is_completed, is_bookmarked
            FROM lessons
            WHERE course_id = ?
            ORDER BY module_number ASC, item_order ASC
            """,
            (course["id"],),
        ).fetchall()

        quiz_counts = {
            r["module_number"]: r["cnt"]
            for r in conn.execute(
                "SELECT module_number, SUM(question_count) AS cnt FROM quizzes WHERE course_id = ? GROUP BY module_number",
                (course["id"],),
            ).fetchall()
        }

        lessons_by_mod: dict[int, list[dict[str, Any]]] = {}
        for lr in lesson_rows:
            d = dict(lr)
            d["is_completed"] = bool(d["is_completed"])
            d["is_bookmarked"] = bool(d["is_bookmarked"])
            lessons_by_mod.setdefault(d["module_number"], []).append(d)

        modules: list[dict[str, Any]] = []
        for mr in module_rows:
            m = dict(mr)
            m["has_guide"] = bool(m["has_guide"])
            mod_lessons = lessons_by_mod.get(m["module_number"], [])
            m["lessons"] = mod_lessons
            m["total_lessons"] = len(mod_lessons)
            m["completed_lessons"] = sum(1 for x in mod_lessons if x["is_completed"])
            m["total_minutes"] = sum(int(x["read_minutes"]) for x in mod_lessons)
            m["quiz_questions"] = int(quiz_counts.get(m["module_number"], 0))
            modules.append(m)

        return {"course": course, "modules": modules}
    finally:
        conn.close()


@app.get("/api/courses/{course_key}/modules/{module_number}")
def get_module_guide(course_key: str, module_number: int) -> dict[str, Any]:
    conn = get_connection()
    try:
        course = conn.execute("SELECT id, key, name, short_name FROM courses WHERE key = ?", (course_key,)).fetchone()
        if not course:
            raise HTTPException(status_code=404, detail=f"Course '{course_key}' not found.")

        mod = conn.execute(
            "SELECT * FROM modules WHERE course_id = ? AND module_number = ?",
            (course["id"], module_number),
        ).fetchone()
        if not mod:
            raise HTTPException(status_code=404, detail=f"Module {module_number} not found in '{course_key}'.")

        lessons = conn.execute(
            """
            SELECT id, item_order, item_type, category, title, url, char_count, read_minutes, is_completed, is_bookmarked
            FROM lessons
            WHERE module_id = ?
            ORDER BY item_order ASC
            """,
            (mod["id"],),
        ).fetchall()

        quiz_q_count = conn.execute(
            "SELECT COALESCE(SUM(question_count), 0) FROM quizzes WHERE course_id = ? AND module_number = ?",
            (course["id"], module_number),
        ).fetchone()[0]

        all_mods = conn.execute(
            "SELECT module_number, title FROM modules WHERE course_id = ? ORDER BY module_number ASC",
            (course["id"],),
        ).fetchall()
        prev_mod = None
        next_mod = None
        for idx, am in enumerate(all_mods):
            if am["module_number"] == module_number:
                if idx > 0:
                    prev_mod = dict(all_mods[idx - 1])
                if idx + 1 < len(all_mods):
                    next_mod = dict(all_mods[idx + 1])
                break

        return {
            "course": dict(course),
            "module": dict(mod),
            "source_lessons": rows_to_dicts(lessons),
            "quiz_questions": int(quiz_q_count),
            "prev_module": prev_mod,
            "next_module": next_mod,
        }
    finally:
        conn.close()


@app.get("/api/lessons/{lesson_id}")
def get_lesson_detail(lesson_id: int) -> dict[str, Any]:
    conn = get_connection()
    try:
        row = conn.execute(
            """
            SELECT l.*, m.title AS module_title, c.key AS course_key, c.name AS course_name
            FROM lessons l
            JOIN modules m ON m.id = l.module_id
            JOIN courses c ON c.id = l.course_id
            WHERE l.id = ?
            """,
            (lesson_id,),
        ).fetchone()
        if not row:
            raise HTTPException(status_code=404, detail=f"Lesson {lesson_id} not found.")

        lesson = dict(row)
        lesson["is_completed"] = bool(lesson["is_completed"])
        lesson["is_bookmarked"] = bool(lesson["is_bookmarked"])

        siblings = conn.execute(
            """
            SELECT id, title, module_number, item_type
            FROM lessons
            WHERE course_id = ?
            ORDER BY module_number ASC, item_order ASC
            """,
            (lesson["course_id"],),
        ).fetchall()

        prev_lesson = None
        next_lesson = None
        for idx, sib in enumerate(siblings):
            if sib["id"] == lesson_id:
                if idx > 0:
                    prev_lesson = dict(siblings[idx - 1])
                if idx + 1 < len(siblings):
                    next_lesson = dict(siblings[idx + 1])
                break

        return {
            "lesson": lesson,
            "prev_lesson": prev_lesson,
            "next_lesson": next_lesson,
        }
    finally:
        conn.close()


@app.patch("/api/lessons/{lesson_id}/state")
def update_lesson_state(lesson_id: int, patch: LessonStatePatch) -> dict[str, Any]:
    conn = get_connection()
    try:
        existing = conn.execute(
            "SELECT id, is_completed, is_bookmarked FROM lessons WHERE id = ?",
            (lesson_id,),
        ).fetchone()
        if not existing:
            raise HTTPException(status_code=404, detail=f"Lesson {lesson_id} not found.")

        new_completed = int(patch.is_completed) if patch.is_completed is not None else existing["is_completed"]
        new_bookmarked = int(patch.is_bookmarked) if patch.is_bookmarked is not None else existing["is_bookmarked"]

        conn.execute(
            "UPDATE lessons SET is_completed = ?, is_bookmarked = ? WHERE id = ?",
            (new_completed, new_bookmarked, lesson_id),
        )
        conn.commit()
        return {
            "id": lesson_id,
            "is_completed": bool(new_completed),
            "is_bookmarked": bool(new_bookmarked),
        }
    finally:
        conn.close()


@app.get("/api/courses/{course_key}/quizzes")
def get_course_quizzes(course_key: str, module_number: int | None = None) -> dict[str, Any]:
    conn = get_connection()
    try:
        course = conn.execute("SELECT id, key, name FROM courses WHERE key = ?", (course_key,)).fetchone()
        if not course:
            raise HTTPException(status_code=404, detail=f"Course '{course_key}' not found.")

        if module_number is not None:
            qz_rows = conn.execute(
                "SELECT * FROM quizzes WHERE course_id = ? AND module_number = ? ORDER BY id ASC",
                (course["id"], module_number),
            ).fetchall()
        else:
            qz_rows = conn.execute(
                "SELECT * FROM quizzes WHERE course_id = ? ORDER BY module_number ASC, id ASC",
                (course["id"],),
            ).fetchall()

        quizzes: list[dict[str, Any]] = []
        for qz in qz_rows:
            qd = dict(qz)
            q_rows = conn.execute(
                "SELECT id, q_index, question_type, prompt_text, options_json FROM quiz_questions WHERE quiz_id = ? ORDER BY q_index ASC",
                (qd["id"],),
            ).fetchall()
            questions = []
            for qr in q_rows:
                questions.append(
                    {
                        "id": qr["id"],
                        "q_index": qr["q_index"],
                        "question_type": qr["question_type"],
                        "prompt_text": qr["prompt_text"],
                        "options": json.loads(qr["options_json"]),
                    }
                )
            qd["questions"] = questions
            quizzes.append(qd)

        return {"course": dict(course), "quizzes": quizzes}
    finally:
        conn.close()


def _sanitize_fts_query(raw_q: str) -> str:
    # Preserve Unicode word characters (including Vietnamese diacritics) while stripping punctuation/operators
    tokens = re.findall(r"[^\W]+", raw_q, flags=re.UNICODE)
    if not tokens:
        return ""
    return " ".join(f'"{t}"*' for t in tokens[:8])


_MARK_OPEN = "\u0001"
_MARK_CLOSE = "\u0002"


def _escape_fts_snippet(raw_snippet: str) -> str:
    escaped = html.escape(raw_snippet or "", quote=True)
    return escaped.replace(_MARK_OPEN, "<mark>").replace(_MARK_CLOSE, "</mark>")


@app.get("/api/search")
def search_knowledge(
    q: str = Query(..., min_length=1, max_length=120),
    course: str | None = None,
    limit: int = Query(20, ge=1, le=50),
) -> dict[str, Any]:
    fts_query = _sanitize_fts_query(q)
    if not fts_query:
        return {"query": q, "results": []}

    conn = get_connection()
    try:
        sql = """
            SELECT
                CAST(lessons_fts.lesson_id AS INTEGER) AS lesson_id,
                lessons_fts.course_key,
                CAST(lessons_fts.module_number AS INTEGER) AS module_number,
                lessons_fts.item_type,
                lessons_fts.title,
                snippet(lessons_fts, 1, ?, ?, ' … ', 26) AS snippet,
                bm25(lessons_fts, 4.0, 1.0) AS rank
            FROM lessons_fts
            WHERE lessons_fts MATCH ?
        """
        params: list[Any] = [_MARK_OPEN, _MARK_CLOSE, fts_query]
        if course:
            sql += " AND lessons_fts.course_key = ?"
            params.append(course)
        sql += " ORDER BY rank ASC LIMIT ?"
        params.append(limit)

        rows = rows_to_dicts(conn.execute(sql, params).fetchall())
        for r in rows:
            r["snippet"] = _escape_fts_snippet(r.get("snippet", ""))
        return {"query": q, "results": rows}
    except Exception:
        return {"query": q, "results": []}
    finally:
        conn.close()


if STATIC_DIR.exists():
    app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")


@app.get("/")
def serve_index():
    index_path = STATIC_DIR / "index.html"
    if not index_path.exists():
        return JSONResponse({"message": "Frontend not built yet."}, status_code=404)
    return FileResponse(str(index_path))

"""
SQLite3 + FTS5 database layer for the DWP301c Knowledge Codex.
Normalized relational schema with full-text search indexing and parameterized queries.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path
from typing import Any

DB_PATH = Path(__file__).resolve().parent / "dwp301c_hub.db"


def get_connection(db_path: Path | None = None) -> sqlite3.Connection:
    path = db_path or DB_PATH
    conn = sqlite3.connect(str(path), check_same_thread=False)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def init_db(db_path: Path | None = None) -> None:
    conn = get_connection(db_path)
    try:
        conn.executescript(
            """
            CREATE TABLE IF NOT EXISTS courses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                key TEXT UNIQUE NOT NULL,
                slug TEXT NOT NULL,
                name TEXT NOT NULL,
                short_name TEXT NOT NULL,
                course_order INTEGER NOT NULL,
                url TEXT NOT NULL,
                is_seeded INTEGER NOT NULL DEFAULT 0,
                total_modules INTEGER NOT NULL DEFAULT 0,
                total_lessons INTEGER NOT NULL DEFAULT 0,
                total_videos INTEGER NOT NULL DEFAULT 0,
                total_readings INTEGER NOT NULL DEFAULT 0,
                total_quizzes INTEGER NOT NULL DEFAULT 0,
                total_questions INTEGER NOT NULL DEFAULT 0,
                total_chars INTEGER NOT NULL DEFAULT 0
            );

            CREATE TABLE IF NOT EXISTS modules (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                course_id INTEGER NOT NULL REFERENCES courses(id) ON DELETE CASCADE,
                module_number INTEGER NOT NULL,
                title TEXT NOT NULL,
                guide_md TEXT NOT NULL DEFAULT '',
                guide_summary TEXT NOT NULL DEFAULT '',
                guide_chars INTEGER NOT NULL DEFAULT 0,
                guide_read_minutes INTEGER NOT NULL DEFAULT 0,
                UNIQUE(course_id, module_number)
            );

            CREATE TABLE IF NOT EXISTS lessons (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                course_id INTEGER NOT NULL REFERENCES courses(id) ON DELETE CASCADE,
                module_id INTEGER NOT NULL REFERENCES modules(id) ON DELETE CASCADE,
                module_number INTEGER NOT NULL,
                item_order INTEGER NOT NULL,
                item_type TEXT NOT NULL CHECK(item_type IN ('video', 'reading')),
                category TEXT NOT NULL DEFAULT 'lesson',
                title TEXT NOT NULL,
                url TEXT NOT NULL,
                content_md TEXT NOT NULL,
                char_count INTEGER NOT NULL DEFAULT 0,
                read_minutes INTEGER NOT NULL DEFAULT 1,
                is_completed INTEGER NOT NULL DEFAULT 0,
                is_bookmarked INTEGER NOT NULL DEFAULT 0,
                UNIQUE(course_id, url)
            );

            CREATE TABLE IF NOT EXISTS quizzes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                course_id INTEGER NOT NULL REFERENCES courses(id) ON DELETE CASCADE,
                module_number INTEGER NOT NULL DEFAULT 0,
                source_label TEXT NOT NULL,
                kind TEXT NOT NULL,
                title TEXT NOT NULL,
                url TEXT NOT NULL,
                question_count INTEGER NOT NULL DEFAULT 0,
                UNIQUE(course_id, url)
            );

            CREATE TABLE IF NOT EXISTS quiz_questions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                quiz_id INTEGER NOT NULL REFERENCES quizzes(id) ON DELETE CASCADE,
                q_index INTEGER NOT NULL,
                question_type TEXT NOT NULL,
                prompt_text TEXT NOT NULL,
                options_json TEXT NOT NULL
            );

            CREATE INDEX IF NOT EXISTS idx_lessons_course_order ON lessons(course_id, module_number, item_order);
            CREATE INDEX IF NOT EXISTS idx_lessons_category ON lessons(course_id, category);
            CREATE INDEX IF NOT EXISTS idx_quizzes_course_mod ON quizzes(course_id, module_number);

            CREATE VIRTUAL TABLE IF NOT EXISTS lessons_fts USING fts5(
                title,
                content_md,
                course_key UNINDEXED,
                lesson_id UNINDEXED,
                module_number UNINDEXED,
                item_type UNINDEXED,
                tokenize='porter unicode61'
            );
            """
        )
        conn.commit()
    finally:
        conn.close()


def rows_to_dicts(rows: list[sqlite3.Row]) -> list[dict[str, Any]]:
    return [dict(r) for r in rows]

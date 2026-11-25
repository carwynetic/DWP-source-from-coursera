"""
Exports the entire DWP301c Knowledge Codex (all 7 courses, 35 Study Guides,
241 source lessons, and 55 quizzes / 381 questions) from dwp301c_hub.db into
a single self-contained offline HTML file (`DWP301c_Offline.html`).

Designed for 100% offline use on iPhone 7 Plus (iOS 15.8.x) and desktop:
  - Hex/RGB CSS fallbacks before oklch() for Safari 15 compatibility
  - No external network requests (Google Fonts removed, system UI + Georgia + SF Mono stacks)
  - Full client-side Unicode search & localStorage progress/bookmark persistence
  - Mobile bottom-accessible mode switcher bar for <= 900px viewports
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from db import DB_PATH, get_connection

APP_DIR = Path(__file__).resolve().parent
STATIC_DIR = APP_DIR / "static"
DEFAULT_OUTPUT = APP_DIR / "DWP301c_Offline.html"

# Hex/RGB fallback tokens for Safari 15.8 (iPhone 7 Plus) which lacks oklch()
IOS15_FALLBACK_CSS = """
/* === iOS 15.8 / Safari < 16.2 Hex Fallbacks === */
:root {
  --bg: #ffffff;
  --surface: #f3f5f8;
  --surface-hover: #eaeef4;
  --surface-elevated: #f9fafc;
  --border: #d7dde6;
  --border-subtle: #e7ebf1;
  --ink: #1e2430;
  --ink-secondary: #3b4454;
  --muted: #5d6778;
  --primary: #1f5bb5;
  --primary-hover: #174996;
  --primary-soft: #eaf1fc;
  --primary-border: #adc6eb;
  --on-primary: #ffffff;
  --accent: #b85d19;
  --accent-soft: #fdf0e6;
  --on-accent: #ffffff;
  --success: #1d7a4c;
  --success-soft: #e9f6ef;
  --danger: #c4312b;
  --danger-soft: #fceceb;
  --code-bg: #f1f4f8;
  --code-block-bg: #181d27;
  --code-block-ink: #e8ecf4;
  --shadow-sm: 0 1px 2px rgba(20, 30, 50, 0.06);
  --shadow-md: 0 8px 24px -4px rgba(20, 30, 50, 0.10), 0 2px 6px rgba(20, 30, 50, 0.05);
  --shadow-lg: 0 20px 48px -8px rgba(20, 30, 50, 0.18), 0 4px 12px rgba(20, 30, 50, 0.08);
}

[data-theme="dark"] {
  --bg: #0f1115;
  --surface: #171b22;
  --surface-hover: #212732;
  --surface-elevated: #1c212b;
  --border: #2e3645;
  --border-subtle: #242b37;
  --ink: #eef1f6;
  --ink-secondary: #c5ccd8;
  --muted: #939cad;
  --primary: #5c96f5;
  --primary-hover: #76a8f8;
  --primary-soft: #1b2840;
  --primary-border: #324e7d;
  --on-primary: #ffffff;
  --accent: #e08a42;
  --accent-soft: #2e2016;
  --on-accent: #14100c;
  --success: #3fb97a;
  --success-soft: #162b20;
  --danger: #eb6b65;
  --danger-soft: #311a19;
  --code-bg: #1e2430;
  --code-block-bg: #13161d;
  --code-block-ink: #e5e9f2;
  --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.35);
  --shadow-md: 0 10px 28px -4px rgba(0, 0, 0, 0.45);
  --shadow-lg: 0 24px 56px -8px rgba(0, 0, 0, 0.65);
}
"""

MOBILE_MODE_BAR_CSS = """
/* === Offline Mobile Mode Bar (iPhone 7 Plus <= 900px) === */
.mobile-mode-bar {
  display: none;
}

@media (max-width: 900px) {
  .mobile-mode-bar {
    display: flex;
    align-items: center;
    gap: 4px;
    padding: 6px 10px;
    background: var(--surface);
    border-bottom: 1px solid var(--border-subtle);
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
    position: sticky;
    top: var(--topbar-h);
    z-index: 19;
  }
  .mobile-mode-bar .mode-tab {
    flex: 0 0 auto;
    font-size: 0.78rem;
    padding: 5px 10px;
  }
  .syllabus-rail {
    top: calc(var(--topbar-h) + 41px);
  }
  .main-stage {
    overflow-x: hidden;
    overflow-x: clip;
  }
}
"""

OFFLINE_API_SHIM = r"""
// =========================================================================
// Offline In-Memory Data & localStorage Persistence (Zero Network Required)
// =========================================================================
const __OFFLINE_DB__ = window.__DWP301C_DATA__;
const __STATE_STORAGE_KEY__ = "dwp301c_offline_lesson_state_v1";

function __loadSavedStates() {
  try {
    return JSON.parse(localStorage.getItem(__STATE_STORAGE_KEY__) || "{}");
  } catch (_) {
    return {};
  }
}

function __saveLessonState(lessonId, patch) {
  const all = __loadSavedStates();
  const prev = all[String(lessonId)] || {};
  all[String(lessonId)] = { ...prev, ...patch };
  try {
    localStorage.setItem(__STATE_STORAGE_KEY__, JSON.stringify(all));
  } catch (_) {}
  return all[String(lessonId)];
}

function __getLessonFlags(lesson) {
  const saved = __loadSavedStates()[String(lesson.id)];
  return {
    is_completed: saved && saved.is_completed !== undefined ? Boolean(saved.is_completed) : Boolean(lesson.is_completed),
    is_bookmarked: saved && saved.is_bookmarked !== undefined ? Boolean(saved.is_bookmarked) : Boolean(lesson.is_bookmarked),
  };
}

function __buildCourseSummary(course) {
  const detail = __OFFLINE_DB__.course_details[course.key];
  let completed = 0;
  let bookmarked = 0;
  if (detail) {
    for (const mod of detail.modules) {
      for (const l of mod.lessons) {
        const flags = __getLessonFlags(l);
        if (flags.is_completed) completed++;
        if (flags.is_bookmarked) bookmarked++;
      }
    }
  }
  return { ...course, completed_lessons: completed, bookmarked_lessons: bookmarked };
}

function __escapeHtmlStr(s) {
  return String(s || "")
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

function __escapeRegex(s) {
  return s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}

function __offlineSearch(rawQuery, courseKey, limit) {
  const tokens = String(rawQuery || "")
    .trim()
    .toLowerCase()
    .split(/\s+/)
    .filter(Boolean)
    .slice(0, 8);
  if (tokens.length === 0) return { query: rawQuery, results: [] };

  const docs = __OFFLINE_DB__.search_docs.filter((d) => !courseKey || d.course_key === courseKey);
  const scored = [];
  for (const doc of docs) {
    const hayTitle = doc.title_low;
    const hayBody = doc.body_low;
    let allMatch = true;
    let score = 0;
    let firstPos = -1;
    for (const tk of tokens) {
      const inTitle = hayTitle.includes(tk);
      const bodyIdx = hayBody.indexOf(tk);
      if (!inTitle && bodyIdx === -1) {
        allMatch = false;
        break;
      }
      if (inTitle) score += 6;
      if (bodyIdx !== -1) {
        score += 2;
        if (firstPos === -1 || bodyIdx < firstPos) firstPos = bodyIdx;
      }
    }
    if (!allMatch) continue;

    const start = Math.max(0, (firstPos === -1 ? 0 : firstPos) - 60);
    const end = Math.min(doc.body_raw.length, start + 210);
    let rawSlice = doc.body_raw.slice(start, end).replace(/\s+/g, " ").trim();
    if (start > 0) rawSlice = "… " + rawSlice;
    if (end < doc.body_raw.length) rawSlice = rawSlice + " …";

    let safeSnippet = __escapeHtmlStr(rawSlice);
    const pattern = new RegExp(`(${tokens.map(__escapeRegex).join("|")})`, "gi");
    safeSnippet = safeSnippet.replace(pattern, "<mark>$1</mark>");

    scored.push({
      score,
      lesson_id: doc.lesson_id,
      course_key: doc.course_key,
      module_number: doc.module_number,
      item_type: doc.item_type,
      title: doc.title,
      snippet: safeSnippet,
    });
  }
  scored.sort((a, b) => b.score - a.score);
  return { query: rawQuery, results: scored.slice(0, limit || 18) };
}

async function api(path, options = {}) {
  const url = new URL(path, "http://offline.local");
  const p = url.pathname;
  const method = (options.method || "GET").toUpperCase();

  if (p === "/api/courses") {
    return { courses: __OFFLINE_DB__.courses.map(__buildCourseSummary) };
  }

  let m = p.match(/^\/api\/courses\/([^/]+)$/);
  if (m) {
    const key = decodeURIComponent(m[1]);
    const detail = __OFFLINE_DB__.course_details[key];
    if (!detail) throw new Error(`Course '${key}' not found.`);
    const course = __buildCourseSummary(__OFFLINE_DB__.courses.find((c) => c.key === key));
    const modules = detail.modules.map((mod) => {
      const lessons = mod.lessons.map((l) => ({ ...l, ...__getLessonFlags(l) }));
      return {
        ...mod,
        lessons,
        completed_lessons: lessons.filter((x) => x.is_completed).length,
      };
    });
    return { course, modules };
  }

  m = p.match(/^\/api\/courses\/([^/]+)\/modules\/(\d+)$/);
  if (m) {
    const key = decodeURIComponent(m[1]);
    const modNum = Number(m[2]);
    const pack = __OFFLINE_DB__.module_guides[`${key}:${modNum}`];
    if (!pack) throw new Error(`Module ${modNum} not found in '${key}'.`);
    return {
      ...pack,
      source_lessons: pack.source_lessons.map((l) => ({ ...l, ...__getLessonFlags(l) })),
    };
  }

  m = p.match(/^\/api\/lessons\/(\d+)$/);
  if (m) {
    const lid = Number(m[1]);
    const pack = __OFFLINE_DB__.lessons[String(lid)];
    if (!pack) throw new Error(`Lesson ${lid} not found.`);
    return {
      ...pack,
      lesson: { ...pack.lesson, ...__getLessonFlags(pack.lesson) },
    };
  }

  m = p.match(/^\/api\/lessons\/(\d+)\/state$/);
  if (m && method === "PATCH") {
    const lid = Number(m[1]);
    const patch = JSON.parse(options.body || "{}");
    const saved = __saveLessonState(lid, patch);
    return {
      id: lid,
      is_completed: Boolean(saved.is_completed),
      is_bookmarked: Boolean(saved.is_bookmarked),
    };
  }

  m = p.match(/^\/api\/courses\/([^/]+)\/quizzes$/);
  if (m) {
    const key = decodeURIComponent(m[1]);
    const qpack = __OFFLINE_DB__.quizzes[key];
    if (!qpack) throw new Error(`Quizzes for '${key}' not found.`);
    return qpack;
  }

  if (p === "/api/search") {
    const q = url.searchParams.get("q") || "";
    const course = url.searchParams.get("course") || "";
    const limit = Number(url.searchParams.get("limit") || 18);
    return __offlineSearch(q, course, limit);
  }

  throw new Error(`Unsupported offline route: ${path}`);
}
"""


def build_offline_payload() -> dict[str, Any]:
    conn = get_connection(DB_PATH)
    try:
        courses = [dict(r) for r in conn.execute("SELECT * FROM courses ORDER BY course_order ASC").fetchall()]
        course_details: dict[str, Any] = {}
        module_guides: dict[str, Any] = {}
        lessons_map: dict[str, Any] = {}
        quizzes_map: dict[str, Any] = {}
        search_docs: list[dict[str, Any]] = []

        for c in courses:
            cid = c["id"]
            ckey = c["key"]
            mod_rows = [
                dict(r)
                for r in conn.execute(
                    "SELECT * FROM modules WHERE course_id = ? ORDER BY module_number ASC",
                    (cid,),
                ).fetchall()
            ]
            lesson_rows = [
                dict(r)
                for r in conn.execute(
                    "SELECT * FROM lessons WHERE course_id = ? ORDER BY module_number ASC, item_order ASC",
                    (cid,),
                ).fetchall()
            ]
            quiz_counts = {
                r["module_number"]: int(r["cnt"])
                for r in conn.execute(
                    "SELECT module_number, SUM(question_count) AS cnt FROM quizzes WHERE course_id = ? GROUP BY module_number",
                    (cid,),
                ).fetchall()
            }

            lessons_by_mod: dict[int, list[dict[str, Any]]] = {}
            for idx, lr in enumerate(lesson_rows):
                lr["is_completed"] = bool(lr["is_completed"])
                lr["is_bookmarked"] = bool(lr["is_bookmarked"])
                # Lightweight summary entry for syllabus list
                summary_entry = {
                    k: lr[k]
                    for k in (
                        "id",
                        "module_id",
                        "module_number",
                        "item_order",
                        "item_type",
                        "category",
                        "title",
                        "url",
                        "char_count",
                        "read_minutes",
                        "is_completed",
                        "is_bookmarked",
                    )
                }
                lessons_by_mod.setdefault(lr["module_number"], []).append(summary_entry)

                prev_l = (
                    {k: lesson_rows[idx - 1][k] for k in ("id", "title", "module_number", "item_type")}
                    if idx > 0
                    else None
                )
                next_l = (
                    {k: lesson_rows[idx + 1][k] for k in ("id", "title", "module_number", "item_type")}
                    if idx + 1 < len(lesson_rows)
                    else None
                )
                mod_title = next((m["title"] for m in mod_rows if m["module_number"] == lr["module_number"]), "")
                lessons_map[str(lr["id"])] = {
                    "lesson": {**lr, "module_title": mod_title, "course_key": ckey, "course_name": c["name"]},
                    "prev_lesson": prev_l,
                    "next_lesson": next_l,
                }

                plain_body = re.sub(r"[`*_#|>-]+", " ", lr["content_md"])
                search_docs.append(
                    {
                        "lesson_id": lr["id"],
                        "course_key": ckey,
                        "module_number": lr["module_number"],
                        "item_type": lr["item_type"],
                        "title": lr["title"],
                        "title_low": lr["title"].lower(),
                        "body_raw": plain_body,
                        "body_low": plain_body.lower(),
                    }
                )

            detail_modules = []
            for m_idx, mr in enumerate(mod_rows):
                m_num = mr["module_number"]
                m_lessons = lessons_by_mod.get(m_num, [])
                detail_modules.append(
                    {
                        "id": mr["id"],
                        "module_number": m_num,
                        "title": mr["title"],
                        "guide_summary": mr["guide_summary"],
                        "guide_chars": mr["guide_chars"],
                        "guide_read_minutes": mr["guide_read_minutes"],
                        "has_guide": bool(len(mr["guide_md"]) > 0),
                        "lessons": m_lessons,
                        "total_lessons": len(m_lessons),
                        "completed_lessons": 0,
                        "total_minutes": sum(int(x["read_minutes"]) for x in m_lessons),
                        "quiz_questions": quiz_counts.get(m_num, 0),
                    }
                )

                prev_m = (
                    {"module_number": mod_rows[m_idx - 1]["module_number"], "title": mod_rows[m_idx - 1]["title"]}
                    if m_idx > 0
                    else None
                )
                next_m = (
                    {"module_number": mod_rows[m_idx + 1]["module_number"], "title": mod_rows[m_idx + 1]["title"]}
                    if m_idx + 1 < len(mod_rows)
                    else None
                )
                module_guides[f"{ckey}:{m_num}"] = {
                    "course": {"id": cid, "key": ckey, "name": c["name"], "short_name": c["short_name"]},
                    "module": mr,
                    "source_lessons": m_lessons,
                    "quiz_questions": quiz_counts.get(m_num, 0),
                    "prev_module": prev_m,
                    "next_module": next_m,
                }

                if mr["guide_md"]:
                    g_title = f"Module {m_num} Study Guide: {mr['title']}"
                    plain_guide = re.sub(r"[`*_#|>-]+", " ", mr["guide_md"])
                    search_docs.append(
                        {
                            "lesson_id": 0,
                            "course_key": ckey,
                            "module_number": m_num,
                            "item_type": "guide",
                            "title": g_title,
                            "title_low": g_title.lower(),
                            "body_raw": plain_guide,
                            "body_low": plain_guide.lower(),
                        }
                    )

            course_details[ckey] = {"modules": detail_modules}

            qz_rows = [
                dict(r)
                for r in conn.execute(
                    "SELECT * FROM quizzes WHERE course_id = ? ORDER BY module_number ASC, id ASC",
                    (cid,),
                ).fetchall()
            ]
            for qz in qz_rows:
                q_rows = conn.execute(
                    "SELECT id, q_index, question_type, prompt_text, options_json FROM quiz_questions WHERE quiz_id = ? ORDER BY q_index ASC",
                    (qz["id"],),
                ).fetchall()
                qz["questions"] = [
                    {
                        "id": qr["id"],
                        "q_index": qr["q_index"],
                        "question_type": qr["question_type"],
                        "prompt_text": qr["prompt_text"],
                        "options": json.loads(qr["options_json"]),
                    }
                    for qr in q_rows
                ]
            quizzes_map[ckey] = {
                "course": {"id": cid, "key": ckey, "name": c["name"]},
                "quizzes": qz_rows,
            }

        return {
            "courses": courses,
            "course_details": course_details,
            "module_guides": module_guides,
            "lessons": lessons_map,
            "quizzes": quizzes_map,
            "search_docs": search_docs,
        }
    finally:
        conn.close()


def export_offline_html(output_path: Path | None = None) -> Path:
    out_file = output_path or DEFAULT_OUTPUT
    html_src = (STATIC_DIR / "index.html").read_text(encoding="utf-8")
    css_src = (STATIC_DIR / "styles.css").read_text(encoding="utf-8")
    js_src = (STATIC_DIR / "app.js").read_text(encoding="utf-8")

    # 1. Remove external Google Fonts links so offline iOS loads immediately
    html_src = re.sub(r'<link[^>]+fonts\.(googleapis|gstatic)\.com[^>]*>\s*', "", html_src, flags=re.IGNORECASE)

    # 2. Inline CSS with iOS 15.8 hex fallbacks + mobile mode bar
    combined_css = f"{IOS15_FALLBACK_CSS}\n{css_src}\n{MOBILE_MODE_BAR_CSS}"
    html_src = html_src.replace(
        '<link rel="stylesheet" href="/static/styles.css" />',
        f"<style>\n{combined_css}\n</style>",
    )

    # 3. Add mobile mode bar right after </header> so iPhone 7 Plus users can tap tabs directly
    mobile_bar_html = """
  <nav class="mobile-mode-bar" aria-label="Mobile workspace modes">
    <button class="mode-tab is-active" data-mode="overview">Overview</button>
    <button class="mode-tab" data-mode="guides">Study Guides</button>
    <button class="mode-tab" data-mode="reader">Source</button>
    <button class="mode-tab" data-mode="cheatsheets">Sheets</button>
    <button class="mode-tab" data-mode="quizzes">Quiz</button>
  </nav>"""
    html_src = html_src.replace("</header>", f"</header>\n{mobile_bar_html}", 1)

    # 4. Replace api() in app.js with offlineApi shim and wrap in IIFE
    api_pattern = re.compile(
        r"// =========================================================================\s*\n// API Client\s*\n// =========================================================================\s*\nasync function api\(path, options = \{\}\) \{[\s\S]*?\n\}",
        re.MULTILINE,
    )
    if not api_pattern.search(js_src):
        raise RuntimeError("Could not locate api() block in web_app/static/app.js")
    offline_js = api_pattern.sub(OFFLINE_API_SHIM.replace("\\", "\\\\"), js_src, count=1)

    # 5. Serialize database payload safely for inline <script> (escape </script>)
    payload = build_offline_payload()
    payload_json = json.dumps(payload, ensure_ascii=False).replace("</", "<\\/")

    inline_scripts = (
        f"<script>\nwindow.__DWP301C_DATA__ = {payload_json};\n</script>\n"
        f"<script>\n(function() {{\n{offline_js}\n}})();\n</script>"
    )
    html_src = html_src.replace('<script src="/static/app.js" type="module"></script>', inline_scripts)

    out_file.write_text(html_src, encoding="utf-8")
    return out_file


if __name__ == "__main__":
    out = export_offline_html()
    size_mb = out.stat().st_size / (1024 * 1024)
    print(f"Exported standalone offline app: {out} ({size_mb:.2f} MB)")

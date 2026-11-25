"""
Automated API integration + Playwright E2E & responsive verification tests
for DWP301c Codex (web_app) covering all 7 Coursera courses (35 modules, 241 lessons, 381 questions).
"""

from __future__ import annotations

import re
import socket
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

from fastapi.testclient import TestClient
from playwright.sync_api import sync_playwright

APP_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(APP_DIR))

import server  # noqa: E402

EXPECTED_COURSES = {
    "coursera1": {"modules": 5, "lessons": 46, "quizzes": 11, "questions": 66, "search_term": "ORM"},
    "coursera2": {"modules": 4, "lessons": 29, "quizzes": 7, "questions": 50, "search_term": "TEXT_NODE"},
    "coursera3": {"modules": 4, "lessons": 19, "quizzes": 5, "questions": 27, "search_term": "upstream"},
    "coursera4": {"modules": 4, "lessons": 50, "quizzes": 9, "questions": 70, "search_term": "configureStore"},
    "coursera5": {"modules": 5, "lessons": 49, "quizzes": 8, "questions": 60, "search_term": "kubelet"},
    "coursera6": {"modules": 6, "lessons": 35, "quizzes": 10, "questions": 70, "search_term": "Knative"},
    "coursera7": {"modules": 7, "lessons": 13, "quizzes": 5, "questions": 38, "search_term": "CarModel"},
}


def test_api_endpoints():
    client = TestClient(server.app)

    # 1. Health endpoint reflects all 7 seeded courses
    r = client.get("/api/health")
    assert r.status_code == 200
    h = r.json()
    assert h["status"] == "ok"
    assert h["courses_seeded"] == 7, f"Expected 7 seeded courses, got {h['courses_seeded']}"
    assert h["total_lessons"] == 241, f"Expected 241 lessons, got {h['total_lessons']}"
    assert h["total_questions"] == 381, f"Expected 381 questions, got {h['total_questions']}"

    # 2. Courses list (all 7 registered and seeded)
    r = client.get("/api/courses")
    assert r.status_code == 200
    courses = r.json()["courses"]
    assert len(courses) == 7
    for c in courses:
        assert c["is_seeded"] == 1, f"Course {c['key']} is not seeded"
        exp = EXPECTED_COURSES[c["key"]]
        assert c["total_modules"] == exp["modules"]
        assert c["total_lessons"] == exp["lessons"]
        assert c["total_quizzes"] == exp["quizzes"]
        assert c["total_questions"] == exp["questions"]

    # 3. Verify all 35 synthesized module study guides & quizzes across all 7 courses
    total_guides_verified = 0
    first_lesson_id = None
    for c_key, exp in EXPECTED_COURSES.items():
        r = client.get(f"/api/courses/{c_key}")
        assert r.status_code == 200
        detail = r.json()
        assert len(detail["modules"]) == exp["modules"], f"{c_key}: wrong module count"

        for m in detail["modules"]:
            assert m["has_guide"] is True, f"{c_key} M{m['module_number']} missing guide"
            assert m["guide_chars"] >= 1500, f"{c_key} M{m['module_number']} guide too short ({m['guide_chars']})"
            assert len(m["guide_summary"]) > 40, f"{c_key} M{m['module_number']} missing core takeaway summary"

            mr = client.get(f"/api/courses/{c_key}/modules/{m['module_number']}")
            assert mr.status_code == 200
            md = mr.json()
            assert len(md["module"]["guide_md"]) >= 1500
            assert len(md["source_lessons"]) >= 1
            total_guides_verified += 1

        if first_lesson_id is None:
            first_lesson_id = detail["modules"][0]["lessons"][0]["id"]

        # FTS5 course-scoped search for each course's signature synthesized concept
        sr = client.get("/api/search", params={"q": exp["search_term"], "course": c_key})
        assert sr.status_code == 200
        hits = sr.json()["results"]
        assert len(hits) >= 1, f"No FTS5 hits for '{exp['search_term']}' in {c_key}"
        assert any(h["item_type"] == "guide" for h in hits), f"Expected guide hit for '{exp['search_term']}' in {c_key}"
        assert any("<mark>" in h["snippet"] for h in hits)

        # Quizzes endpoint (exact count, 0 empty prompts, 100% verified answers + explanations)
        qr = client.get(f"/api/courses/{c_key}/quizzes")
        assert qr.status_code == 200
        qzs = qr.json()["quizzes"]
        assert len(qzs) == exp["quizzes"]
        assert sum(q["question_count"] for q in qzs) == exp["questions"]
        for qz in qzs:
            for q_item in qz["questions"]:
                assert q_item["prompt_text"].strip() != "", f"Empty prompt in {c_key} quiz {qz['title']}"
                assert any(o.get("checked") for o in q_item["options"]), f"Missing answer key in {c_key} Q{q_item['id']}"
                assert len((q_item.get("explanation") or "").strip()) >= 20, f"Missing explanation in {c_key} Q{q_item['id']}"

    assert total_guides_verified == 35

    # 4. Lesson detail, prev/next & state persistence
    r = client.get(f"/api/lessons/{first_lesson_id}")
    assert r.status_code == 200
    ld = r.json()
    assert ld["lesson"]["char_count"] > 100
    assert ld["next_lesson"] is not None

    r = client.patch(f"/api/lessons/{first_lesson_id}/state", json={"is_completed": True, "is_bookmarked": True})
    assert r.status_code == 200 and r.json()["is_completed"] is True and r.json()["is_bookmarked"] is True
    client.patch(f"/api/lessons/{first_lesson_id}/state", json={"is_completed": False, "is_bookmarked": False})

    # 5. Edge cases: invalid course/module, punctuation-only search, Vietnamese Unicode search, HTML-safe snippets
    assert client.get("/api/courses/nonexistent").status_code == 404
    assert client.get("/api/courses/coursera2/modules/99").status_code == 404
    assert client.get("/api/search", params={"q": "!!!"}).json()["results"] == []

    # Vietnamese Unicode FTS5 search must preserve diacritics (not split into single ASCII letters)
    vn_hits = client.get("/api/search", params={"q": "bảo mật"}).json()["results"]
    assert len(vn_hits) >= 1, "Expected Vietnamese FTS5 hits for 'bảo mật'"
    assert any("bảo" in h["snippet"].lower() or "mật" in h["snippet"].lower() for h in vn_hits), (
        f"Vietnamese query returned non-Vietnamese noise: {vn_hits[0]['snippet']!r}"
    )

    # Search snippets must escape raw HTML tags (like <script> / <div>) while preserving <mark>
    html_hits = client.get("/api/search", params={"q": "script", "course": "coursera2"}).json()["results"]
    assert len(html_hits) >= 1
    for h in html_hits:
        stripped = h["snippet"].replace("<mark>", "").replace("</mark>", "")
        assert not re.search(r"<[a-zA-Z/][^>]*>", stripped), f"Unescaped HTML tag in search snippet: {h['snippet']!r}"

    print("API INTEGRATION TESTS PASSED (7 courses, 35 guides, 241 lessons, 381 questions)!")


def _pick_free_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


def test_playwright_e2e():
    port = _pick_free_port()
    base_url = f"http://127.0.0.1:{port}"
    proc = subprocess.Popen(
        [sys.executable, "-m", "uvicorn", "server:app", "--host", "127.0.0.1", "--port", str(port), "--log-level", "warning"],
        cwd=str(APP_DIR),
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    ready = False
    for _ in range(50):
        try:
            with urllib.request.urlopen(f"{base_url}/api/health", timeout=1) as resp:
                if resp.status == 200:
                    ready = True
                    break
        except Exception:
            time.sleep(0.3)
    assert ready, f"Uvicorn test server failed to start on port {port}"

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(channel="msedge", headless=True)

            # 1. Desktop 1440x900
            page = browser.new_page(viewport={"width": 1440, "height": 900})
            console_errors = []
            http_errors = []
            page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)
            page.on("pageerror", lambda err: console_errors.append(str(err)))
            page.on("response", lambda res: http_errors.append((res.status, res.url)) if res.status >= 400 else None)

            page.goto(f"{base_url}/", wait_until="networkidle")
            page.wait_for_selector(".course-hero h1")
            assert "Django Application Development" in page.locator(".course-hero h1").inner_text()

            # Check zero horizontal overflow on desktop
            overflow_desktop = page.evaluate("document.documentElement.scrollWidth > window.innerWidth + 1")
            assert not overflow_desktop, "Horizontal overflow on desktop!"

            # Open Course Switcher and verify all 7 courses are enabled (not disabled)
            page.click("#courseSwitcherBtn")
            page.wait_for_selector("#courseMenuPopover:not(.hidden)")
            assert page.locator(".course-option").count() == 7
            assert page.locator(".course-option[disabled]").count() == 0
            page.click("#courseSwitcherBtn")

            # Exhaustively render ALL 7 courses and ALL 35 Study Guides in the real browser
            guides_rendered = 0
            for idx, (c_key, exp) in enumerate(EXPECTED_COURSES.items(), 1):
                if idx > 1:
                    page.click("#courseSwitcherBtn")
                    page.wait_for_selector("#courseMenuPopover:not(.hidden)")
                    page.click(f'.course-option[data-course-key="{c_key}"]')
                    page.wait_for_function(
                        f"document.querySelector('#activeCourseLabel')?.textContent?.startsWith('C{idx} ')"
                    )
                    page.wait_for_selector(".roadmap-row")

                # Overview roadmap summaries must render formatted inline Markdown (no raw ** or backticks)
                summaries = page.locator(".roadmap-summary").all_inner_texts()
                assert len(summaries) == exp["modules"], f"{c_key}: expected {exp['modules']} roadmap summaries"
                for s_txt in summaries:
                    assert "**" not in s_txt, f"{c_key}: raw '**' in roadmap summary: {s_txt!r}"

                # Open Module 1 Study Guide, then step through every module pill in this course
                page.click(".hero-actions .btn-primary")
                for m_num in range(1, exp["modules"] + 1):
                    if m_num > 1:
                        page.click(f'.mod-pill-btn[data-open-module-guide="{m_num}"]')
                    page.wait_for_function(
                        f"document.querySelector('.reader-title')?.innerText.startsWith('Module {m_num}:')"
                    )
                    prose_text = page.locator(".prose").inner_text()
                    assert len(prose_text.strip()) > 800, f"{c_key} M{m_num}: rendered prose too short"
                    assert "<br>" not in prose_text.lower(), f"{c_key} M{m_num}: literal '<br>' leaked into rendered text"
                    # Inline code spans must never be corrupted with nested <em> or <strong>
                    bad_code = page.locator(".prose code em, .prose code strong").count()
                    assert bad_code == 0, f"{c_key} M{m_num}: corrupted inline code containing em/strong"
                    # Zero horizontal overflow on desktop for every guide
                    assert not page.evaluate("document.documentElement.scrollWidth > window.innerWidth + 1"), (
                        f"{c_key} M{m_num}: horizontal overflow on desktop!"
                    )
                    if c_key == "coursera2" and m_num == 3:
                        assert "<script>/* mã ngắn */</script>" in prose_text
                    if c_key == "coursera6" and m_num == 3:
                        assert page.locator(".prose table br").count() >= 4
                    guides_rendered += 1

            assert guides_rendered == 35, f"Expected 35 guides rendered, got {guides_rendered}"

            # State-reset regression: we are currently on Course 7 Module 7; filter M5 quizzes (> C2's 4 modules),
            # then switch to Course 2 (4 modules) and verify Study Guides, Quizzes, and Raw Source all reset cleanly!
            page.click('.mode-tab[data-mode="quizzes"]')
            page.wait_for_selector(".question-item")
            page.click('.quiz-filter-bar [data-quiz-mod="5"]')

            page.click("#courseSwitcherBtn")
            page.wait_for_selector("#courseMenuPopover:not(.hidden)")
            page.click('.course-option[data-course-key="coursera2"]')
            page.wait_for_function("document.querySelector('.course-hero h1')?.innerText.includes('HTML')")

            # Clicking Study Guides tab must load Module 1 (NOT 404 on Module 7!)
            page.click('.mode-tab[data-mode="guides"]')
            page.wait_for_function("document.querySelector('.reader-title')?.innerText.startsWith('Module 1:')")

            # Clicking Quizzes tab must show all 50 Course 2 questions (NOT 0 from stale M7 filter!)
            page.click('.mode-tab[data-mode="quizzes"]')
            page.wait_for_selector(".question-item")
            assert page.locator(".question-item").count() == 50
            assert page.locator("[data-reveal-q]").count() == 50

            # Scroll-lock & explanation test: scroll to a lower question (#25), pick option & Check answer -> zero jump!
            target_card = page.locator(".question-item").nth(24)
            target_card.scroll_into_view_if_needed()
            scroll_before = page.evaluate("window.scrollY")
            assert scroll_before > 500, f"Expected scrolled position > 500, got {scroll_before}"
            target_card.locator("[data-pick-q]").first.click()
            scroll_after_pick = page.evaluate("window.scrollY")
            assert abs(scroll_after_pick - scroll_before) < 40, (
                f"Scroll jumped on option pick! before={scroll_before}, after={scroll_after_pick}"
            )
            target_card.locator("[data-reveal-q]").click()
            assert target_card.locator(".question-explanation").count() == 1
            scroll_after_check = page.evaluate("window.scrollY")
            assert abs(scroll_after_check - scroll_before) < 60, (
                f"Scroll jumped on Check answer! before={scroll_before}, after={scroll_after_check}"
            )

            # Clicking Raw Source tab must load a Course 2 lesson (NOT a stale Course 7 lesson!)
            page.click('.mode-tab[data-mode="reader"]')
            page.wait_for_selector(".reader-breadcrumb")
            assert "HTML" in page.locator(".reader-breadcrumb").inner_text()

            # Test Ctrl+K FTS5 Search with HTML-containing query ("script" in Course 2)
            page.keyboard.press("Control+k")
            page.wait_for_selector("#searchDialog[open]")
            page.fill("#searchInput", "script")
            page.wait_for_selector(".search-hit", timeout=5000)
            assert page.locator(".search-hit").count() >= 1
            page.keyboard.press("Escape")

            # Toggle dark mode
            page.click("#themeToggleBtn")
            assert page.evaluate("document.documentElement.getAttribute('data-theme')") == "dark"
            page.click("#themeToggleBtn")

            assert not console_errors, f"Console errors detected: {console_errors}"
            assert not http_errors, f"HTTP 4xx/5xx errors detected: {http_errors}"

            # 2. Mobile 390x844
            mobile = browser.new_page(viewport={"width": 390, "height": 844})
            mobile.goto(f"{base_url}/", wait_until="networkidle")
            mobile.wait_for_selector(".course-hero h1")
            overflow_mobile = mobile.evaluate("document.documentElement.scrollWidth > window.innerWidth + 1")
            assert not overflow_mobile, "Horizontal overflow on mobile 390px!"

            browser.close()
        print("PLAYWRIGHT E2E & RESPONSIVE TESTS PASSED!")
    finally:
        proc.terminate()
        proc.wait(timeout=5)


if __name__ == "__main__":
    test_api_endpoints()
    test_playwright_e2e()

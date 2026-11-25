"""
Verifies the standalone offline HTML export (DWP301c_Offline.html) in headless Edge
with network disabled (offline mode) on both Desktop (1440x900) and iPhone 7 Plus (414x736).
"""

from __future__ import annotations

from pathlib import Path
from playwright.sync_api import sync_playwright

APP_DIR = Path(__file__).resolve().parent
OFFLINE_HTML = APP_DIR / "DWP301c_Offline.html"


def test_offline_html():
    assert OFFLINE_HTML.exists(), f"Missing {OFFLINE_HTML}"
    file_url = OFFLINE_HTML.as_uri()

    with sync_playwright() as p:
        browser = p.chromium.launch(channel="msedge", headless=True)

        # 1. Desktop offline verification
        ctx = browser.new_context(viewport={"width": 1440, "height": 900}, offline=True)
        page = ctx.new_page()
        errors = []
        page.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)
        page.on("pageerror", lambda e: errors.append(str(e)))

        page.goto(file_url, wait_until="domcontentloaded")
        page.wait_for_selector(".course-hero h1")
        assert "Django Application Development" in page.locator(".course-hero h1").inner_text()

        # Switch through all 7 courses via Course Switcher
        for idx, ckey in enumerate(["coursera2", "coursera3", "coursera4", "coursera5", "coursera6", "coursera7", "coursera1"], 1):
            page.click("#courseSwitcherBtn")
            page.click(f'.course-option[data-course-key="{ckey}"]')
            page.wait_for_selector(".roadmap-row")
            assert page.locator(".roadmap-row").count() >= 4

        # Open Module 1 Study Guide & mark a source lesson completed -> check localStorage persistence
        page.click(".hero-actions .btn-primary")
        page.wait_for_selector(".reader-title")
        assert "Module 1:" in page.locator(".reader-title").inner_text()
        page.click('.source-drawer summary')
        page.click('.source-drawer [data-open-lesson]')
        page.wait_for_selector("#toggleCompleteBtn")
        page.click("#toggleCompleteBtn")
        assert "Completed" in page.locator("#toggleCompleteBtn").inner_text()

        # Reload offline page -> confirm completed progress persisted in localStorage
        page.reload(wait_until="domcontentloaded")
        page.wait_for_selector("#headerProgressText")
        assert page.locator("#headerProgressText").inner_text().startswith("1/")

        # Ctrl+K Vietnamese offline search
        page.keyboard.press("Control+k")
        page.wait_for_selector("#searchDialog[open]")
        page.fill("#searchInput", "bảo mật")
        page.wait_for_selector(".search-hit", timeout=3000)
        assert page.locator(".search-hit").count() >= 1
        page.keyboard.press("Escape")

        assert not errors, f"Console errors in offline desktop test: {errors}"
        ctx.close()

        # 2. iPhone 7 Plus (414x736) offline verification
        m_ctx = browser.new_context(viewport={"width": 414, "height": 736}, offline=True)
        mobile = m_ctx.new_page()
        m_errors = []
        mobile.on("console", lambda m: m_errors.append(m.text) if m.type == "error" else None)
        mobile.on("pageerror", lambda e: m_errors.append(str(e)))

        mobile.goto(file_url, wait_until="domcontentloaded")
        mobile.wait_for_selector(".mobile-mode-bar")
        mobile.click('.mobile-mode-bar .mode-tab[data-mode="guides"]')
        mobile.wait_for_selector(".reader-title")
        overflow = mobile.evaluate("document.documentElement.scrollWidth > window.innerWidth + 1")
        assert not overflow, "Horizontal overflow on iPhone 7 Plus (414px)!"

        mobile.click('.mobile-mode-bar .mode-tab[data-mode="quizzes"]')
        mobile.wait_for_selector(".question-item")
        assert mobile.locator(".question-item").count() == 66

        assert not m_errors, f"Console errors in offline mobile test: {m_errors}"
        m_ctx.close()
        browser.close()

    print("OFFLINE HTML EXPORT VERIFIED (DESKTOP + IPHONE 7 PLUS OFFLINE, 0 ERRORS)!")


if __name__ == "__main__":
    test_offline_html()

"""
Coursera Multiple-Choice Quiz Raw Crawler
=========================================
Opens a real Microsoft Edge browser (persistent profile) via Playwright so the user
can log in manually to Coursera. Once logged in, the script scans all modules of the
specified course, visits every quiz/practice item, checks if it contains multiple-choice
questions (radio / checkbox), and saves the raw question & option data to JSON and TXT.

Read-only: NEVER submits any quiz or clicks any Submit button.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Any
from urllib.parse import urljoin, urlparse

from playwright.sync_api import Page, BrowserContext, TimeoutError as PlaywrightTimeoutError, sync_playwright

# All 7 DWP301c Coursera courses
COURSES: dict[str, dict[str, str]] = {
    "coursera1": {
        "name": "Django Application Development with SQL and Databases",
        "slug": "developing-applications-with-sql-databases-and-django",
        "url": "https://www.coursera.org/learn/developing-applications-with-sql-databases-and-django",
    },
    "coursera2": {
        "name": "Introduction to HTML, CSS, & JavaScript",
        "slug": "introduction-html-css-javascript",
        "url": "https://www.coursera.org/learn/introduction-html-css-javascript",
    },
    "coursera3": {
        "name": "Getting Started with Git and GitHub",
        "slug": "getting-started-with-git-and-github",
        "url": "https://www.coursera.org/learn/getting-started-with-git-and-github",
    },
    "coursera4": {
        "name": "Developing Front-End Apps with React",
        "slug": "developing-frontend-apps-with-react",
        "url": "https://www.coursera.org/learn/developing-frontend-apps-with-react",
    },
    "coursera5": {
        "name": "Introduction to Containers w/ Docker, Kubernetes & OpenShift",
        "slug": "ibm-containers-docker-kubernetes-openshift",
        "url": "https://www.coursera.org/learn/ibm-containers-docker-kubernetes-openshift",
    },
    "coursera6": {
        "name": "Application Development using Microservices and Serverless",
        "slug": "applications-development-microservices-serverless-openshift",
        "url": "https://www.coursera.org/learn/applications-development-microservices-serverless-openshift",
    },
    "coursera7": {
        "name": "Full Stack Application Development Capstone Project",
        "slug": "ibm-cloud-native-full-stack-development-capstone",
        "url": "https://www.coursera.org/learn/ibm-cloud-native-full-stack-development-capstone",
    },
}

# Quiz URL patterns on Coursera (practice quizzes, graded quizzes, unified assignments)
QUIZ_URL_PATTERNS = (
    "/quiz/",
    "/exam/",
    "/assignment-submission/",
)

# Non-quiz URL patterns to skip
SKIP_URL_PATTERNS = (
    "/lecture/",
    "/supplement/",
    "/ungradedLti/",
    "/ungradedLab/",
    "/ungradedWidget/",
    "/peer/",
    "/programming/",
    "/discussionPrompt/",
    "/staffgraded/",
    "/teammateReview/",
)

# Title keywords that clearly indicate non-multiple-choice items
SKIP_TITLE_KEYWORDS = (
    "hands-on lab",
    "peer-graded",
    "peer graded",
    "peer review",
    "final project",
    "cheat sheet",
    "glossary",
    "reading:",
)


def log(msg: str) -> None:
    ts = datetime.now().strftime("%H:%M:%S")
    print(f"[{ts}] {msg}", flush=True)


def safe_goto(page: Page, url: str, timeout: int = 60000, retries: int = 4) -> None:
    """Navigate to URL, retrying cleanly if Coursera triggers an organization/auth redirect."""
    last_err: Exception | None = None
    for attempt in range(1, retries + 1):
        try:
            page.goto(url, wait_until="domcontentloaded", timeout=timeout)
            return
        except Exception as e:
            last_err = e
            msg = str(e)
            if "interrupted by another navigation" in msg or "ERR_ABORTED" in msg:
                log(f"  -> Navigation interrupted by Coursera redirect (attempt {attempt}/{retries}), waiting 3s & retrying...")
                time.sleep(3)
                try:
                    page.wait_for_load_state("domcontentloaded", timeout=15000)
                except Exception:
                    pass
                continue
            if attempt < retries:
                log(f"  -> Navigation warning (attempt {attempt}/{retries}): {e}. Retrying in 2s...")
                time.sleep(2)
            else:
                raise
    if last_err:
        raise last_err


def is_authenticated(context: BrowserContext) -> bool:
    """Check if Coursera auth cookie (CAUTH) is present or logged-in UI is visible."""
    try:
        cookies = context.cookies()
        for c in cookies:
            if c.get("name") == "CAUTH" and c.get("value"):
                return True
    except Exception:
        pass

    # Fallback DOM check across open Coursera pages
    try:
        for p in context.pages:
            if "coursera.org" in (p.url or ""):
                logged_in = p.evaluate(
                    """() => {
                        const hasProfile = Boolean(
                            document.querySelector('[data-e2e="header-profile"], [data-testid="profile-menu-trigger"], button[aria-label*="Profile"], a[href*="/my-learning"]')
                        );
                        const hasLoginBtn = Array.from(document.querySelectorAll('a, button')).some(
                            el => /^log in$/i.test((el.innerText || '').trim())
                        );
                        return hasProfile && !hasLoginBtn;
                    }"""
                )
                if logged_in:
                    return True
    except Exception:
        pass
    return False


def wait_for_login(
    page: Page,
    context: BrowserContext,
    course_home_url: str,
    timeout_sec: int = 300,
    wait_enter: bool = False,
) -> bool:
    """Open the course home page and wait until the user finishes logging in manually."""
    log(f"Opening Coursera course: {course_home_url}")
    safe_goto(page, course_home_url, timeout=60000)
    time.sleep(2.5)

    if is_authenticated(context):
        log("Already logged in (Coursera session detected).")
        return True

    # Open login modal/page directly for convenience
    try:
        safe_goto(page, "https://www.coursera.org/?authMode=login", timeout=60000)
    except Exception:
        pass

    log("=" * 65)
    log("VUI LONG DANG NHAP COURSERA TREN CUA SO EDGE VUA MO!")
    if wait_enter:
        log("Sau khi dang nhap thanh cong, quay lai terminal va nhan ENTER...")
        log("=" * 65)
        input()
        time.sleep(2.5)
        return True

    log("Script se tu dong tiep tuc ngay sau khi ban dang nhap thanh cong...")
    log("=" * 65)

    start = time.time()
    while time.time() - start < timeout_sec:
        if is_authenticated(context):
            log("Login detected! Navigating to course home...")
            time.sleep(3)
            return True
        time.sleep(1.5)

    log("Timeout waiting for login.")
    return False


def normalize_quiz_url(url: str) -> str:
    """Normalize quiz URL by stripping query params and trailing /attempt or /view-feedback."""
    parsed = urlparse(url)
    path = parsed.path.rstrip("/")
    for suffix in ("/attempt", "/view-feedback", "/submission", "/feedback"):
        if path.endswith(suffix):
            path = path[: -len(suffix)]
    return f"{parsed.scheme}://{parsed.netloc}{path}"


def is_candidate_quiz_url(url: str, slug: str) -> bool:
    if f"/learn/{slug}/" not in url:
        return False
    if any(skip in url for skip in SKIP_URL_PATTERNS):
        return False
    return any(pat in url for pat in QUIZ_URL_PATTERNS)


def discover_quizzes(page: Page, course_url: str, slug: str) -> list[dict[str, str]]:
    """
    Scan all modules (/home/module/1..N) and /home/assignments to discover all
    practice quizzes and graded quizzes in the course.
    """
    discovered: dict[str, dict[str, str]] = {}

    # 1. Go to /home/module/1 to find all module links in the left sidebar
    first_mod_url = f"{course_url}/home/module/1"
    log(f"Scanning course modules starting from {first_mod_url}")
    safe_goto(page, first_mod_url, timeout=60000)
    time.sleep(4)

    # Collect module URLs from sidebar
    module_urls: list[str] = page.evaluate(
        """(slug) => {
            const links = Array.from(document.querySelectorAll('a[href]'));
            const mods = new Set();
            for (const a of links) {
                const href = a.href || '';
                if (href.includes(`/learn/${slug}/home/module/`)) {
                    const m = href.match(/^(https:\\/\\/[^?#]+\\/home\\/module\\/\\d+)/);
                    if (m) mods.add(m[1]);
                }
            }
            return Array.from(mods).sort((a, b) => {
                const na = parseInt(a.split('/').pop(), 10);
                const nb = parseInt(b.split('/').pop(), 10);
                return na - nb;
            });
        }""",
        slug,
    )

    if not module_urls:
        # Fallback: try modules 1..10 until a page redirects or has no items
        log("No sidebar module links found directly; falling back to /home/module/1..8")
        module_urls = [f"{course_url}/home/module/{i}" for i in range(1, 9)]
    else:
        log(f"Found {len(module_urls)} modules: {[u.split('/')[-1] for u in module_urls]}")

    # Helper to extract quiz links from currently loaded page
    def scrape_links_from_page(source_label: str) -> int:
        # Expand any collapsed accordions/sections if present
        try:
            page.evaluate(
                """() => {
                    const buttons = Array.from(document.querySelectorAll('button[aria-expanded="false"]'));
                    for (const btn of buttons) {
                        const txt = (btn.innerText || '').toLowerCase();
                        // Avoid clicking navigation/account menus
                        if (txt.includes('module') || txt.includes('lesson') || txt.includes('show') || txt.includes('item')) {
                            try { btn.click(); } catch (e) {}
                        }
                    }
                }"""
            )
            time.sleep(1.0)
        except Exception:
            pass

        items = page.evaluate(
            """() => {
                const results = [];
                const anchors = Array.from(document.querySelectorAll('a[href]'));
                for (const a of anchors) {
                    const href = a.href || '';
                    const text = (a.innerText || a.getAttribute('aria-label') || '').replace(/\\s+/g, ' ').trim();
                    results.push({ href, text });
                }
                return results;
            }"""
        )

        added = 0
        for item in items:
            href = item.get("href", "")
            text = item.get("text", "")
            if not is_candidate_quiz_url(href, slug):
                continue

            lower_text = text.lower()
            if any(kw in lower_text for kw in SKIP_TITLE_KEYWORDS):
                continue

            norm_url = normalize_quiz_url(href)
            if norm_url not in discovered:
                discovered[norm_url] = {
                    "url": norm_url,
                    "raw_href": href,
                    "title": text or norm_url.split("/")[-1],
                    "source": source_label,
                    "kind": "practice_quiz" if "/quiz/" in norm_url or "practice" in lower_text else "graded_quiz",
                }
                added += 1
        return added

    # Visit each module page
    for mod_url in module_urls:
        mod_num = mod_url.split("/")[-1]
        log(f"Scanning Module {mod_num}: {mod_url}")
        try:
            safe_goto(page, mod_url, timeout=60000)
            time.sleep(3)
            # Scroll down to trigger lazy rendering
            page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(1.5)
            page.evaluate("window.scrollTo(0, 0)")
            cnt = scrape_links_from_page(f"Module {mod_num}")
            log(f"  -> Found {cnt} new quiz link(s) in Module {mod_num}")
        except Exception as e:
            log(f"  -> Warning scanning Module {mod_num}: {e}")

    # 2. Also scan /home/assignments as a cross-check
    assignments_url = f"{course_url}/home/assignments"
    log(f"Cross-checking Assignments page: {assignments_url}")
    try:
        safe_goto(page, assignments_url, timeout=60000)
        time.sleep(3)
        cnt = scrape_links_from_page("Assignments")
        log(f"  -> Found {cnt} additional quiz link(s) on Assignments page")
    except Exception as e:
        log(f"  -> Warning scanning Assignments page: {e}")

    quiz_list = list(discovered.values())
    log(f"Total unique candidate quizzes discovered: {len(quiz_list)}")
    for idx, q in enumerate(quiz_list, 1):
        log(f"  {idx}. [{q['source']}] [{q['kind']}] {q['title']} -> {q['url']}")
    return quiz_list


def open_quiz_questions_view(page: Page, quiz_url: str) -> str:
    """
    Navigate to a quiz URL and open the questions view (e.g., /attempt or /view-feedback).
    Waits explicitly for Coursera's React SPA to finish rendering (past 'Loading...').
    NEVER clicks any Submit button.
    Returns a status string describing how the questions view was reached.
    """
    safe_button_patterns = [
        r"^view feedback$",
        r"^review$",
        r"^view submission$",
        r"^resume$",
        r"^resume assignment$",
        r"^continue$",
        r"^try again$",
        r"^practice again$",
        r"^retake$",
        r"^start$",
        r"^start assignment$",
        r"^start quiz$",
        r"^begin$",
        r"^open assignment$",
    ]

    def has_mc_inputs() -> bool:
        try:
            count = page.locator(
                'input[type="radio"], input[type="checkbox"], [role="radio"], [role="checkbox"]'
            ).count()
            return count > 0
        except Exception:
            return False

    def find_visible_action_button():
        for pat in safe_button_patterns:
            try:
                loc = page.locator("button, a").filter(has_text=re.compile(pat, re.IGNORECASE))
                count = loc.count()
                for i in range(count):
                    el = loc.nth(i)
                    if el.is_visible():
                        txt = (el.inner_text() or "").strip()
                        if "submit" in txt.lower():
                            continue
                        return el, txt
            except Exception:
                continue
        return None, None

    def wait_for_content_ready(timeout_sec: float = 20.0) -> str:
        """Wait until either MC inputs OR a cover action button appears (past Loading...)."""
        deadline = time.time() + timeout_sec
        while time.time() < deadline:
            if has_mc_inputs():
                time.sleep(1.0)  # allow remaining questions to finish mounting
                return "mc_ready"
            el, _ = find_visible_action_button()
            if el is not None:
                return "button_ready"
            time.sleep(0.5)
        return "timeout"

    safe_goto(page, quiz_url, timeout=60000)
    state = wait_for_content_ready(timeout_sec=20.0)

    if state == "mc_ready":
        return "direct_mc_found"

    for attempt_step in range(3):
        if has_mc_inputs():
            return f"opened_after_step_{attempt_step}"

        el, txt = find_visible_action_button()
        if el is None:
            # Wait a bit more in case React is still hydrating
            state = wait_for_content_ready(timeout_sec=8.0)
            if state == "mc_ready":
                return f"opened_after_wait_{attempt_step}"
            el, txt = find_visible_action_button()
            if el is None:
                break

        try:
            log(f"    Clicking button '{txt}' to view quiz questions...")
            el.click(timeout=10000)
        except Exception as e:
            log(f"    Click warning on '{txt}': {e}")
            break

        post_state = wait_for_content_ready(timeout_sec=20.0)
        if post_state == "mc_ready":
            return f"opened_via_button:{txt}"

    if has_mc_inputs():
        return "opened_via_button"

    # Fallback: try appending /view-feedback or /attempt directly
    for suffix in ("/view-feedback", "/attempt"):
        try_url = quiz_url.rstrip("/") + suffix
        log(f"    Trying direct URL: {try_url}")
        try:
            safe_goto(page, try_url, timeout=45000)
            post_state = wait_for_content_ready(timeout_sec=15.0)
            if post_state == "mc_ready" or has_mc_inputs():
                return f"opened_via_{suffix.strip('/')}"
        except Exception:
            pass

    return "no_mc_inputs_found"


def extract_mc_questions(page: Page) -> dict[str, Any]:
    """
    Extract all multiple-choice (radio & checkbox) questions from the current quiz page.
    Uses a DOM-resilient strategy: finds all radio/checkbox inputs, groups them by their
    question container, and extracts raw prompt text, option list, and raw block text.
    """
    # Scroll smoothly down and back up to make sure all lazy-loaded elements render
    try:
        total_h = page.evaluate("document.body.scrollHeight")
        for y in range(0, int(total_h) + 600, 600):
            page.evaluate(f"window.scrollTo(0, {y})")
            time.sleep(0.2)
        page.evaluate("window.scrollTo(0, 0)")
        time.sleep(0.5)
    except Exception:
        pass

    result = page.evaluate(
        """() => {
            const pageTitle = (
                document.querySelector('h1')?.innerText ||
                document.title ||
                ''
            ).trim();

            let inputs = Array.from(
                document.querySelectorAll('input[type="radio"], input[type="checkbox"]')
            );
            // Fallback to ARIA radio/checkbox elements if native inputs are not used
            if (inputs.length === 0) {
                inputs = Array.from(
                    document.querySelectorAll('[role="radio"], [role="checkbox"]')
                );
            }
            inputs = inputs.filter(el => {
                // Exclude honor-code / agreement checkboxes outside questions
                const labelText = (el.closest('label')?.innerText || el.innerText || '').toLowerCase();
                if (
                    labelText.includes('honor code') ||
                    labelText.includes('understand that submitting') ||
                    labelText.includes('understand and agree') ||
                    labelText.includes('agree to the')
                ) {
                    return false;
                }
                return true;
            });

            if (inputs.length === 0) {
                return {
                    page_title: pageTitle,
                    current_url: window.location.href,
                    question_count: 0,
                    questions: [],
                    raw_page_text: (document.body?.innerText || '').trim(),
                };
            }

            // Find the question container for each input
            function findQuestionContainer(input) {
                const selectors = [
                    '[data-testid^="part-Submission_"]',
                    '[data-testid="question-container"]',
                    '.rc-FormPartsQuestion',
                    '.rc-FormPartsMcq',
                    '[role="group"]',
                    '[role="radiogroup"]',
                ];
                for (const sel of selectors) {
                    const match = input.closest(sel);
                    if (match) {
                        // If we matched radiogroup/group, check if parent is a broader FormPartsQuestion
                        const outer = match.closest('[data-testid^="part-Submission_"], .rc-FormPartsQuestion');
                        return outer || match;
                    }
                }
                // Fallback: climb up to a container that holds multiple inputs of the same question
                let cur = input.parentElement;
                let best = cur;
                for (let depth = 0; depth < 8 && cur; depth++) {
                    const subInputs = cur.querySelectorAll('input[type="radio"], input[type="checkbox"]');
                    if (subInputs.length >= 2 && subInputs.length <= 12) {
                        best = cur;
                        // Try one more level up to include the prompt text
                        if (cur.parentElement && cur.parentElement.querySelectorAll('input[type="radio"], input[type="checkbox"]').length === subInputs.length) {
                            best = cur.parentElement;
                        }
                        break;
                    }
                    cur = cur.parentElement;
                }
                return best;
            }

            const containerMap = new Map();
            for (const inp of inputs) {
                const container = findQuestionContainer(inp);
                if (!container) continue;
                if (!containerMap.has(container)) {
                    containerMap.set(container, []);
                }
                containerMap.get(container).push(inp);
            }

            const questions = [];
            let qIdx = 0;
            for (const [container, qInputs] of containerMap.entries()) {
                qIdx += 1;
                const firstEl = qInputs[0];
                const firstType = firstEl?.type || firstEl?.getAttribute?.('role') || 'radio';
                const questionType = firstType === 'checkbox' ? 'multiple_select' : 'single_choice';

                // Extract option texts
                const options = [];
                const optionElements = new Set();
                for (const inp of qInputs) {
                    let optContainer = inp.closest('label') || inp.closest('[class*="option"], [class*="Option"], li') || inp.parentElement;
                    if (optContainer) optionElements.add(optContainer);
                    let optText = '';
                    if (optContainer) {
                        optText = (optContainer.innerText || '').trim();
                    } else if (inp.id) {
                        const lbl = document.querySelector(`label[for="${CSS.escape(inp.id)}"]`);
                        optText = (lbl?.innerText || '').trim();
                    }
                    const isChecked = Boolean(inp.checked || inp.getAttribute?.('aria-checked') === 'true');
                    options.push({
                        text: optText,
                        checked: isChecked,
                    });
                }

                // Extract prompt text: look for dedicated prompt element first, else derive from container text
                let promptText = '';
                const promptEl = container.querySelector(
                    '[data-testid="cml-viewer"], .rc-FormPartsQuestion__contentCell .rc-CML, .rc-Prompt, [id*="prompt"]'
                );
                if (promptEl && !Array.from(optionElements).some(oe => oe.contains(promptEl))) {
                    promptText = (promptEl.innerText || '').trim();
                }

                const rawBlockText = (container.innerText || '').trim();
                if (!promptText) {
                    // Remove option lines from rawBlockText as a clean approximation
                    let approx = rawBlockText;
                    for (const opt of options) {
                        if (opt.text) {
                            approx = approx.replace(opt.text, '');
                        }
                    }
                    promptText = approx.replace(/\\n{3,}/g, '\\n\\n').trim();
                }

                questions.push({
                    index: qIdx,
                    question_type: questionType,
                    prompt_text: promptText,
                    options: options,
                    raw_block_text: rawBlockText,
                });
            }

            const mainEl = document.querySelector('main') || document.body;
            return {
                page_title: pageTitle,
                current_url: window.location.href,
                question_count: questions.length,
                questions: questions,
                raw_page_text: (mainEl?.innerText || '').trim(),
            };
        }"""
    )
    return result


def save_outputs(output_dir: Path, course_info: dict[str, Any], quizzes_data: list[dict[str, Any]]) -> tuple[Path, Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    json_path = output_dir / "raw_quizzes.json"
    txt_path = output_dir / "raw_quizzes.txt"

    payload = {
        "crawled_at": datetime.now().isoformat(),
        "course": course_info,
        "total_quizzes_discovered": len(quizzes_data),
        "total_mc_quizzes_extracted": sum(1 for q in quizzes_data if q.get("question_count", 0) > 0),
        "total_mc_questions": sum(q.get("question_count", 0) for q in quizzes_data),
        "quizzes": quizzes_data,
    }

    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    # Also write a clean human-readable raw text dump
    lines: list[str] = []
    lines.append("=" * 80)
    lines.append(f"COURSE: {course_info['name']}")
    lines.append(f"URL: {course_info['url']}")
    lines.append(f"CRAWLED AT: {payload['crawled_at']}")
    lines.append(
        f"SUMMARY: {payload['total_mc_quizzes_extracted']}/{payload['total_quizzes_discovered']} "
        f"MC quizzes | {payload['total_mc_questions']} questions"
    )
    lines.append("=" * 80)
    lines.append("")

    for idx, qz in enumerate(quizzes_data, 1):
        lines.append("-" * 80)
        lines.append(f"[QUIZ {idx}] {qz.get('title', 'Untitled')}")
        lines.append(f"Source: {qz.get('source')} | Kind: {qz.get('kind')} | Status: {qz.get('status')}")
        lines.append(f"URL: {qz.get('final_url') or qz.get('url')}")
        lines.append(f"Questions extracted: {qz.get('question_count', 0)}")
        lines.append("-" * 80)

        for q in qz.get("questions", []):
            lines.append(f"\nQ{q['index']} ({q['question_type']}):")
            lines.append(q.get("prompt_text", "").strip())
            for opt_i, opt in enumerate(q.get("options", []), 1):
                mark = "[x]" if opt.get("checked") else "[ ]"
                lines.append(f"   {opt_i}. {mark} {opt.get('text', '').strip()}")
        lines.append("")

    txt_path.write_text("\n".join(lines), encoding="utf-8")
    return json_path, txt_path


def crawl_course(
    course_key: str,
    custom_url: str | None = None,
    only_practice: bool = False,
    profile_dir: Path | None = None,
    output_root: Path | None = None,
    login_timeout: int = 300,
    wait_enter: bool = False,
) -> tuple[Path, Path]:
    if custom_url:
        m = re.search(r"/learn/([^/?#]+)", custom_url)
        slug = m.group(1) if m else "custom_course"
        course_info = {"key": "custom", "name": slug, "slug": slug, "url": f"https://www.coursera.org/learn/{slug}"}
    else:
        if course_key not in COURSES:
            raise ValueError(f"Unknown course key '{course_key}'. Choose from: {list(COURSES.keys())}")
        course_info = {"key": course_key, **COURSES[course_key]}

    base_dir = Path(__file__).resolve().parent
    # Store browser profile on local SSD (not Google Drive) for fast startup and reliable cookies
    local_app_data = os.environ.get("LOCALAPPDATA")
    default_profile = (
        Path(local_app_data) / "coursera_quiz_crawler_profile"
        if local_app_data
        else Path.home() / ".coursera_quiz_crawler_profile"
    )
    profile_path = profile_dir or default_profile
    out_dir = (output_root or (base_dir / "output")) / f"{course_info['key']}_{course_info['slug']}"

    log(f"Starting crawler for: {course_info['name']}")
    log(f"Browser profile dir: {profile_path}")
    log(f"Output dir: {out_dir}")

    quizzes_data: list[dict[str, Any]] = []

    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir=str(profile_path),
            channel="msedge",
            headless=False,
            viewport={"width": 1400, "height": 900},
            args=["--disable-blink-features=AutomationControlled"],
        )
        page = context.pages[0] if context.pages else context.new_page()

        try:
            logged_in = wait_for_login(
                page,
                context,
                f"{course_info['url']}/home/module/1",
                timeout_sec=login_timeout,
                wait_enter=wait_enter,
            )
            if not logged_in:
                raise RuntimeError("User did not complete login within timeout.")

            candidates = discover_quizzes(page, course_info["url"], course_info["slug"])
            if only_practice:
                candidates = [c for c in candidates if c["kind"] == "practice_quiz"]
                log(f"Filtered to practice quizzes only: {len(candidates)} item(s)")

            for idx, item in enumerate(candidates, 1):
                log(f"\n[{idx}/{len(candidates)}] Visiting: {item['title']} ({item['url']})")
                try:
                    status = open_quiz_questions_view(page, item["url"])
                    extracted = extract_mc_questions(page)
                    q_count = extracted.get("question_count", 0)
                    log(f"  -> Status: {status} | MC questions found: {q_count}")

                    quizzes_data.append(
                        {
                            "title": item["title"],
                            "page_title": extracted.get("page_title", ""),
                            "source": item["source"],
                            "kind": item["kind"],
                            "url": item["url"],
                            "final_url": extracted.get("current_url", page.url),
                            "status": status,
                            "question_count": q_count,
                            "questions": extracted.get("questions", []),
                            "raw_page_text": extracted.get("raw_page_text", ""),
                        }
                    )
                    # Save incrementally after every quiz so no progress is lost
                    save_outputs(out_dir, course_info, quizzes_data)
                except Exception as e:
                    log(f"  -> Error on quiz '{item['title']}': {e}")
                    quizzes_data.append(
                        {
                            "title": item["title"],
                            "source": item["source"],
                            "kind": item["kind"],
                            "url": item["url"],
                            "status": f"error: {e}",
                            "question_count": 0,
                            "questions": [],
                            "raw_page_text": "",
                        }
                    )
                    save_outputs(out_dir, course_info, quizzes_data)

        finally:
            json_path, txt_path = save_outputs(out_dir, course_info, quizzes_data)
            log(f"\nSaved JSON: {json_path}")
            log(f"Saved TXT : {txt_path}")
            context.close()

    return json_path, txt_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Coursera Multiple-Choice Quiz Raw Crawler")
    parser.add_argument(
        "--course",
        default="coursera1",
        choices=list(COURSES.keys()),
        help="Course key to crawl (default: coursera1)",
    )
    parser.add_argument(
        "--url",
        default=None,
        help="Optional custom Coursera course URL (overrides --course)",
    )
    parser.add_argument(
        "--only-practice",
        action="store_true",
        help="Only crawl practice quizzes (skip graded quizzes)",
    )
    parser.add_argument(
        "--login-timeout",
        type=int,
        default=300,
        help="Seconds to wait for manual login (default: 300)",
    )
    parser.add_argument(
        "--wait-enter",
        action="store_true",
        help="Wait for user to press Enter in terminal after manual login (never times out)",
    )
    args = parser.parse_args()

    crawl_course(
        course_key=args.course,
        custom_url=args.url,
        only_practice=args.only_practice,
        login_timeout=args.login_timeout,
        wait_enter=args.wait_enter,
    )


if __name__ == "__main__":
    main()

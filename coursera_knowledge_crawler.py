"""
Coursera Course Knowledge Crawler (Video Transcripts & Readings)
================================================================
Uses Playwright + Microsoft Edge (reusing the saved persistent login profile from
coursera_quiz_crawler.py) to crawl all learning content across Coursera courses:
  - Video lectures (/lecture/...): extracts full Transcript / Script / Subtitles
    (and auto-mutes/pauses video playback).
  - Readings (/supplement/...): extracts clean structured text, headings, lists,
    code blocks, and tables (cheat sheets, summaries, guides).

Skips all quizzes, exams, peer-graded projects, programming assignments, and labs.
Saves structured outputs to:
  Source_from_Coursera/knowledge/<course_key>_<course_slug>/
    - knowledge.json
    - knowledge.md
    - modules/module_01.md, module_02.md, ...
"""

from __future__ import annotations

import argparse
import json
import os
import re
import time
from datetime import datetime
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

from playwright.sync_api import BrowserContext, Page, sync_playwright

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
    "coursera8": {
        "name": "Introduction to Cloud Computing",
        "slug": "introduction-to-cloud",
        "url": "https://www.coursera.org/learn/introduction-to-cloud",
    },
    "coursera9": {
        "name": "Developing Back-End Apps with Node.js and Express",
        "slug": "developing-backend-apps-with-nodejs-and-express",
        "url": "https://www.coursera.org/learn/developing-backend-apps-with-nodejs-and-express",
    },
    "coursera10": {
        "name": "Python for Data Science, AI & Development",
        "slug": "python-for-applied-data-science-ai",
        "url": "https://www.coursera.org/learn/python-for-applied-data-science-ai",
    },
    "coursera11": {
        "name": "Python Project for AI & Application Development",
        "slug": "python-project-for-ai-application-development",
        "url": "https://www.coursera.org/learn/python-project-for-ai-application-development",
    },
    "coursera12": {
        "name": "Full-Stack Software Developer Assessment",
        "slug": "full-stack-software-developer-assessment",
        "url": "https://www.coursera.org/learn/full-stack-software-developer-assessment",
    },
    "coursera13": {
        "name": "Introduction to Web Development with HTML, CSS, JavaScript",
        "slug": "introduction-to-web-development-with-html-css-javacript",
        "url": "https://www.coursera.org/learn/introduction-to-web-development-with-html-css-javacript",
    },
}

KNOWLEDGE_URL_PATTERNS = (
    "/lecture/",
    "/supplement/",
)

SKIP_URL_PATTERNS = (
    "/quiz/",
    "/exam/",
    "/assignment-submission/",
    "/peer/",
    "/programming/",
    "/discussionPrompt/",
    "/ungradedLti/",
    "/ungradedLab/",
    "/ungradedWidget/",
    "/staffgraded/",
    "/teammateReview/",
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
                log(f"  -> Redirect interrupted navigation (attempt {attempt}/{retries}), waiting 3s & retrying...")
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
        for c in context.cookies():
            if c.get("name") == "CAUTH" and c.get("value"):
                return True
    except Exception:
        pass
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
    log(f"Opening Coursera course: {course_home_url}")
    safe_goto(page, course_home_url, timeout=60000)
    time.sleep(2.5)

    if is_authenticated(context):
        log("Already logged in (Coursera session detected).")
        return True

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


def normalize_item_url(url: str) -> str:
    parsed = urlparse(url)
    path = parsed.path.rstrip("/")
    return f"{parsed.scheme}://{parsed.netloc}{path}"


def is_knowledge_url(url: str, slug: str) -> bool:
    if f"/learn/{slug}/" not in url:
        return False
    if any(skip in url for skip in SKIP_URL_PATTERNS):
        return False
    return any(pat in url for pat in KNOWLEDGE_URL_PATTERNS)


def clean_item_title(raw_text: str, url: str) -> str:
    """Clean Coursera sidebar link text (remove trailing 'Video. Duration: 5 minutes 5 min', etc.)."""
    text = re.sub(r"\s+", " ", (raw_text or "")).strip()
    # Remove common Coursera item metadata suffixes
    text = re.sub(
        r"\s*(Video|Reading)\s*(\.\s*Duration:\s*[\d\w\s]+?)?(\d+\s*min(s|utes?)?|\d+\s*hr.*)?(\s*Completed)?$",
        "",
        text,
        flags=re.IGNORECASE,
    ).strip()
    if not text:
        text = url.rstrip("/").split("/")[-1].replace("-", " ").title()
    return text


def discover_knowledge_items(page: Page, course_url: str, slug: str) -> list[dict[str, Any]]:
    """
    Scan all modules (/home/module/1..N) in order and collect every Video (/lecture/)
    and Reading (/supplement/) item, preserving module number and order.
    """
    first_mod_url = f"{course_url}/home/module/1"
    log(f"Discovering modules from: {first_mod_url}")
    safe_goto(page, first_mod_url, timeout=60000)
    time.sleep(4)

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
                return parseInt(a.split('/').pop(), 10) - parseInt(b.split('/').pop(), 10);
            });
        }""",
        slug,
    )

    if not module_urls:
        log("Sidebar module links not found directly; falling back to /home/module/1..8")
        module_urls = [f"{course_url}/home/module/{i}" for i in range(1, 9)]
    else:
        log(f"Found {len(module_urls)} modules: {[u.split('/')[-1] for u in module_urls]}")

    seen_urls: set[str] = set()
    items: list[dict[str, Any]] = []

    for mod_url in module_urls:
        mod_num = int(mod_url.split("/")[-1])
        log(f"Scanning Module {mod_num}: {mod_url}")
        try:
            safe_goto(page, mod_url, timeout=60000)
            time.sleep(3.5)

            # Expand any collapsed lesson/module accordions
            try:
                page.evaluate(
                    """() => {
                        const buttons = Array.from(document.querySelectorAll('button[aria-expanded="false"]'));
                        for (const btn of buttons) {
                            const txt = (btn.innerText || '').toLowerCase();
                            if (txt.includes('module') || txt.includes('lesson') || txt.includes('show') || txt.includes('item')) {
                                try { btn.click(); } catch (e) {}
                            }
                        }
                    }"""
                )
                time.sleep(1.0)
            except Exception:
                pass

            page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(1.2)
            page.evaluate("window.scrollTo(0, 0)")

            mod_title = page.evaluate(
                """(modNum) => {
                    const skipRe = /congratulations|today's goal|welcome back|stay at a good pace/i;
                    // 1. Check active sidebar module link first
                    const activeLink = document.querySelector(`a[href*="/home/module/${modNum}"]`);
                    if (activeLink) {
                        const t = (activeLink.innerText || '').replace(/\\s+/g, ' ').trim();
                        const cleaned = t.replace(/^Module\\s*\\d+\\s*/i, '').trim();
                        if (cleaned && !skipRe.test(cleaned)) return cleaned;
                    }
                    // 2. Check headings in main, skipping completion banners
                    const headings = Array.from(document.querySelectorAll('main h1, main h2, [data-testid="module-title"]'));
                    for (const h of headings) {
                        const t = (h.innerText || '').replace(/\\s+/g, ' ').trim();
                        if (t && !skipRe.test(t) && t.length > 3) return t;
                    }
                    return '';
                }""",
                mod_num,
            ) or f"Module {mod_num}"

            anchors = page.evaluate(
                """() => {
                    const main = document.querySelector('main') || document.body;
                    return Array.from(main.querySelectorAll('a[href]')).map(a => ({
                        href: a.href || '',
                        text: (a.innerText || a.getAttribute('aria-label') || '').replace(/\\s+/g, ' ').trim()
                    }));
                }"""
            )

            added = 0
            for a in anchors:
                href = a.get("href", "")
                if not is_knowledge_url(href, slug):
                    continue
                norm = normalize_item_url(href)
                if norm in seen_urls:
                    continue
                seen_urls.add(norm)
                item_type = "video" if "/lecture/" in norm else "reading"
                items.append(
                    {
                        "module_number": mod_num,
                        "module_title": mod_title,
                        "type": item_type,
                        "title": clean_item_title(a.get("text", ""), norm),
                        "url": norm,
                    }
                )
                added += 1
            log(f"  -> Module {mod_num} ({mod_title[:50]}): found {added} knowledge item(s)")
        except Exception as e:
            log(f"  -> Warning scanning Module {mod_num}: {e}")

    v_cnt = sum(1 for x in items if x["type"] == "video")
    r_cnt = sum(1 for x in items if x["type"] == "reading")
    log(f"Total knowledge items discovered: {len(items)} ({v_cnt} videos, {r_cnt} readings)")
    return items


def mute_and_pause_videos(page: Page) -> None:
    try:
        page.evaluate(
            """() => {
                document.querySelectorAll('video, audio').forEach(v => {
                    try { v.muted = true; v.pause(); } catch (e) {}
                });
            }"""
        )
    except Exception:
        pass


def parse_vtt_to_text(vtt_content: str) -> str:
    """Convert WebVTT subtitle content into clean readable text."""
    lines: list[str] = []
    for raw_line in vtt_content.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if line.startswith("WEBVTT") or line.startswith("NOTE") or "-->" in line:
            continue
        if re.fullmatch(r"\d+", line):
            continue
        # Strip HTML/VTT tags like <c>, <i>, etc.
        line = re.sub(r"<[^>]+>", "", line).strip()
        if line and (not lines or lines[-1] != line):
            lines.append(line)
    return " ".join(lines).strip()


def extract_video_transcript(page: Page) -> dict[str, Any]:
    """
    Extract transcript/script from a Coursera /lecture/ page.
    Strategy:
      1. Mute/pause video and wait for transcript container or Transcript tab.
      2. Click Transcript tab if present and not active.
      3. Extract structured paragraphs/phrases from DOM transcript container.
      4. Fallback: fetch English WebVTT <track> or Transcript download link if DOM is empty.
    """
    mute_and_pause_videos(page)

    def try_click_transcript_tab() -> None:
        try:
            tab = page.locator('button[role="tab"], button, a').filter(
                has_text=re.compile(r"^transcript$", re.IGNORECASE)
            )
            for i in range(tab.count()):
                el = tab.nth(i)
                if el.is_visible():
                    aria_sel = el.get_attribute("aria-selected")
                    if aria_sel != "true":
                        el.click(timeout=5000)
                        time.sleep(1.5)
                    return
        except Exception:
            pass

    def grab_dom_transcript() -> dict[str, Any]:
        return page.evaluate(
            """() => {
                const heading = (
                    document.querySelector('h1.video-name, [data-testid="video-title"], main h1, h1')?.innerText ||
                    document.title ||
                    ''
                ).replace(/\\s+/g, ' ').trim();

                // 1. Look for Coursera transcript container
                const containerSelectors = [
                    '.rc-Transcript',
                    '[data-testid="transcript"]',
                    '[class*="Transcript"]',
                    '[aria-label*="Transcript"]',
                    '[id*="transcript"]',
                ];
                let container = null;
                for (const sel of containerSelectors) {
                    const el = document.querySelector(sel);
                    if (el && (el.innerText || '').trim().length > 40) {
                        container = el;
                        break;
                    }
                }

                let paragraphs = [];
                if (container) {
                    // Prefer grouped paragraphs (.rc-Paragraph) if present
                    const paraEls = container.querySelectorAll('.rc-Paragraph, [class*="Paragraph"], p');
                    if (paraEls.length > 0) {
                        for (const p of paraEls) {
                            const phrases = p.querySelectorAll('.rc-Phrase, [data-testid="transcript-phrase"], span[role="button"]');
                            let txt = '';
                            if (phrases.length > 0) {
                                txt = Array.from(phrases).map(s => (s.innerText || '').trim()).filter(Boolean).join(' ');
                            } else {
                                txt = (p.innerText || '').trim();
                            }
                            // Remove leading timestamps like "0:15" or "12:04"
                            txt = txt.replace(/^\\d{1,2}:\\d{2}\\s*/g, '').replace(/\\s+/g, ' ').trim();
                            if (txt) paragraphs.push(txt);
                        }
                    } else {
                        const phrases = container.querySelectorAll('.rc-Phrase, [data-testid="transcript-phrase"]');
                        if (phrases.length > 0) {
                            const joined = Array.from(phrases).map(s => (s.innerText || '').trim()).filter(Boolean).join(' ');
                            if (joined) paragraphs.push(joined);
                        } else {
                            const raw = (container.innerText || '').trim();
                            // Strip standalone timestamp lines
                            const cleanedLines = raw
                                .split('\\n')
                                .map(l => l.trim())
                                .filter(l => l && !/^\\d{1,2}:\\d{2}(:\\d{2})?$/.test(l) && !/^transcript$/i.test(l));
                            if (cleanedLines.length > 0) {
                                paragraphs.push(cleanedLines.join(' '));
                            }
                        }
                    }
                }

                // Also collect any VTT <track> URLs or downloadable transcript links as fallback
                const trackUrls = Array.from(document.querySelectorAll('video track[src]')).map(t => ({
                    src: t.src,
                    srclang: (t.getAttribute('srclang') || '').toLowerCase(),
                    label: (t.getAttribute('label') || '').toLowerCase(),
                }));
                const txtLinks = Array.from(document.querySelectorAll('a[href]'))
                    .filter(a => /transcript|subtitle|\\.vtt|\\.txt/i.test((a.innerText || '') + ' ' + (a.href || '')))
                    .map(a => a.href);

                return {
                    page_title: heading,
                    paragraphs: paragraphs,
                    content: paragraphs.join('\\n\\n').trim(),
                    track_urls: trackUrls,
                    txt_links: txtLinks,
                };
            }"""
        )

    # Wait up to 20s for transcript content or video player to load
    deadline = time.time() + 20.0
    data: dict[str, Any] = {"page_title": "", "paragraphs": [], "content": "", "track_urls": [], "txt_links": []}
    while time.time() < deadline:
        mute_and_pause_videos(page)
        try_click_transcript_tab()
        data = grab_dom_transcript()
        if len(data.get("content", "")) >= 40:
            return {
                "page_title": data["page_title"],
                "content": data["content"],
                "extraction_method": "dom_transcript",
            }
        time.sleep(1.0)

    # Fallback: try fetching WebVTT track (prefer English)
    track_urls = data.get("track_urls", [])
    if track_urls:
        track_urls.sort(key=lambda t: 0 if ("en" in t.get("srclang", "") or "english" in t.get("label", "")) else 1)
        for tr in track_urls:
            src = tr.get("src")
            if not src:
                continue
            try:
                vtt_text = page.evaluate(
                    """async (u) => {
                        const r = await fetch(u);
                        return r.ok ? await r.text() : '';
                    }""",
                    src,
                )
                parsed = parse_vtt_to_text(vtt_text or "")
                if len(parsed) >= 30:
                    return {
                        "page_title": data.get("page_title", ""),
                        "content": parsed,
                        "extraction_method": "vtt_track_fallback",
                    }
            except Exception:
                continue

    return {
        "page_title": data.get("page_title", ""),
        "content": data.get("content", ""),
        "extraction_method": "empty_transcript",
    }


def extract_reading_content(page: Page) -> dict[str, Any]:
    """
    Extract clean Markdown-structured content from a Coursera /supplement/ reading page.
    Waits past 'Loading...' for Coursera CML viewer to mount.
    """
    def grab_reading() -> dict[str, Any]:
        return page.evaluate(
            """() => {
                const heading = (
                    document.querySelector('[data-testid="reading-title"], .rc-ReadingItem h1, main h1, h1')?.innerText ||
                    document.title ||
                    ''
                ).replace(/\\s+/g, ' ').trim();

                const selectors = [
                    '.rc-ReadingItem .rc-CML',
                    '.rc-CML',
                    '[data-testid="cml-viewer"]',
                    '.rc-ReadingItem',
                    'main article',
                    '[role="main"] .rc-CML',
                ];
                let root = null;
                for (const sel of selectors) {
                    const el = document.querySelector(sel);
                    if (el && (el.innerText || '').trim().length > 30) {
                        root = el;
                        break;
                    }
                }

                if (!root) {
                    return { page_title: heading, content: '' };
                }

                // Convert structured HTML inside CML to clean Markdown
                function nodeToMd(node) {
                    if (node.nodeType === Node.TEXT_NODE) {
                        return node.textContent || '';
                    }
                    if (node.nodeType !== Node.ELEMENT_NODE) return '';
                    const tag = node.tagName.toLowerCase();
                    if (['script', 'style', 'noscript', 'svg', 'button'].includes(tag)) return '';

                    if (tag === 'pre') {
                        const code = (node.innerText || '').trim();
                        return '\\n```\\n' + code + '\\n```\\n\\n';
                    }
                    if (tag === 'code' && node.parentElement?.tagName.toLowerCase() !== 'pre') {
                        return '`' + (node.innerText || '').trim() + '`';
                    }
                    if (tag === 'h1') return '\\n## ' + (node.innerText || '').trim() + '\\n\\n';
                    if (tag === 'h2') return '\\n### ' + (node.innerText || '').trim() + '\\n\\n';
                    if (tag === 'h3' || tag === 'h4') return '\\n#### ' + (node.innerText || '').trim() + '\\n\\n';
                    if (tag === 'li') {
                        const inner = Array.from(node.childNodes).map(nodeToMd).join('').replace(/\\s+/g, ' ').trim();
                        return inner ? '- ' + inner + '\\n' : '';
                    }
                    if (tag === 'ul' || tag === 'ol') {
                        const inner = Array.from(node.childNodes).map(nodeToMd).join('');
                        return '\\n' + inner + '\\n';
                    }
                    if (tag === 'table') {
                        const rows = Array.from(node.querySelectorAll('tr')).map(tr =>
                            Array.from(tr.querySelectorAll('th, td')).map(c => (c.innerText || '').replace(/\\s+/g, ' ').trim())
                        ).filter(r => r.length > 0);
                        if (rows.length === 0) return '';
                        const out = [];
                        out.push('| ' + rows[0].join(' | ') + ' |');
                        out.push('| ' + rows[0].map(() => '---').join(' | ') + ' |');
                        for (let i = 1; i < rows.length; i++) {
                            out.push('| ' + rows[i].join(' | ') + ' |');
                        }
                        return '\\n' + out.join('\\n') + '\\n\\n';
                    }
                    if (tag === 'p') {
                        const inner = Array.from(node.childNodes).map(nodeToMd).join('').trim();
                        return inner ? inner + '\\n\\n' : '';
                    }
                    if (tag === 'br') return '\\n';

                    return Array.from(node.childNodes).map(nodeToMd).join('');
                }

                let md = nodeToMd(root).replace(/\\n{3,}/g, '\\n\\n').trim();
                if (!md) {
                    md = (root.innerText || '').trim();
                }
                return { page_title: heading, content: md };
            }"""
        )

    deadline = time.time() + 20.0
    data: dict[str, Any] = {"page_title": "", "content": ""}
    while time.time() < deadline:
        data = grab_reading()
        if len(data.get("content", "")) >= 30:
            return {
                "page_title": data["page_title"],
                "content": data["content"],
                "extraction_method": "dom_reading_cml",
            }
        time.sleep(0.8)

    return {
        "page_title": data.get("page_title", ""),
        "content": data.get("content", ""),
        "extraction_method": "empty_reading",
    }


def save_knowledge_outputs(
    output_dir: Path,
    course_info: dict[str, Any],
    items_data: list[dict[str, Any]],
) -> tuple[Path, Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    modules_dir = output_dir / "modules"
    modules_dir.mkdir(parents=True, exist_ok=True)

    json_path = output_dir / "knowledge.json"
    md_path = output_dir / "knowledge.md"

    non_empty = sum(1 for x in items_data if len((x.get("content") or "").strip()) > 0)
    total_chars = sum(len((x.get("content") or "").strip()) for x in items_data)

    payload = {
        "crawled_at": datetime.now().isoformat(),
        "course": course_info,
        "total_items_discovered": len(items_data),
        "total_items_extracted": non_empty,
        "total_videos": sum(1 for x in items_data if x.get("type") == "video"),
        "total_readings": sum(1 for x in items_data if x.get("type") == "reading"),
        "total_characters": total_chars,
        "items": items_data,
    }
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    # Group items by module_number
    by_module: dict[int, list[dict[str, Any]]] = {}
    for item in items_data:
        m_num = int(item.get("module_number", 0))
        by_module.setdefault(m_num, []).append(item)

    full_md: list[str] = [
        f"# {course_info['name']}",
        "",
        f"- **Course URL:** {course_info['url']}",
        f"- **Crawled at:** {payload['crawled_at']}",
        f"- **Extracted:** {non_empty}/{len(items_data)} items ({payload['total_videos']} videos, {payload['total_readings']} readings) | {total_chars:,} chars",
        "",
        "---",
        "",
    ]

    for mod_num in sorted(by_module.keys()):
        mod_items = by_module[mod_num]
        mod_title = mod_items[0].get("module_title", f"Module {mod_num}")
        mod_lines: list[str] = [
            f"# Module {mod_num}: {mod_title}",
            "",
        ]
        full_md.append(f"## Module {mod_num}: {mod_title}")
        full_md.append("")

        for idx, it in enumerate(mod_items, 1):
            badge = "VIDEO TRANSCRIPT" if it.get("type") == "video" else "READING"
            title = it.get("title") or it.get("page_title") or f"Item {idx}"
            content = (it.get("content") or "").strip() or "_[No content extracted]_"

            section = [
                f"### {idx}. [{badge}] {title}",
                f"- **URL:** {it.get('url')}",
                f"- **Method:** `{it.get('extraction_method', '')}` | **Length:** {len(content)} chars",
                "",
                content,
                "",
                "---",
                "",
            ]
            mod_lines.extend(section)
            full_md.extend(section)

        mod_file = modules_dir / f"module_{mod_num:02d}.md"
        mod_file.write_text("\n".join(mod_lines), encoding="utf-8")

    md_path.write_text("\n".join(full_md), encoding="utf-8")
    return json_path, md_path


def crawl_course_knowledge(
    course_key: str,
    custom_url: str | None = None,
    profile_dir: Path | None = None,
    output_root: Path | None = None,
    login_timeout: int = 300,
    wait_enter: bool = False,
    resume: bool = True,
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
    local_app_data = os.environ.get("LOCALAPPDATA")
    default_profile = (
        Path(local_app_data) / "coursera_quiz_crawler_profile"
        if local_app_data
        else Path.home() / ".coursera_quiz_crawler_profile"
    )
    profile_path = profile_dir or default_profile
    out_dir = (output_root or (base_dir / "knowledge")) / f"{course_info['key']}_{course_info['slug']}"

    log(f"Starting KNOWLEDGE crawler for: {course_info['name']}")
    log(f"Browser profile dir: {profile_path}")
    log(f"Output dir: {out_dir}")

    # Load existing successful items for auto-resume
    existing_by_url: dict[str, dict[str, Any]] = {}
    existing_json = out_dir / "knowledge.json"
    if resume and existing_json.exists():
        try:
            prev = json.loads(existing_json.read_text(encoding="utf-8"))
            for prev_item in prev.get("items", []):
                if prev_item.get("url") and int(prev_item.get("char_count", 0)) > 0:
                    existing_by_url[prev_item["url"]] = prev_item
            if existing_by_url:
                log(f"Auto-resume loaded {len(existing_by_url)} already-extracted item(s) from previous run.")
        except Exception as e:
            log(f"Warning loading existing knowledge.json for resume: {e}")

    items_data: list[dict[str, Any]] = []

    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir=str(profile_path),
            channel="msedge",
            headless=False,
            viewport={"width": 1400, "height": 900},
            args=["--disable-blink-features=AutomationControlled", "--mute-audio"],
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

            discovered = discover_knowledge_items(page, course_info["url"], course_info["slug"])

            for idx, item in enumerate(discovered, 1):
                if item["url"] in existing_by_url:
                    cached = dict(existing_by_url[item["url"]])
                    # Refresh module_title and title from latest discovery
                    cached["module_number"] = item["module_number"]
                    cached["module_title"] = item["module_title"]
                    cached["title"] = item["title"]
                    items_data.append(cached)
                    log(
                        f"[{idx}/{len(discovered)}] [M{item['module_number']}][{item['type']}] "
                        f"SKIP (cached {cached['char_count']} chars): {item['title']}"
                    )
                    continue

                log(
                    f"[{idx}/{len(discovered)}] [M{item['module_number']}][{item['type']}] "
                    f"{item['title']} -> {item['url']}"
                )
                try:
                    content = ""
                    method = "unknown"
                    extracted: dict[str, Any] = {}
                    for retry_attempt in range(2):
                        safe_goto(page, item["url"], timeout=60000)
                        if item["type"] == "video":
                            extracted = extract_video_transcript(page)
                        else:
                            extracted = extract_reading_content(page)
                        content = (extracted.get("content") or "").replace("\u200b", "").strip()
                        method = extracted.get("extraction_method", "unknown")
                        if content:
                            break
                        if retry_attempt == 0:
                            log("  -> Empty content on first try, reloading once...")
                            time.sleep(2)

                    log(f"  -> {method} | {len(content)} chars")

                    items_data.append(
                        {
                            **item,
                            "page_title": extracted.get("page_title", ""),
                            "extraction_method": method,
                            "char_count": len(content),
                            "content": content,
                        }
                    )
                    save_knowledge_outputs(out_dir, course_info, items_data)
                except Exception as e:
                    log(f"  -> Error on '{item['title']}': {e}")
                    items_data.append(
                        {
                            **item,
                            "page_title": "",
                            "extraction_method": f"error: {e}",
                            "char_count": 0,
                            "content": "",
                        }
                    )
                    save_knowledge_outputs(out_dir, course_info, items_data)
        finally:
            json_path, md_path = save_knowledge_outputs(out_dir, course_info, items_data)
            log(f"\nSaved JSON: {json_path}")
            log(f"Saved MD  : {md_path}")
            context.close()

    return json_path, md_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Coursera Course Knowledge Crawler (Transcripts & Readings)")
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
        "--login-timeout",
        type=int,
        default=300,
        help="Seconds to wait for manual login if session expired (default: 300)",
    )
    parser.add_argument(
        "--wait-enter",
        action="store_true",
        help="Wait for user to press Enter after manual login",
    )
    parser.add_argument(
        "--no-resume",
        action="store_true",
        help="Ignore cached items in existing knowledge.json and re-crawl everything",
    )
    args = parser.parse_args()

    crawl_course_knowledge(
        course_key=args.course,
        custom_url=args.url,
        login_timeout=args.login_timeout,
        wait_enter=args.wait_enter,
        resume=not args.no_resume,
    )


if __name__ == "__main__":
    main()

/**
 * DWP301c Codex — Frontend Controller
 * Zero-dependency ES module: clean Markdown renderer, FTS5 Command Palette (Ctrl+K),
 * syllabus accordion, reading progress bar, interactive quiz practice, and theme switcher.
 */

const state = {
  courses: [],
  activeCourseKey: "coursera8",
  courseData: null,
  mode: "overview", // overview | guides | reader | cheatsheets | quizzes
  filter: "all",
  activeModuleNumber: 1,
  activeLessonId: null,
  activeLessonData: null,
  openModules: new Set([1]),
  quizzesData: null,
  quizModuleFilter: "all",
  quizPicks: {}, // questionId -> Set of option indices
  quizRevealed: new Set(),
  searchSelectedIdx: 0,
  searchHits: [],
};

// DOM References
const $ = (sel) => document.querySelector(sel);
const $$ = (sel) => Array.from(document.querySelectorAll(sel));

const el = {
  readProgressBar: $("#readProgressBar"),
  mobileMenuBtn: $("#mobileMenuBtn"),
  sidebarBackdrop: $("#sidebarBackdrop"),
  syllabusRail: $("#syllabusRail"),
  syllabusTree: $("#syllabusTree"),
  stageContainer: $("#stageContainer"),
  tocRail: $("#tocRail"),
  tocList: $("#tocList"),
  courseSwitcherBtn: $("#courseSwitcherBtn"),
  activeCourseLabel: $("#activeCourseLabel"),
  courseMenuPopover: $("#courseMenuPopover"),
  headerProgressText: $("#headerProgressText"),
  themeToggleBtn: $("#themeToggleBtn"),
  themeIconSun: $("#themeIconSun"),
  themeIconMoon: $("#themeIconMoon"),
  searchTriggerBtn: $("#searchTriggerBtn"),
  searchDialog: $("#searchDialog"),
  searchInput: $("#searchInput"),
  searchResults: $("#searchResults"),
  searchCloseBtn: $("#searchCloseBtn"),
  toast: $("#toast"),
};

// Consistent SVG icons (1.75px stroke, zero emoji)
const ICONS = {
  video: `<svg class="lesson-nav-icon" viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><polygon points="6 4 20 12 6 20 6 4"/></svg>`,
  reading: `<svg class="lesson-nav-icon" viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1 0-5H20"/></svg>`,
  check: `<svg class="lesson-nav-icon" viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>`,
  chevron: `<svg class="mod-chevron" viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"/></svg>`,
  bookmark: `<svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/></svg>`,
  checkCircle: `<svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>`,
  external: `<svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>`,
};

function escapeHtml(str) {
  return String(str || "")
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

function showToast(msg) {
  el.toast.textContent = msg;
  el.toast.classList.remove("hidden");
  clearTimeout(showToast._timer);
  showToast._timer = setTimeout(() => el.toast.classList.add("hidden"), 2200);
}

// =========================================================================
// Lightweight Zero-Dependency Markdown Renderer (headings, code, tables, lists)
// =========================================================================
function renderInline(text) {
  const codeSlots = [];
  // Protect inline code spans before escaping & bold/italic formatting so `*` or `<br>` inside code stays intact
  const withPlaceholders = String(text || "").replace(/`([^`]+)`/g, (_, code) => {
    const idx = codeSlots.length;
    codeSlots.push(`<code>${escapeHtml(code)}</code>`);
    return `\u0000CODE${idx}\u0000`;
  });

  let out = escapeHtml(withPlaceholders);
  // Allow explicit Markdown table line breaks (<br> / <br/>) outside inline code
  out = out.replace(/&lt;br\s*\/?&gt;/gi, "<br>");
  // Bold
  out = out.replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>");
  // Italic
  out = out.replace(/(^|[^*])\*([^*]+)\*/g, "$1<em>$2</em>");
  // Restore protected inline code spans
  out = out.replace(/\u0000CODE(\d+)\u0000/g, (_, idx) => codeSlots[Number(idx)] || "");
  return out;
}

function renderMarkdown(md) {
  const lines = String(md || "").replace(/\r\n/g, "\n").split("\n");
  const html = [];
  const headings = [];
  let i = 0;

  while (i < lines.length) {
    const line = lines[i];

    // Fenced code block
    if (line.trim().startsWith("```")) {
      const lang = line.trim().slice(3).trim() || "code";
      const codeLines = [];
      i++;
      while (i < lines.length && !lines[i].trim().startsWith("```")) {
        codeLines.push(lines[i]);
        i++;
      }
      i++; // skip closing ```
      const codeText = codeLines.join("\n");
      html.push(
        `<div class="code-block-wrap">
          <div class="code-block-head">
            <span>${escapeHtml(lang)}</span>
            <button type="button" class="copy-code-btn" data-copy>Copy</button>
          </div>
          <pre><code>${escapeHtml(codeText)}</code></pre>
        </div>`
      );
      continue;
    }

    // Markdown table
    if (
      line.trim().startsWith("|") &&
      i + 1 < lines.length &&
      /^\|\s*[-:]+/.test(lines[i + 1].trim())
    ) {
      const parseRow = (row) =>
        row
          .trim()
          .replace(/^\|/, "")
          .replace(/\|$/, "")
          .split("|")
          .map((c) => renderInline(c.trim()));

      const headerCells = parseRow(line);
      i += 2; // skip header & separator
      const bodyRows = [];
      while (i < lines.length && lines[i].trim().startsWith("|")) {
        bodyRows.push(parseRow(lines[i]));
        i++;
      }
      html.push(
        `<div class="table-scroll"><table><thead><tr>${headerCells
          .map((c) => `<th>${c}</th>`)
          .join("")}</tr></thead><tbody>${bodyRows
          .map((r) => `<tr>${r.map((c) => `<td>${c}</td>`).join("")}</tr>`)
          .join("")}</tbody></table></div>`
      );
      continue;
    }

    // Headings
    const hMatch = line.match(/^(#{1,4})\s+(.+)$/);
    if (hMatch) {
      const level = Math.min(4, Math.max(2, hMatch[1].length));
      const rawText = hMatch[2].trim();
      const id = `sec-${headings.length + 1}-${rawText
        .toLowerCase()
        .replace(/[^a-z0-9]+/g, "-")
        .slice(0, 32)}`;
      headings.push({ id, text: rawText, level });
      html.push(`<h${level} id="${id}">${renderInline(rawText)}</h${level}>`);
      i++;
      continue;
    }

    // Blockquote
    if (line.trim().startsWith(">")) {
      const qLines = [];
      while (i < lines.length && lines[i].trim().startsWith(">")) {
        qLines.push(lines[i].trim().replace(/^>\s?/, ""));
        i++;
      }
      html.push(`<blockquote><p>${renderInline(qLines.join(" "))}</p></blockquote>`);
      continue;
    }

    // Unordered list
    if (/^\s*[-*]\s+/.test(line)) {
      const items = [];
      while (i < lines.length && /^\s*[-*]\s+/.test(lines[i])) {
        items.push(`<li>${renderInline(lines[i].replace(/^\s*[-*]\s+/, ""))}</li>`);
        i++;
      }
      html.push(`<ul>${items.join("")}</ul>`);
      continue;
    }

    // Ordered list
    if (/^\s*\d+\.\s+/.test(line)) {
      const items = [];
      while (i < lines.length && /^\s*\d+\.\s+/.test(lines[i])) {
        items.push(`<li>${renderInline(lines[i].replace(/^\s*\d+\.\s+/, ""))}</li>`);
        i++;
      }
      html.push(`<ol>${items.join("")}</ol>`);
      continue;
    }

    // Empty line
    if (!line.trim()) {
      i++;
      continue;
    }

    // Paragraph (collect consecutive non-special lines)
    const para = [];
    while (
      i < lines.length &&
      lines[i].trim() &&
      !lines[i].trim().startsWith("```") &&
      !lines[i].trim().startsWith("|") &&
      !lines[i].trim().startsWith(">") &&
      !/^#{1,4}\s+/.test(lines[i]) &&
      !/^\s*[-*]\s+/.test(lines[i]) &&
      !/^\s*\d+\.\s+/.test(lines[i])
    ) {
      para.push(lines[i].trim());
      i++;
    }
    html.push(`<p>${renderInline(para.join(" "))}</p>`);
  }

  return { html: html.join("\n"), headings };
}

// =========================================================================
// API Client
// =========================================================================
async function api(path, options = {}) {
  const res = await fetch(path, {
    headers: { "Content-Type": "application/json" },
    ...options,
  });
  if (!res.ok) {
    throw new Error(`API ${res.status}: ${path}`);
  }
  return res.json();
}

// =========================================================================
// Theme Management
// =========================================================================
function initTheme() {
  const saved = localStorage.getItem("dwp301c_theme") || "light";
  applyTheme(saved);
}

function applyTheme(theme) {
  document.documentElement.setAttribute("data-theme", theme);
  localStorage.setItem("dwp301c_theme", theme);
  el.themeIconSun.classList.toggle("hidden", theme === "dark");
  el.themeIconMoon.classList.toggle("hidden", theme !== "dark");
}

// =========================================================================
// Rendering: Course Switcher & Syllabus Rail
// =========================================================================
function renderCourseSwitcher() {
  const active = state.courses.find((c) => c.key === state.activeCourseKey);
  if (active) {
    el.activeCourseLabel.textContent = `C${active.course_order} · ${active.short_name}`;
    el.headerProgressText.textContent = `${active.completed_lessons}/${active.total_lessons}`;
  }

  el.courseMenuPopover.innerHTML = state.courses
    .map((c) => {
      const selected = c.key === state.activeCourseKey ? "is-selected" : "";
      const disabled = !c.is_seeded ? "disabled" : "";
      const badge = c.is_seeded
        ? `<span class="status-badge is-live">Live · ${c.total_lessons}</span>`
        : `<span class="status-badge is-ready">Ready</span>`;
      const sub = c.is_seeded
        ? `${c.total_modules} modules · ${c.total_videos} videos · ${c.total_readings} readings · ${c.total_questions} quiz Qs`
        : `Crawled & ready to import via seed_db.py --all`;
      return `
        <button class="course-option ${selected}" data-course-key="${c.key}" ${disabled} role="option">
          <div>
            <div class="course-option-title">Course ${c.course_order}: ${escapeHtml(c.name)}</div>
            <div class="course-option-sub">${sub}</div>
          </div>
          ${badge}
        </button>`;
    })
    .join("");
}

function renderSyllabus() {
  if (!state.courseData) return;
  const { modules } = state.courseData;
  const f = state.filter;

  const html = modules
    .map((mod) => {
      const filteredLessons = mod.lessons.filter((l) => {
        if (f === "all") return true;
        if (f === "bookmarked") return l.is_bookmarked;
        if (f === "cheat_sheet") return l.category === "cheat_sheet";
        return l.item_type === f;
      });
      if (filteredLessons.length === 0) return "";

      const isOpen = state.openModules.has(mod.module_number) || f !== "all";
      const guideActive = state.mode === "guides" && state.activeModuleNumber === mod.module_number ? "is-active" : "";
      const guideRow = mod.has_guide
        ? `<button class="guide-nav-item ${guideActive}" data-open-module-guide="${mod.module_number}">
            <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>
            <span>Module ${mod.module_number} Study Guide</span>
          </button>`
        : "";
      const rows = filteredLessons
        .map((l) => {
          const active = state.mode === "reader" && state.activeLessonId === l.id ? "is-active" : "";
          const done = l.is_completed ? "is-done" : "";
          const icon = l.is_completed ? ICONS.check : l.item_type === "video" ? ICONS.video : ICONS.reading;
          return `
            <button class="lesson-nav-item ${active} ${done}" data-lesson-id="${l.id}">
              ${icon}
              <span class="lesson-nav-text">${escapeHtml(l.title)}</span>
              <span class="lesson-nav-meta tabular">${l.read_minutes}m</span>
            </button>`;
        })
        .join("");

      return `
        <div class="mod-group ${isOpen ? "is-open" : ""}" data-mod-num="${mod.module_number}">
          <button class="mod-trigger" data-toggle-mod="${mod.module_number}" aria-expanded="${isOpen}">
            <span class="mod-trigger-left">
              <span class="mod-num">M${mod.module_number}</span>
              <span class="mod-name">${escapeHtml(mod.title)}</span>
            </span>
            ${ICONS.chevron}
          </button>
          <div class="mod-lessons-wrap">
            <div class="mod-lessons-inner">${guideRow}${rows}</div>
          </div>
        </div>`;
    })
    .join("");

  el.syllabusTree.innerHTML =
    html ||
    `<div class="search-empty">No lessons match this filter yet. Try switching back to <strong>All</strong>.</div>`;
}

// =========================================================================
// Rendering: Main Stage Views
// =========================================================================
function setActiveModeTab(mode) {
  state.mode = mode;
  $$(".mode-tab").forEach((btn) => {
    btn.classList.toggle("is-active", btn.dataset.mode === mode);
  });
  el.tocRail.classList.toggle("hidden", mode !== "reader" && mode !== "guides");
}

function animateStageSwap(html) {
  el.stageContainer.style.animation = "none";
  el.stageContainer.innerHTML = html;
  void el.stageContainer.offsetWidth;
  el.stageContainer.style.animation = "";
  window.scrollTo({ top: 0, behavior: "instant" });
  updateScrollProgress();
}

function renderOverview() {
  if (!state.courseData) return;
  setActiveModeTab("overview");
  const { course, modules } = state.courseData;
  const cheatSheets = modules.flatMap((m) => m.lessons.filter((l) => l.category === "cheat_sheet"));
  const synthesizedCount = modules.filter((m) => m.has_guide).length;

  const roadmapHtml = modules
    .map((m) => {
      const previewLessons = m.lessons.slice(0, 5);
      const moreCount = m.lessons.length - previewLessons.length;
      const chips = previewLessons
        .map((l) => {
          const isSheet = l.category === "cheat_sheet" ? "is-sheet" : "";
          return `<button class="lesson-pill ${isSheet}" data-open-lesson="${l.id}">${escapeHtml(l.title)}</button>`;
        })
        .join("");

      return `
        <div class="roadmap-row">
          <div class="roadmap-mod-tag">Module ${m.module_number}</div>
          <div>
            <h3 class="roadmap-title">${escapeHtml(m.title)}</h3>
            ${m.guide_summary ? `<p class="roadmap-summary">${renderInline(m.guide_summary)}</p>` : ""}
            <div class="roadmap-stats tabular">
              ${m.has_guide ? `<strong>Study Guide (${m.guide_read_minutes}m)</strong> · ` : ""}${m.total_lessons} source items${m.quiz_questions ? ` · ${m.quiz_questions} quiz Qs` : ""} · ${m.completed_lessons}/${m.total_lessons} read
            </div>
            <div class="roadmap-chips">
              ${chips}
              ${moreCount > 0 ? `<button class="lesson-pill" data-open-lesson="${m.lessons[5].id}">+${moreCount} source items</button>` : ""}
            </div>
          </div>
          <div>
            ${
              m.has_guide
                ? `<button class="btn btn-primary btn-sm" data-open-module-guide="${m.module_number}">Study Guide</button>`
                : m.lessons[0]
                ? `<button class="btn btn-ghost btn-sm" data-open-lesson="${m.lessons[0].id}">Open</button>`
                : ""
            }
          </div>
        </div>`;
    })
    .join("");

  const curriculumRows = state.courses
    .map((c) => {
      const isCurrent = c.key === course.key ? "is-current" : "";
      const status = c.is_seeded
        ? `<span class="status-badge is-live">Active · Synthesized</span>`
        : `<span class="status-badge is-ready">Ready to Import</span>`;
      return `
        <tr class="${isCurrent}">
          <td class="tabular"><strong>C${c.course_order}</strong></td>
          <td>${escapeHtml(c.name)}</td>
          <td class="tabular">${c.is_seeded ? `${c.total_modules} guides · ${c.total_lessons} sources` : "Crawled"}</td>
          <td class="tabular">${c.is_seeded ? `${c.total_questions} Qs` : "Crawled"}</td>
          <td>${status}</td>
        </tr>`;
    })
    .join("");

  animateStageSwap(`
    <section class="course-hero">
      <h1>${escapeHtml(course.name)}</h1>
      <p class="course-hero-lead">
        Kiến thức đã được hệ thống hóa bài bản thành ${synthesizedCount} Module Study Guides (tư duy nền tảng, bảng so sánh phản biện, code mẫu chuẩn &amp; bẫy thi) dựa trên toàn bộ ${course.total_videos} video transcripts, ${course.total_readings} readings và ${course.total_questions} câu hỏi trắc nghiệm gốc.
      </p>
      <div class="course-meta-strip tabular">
        <span class="course-meta-item"><strong>${synthesizedCount}</strong> Synthesized Module Guides</span>
        <span class="course-meta-item"><strong>${course.total_lessons}</strong> Source Items</span>
        <span class="course-meta-item"><strong>${cheatSheets.length}</strong> Cheat Sheets</span>
        <span class="course-meta-item"><strong>${course.total_questions}</strong> Quiz Questions</span>
      </div>
      <div class="hero-actions">
        <button class="btn btn-primary" data-open-module-guide="1">Start Module 1 Study Guide</button>
        <button class="btn btn-secondary" data-switch-mode="cheatsheets">Cheat Sheets (${cheatSheets.length})</button>
        <button class="btn btn-secondary" data-switch-mode="quizzes">Practice Quizzes (${course.total_questions} Qs)</button>
      </div>
    </section>

    <section>
      <h2 class="section-heading">Synthesized Module Roadmap</h2>
      <div class="roadmap-list">${roadmapHtml}</div>
    </section>

    <section class="curriculum-section">
      <h2 class="section-heading">Full ${state.courses.length}-Course DWP301c Architecture (FLM Track)</h2>
      <div class="table-scroll">
        <table class="curriculum-table">
          <thead>
            <tr>
              <th>#</th>
              <th>Course Title</th>
              <th>Knowledge</th>
              <th>Quizzes</th>
              <th>Status</th>
            </tr>
          </thead>
          <tbody>${curriculumRows}</tbody>
        </table>
      </div>
    </section>
  `);
  renderSyllabus();
}

async function openModuleGuide(moduleNumber) {
  setActiveModeTab("guides");
  state.activeModuleNumber = Number(moduleNumber);
  state.openModules.add(state.activeModuleNumber);
  closeMobileSidebar();

  el.stageContainer.innerHTML = `
    <div class="skeleton-stack">
      <div class="skeleton-line w-65"></div>
      <div class="skeleton-line w-100"></div>
      <div class="skeleton-line w-85"></div>
    </div>`;

  const data = await api(`/api/courses/${state.activeCourseKey}/modules/${moduleNumber}`);
  const { course, module: mod, source_lessons, quiz_questions, prev_module, next_module } = data;

  // Strip leading H1 from markdown because we render a dedicated header
  const cleanedMd = (mod.guide_md || "").replace(/^#\s+[^\n]+\n+/, "");
  const { html: bodyHtml, headings } = renderMarkdown(cleanedMd);

  const modPills = (state.courseData?.modules || [])
    .map(
      (m) => `
      <button type="button" class="mod-pill-btn ${m.module_number === mod.module_number ? "is-active" : ""}" data-open-module-guide="${m.module_number}">
        <span>M${m.module_number}</span>
      </button>`
    )
    .join("");

  const sourceRows = source_lessons
    .map(
      (l, idx) => `
      <button type="button" class="lesson-nav-item" data-open-lesson="${l.id}">
        ${l.item_type === "video" ? ICONS.video : ICONS.reading}
        <span class="lesson-nav-text">${idx + 1}. ${escapeHtml(l.title)}</span>
        <span class="lesson-nav-meta tabular">${l.read_minutes}m · ${l.char_count.toLocaleString()} ch</span>
      </button>`
    )
    .join("");

  animateStageSwap(`
    <div class="module-switcher-bar" role="tablist" aria-label="Switch module study guide">
      ${modPills}
    </div>

    <article>
      <div class="reader-breadcrumb">
        <button type="button" data-switch-mode="overview">${escapeHtml(course.name)}</button>
        <span>/</span>
        <span>Module ${mod.module_number} Study Guide</span>
      </div>

      <header class="reader-header">
        <h1 class="reader-title">Module ${mod.module_number}: ${escapeHtml(mod.title)}</h1>
        <div class="reader-toolbar">
          <div class="reader-meta tabular">
            <span class="type-badge is-video">Synthesized Study Guide</span>
            <span>${mod.guide_read_minutes} min read</span>
            <span>Compiled from ${source_lessons.length} sources</span>
          </div>
          <div class="reader-actions">
            ${
              quiz_questions > 0
                ? `<button type="button" class="btn btn-secondary btn-sm" data-open-mod-quiz="${mod.module_number}">Practice Module ${mod.module_number} Quiz (${quiz_questions} Qs)</button>`
                : ""
            }
          </div>
        </div>
      </header>

      <div class="prose">${bodyHtml}</div>

      <details class="source-drawer">
        <summary>
          <span>Original Coursera Source Material (${source_lessons.length} transcripts &amp; readings)</span>
          <span class="lesson-nav-meta">Expand</span>
        </summary>
        <div class="source-drawer-list">${sourceRows}</div>
      </details>

      <footer class="reader-footer">
        ${
          prev_module
            ? `<button class="nav-pager-btn" data-open-module-guide="${prev_module.module_number}">
                <span class="nav-pager-label">← Previous Study Guide</span>
                <span class="nav-pager-title">Module ${prev_module.module_number}: ${escapeHtml(prev_module.title)}</span>
              </button>`
            : `<div></div>`
        }
        ${
          next_module
            ? `<button class="nav-pager-btn is-next" data-open-module-guide="${next_module.module_number}">
                <span class="nav-pager-label">Next Study Guide →</span>
                <span class="nav-pager-title">Module ${next_module.module_number}: ${escapeHtml(next_module.title)}</span>
              </button>`
            : `<div></div>`
        }
      </footer>
    </article>
  `);

  if (headings.length >= 2) {
    el.tocRail.classList.remove("hidden");
    el.tocList.innerHTML = headings
      .map(
        (h) =>
          `<li><a class="toc-link" href="#${h.id}" style="padding-left:${h.level > 2 ? 22 : 12}px">${escapeHtml(h.text)}</a></li>`
      )
      .join("");
  } else {
    el.tocRail.classList.add("hidden");
  }

  renderSyllabus();
}

async function openLesson(lessonId) {
  setActiveModeTab("reader");
  state.activeLessonId = Number(lessonId);
  closeMobileSidebar();

  el.stageContainer.innerHTML = `
    <div class="skeleton-stack">
      <div class="skeleton-line w-65"></div>
      <div class="skeleton-line w-100"></div>
      <div class="skeleton-line w-85"></div>
      <div class="skeleton-line w-100"></div>
    </div>`;

  const data = await api(`/api/lessons/${lessonId}`);
  state.activeLessonData = data;
  const { lesson, prev_lesson, next_lesson } = data;
  state.openModules.add(lesson.module_number);

  const { html: bodyHtml, headings } = renderMarkdown(lesson.content_md);
  const typeClass = lesson.item_type === "video" ? "is-video" : "is-reading";
  const typeLabel =
    lesson.category === "cheat_sheet"
      ? "Cheat Sheet"
      : lesson.item_type === "video"
      ? "Video Transcript"
      : "Reading";

  animateStageSwap(`
    <article>
      <div class="reader-breadcrumb">
        <button type="button" data-switch-mode="overview">${escapeHtml(lesson.course_name)}</button>
        <span>/</span>
        <span>Module ${lesson.module_number}: ${escapeHtml(lesson.module_title)}</span>
      </div>

      <header class="reader-header">
        <h1 class="reader-title">${escapeHtml(lesson.title)}</h1>
        <div class="reader-toolbar">
          <div class="reader-meta tabular">
            <span class="type-badge ${typeClass}">${typeLabel}</span>
            <span>${lesson.read_minutes} min read</span>
            <span>${lesson.char_count.toLocaleString()} chars</span>
            <a href="${escapeHtml(lesson.url)}" target="_blank" rel="noopener noreferrer" style="display:inline-flex;align-items:center;gap:4px;">
              Coursera ${ICONS.external}
            </a>
          </div>
          <div class="reader-actions">
            <button id="toggleBookmarkBtn" class="btn btn-ghost btn-sm btn-state ${lesson.is_bookmarked ? "is-saved" : ""}">
              ${ICONS.bookmark}
              <span>${lesson.is_bookmarked ? "Saved" : "Save"}</span>
            </button>
            <button id="toggleCompleteBtn" class="btn btn-ghost btn-sm btn-state ${lesson.is_completed ? "is-done" : ""}">
              ${ICONS.checkCircle}
              <span>${lesson.is_completed ? "Completed" : "Mark read"}</span>
            </button>
          </div>
        </div>
      </header>

      <div class="prose">${bodyHtml}</div>

      <footer class="reader-footer">
        ${
          prev_lesson
            ? `<button class="nav-pager-btn" data-open-lesson="${prev_lesson.id}">
                <span class="nav-pager-label">← Previous · Module ${prev_lesson.module_number}</span>
                <span class="nav-pager-title">${escapeHtml(prev_lesson.title)}</span>
              </button>`
            : `<div></div>`
        }
        ${
          next_lesson
            ? `<button class="nav-pager-btn is-next" data-open-lesson="${next_lesson.id}">
                <span class="nav-pager-label">Next · Module ${next_lesson.module_number} →</span>
                <span class="nav-pager-title">${escapeHtml(next_lesson.title)}</span>
              </button>`
            : `<div></div>`
        }
      </footer>
    </article>
  `);

  // Render On-Page TOC
  if (headings.length >= 2) {
    el.tocRail.classList.remove("hidden");
    el.tocList.innerHTML = headings
      .map(
        (h) =>
          `<li><a class="toc-link" href="#${h.id}" style="padding-left:${h.level > 2 ? 22 : 12}px">${escapeHtml(h.text)}</a></li>`
      )
      .join("");
  } else {
    el.tocRail.classList.add("hidden");
  }

  renderSyllabus();
}

async function renderCheatSheetsView() {
  if (!state.courseData) return;
  setActiveModeTab("cheatsheets");

  const sheets = state.courseData.modules.flatMap((m) =>
    m.lessons
      .filter((l) => l.category === "cheat_sheet" || l.category === "summary")
      .map((l) => ({ ...l, module_title: m.title }))
  );

  // Fetch full contents of cheat sheets in parallel
  const fullSheets = await Promise.all(
    sheets.filter((s) => s.category === "cheat_sheet").map((s) => api(`/api/lessons/${s.id}`))
  );

  const blocks = fullSheets
    .map(({ lesson }) => {
      const { html } = renderMarkdown(lesson.content_md);
      return `
        <section style="margin-bottom: 44px; padding-bottom: 32px; border-bottom: 1px solid var(--border-subtle);">
          <div class="reader-breadcrumb">
            <span>Module ${lesson.module_number}</span>
            <span>·</span>
            <span>${escapeHtml(lesson.module_title)}</span>
          </div>
          <h2 class="section-heading" style="margin-bottom: 14px;">${escapeHtml(lesson.title)}</h2>
          <div class="prose" style="max-width: 100%;">${html}</div>
        </section>`;
    })
    .join("");

  animateStageSwap(`
    <header class="course-hero">
      <h1>Quick Reference Cheat Sheets</h1>
      <p class="course-hero-lead">All ${fullSheets.length} official module cheat sheets consolidated into one searchable, copyable engineering reference.</p>
    </header>
    ${blocks || `<p class="muted">No cheat sheets found for this course.</p>`}
  `);
}

function findQuizQuestionById(qId) {
  const quizzes = state.quizzesData?.quizzes || [];
  for (const qz of quizzes) {
    const found = qz.questions.find((q) => q.id === qId);
    if (found) return found;
  }
  return null;
}

function buildQuestionInnerHtml(q) {
  const picked = state.quizPicks[q.id] || new Set();
  const revealed = state.quizRevealed.has(q.id);
  const correctSet = new Set(
    q.options.map((o, i) => (o.checked ? i : -1)).filter((i) => i >= 0)
  );
  const hasKey = correctSet.size > 0;

  let statusBadge = "";
  if (revealed && hasKey && picked.size > 0) {
    const isExact =
      picked.size === correctSet.size && [...picked].every((i) => correctSet.has(i));
    statusBadge = isExact
      ? `<span class="question-status-pill is-ok">Correct</span>`
      : `<span class="question-status-pill is-bad">Review</span>`;
  }

  const optsHtml = q.options
    .map((opt, idx) => {
      let cls = "";
      if (revealed && hasKey) {
        if (opt.checked) cls = "is-correct";
        else if (picked.has(idx)) cls = "is-wrong";
      } else if (picked.has(idx)) {
        cls = "is-picked";
      }
      const letter = String.fromCharCode(65 + idx);
      return `
        <button type="button" class="option-btn ${cls}" data-pick-q="${q.id}" data-pick-opt="${idx}" data-q-type="${q.question_type}">
          <span class="option-index">${letter}.</span>
          <span>${escapeHtml(opt.text)}</span>
        </button>`;
    })
    .join("");

  const correctLetters = [...correctSet].map((i) => String.fromCharCode(65 + i)).join(", ");
  const explanationHtml =
    revealed && (hasKey || q.explanation)
      ? `<div class="question-explanation">
          ${hasKey ? `<strong>Đáp án đúng (${correctLetters}):</strong> ` : ""}
          ${renderInline(q.explanation || "Đã đối chiếu theo tài liệu khóa học.")}
        </div>`
      : "";

  return `
    <p class="question-prompt">${q.q_index}. ${escapeHtml(q.prompt_text)}</p>
    <div class="question-options">${optsHtml}</div>
    <div class="question-actions">
      <div style="display:flex;align-items:center;gap:8px;">
        <span>${q.question_type === "multiple_select" ? "Multiple select" : "Single choice"}</span>
        ${statusBadge}
      </div>
      ${
        hasKey
          ? `<button type="button" class="btn btn-ghost btn-sm" data-reveal-q="${q.id}">${revealed ? "Hide answer" : "Check answer"}</button>`
          : `<span>Self-check against module notes</span>`
      }
    </div>
    ${explanationHtml}
  `;
}

function updateQuestionCardInPlace(qId, focusSelector = null) {
  const card = el.stageContainer.querySelector(`.question-item[data-q-card="${qId}"]`);
  const q = findQuizQuestionById(qId);
  if (!card || !q) return;

  const savedScrollY = window.scrollY;
  card.innerHTML = buildQuestionInnerHtml(q);

  if (focusSelector) {
    const focusEl = card.querySelector(focusSelector);
    if (focusEl) {
      focusEl.focus({ preventScroll: true });
    }
  }
  if (Math.abs(window.scrollY - savedScrollY) > 2) {
    window.scrollTo({ top: savedScrollY, behavior: "instant" });
  }
  requestAnimationFrame(() => {
    if (Math.abs(window.scrollY - savedScrollY) > 2) {
      window.scrollTo({ top: savedScrollY, behavior: "instant" });
    }
  });
}

async function renderQuizzesView() {
  setActiveModeTab("quizzes");
  if (!state.quizzesData || state.quizzesData.course.key !== state.activeCourseKey) {
    state.quizzesData = await api(`/api/courses/${state.activeCourseKey}/quizzes`);
  }

  const allQuizzes = state.quizzesData.quizzes || [];
  const modNums = [...new Set(allQuizzes.map((q) => q.module_number))].sort((a, b) => a - b);
  const visibleQuizzes =
    state.quizModuleFilter === "all"
      ? allQuizzes
      : allQuizzes.filter((q) => String(q.module_number) === String(state.quizModuleFilter));

  const filterButtons = [
    `<button class="filter-chip ${state.quizModuleFilter === "all" ? "is-active" : ""}" data-quiz-mod="all">All Modules (${allQuizzes.length})</button>`,
    ...modNums.map(
      (n) =>
        `<button class="filter-chip ${String(state.quizModuleFilter) === String(n) ? "is-active" : ""}" data-quiz-mod="${n}">Module ${n}</button>`
    ),
  ].join("");

  const quizBlocks = visibleQuizzes
    .map((qz) => {
      const qsHtml = qz.questions
        .map(
          (q) => `<div class="question-item" data-q-card="${q.id}">${buildQuestionInnerHtml(q)}</div>`
        )
        .join("");

      return `
        <section class="quiz-block">
          <div class="quiz-block-header">
            <h2 class="quiz-block-title">${escapeHtml(qz.title)}</h2>
            <span class="type-badge ${qz.kind === "graded_quiz" ? "is-video" : "is-reading"}">
              Module ${qz.module_number} · ${qz.question_count} Qs
            </span>
          </div>
          ${qsHtml}
        </section>`;
    })
    .join("");

  animateStageSwap(`
    <header class="course-hero" style="margin-bottom:20px;">
      <h1>Practice Quiz Workbench</h1>
      <p class="course-hero-lead">Toàn bộ ${allQuizzes.reduce((a, b) => a + b.question_count, 0)} câu hỏi trắc nghiệm của ${escapeHtml(state.quizzesData.course.name)} — thống nhất đầy đủ đáp án đúng và giải thích chi tiết.</p>
    </header>
    <div class="quiz-filter-bar">
      <div class="rail-filter-group">${filterButtons}</div>
    </div>
    ${quizBlocks}
  `);
}

// =========================================================================
// Command Palette Search (SQLite FTS5)
// =========================================================================
function openSearchDialog() {
  if (!el.searchDialog.open) {
    el.searchDialog.showModal();
  }
  el.searchInput.focus();
  el.searchInput.select();
}

let searchTimer = null;
async function runSearch(query) {
  const q = query.trim();
  if (!q) {
    state.searchHits = [];
    el.searchResults.innerHTML = `<div class="search-empty">Type any keyword (e.g. <code>SELECT</code>, <code>ORM</code>, <code>ForeignKey</code>, <code>Bootstrap</code>) to search full transcripts and cheat sheets instantly via SQLite FTS5.</div>`;
    return;
  }

  const data = await api(`/api/search?q=${encodeURIComponent(q)}&course=${encodeURIComponent(state.activeCourseKey)}&limit=18`);
  state.searchHits = data.results || [];
  state.searchSelectedIdx = 0;

  if (state.searchHits.length === 0) {
    el.searchResults.innerHTML = `<div class="search-empty">No matches for <strong>${escapeHtml(q)}</strong> in this course.</div>`;
    return;
  }

  renderSearchHits();
}

function renderSearchHits() {
  el.searchResults.innerHTML = state.searchHits
    .map(
      (h, idx) => `
      <button type="button" class="search-hit ${idx === state.searchSelectedIdx ? "is-selected" : ""}" data-search-idx="${idx}" data-search-lesson="${h.lesson_id}">
        <div class="search-hit-head">
          <span>${escapeHtml(h.title)}</span>
          <span class="lesson-nav-meta tabular">M${h.module_number} · ${h.item_type === "guide" ? "Study Guide" : h.item_type}</span>
        </div>
        <div class="search-hit-snippet">${h.snippet}</div>
      </button>`
    )
    .join("");
}

// =========================================================================
// Helpers & Event Wiring
// =========================================================================
function closeMobileSidebar() {
  el.syllabusRail.classList.remove("is-mobile-open");
  el.sidebarBackdrop.classList.add("hidden");
  el.mobileMenuBtn.setAttribute("aria-expanded", "false");
}

function updateScrollProgress() {
  const doc = document.documentElement;
  const scrollTop = window.scrollY || doc.scrollTop;
  const scrollMax = doc.scrollHeight - doc.clientHeight;
  const ratio = scrollMax > 0 ? Math.min(1, Math.max(0, scrollTop / scrollMax)) : 0;
  el.readProgressBar.style.transform = `scaleX(${ratio})`;
}

async function loadCourse(courseKey) {
  state.activeCourseKey = courseKey;
  try {
    localStorage.setItem("dwp301c_active_course", courseKey);
  } catch (_) {}
  state.activeModuleNumber = 1;
  state.activeLessonId = null;
  state.activeLessonData = null;
  state.quizModuleFilter = "all";
  state.searchHits = [];
  if (el.searchInput) el.searchInput.value = "";
  const [coursesRes, detailRes] = await Promise.all([
    api("/api/courses"),
    api(`/api/courses/${courseKey}`),
  ]);
  state.courses = coursesRes.courses;
  state.courseData = detailRes;
  state.quizzesData = null;
  state.openModules = new Set([1]);
  renderCourseSwitcher();
  renderOverview();
}

async function toggleLessonFlag(field) {
  if (!state.activeLessonData) return;
  const lesson = state.activeLessonData.lesson;
  const nextVal = !lesson[field];
  const updated = await api(`/api/lessons/${lesson.id}/state`, {
    method: "PATCH",
    body: JSON.stringify({ [field]: nextVal }),
  });
  lesson.is_completed = updated.is_completed;
  lesson.is_bookmarked = updated.is_bookmarked;

  // Sync in cached courseData & courses summary
  for (const m of state.courseData.modules) {
    const found = m.lessons.find((x) => x.id === lesson.id);
    if (found) {
      found.is_completed = updated.is_completed;
      found.is_bookmarked = updated.is_bookmarked;
      m.completed_lessons = m.lessons.filter((x) => x.is_completed).length;
    }
  }
  const cObj = state.courses.find((c) => c.key === state.activeCourseKey);
  if (cObj) {
    cObj.completed_lessons = state.courseData.modules.reduce((acc, m) => acc + m.completed_lessons, 0);
  }

  renderCourseSwitcher();
  renderSyllabus();

  const btn = field === "is_completed" ? $("#toggleCompleteBtn") : $("#toggleBookmarkBtn");
  if (btn) {
    if (field === "is_completed") {
      btn.classList.toggle("is-done", updated.is_completed);
      btn.querySelector("span").textContent = updated.is_completed ? "Completed" : "Mark read";
      showToast(updated.is_completed ? "Marked lesson as completed" : "Removed completed mark");
    } else {
      btn.classList.toggle("is-saved", updated.is_bookmarked);
      btn.querySelector("span").textContent = updated.is_bookmarked ? "Saved" : "Save";
      showToast(updated.is_bookmarked ? "Saved to bookmarks" : "Removed from bookmarks");
    }
  }
}

function wireEvents() {
  window.addEventListener("scroll", updateScrollProgress, { passive: true });

  // Theme toggle
  el.themeToggleBtn.addEventListener("click", () => {
    const cur = document.documentElement.getAttribute("data-theme") || "light";
    applyTheme(cur === "dark" ? "light" : "dark");
  });

  // Brand link -> Overview
  $("#brandLink").addEventListener("click", (e) => {
    e.preventDefault();
    renderOverview();
  });

  // Mode tabs
  $$(".mode-tab").forEach((btn) => {
    btn.addEventListener("click", () => {
      const m = btn.dataset.mode;
      if (m === "overview") renderOverview();
      else if (m === "guides") openModuleGuide(state.activeModuleNumber || 1);
      else if (m === "reader") {
        const targetId = state.activeLessonId || state.courseData?.modules?.[0]?.lessons?.[0]?.id;
        if (targetId) openLesson(targetId);
      } else if (m === "cheatsheets") renderCheatSheetsView();
      else if (m === "quizzes") renderQuizzesView();
    });
  });

  // Course switcher popover
  el.courseSwitcherBtn.addEventListener("click", (e) => {
    e.stopPropagation();
    const isHidden = el.courseMenuPopover.classList.toggle("hidden");
    el.courseSwitcherBtn.setAttribute("aria-expanded", String(!isHidden));
  });

  document.addEventListener("click", (e) => {
    if (!el.courseMenuPopover.contains(e.target) && !el.courseSwitcherBtn.contains(e.target)) {
      el.courseMenuPopover.classList.add("hidden");
      el.courseSwitcherBtn.setAttribute("aria-expanded", "false");
    }
  });

  el.courseMenuPopover.addEventListener("click", (e) => {
    const btn = e.target.closest("[data-course-key]");
    if (!btn || btn.disabled) return;
    el.courseMenuPopover.classList.add("hidden");
    loadCourse(btn.dataset.courseKey);
  });

  // Filter chips in syllabus rail
  $$(".rail-header .filter-chip").forEach((chip) => {
    chip.addEventListener("click", () => {
      state.filter = chip.dataset.filter;
      $$(".rail-header .filter-chip").forEach((c) => c.classList.toggle("is-active", c === chip));
      renderSyllabus();
    });
  });

  // Syllabus tree delegation
  el.syllabusTree.addEventListener("click", (e) => {
    const guideBtn = e.target.closest("[data-open-module-guide]");
    if (guideBtn) {
      openModuleGuide(Number(guideBtn.dataset.openModuleGuide));
      return;
    }
    const modBtn = e.target.closest("[data-toggle-mod]");
    if (modBtn) {
      const num = Number(modBtn.dataset.toggleMod);
      if (state.openModules.has(num)) state.openModules.delete(num);
      else state.openModules.add(num);
      renderSyllabus();
      return;
    }
    const lessonBtn = e.target.closest("[data-lesson-id]");
    if (lessonBtn) {
      openLesson(Number(lessonBtn.dataset.lessonId));
    }
  });

  // Mobile sidebar drawer
  el.mobileMenuBtn.addEventListener("click", () => {
    const open = el.syllabusRail.classList.toggle("is-mobile-open");
    el.sidebarBackdrop.classList.toggle("hidden", !open);
    el.mobileMenuBtn.setAttribute("aria-expanded", String(open));
  });
  el.sidebarBackdrop.addEventListener("click", closeMobileSidebar);

  // Main stage delegation
  el.stageContainer.addEventListener("click", async (e) => {
    const guideBtn = e.target.closest("[data-open-module-guide]");
    if (guideBtn) {
      openModuleGuide(Number(guideBtn.dataset.openModuleGuide));
      return;
    }
    const modQuizBtn = e.target.closest("[data-open-mod-quiz]");
    if (modQuizBtn) {
      state.quizModuleFilter = modQuizBtn.dataset.openModQuiz;
      renderQuizzesView();
      return;
    }
    const openBtn = e.target.closest("[data-open-lesson]");
    if (openBtn) {
      openLesson(Number(openBtn.dataset.openLesson));
      return;
    }
    const modeBtn = e.target.closest("[data-switch-mode]");
    if (modeBtn) {
      const m = modeBtn.dataset.switchMode;
      if (m === "overview") renderOverview();
      else if (m === "cheatsheets") renderCheatSheetsView();
      else if (m === "quizzes") renderQuizzesView();
      return;
    }
    if (e.target.closest("#toggleCompleteBtn")) {
      await toggleLessonFlag("is_completed");
      return;
    }
    if (e.target.closest("#toggleBookmarkBtn")) {
      await toggleLessonFlag("is_bookmarked");
      return;
    }
    const copyBtn = e.target.closest("[data-copy]");
    if (copyBtn) {
      const pre = copyBtn.closest(".code-block-wrap")?.querySelector("pre code");
      if (pre) {
        await navigator.clipboard.writeText(pre.textContent || "");
        copyBtn.textContent = "Copied";
        setTimeout(() => (copyBtn.textContent = "Copy"), 1500);
      }
      return;
    }
    const qModBtn = e.target.closest("[data-quiz-mod]");
    if (qModBtn) {
      state.quizModuleFilter = qModBtn.dataset.quizMod;
      renderQuizzesView();
      return;
    }
    const pickBtn = e.target.closest("[data-pick-q]");
    if (pickBtn) {
      const qId = Number(pickBtn.dataset.pickQ);
      const optIdx = Number(pickBtn.dataset.pickOpt);
      const qType = pickBtn.dataset.qType;
      if (!state.quizPicks[qId]) state.quizPicks[qId] = new Set();
      if (qType === "multiple_select") {
        if (state.quizPicks[qId].has(optIdx)) state.quizPicks[qId].delete(optIdx);
        else state.quizPicks[qId].add(optIdx);
      } else {
        state.quizPicks[qId] = new Set([optIdx]);
      }
      updateQuestionCardInPlace(qId, `[data-pick-opt="${optIdx}"]`);
      return;
    }
    const revBtn = e.target.closest("[data-reveal-q]");
    if (revBtn) {
      const qId = Number(revBtn.dataset.revealQ);
      if (state.quizRevealed.has(qId)) state.quizRevealed.delete(qId);
      else state.quizRevealed.add(qId);
      updateQuestionCardInPlace(qId, `[data-reveal-q="${qId}"]`);
    }
  });

  // Search dialog & keyboard shortcuts
  el.searchTriggerBtn.addEventListener("click", openSearchDialog);
  el.searchCloseBtn.addEventListener("click", () => el.searchDialog.close());
  el.searchDialog.addEventListener("click", (e) => {
    if (e.target === el.searchDialog) el.searchDialog.close();
  });

  el.searchInput.addEventListener("input", () => {
    clearTimeout(searchTimer);
    searchTimer = setTimeout(() => runSearch(el.searchInput.value), 120);
  });

  el.searchResults.addEventListener("click", (e) => {
    const hitBtn = e.target.closest("[data-search-idx]");
    if (!hitBtn) return;
    const hit = state.searchHits[Number(hitBtn.dataset.searchIdx)];
    if (!hit) return;
    el.searchDialog.close();
    if (hit.item_type === "guide") openModuleGuide(hit.module_number);
    else openLesson(hit.lesson_id);
  });

  document.addEventListener("keydown", (e) => {
    if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "k") {
      e.preventDefault();
      openSearchDialog();
      return;
    }
    if (e.key === "/" && !el.searchDialog.open && !["INPUT", "TEXTAREA"].includes(document.activeElement?.tagName)) {
      e.preventDefault();
      openSearchDialog();
      return;
    }
    if (e.key === "Escape" && el.searchDialog.open) {
      e.preventDefault();
      el.searchDialog.close();
      return;
    }
    if (el.searchDialog.open && state.searchHits.length > 0) {
      if (e.key === "ArrowDown") {
        e.preventDefault();
        state.searchSelectedIdx = (state.searchSelectedIdx + 1) % state.searchHits.length;
        renderSearchHits();
      } else if (e.key === "ArrowUp") {
        e.preventDefault();
        state.searchSelectedIdx = (state.searchSelectedIdx - 1 + state.searchHits.length) % state.searchHits.length;
        renderSearchHits();
      } else if (e.key === "Enter") {
        e.preventDefault();
        const chosen = state.searchHits[state.searchSelectedIdx];
        if (chosen) {
          el.searchDialog.close();
          if (chosen.item_type === "guide") openModuleGuide(chosen.module_number);
          else openLesson(chosen.lesson_id);
        }
      }
    }
  });
}

// Boot
(async function boot() {
  initTheme();
  wireEvents();
  try {
    const coursesRes = await api("/api/courses");
    const list = coursesRes.courses || [];
    let savedKey = null;
    try {
      savedKey = localStorage.getItem("dwp301c_active_course");
    } catch (_) {}
    const validSaved = list.find((c) => c.key === savedKey && c.is_seeded);
    const firstSeeded = list.find((c) => c.is_seeded) || list[0];
    const initialKey = validSaved ? validSaved.key : firstSeeded ? firstSeeded.key : "coursera8";
    await loadCourse(initialKey);
  } catch (err) {
    el.stageContainer.innerHTML = `<div class="search-empty">Failed to load course data: ${escapeHtml(err.message)}</div>`;
  }
})();

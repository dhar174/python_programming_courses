(function () {
  const THEME_STORAGE_KEY = "pyc-theme";
  const THEME_ATTRIBUTE = "data-theme";
  const HELP_DIALOG_ID = "lecture-shortcuts-dialog";

  function root() {
    return document.documentElement;
  }

  function pageBody() {
    return document.body;
  }

  function isLecturePage() {
    const body = pageBody();
    return Boolean(body && (body.classList.contains("lecture-page") || body.dataset.pageKind === "lecture"));
  }

  function safeGetThemePreference() {
    try {
      return localStorage.getItem(THEME_STORAGE_KEY) || "auto";
    } catch {
      return "auto";
    }
  }

  function safeSetThemePreference(value) {
    try {
      localStorage.setItem(THEME_STORAGE_KEY, value);
    } catch {
      // Ignore persistence failures.
    }
  }

  function applyTheme(preference) {
    if (preference === "light" || preference === "dark") {
      root().setAttribute(THEME_ATTRIBUTE, preference);
      return;
    }
    root().removeAttribute(THEME_ATTRIBUTE);
  }

  function bindThemeControl() {
    const select = document.querySelector("[data-theme-toggle]");
    if (!select) {
      return;
    }

    const initial = safeGetThemePreference();
    select.value = initial;
    applyTheme(initial);
    select.addEventListener("change", function (event) {
      const value = event.target.value;
      safeSetThemePreference(value);
      applyTheme(value);
    });
  }

  function findArticle() {
    return document.querySelector("[data-lecture-article]") ||
      document.querySelector("main article") ||
      document.querySelector("article");
  }

  function findContentRegion() {
    return document.querySelector("[data-lecture-content]") ||
      document.getElementById("lecture-content") ||
      document.querySelector("main[role='main']") ||
      document.querySelector("main");
  }

  function slugify(text) {
    return String(text || "")
      .toLowerCase()
      .trim()
      .replace(/&/g, " and ")
      .replace(/[^a-z0-9]+/g, "-")
      .replace(/^-+|-+$/g, "")
      .replace(/-{2,}/g, "-");
  }

  function uniqueId(baseId) {
    const base = baseId || "section";
    let candidate = base;
    let index = 2;
    while (document.getElementById(candidate)) {
      candidate = `${base}-${index}`;
      index += 1;
    }
    return candidate;
  }

  function headingSelector() {
    return "h2, h3, h4";
  }

  function ensureHeadingIds(article) {
    return Array.from(article.querySelectorAll(headingSelector()))
      .filter(function (heading) {
        return heading.textContent && heading.textContent.trim();
      })
      .map(function (heading) {
        if (!heading.id) {
          heading.id = uniqueId(slugify(heading.textContent) || heading.tagName.toLowerCase());
        }
        heading.tabIndex = -1;
        if (!heading.querySelector(".lecture-heading-anchor")) {
          const anchor = document.createElement("a");
          anchor.className = "lecture-heading-anchor";
          anchor.href = `#${heading.id}`;
          anchor.setAttribute("aria-label", `Link to section: ${heading.textContent.trim()}`);
          anchor.textContent = "#";
          heading.appendChild(anchor);
        }
        return heading;
      });
  }

  function buildToc(headings) {
    const tocHost = document.querySelector("[data-lecture-toc]");
    if (!tocHost || !headings.length) {
      return [];
    }

    const list = document.createElement("ol");
    list.className = "lecture-toc-list";
    const links = [];

    headings.forEach(function (heading) {
      const item = document.createElement("li");
      const link = document.createElement("a");
      link.href = `#${heading.id}`;
      link.textContent = heading.textContent.replace(/#$/, "").trim();
      link.dataset.targetId = heading.id;
      link.classList.add(`depth-${heading.tagName.slice(1)}`);
      item.appendChild(link);
      list.appendChild(item);
      links.push(link);
    });

    tocHost.innerHTML = "";
    tocHost.appendChild(list);
    return links;
  }

  function focusHashTarget() {
    const hash = decodeURIComponent(window.location.hash || "").replace(/^#/, "");
    if (!hash) {
      return;
    }

    const target = document.getElementById(hash);
    if (!target) {
      return;
    }

    window.requestAnimationFrame(function () {
      target.focus({ preventScroll: true });
      target.scrollIntoView({ block: "start", behavior: prefersReducedMotion() ? "auto" : "smooth" });
    });
  }

  function prefersReducedMotion() {
    return window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  }

  function updateProgress() {
    const content = findContentRegion();
    if (!content) {
      return;
    }

    const scrollTop = window.scrollY;
    const start = content.getBoundingClientRect().top + scrollTop;
    const max = Math.max(content.scrollHeight - window.innerHeight, 1);
    const progress = Math.max(0, Math.min(100, ((scrollTop - start) / max) * 100));
    root().style.setProperty("--lecture-progress", progress.toFixed(2));
  }

  function nearestHeading(headings) {
    const marker = window.scrollY + Math.min(window.innerHeight * 0.25, 180);
    let current = headings[0] || null;
    headings.forEach(function (heading) {
      if (heading.offsetTop <= marker) {
        current = heading;
      }
    });
    return current;
  }

  function scrollCurrentTocLinkIntoView(currentLink) {
    if (!currentLink) {
      return;
    }

    const tocContainer = currentLink.closest("[data-lecture-toc]");
    if (!tocContainer || tocContainer.scrollHeight <= tocContainer.clientHeight + 1) {
      return;
    }

    const top = currentLink.offsetTop - tocContainer.offsetTop;
    const bottom = top + currentLink.offsetHeight;
    const viewTop = tocContainer.scrollTop;
    const viewBottom = viewTop + tocContainer.clientHeight;
    const margin = 10;

    if (top < viewTop + margin) {
      tocContainer.scrollTo({
        top: Math.max(top - margin, 0),
        behavior: prefersReducedMotion() ? "auto" : "smooth",
      });
      return;
    }

    if (bottom > viewBottom - margin) {
      tocContainer.scrollTo({
        top: Math.max(bottom - tocContainer.clientHeight + margin, 0),
        behavior: prefersReducedMotion() ? "auto" : "smooth",
      });
    }
  }

  function setCurrentHeading(currentHeading, tocLinks, shouldScrollToc) {
    if (!currentHeading) {
      return;
    }

    let currentLink = null;
    tocLinks.forEach(function (link) {
        const isCurrent = link.dataset.targetId === currentHeading.id;
      if (isCurrent) {
        link.setAttribute("aria-current", "true");
        currentLink = link;
      } else {
        link.removeAttribute("aria-current");
      }
    });

    if (shouldScrollToc) {
      scrollCurrentTocLinkIntoView(currentLink);
    }

    const status = document.querySelector("[data-lecture-current-section]");
    if (status) {
      status.textContent = `Current section: ${currentHeading.textContent.replace(/#$/, "").trim()}`;
    }

    if (window.location.hash !== `#${currentHeading.id}` && history.replaceState) {
      history.replaceState(null, "", `#${currentHeading.id}`);
    }
  }

  function findSlideCues() {
    return Array.from(document.querySelectorAll("[data-slide-cue='change']"));
  }

  function nearestSlideCue(cues) {
    const marker = window.scrollY + Math.min(window.innerHeight * 0.25, 180);
    let current = cues[0] || null;
    cues.forEach(function (cue) {
      if (cue.offsetTop <= marker) {
        current = cue;
      }
    });
    return current;
  }

  function updateCurrentSlideCue(currentCue, cues) {
    const containers = document.querySelectorAll("[data-lecture-current-slide-card], [data-lecture-current-slide-banner]");
    const links = document.querySelectorAll("[data-lecture-current-slide-link]");
    const metas = document.querySelectorAll("[data-lecture-current-slide-meta]");

    cues.forEach(function (cue) {
      cue.classList.toggle("is-current-slide", cue === currentCue);
    });

    if (!currentCue) {
      containers.forEach(function (container) {
        container.hidden = true;
      });
      links.forEach(function (link) {
        link.removeAttribute("href");
        link.textContent = "No slide cues in this lecture yet";
      });
      metas.forEach(function (meta) {
        meta.textContent = "Add instructor slide cues to the lecture markdown to enable this indicator.";
      });
      return;
    }

    const page = currentCue.dataset.slidePage || "";
    const title = currentCue.dataset.slideTitle || "Current slide";
    const cueLink = currentCue.querySelector("[data-slide-deck-link]");
    const href = cueLink ? cueLink.getAttribute("href") || "" : "";
    const label = page ? `Slide ${page}: ${title}` : title;

    containers.forEach(function (container) {
      container.hidden = false;
    });
    links.forEach(function (link) {
      link.textContent = label;
      if (href) {
        link.setAttribute("href", href);
      } else {
        link.removeAttribute("href");
      }
    });
    metas.forEach(function (meta) {
      meta.textContent = "This stays current until the next highlighted slide-change cue.";
    });
  }

  function bindScrollState(headings, tocLinks) {
    const slideCues = findSlideCues();
    if (!headings.length && !slideCues.length) {
      return;
    }

    let ticking = false;
    let lastHeadingId = "";
    function refresh() {
      ticking = false;
      updateProgress();
      if (headings.length) {
        const currentHeading = nearestHeading(headings);
        const currentHeadingId = currentHeading ? currentHeading.id : "";
        setCurrentHeading(currentHeading, tocLinks, currentHeadingId !== lastHeadingId);
        lastHeadingId = currentHeadingId;
      }
      updateCurrentSlideCue(nearestSlideCue(slideCues), slideCues);
    }

    refresh();
    window.addEventListener("scroll", function () {
      if (!ticking) {
        ticking = true;
        window.requestAnimationFrame(refresh);
      }
    }, { passive: true });
    window.addEventListener("resize", refresh, { passive: true });
  }

  function getNavLink(type) {
    return document.querySelector(`[data-lecture-${type}]`) ||
      document.querySelector(`a[rel='${type}']`);
  }

  function goToNav(type) {
    const link = getNavLink(type);
    if (!link || !link.href || link.getAttribute("aria-disabled") === "true") {
      return false;
    }
    window.location.href = link.href;
    return true;
  }

  function isEditableTarget(target) {
    if (!target) {
      return false;
    }

    if (target.isContentEditable) {
      return true;
    }

    const interactiveAncestor = target.closest("input, textarea, select, button, summary, [contenteditable='true'], [role='textbox'], [role='button'], [role='combobox'], [role='listbox'], [data-disable-lecture-shortcuts]");
    return Boolean(interactiveAncestor);
  }

  function hasSelection() {
    const selection = window.getSelection && window.getSelection();
    return Boolean(selection && String(selection).length);
  }

  function ensureHelpDialog() {
    let dialog = document.getElementById(HELP_DIALOG_ID);
    if (dialog) {
      return dialog;
    }

    dialog = document.createElement("dialog");
    dialog.id = HELP_DIALOG_ID;
    dialog.className = "lecture-help-dialog";
    dialog.innerHTML = [
      '<div class="lecture-help-inner">',
      '  <div class="lecture-help-header">',
      '    <div>',
      '      <h2>Lecture shortcuts</h2>',
      '      <p>Navigation is additive only and will not trigger while you are typing in fields.</p>',
      "    </div>",
      '    <button type="button" class="lecture-help-close" data-lecture-help-close aria-label="Close shortcuts help">Close</button>',
      "  </div>",
      '  <ul class="lecture-shortcuts-list">',
      "    <li><code>?</code> Open shortcut help</li>",
      "    <li><code>Esc</code> Close shortcut help</li>",
      "    <li><code>ArrowLeft</code> Previous lecture page when a previous link exists</li>",
      "    <li><code>ArrowRight</code> Next lecture page when a next link exists</li>",
      "    <li><code>Home</code> Jump to top of the lecture</li>",
      "    <li><code>End</code> Jump to the end of the lecture</li>",
      "    <li><code>Space</code> Page down &middot; <code>Shift</code> + <code>Space</code> page up</li>",
      "  </ul>",
      "</div>",
    ].join("");
    document.body.appendChild(dialog);

    dialog.querySelector("[data-lecture-help-close]").addEventListener("click", function () {
      closeHelpDialog();
    });

    dialog.addEventListener("cancel", function (event) {
      event.preventDefault();
      closeHelpDialog();
    });

    return dialog;
  }

  function ensureHelpButton() {
    if (document.querySelector("[data-lecture-help-button]")) {
      return;
    }

    const button = document.createElement("button");
    button.type = "button";
    button.className = "lecture-help-button";
    button.dataset.lectureHelpButton = "true";
    button.setAttribute("aria-haspopup", "dialog");
    button.setAttribute("aria-controls", HELP_DIALOG_ID);
    button.textContent = "?";
    button.addEventListener("click", openHelpDialog);
    document.body.appendChild(button);
  }

  function openHelpDialog() {
    const dialog = ensureHelpDialog();
    if (typeof dialog.showModal === "function") {
      if (!dialog.open) {
        dialog.showModal();
      }
    } else {
      dialog.setAttribute("open", "open");
    }
  }

  function closeHelpDialog() {
    const dialog = document.getElementById(HELP_DIALOG_ID);
    if (!dialog) {
      return false;
    }

    if (dialog.open && typeof dialog.close === "function") {
      dialog.close();
      return true;
    }

    if (dialog.hasAttribute("open")) {
      dialog.removeAttribute("open");
      return true;
    }

    return false;
  }

  function scrollPage(direction) {
    const delta = Math.max(window.innerHeight * 0.85, 240);
    window.scrollBy({
      top: direction === "down" ? delta : -delta,
      behavior: prefersReducedMotion() ? "auto" : "smooth",
    });
  }

  function scrollToEdge(position) {
    window.scrollTo({
      top: position === "top" ? 0 : document.documentElement.scrollHeight,
      behavior: prefersReducedMotion() ? "auto" : "smooth",
    });
  }

  function bindKeyboardShortcuts() {
    document.addEventListener("keydown", function (event) {
      if (event.defaultPrevented || event.altKey || event.ctrlKey || event.metaKey) {
        return;
      }

      if (isEditableTarget(event.target) || hasSelection()) {
        return;
      }

      if (event.key === "?") {
        event.preventDefault();
        openHelpDialog();
        return;
      }

      if (event.key === "Escape") {
        if (closeHelpDialog()) {
          event.preventDefault();
        }
        return;
      }

      if (event.key === "ArrowLeft") {
        if (goToNav("prev")) {
          event.preventDefault();
        }
        return;
      }

      if (event.key === "ArrowRight") {
        if (goToNav("next")) {
          event.preventDefault();
        }
        return;
      }

      if (event.key === "Home") {
        event.preventDefault();
        scrollToEdge("top");
        return;
      }

      if (event.key === "End") {
        event.preventDefault();
        scrollToEdge("bottom");
        return;
      }

      if (event.key === " ") {
        event.preventDefault();
        scrollPage(event.shiftKey ? "up" : "down");
      }
    });
  }

  function ensureProgressBar() {
    if (document.querySelector(".lecture-progress")) {
      return;
    }

    const shell = document.querySelector(".lecture-shell");
    if (!shell) {
      return;
    }

    const bar = document.createElement("div");
    bar.className = "lecture-progress";
    bar.setAttribute("aria-hidden", "true");
    shell.insertBefore(bar, shell.firstChild);
  }

  function enhancePrevNextLabels() {
    ["prev", "next"].forEach(function (direction) {
      const link = getNavLink(direction);
      if (!link) {
        return;
      }

      if (!link.textContent.trim()) {
        link.textContent = direction === "prev" ? "Previous lecture" : "Next lecture";
      }
      link.classList.add("lecture-button");
      if (!link.dataset.variant) {
        link.dataset.variant = direction === "next" ? "primary" : "secondary";
      }
    });
  }

  function initLecturePage() {
    if (!isLecturePage()) {
      return;
    }

    ensureProgressBar();
    ensureHelpDialog();
    ensureHelpButton();
    enhancePrevNextLabels();

    const article = findArticle();
    if (!article) {
      return;
    }

    const headings = ensureHeadingIds(article);
    const tocLinks = buildToc(headings);
    bindScrollState(headings, tocLinks);
    focusHashTarget();
    window.addEventListener("hashchange", focusHashTarget);
  }

  function init() {
    const storedTheme = safeGetThemePreference();
    applyTheme(storedTheme);
    bindThemeControl();
    bindKeyboardShortcuts();
    initLecturePage();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init, { once: true });
  } else {
    init();
  }
})();

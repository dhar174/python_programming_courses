(function () {
  const THEME_STORAGE_KEY = "pyc-theme";
  const THEME_ATTRIBUTE = "data-theme";

  function resolveBasePath() {
    if (typeof window.__PYC_BASE_PATH === "string") {
      return window.__PYC_BASE_PATH;
    }

    const repoMarker = "/python_programming_courses/";
    const pathname = window.location.pathname;
    if (pathname.includes(repoMarker)) {
      return pathname.slice(0, pathname.indexOf(repoMarker) + repoMarker.length);
    }
    if (pathname.startsWith("/slides/")) {
      return "/";
    }
    const lastSlash = pathname.lastIndexOf("/");
    return lastSlash >= 0 ? pathname.slice(0, lastSlash + 1) : "/";
  }

  function isSourcePreview() {
    return Boolean(window.__PYC_SOURCE_PREVIEW);
  }

  function withBasePath(relativePath) {
    const normalizedBase = resolveBasePath().replace(/\/+$/, "/");
    const trimmedRelative = String(relativePath || "").replace(/^\/+/, "");
    return `${normalizedBase}${trimmedRelative}`;
  }

  function applyTheme(preference) {
    const root = document.documentElement;
    if (preference === "dark" || preference === "light") {
      root.setAttribute(THEME_ATTRIBUTE, preference);
      return;
    }
    root.removeAttribute(THEME_ATTRIBUTE);
  }

  function bindThemeControl() {
    const select = document.querySelector("[data-theme-toggle]");
    if (!select) {
      return;
    }

    const initial = localStorage.getItem(THEME_STORAGE_KEY) || "auto";
    select.value = initial;
    applyTheme(initial);

    select.addEventListener("change", function (event) {
      const value = event.target.value;
      localStorage.setItem(THEME_STORAGE_KEY, value);
      applyTheme(value);
    });
  }

  function repoBlobUrl(repoPath) {
    const owner = document.body.getAttribute("data-repo-owner") || "dhar174";
    const name = document.body.getAttribute("data-repo-name") || "python_programming_courses";
    return `https://github.com/${owner}/${name}/blob/main/${repoPath}`;
  }

  function setText(selector, value) {
    const node = document.querySelector(selector);
    if (node && value !== undefined && value !== null) {
      node.textContent = String(value);
    }
  }

  function setLink(selector, href) {
    const node = document.querySelector(selector);
    if (!node) {
      return;
    }

    const sourceHref = node.getAttribute("data-source-href");
    const targetHref = isSourcePreview() && sourceHref ? sourceHref : href;
    if (targetHref) {
      node.setAttribute("href", targetHref.startsWith("http") ? targetHref : withBasePath(targetHref));
    }
  }

  function renderModuleSummary(module) {
    const moduleId = module.id;
    setText(`[data-module-days="${moduleId}"]`, module.stats.days);
    setText(`[data-module-slides="${moduleId}"]`, module.stats.slides);
    setText(`[data-module-lectures="${moduleId}"]`, module.stats.lectures);
    setText(`[data-module-assignments="${moduleId}"]`, module.stats.assignments);
    setText(`[data-module-quizzes="${moduleId}"]`, module.stats.quizzes);

    const primaryLink = isSourcePreview()
      ? module.sourcePrimaryHref || module.sourceLandingPage || module.primaryHref || module.landingPage
      : module.primaryHref || module.landingPage;
    if (primaryLink) {
      setLink(`[data-module-link="${moduleId}"]`, primaryLink);
    }

    const repoLinks = document.querySelector(`[data-module-repo-links="${moduleId}"]`);
    if (!repoLinks) {
      return;
    }

    const lecture = module.days.find((day) => day.artifacts.lecture.present);
    const assignment = module.days.find((day) => day.artifacts.assignment.present);
    const quiz = module.days.find((day) => day.artifacts.quiz.present);
    const items = [
      lecture && lecture.artifacts.lecture.repoPath
        ? { label: "Lecture scripts", href: repoBlobUrl(lecture.artifacts.lecture.repoPath) }
        : null,
      assignment && assignment.artifacts.assignment.repoPath
        ? { label: "Assignments", href: repoBlobUrl(assignment.artifacts.assignment.repoPath) }
        : null,
      quiz && quiz.artifacts.quiz.repoPath
        ? { label: "Quizzes", href: repoBlobUrl(quiz.artifacts.quiz.repoPath) }
        : null,
    ].filter(Boolean);

    repoLinks.innerHTML = "";
    items.forEach(function (item) {
      const link = document.createElement("a");
      link.className = "portal-link-chip";
      link.href = item.href;
      link.textContent = item.label;
      repoLinks.appendChild(link);
    });
  }

  function renderFeaturedDays(modules) {
    const container = document.querySelector("[data-featured-days]");
    if (!container) {
      return;
    }

    container.innerHTML = "";
    modules.forEach(function (module) {
      const days = module.days.slice(0, 3);
      days.forEach(function (day) {
        const item = document.createElement("li");
        const link = document.createElement("a");
        link.className = "portal-link-chip";
        const dayTarget = isSourcePreview()
          ? day.sourcePrimaryHref || day.artifacts.slides.sourcePath || day.primaryHref
          : day.primaryHref;
        link.href = dayTarget ? withBasePath(dayTarget) : "#";
        link.textContent = `${module.title} · Day ${day.dayNumber}`;
        item.appendChild(link);
        container.appendChild(item);
      });
    });
  }

  function labelFromLecturePath(repoPath, index) {
    const match = /Hour(\d+)/.exec(repoPath || "");
    if (match) {
      return `Lecture H${match[1]}`;
    }
    return `Lecture ${index + 1}`;
  }

  function appendChip(container, label, href, state) {
    const node = href ? document.createElement("a") : document.createElement("span");
    node.className = "portal-link-chip portal-status-badge";
    node.textContent = label;
    node.dataset.state = state || "available";
    if (href) {
      node.href = href;
    }
    container.appendChild(node);
  }

  function enhanceModulePage(manifest) {
    const moduleId = document.body.dataset.moduleId;
    if (!moduleId) {
      return;
    }

    const module = manifest.modules.find((item) => item.id === moduleId);
    if (!module) {
      return;
    }

    setText("[data-module-total-days]", module.stats.days);
    setText("[data-module-total-lectures]", module.stats.lectures);
    setText("[data-module-total-assignments]", module.stats.assignments);
    setText("[data-module-total-quizzes]", module.stats.quizzes);

    module.days.forEach(function (day) {
      const artifacts = day.artifacts || {};
      const badgeContainer = document.querySelector(`[data-day-badges="${day.id}"]`);
      if (badgeContainer) {
        badgeContainer.innerHTML = "";
        [
          { key: "slides", label: "Slides" },
          { key: "lecture", label: "Lecture" },
          { key: "assignment", label: "Assignment" },
          { key: "quiz", label: "Quiz" },
        ].forEach(function (artifact) {
          const artifactData = artifacts[artifact.key];
          const isPresent = Boolean(artifactData && artifactData.present);
          appendChip(badgeContainer, `${artifact.label} ${isPresent ? "✓" : "—"}`, null, isPresent ? "available" : "missing");
        });
      }

      const linkContainer = document.querySelector(`[data-day-links="${day.id}"]`);
      if (linkContainer) {
        linkContainer.innerHTML = "";

        const lecturePaths = artifacts.lecture && Array.isArray(artifacts.lecture.repoPaths)
          ? artifacts.lecture.repoPaths
          : [];
        lecturePaths.forEach(function (repoPath, index) {
          appendChip(linkContainer, labelFromLecturePath(repoPath, index), repoBlobUrl(repoPath), "available");
        });

        if (artifacts.assignment && artifacts.assignment.repoPath) {
          appendChip(linkContainer, "Assignment", repoBlobUrl(artifacts.assignment.repoPath), "available");
        }
        if (artifacts.quiz && artifacts.quiz.repoPath) {
          appendChip(linkContainer, "Quiz", repoBlobUrl(artifacts.quiz.repoPath), "available");
        }
      }
    });
  }

  function enhanceFromManifest(manifest) {
    if (!manifest || !Array.isArray(manifest.modules)) {
      return;
    }

    document.body.setAttribute("data-repo-owner", manifest.repository.owner);
    document.body.setAttribute("data-repo-name", manifest.repository.name);

    setText("[data-course-modules]", manifest.stats.modules);
    setText("[data-course-days]", manifest.stats.days);
    setText("[data-course-slides]", manifest.stats.slides);
    setText("[data-course-artifacts]", manifest.stats.lectures + manifest.stats.assignments + manifest.stats.quizzes);

    manifest.modules.forEach(renderModuleSummary);
    renderFeaturedDays(manifest.modules);
    enhanceModulePage(manifest);
  }

  function fetchManifest() {
    return fetch(withBasePath("slides/shared/portal/course-manifest.json"), { cache: "no-store" })
      .then(function (response) {
        if (!response.ok) {
          throw new Error(`Manifest request failed: ${response.status}`);
        }
        return response.json();
      });
  }

  function init() {
    bindThemeControl();
    fetchManifest().then(enhanceFromManifest).catch(function () {
      const note = document.querySelector("[data-manifest-status]");
      if (note) {
        note.textContent = "Static overview loaded. Manifest-driven summaries are unavailable in this preview.";
      }
    });
  }

  const storedTheme = localStorage.getItem(THEME_STORAGE_KEY) || "auto";
  applyTheme(storedTheme);
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init, { once: true });
  } else {
    init();
  }
})();

(function () {
  const THEME_STORAGE_KEY = "pyc-theme";
  const THEME_ATTRIBUTE = "data-theme";
  let repositoryMeta = {
    owner: "dhar174",
    name: "python_programming_courses",
    defaultBranch: "main",
  };

  function resolveBasePath() {
    if (typeof window.__PYC_BASE_PATH === "string") {
      return window.__PYC_BASE_PATH;
    }

    const pathname = window.location.pathname;
    const slidesMarker = "/slides/";
    if (pathname.includes(slidesMarker)) {
      return pathname.slice(0, pathname.indexOf(slidesMarker) + 1);
    }
    const htmlMatch = pathname.match(/^(.*\/)(?:index|404)\.html$/);
    if (htmlMatch) {
      return htmlMatch[1] || "/";
    }
    return "/";
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
      // Ignore persistence failures and still apply the theme for the current session.
    }
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

  function repoBlobUrl(repoPath) {
    return `https://github.com/${repositoryMeta.owner}/${repositoryMeta.name}/blob/${repositoryMeta.defaultBranch}/${repoPath}`;
  }

  function repoTreeUrl(repoPath) {
    return `https://github.com/${repositoryMeta.owner}/${repositoryMeta.name}/tree/${repositoryMeta.defaultBranch}/${repoPath}`;
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
    const lectureDirectory = lecture && lecture.artifacts.lecture.repoPath
      ? lecture.artifacts.lecture.repoPath.replace(/\/[^/]+$/, "")
      : null;
    const items = [
      lectureDirectory
        ? { label: "Lecture scripts", href: repoTreeUrl(lectureDirectory) }
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
        const dayTarget = dayOverviewHref(day);
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

  function dayDeckHref(day) {
    const slides = day.artifacts && day.artifacts.slides ? day.artifacts.slides : {};
    if (isSourcePreview()) {
      return day.sourcePrimaryHref || slides.sourcePath || day.primaryHref;
    }
    return day.primaryHref || slides.href;
  }

  function dayOverviewHref(day) {
    if (isSourcePreview()) {
      return day.sourceOverviewHref || day.sourcePrimaryHref || day.overviewHref || day.primaryHref;
    }
    return day.overviewHref || day.primaryHref;
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

  function renderArtifactStatus(container, artifacts) {
    container.innerHTML = "";
    [
      { key: "slides", label: "Slides" },
      { key: "lecture", label: "Lecture" },
      { key: "assignment", label: "Assignment" },
      { key: "quiz", label: "Quiz" },
    ].forEach(function (artifact) {
      const artifactData = artifacts[artifact.key];
      const isPresent = Boolean(artifactData && artifactData.present);
      appendChip(container, `${artifact.label} ${isPresent ? "✓" : "—"}`, null, isPresent ? "available" : "missing");
    });
  }

  function renderArtifactLinks(container, artifacts) {
    container.innerHTML = "";
    const lecturePaths = artifacts.lecture && Array.isArray(artifacts.lecture.repoPaths)
      ? artifacts.lecture.repoPaths
      : [];
    lecturePaths.forEach(function (repoPath, index) {
      appendChip(container, labelFromLecturePath(repoPath, index), repoBlobUrl(repoPath), "available");
    });

    if (artifacts.assignment && artifacts.assignment.repoPath) {
      appendChip(container, "Assignment", repoBlobUrl(artifacts.assignment.repoPath), "available");
    }
    if (artifacts.quiz && artifacts.quiz.repoPath) {
      appendChip(container, "Quiz", repoBlobUrl(artifacts.quiz.repoPath), "available");
    }

    const downloads = artifacts.slides && artifacts.slides.downloads ? artifacts.slides.downloads : {};
    Object.keys(downloads).forEach(function (formatName) {
      const href = downloads[formatName];
      if (href && formatName !== "html") {
        appendChip(container, formatName.toUpperCase(), withBasePath(href), "available");
      }
    });
  }

  function enhanceDayOverviewPage(manifest) {
    if (document.body.dataset.portalRoot !== "day") {
      return;
    }

    const moduleId = document.body.dataset.moduleId;
    const dayId = document.body.dataset.dayId;
    const module = manifest.modules.find((item) => item.id === moduleId);
    if (!module) {
      return;
    }

    const day = module.days.find((item) => item.id === dayId);
    if (!day) {
      return;
    }

    const artifacts = day.artifacts || {};
    const deckLink = document.querySelector("[data-day-deck-link]");
    const deckTarget = dayDeckHref(day);
    if (deckLink && deckTarget) {
      deckLink.href = deckTarget.startsWith("http") ? deckTarget : withBasePath(deckTarget);
    }

    const badgeContainer = document.querySelector("[data-day-overview-badges]");
    if (badgeContainer) {
      renderArtifactStatus(badgeContainer, artifacts);
    }

    const linkContainer = document.querySelector("[data-day-overview-links]");
    if (linkContainer) {
      renderArtifactLinks(linkContainer, artifacts);
    }

    const prevLink = document.querySelector("[data-day-prev]");
    if (prevLink && day.prev && day.prev.href) {
      prevLink.href = withBasePath(isSourcePreview()
        ? day.prev.href.replace(`slides/${moduleId}/`, `${module.sourceRoot}/`)
        : day.prev.href);
    }

    const nextLink = document.querySelector("[data-day-next]");
    if (nextLink && day.next && day.next.href) {
      nextLink.href = withBasePath(isSourcePreview()
        ? day.next.href.replace(`slides/${moduleId}/`, `${module.sourceRoot}/`)
        : day.next.href);
    }
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
        renderArtifactStatus(badgeContainer, artifacts);
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

    repositoryMeta = {
      owner: manifest.repository.owner || repositoryMeta.owner,
      name: manifest.repository.name || repositoryMeta.name,
      defaultBranch: manifest.repository.defaultBranch || repositoryMeta.defaultBranch,
    };

    setText("[data-course-modules]", manifest.stats.modules);
    setText("[data-course-days]", manifest.stats.days);
    setText("[data-course-slides]", manifest.stats.slides);
    setText("[data-course-artifacts]", manifest.stats.lectures + manifest.stats.assignments + manifest.stats.quizzes);

    manifest.modules.forEach(renderModuleSummary);
    renderFeaturedDays(manifest.modules);
    enhanceModulePage(manifest);
    enhanceDayOverviewPage(manifest);
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

  const storedTheme = safeGetThemePreference();
  applyTheme(storedTheme);
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init, { once: true });
  } else {
    init();
  }
})();

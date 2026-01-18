import { defineConfig } from '@marp-team/marp-cli'

export default defineConfig({
  // Where your lesson markdown lives
  inputDir: './lessons',
  // Where compiled outputs go (HTML, PDF, images, etc.)
  output: './site/slides',

  // Register a folder of named themes (each CSS must include `@theme <name>`)
  themeSet: './themes',

  // Produce PDFs by default; add outlines from headings and include presenter notes
  pdf: true,
  pdfOutlines: { headings: true, pages: false },
  pdfNotes: true,

  // Image quality controls
  imageScale: 2,
  jpegQuality: 85,

  // Safer default for educational repos; set to `true` or a whitelist only if needed
  html: false,

  // Template-specific toggles (for the default `bespoke` template)
  bespoke: {
    osc: true,          // on-screen controller
    progress: true,     // progress bar at top
    transition: true,   // enable slide transitions where supported
  },

  // Browser behavior (auto picks a local Chrome/Edge/Firefox)
  browser: 'auto',
  browserTimeout: 30,

  // Engine constructor options (passed to Marp Core)
  options: {
    markdown: {
      breaks: false, // CommonMark line breaks (shift+enter -> <br/> instead of every newline)
    },
    minifyCSS: true, // set to false if you’re actively tweaking themes
  },
})
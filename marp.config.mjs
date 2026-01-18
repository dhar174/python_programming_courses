import { defineConfig } from '@marp-team/marp-cli'

export default defineConfig({
  inputDir: './lessons',
  output: './site/slides',
  themeSet: './themes',
  pdf: true,
  pdfOutlines: { headings: true, pages: false },
  pdfNotes: true,
  imageScale: 2,
  jpegQuality: 85,
  html: false,
  bespoke: { osc: true, progress: true, transition: true },
  browser: 'auto',
  browserTimeout: 30,
  options: {
    markdown: { breaks: false },
    minifyCSS: true,
  },
})
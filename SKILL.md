---
name: repo-showcase
description: >
  Optimize GitHub repository presentation to attract users, stars, and engagement.
  Generates professional README files, badges, visual assets, community files, and
  GitHub SEO metadata. Use when: (1) publishing or pushing a new repo to GitHub,
  (2) the user asks to beautify, decorate, or improve a GitHub repo's appearance,
  (3) generating README for a new project, (4) optimizing repo discoverability,
  (5) setting up GitHub community files (issue templates, PR templates, contributing guide),
  (6) the user mentions "repo marketing", "attract stars", "GitHub SEO", or "social preview".
  Works for all repo types: Codex/Claude Skills, Web Apps, NPM/Python libraries,
  CLI tools, and general open source projects.
---

# Repo Showcase — GitHub Repository Presentation Optimizer

Transform any repository into a professional, star-attracting showcase. This skill
analyzes the repo, selects an optimal presentation strategy, and generates all
necessary files automatically.

## Core Workflow

### Phase 1: Repository Analysis

Analyze the repository to determine its type, tech stack, and target audience.

1. **Detect repo type** by examining files:
   - `SKILL.md` + agent config → **AI Skill** (Codex/Claude Code)
   - `package.json` with `bin` field → **CLI Tool**
   - `package.json` without `bin` → **NPM Library**
   - `pyproject.toml` / `setup.py` → **Python Package**
   - `Dockerfile` / `docker-compose.yml` → **Service/App**
   - `index.html` / frontend framework config → **Web App**
   - `Cargo.toml` → **Rust Crate**
   - Multiple of above → **Hybrid** (use dominant type)

2. **Extract tech stack**: Read `package.json`, `pyproject.toml`, `Cargo.toml`, etc.
   to identify frameworks, languages, and dependencies.

3. **Identify core value proposition**: Read existing README (if any), main entry files,
   and any documentation. Distill into one compelling sentence.

4. **Determine target audience**: Developers? End users? Data scientists? DevOps?
   The audience shapes tone, terminology, and emphasis.

### Phase 2: Generate Presentation Files

Based on the analysis, generate the appropriate files. See `references/readme-templates.md`
for full templates by repo type.

#### 2.1 README.md Generation

Follow this section order (sections marked with conditions are included only when applicable):

| # | Section | Condition |
|---|---------|-----------|
| 1 | **Language Switcher** | Only if repo has i18n READMEs or user requests multilingual |
| 2 | **Hero** (logo + tagline + badges) | Always |
| 3 | **Proof Bar** (star count, downloads, "Used By") | Always — position social proof early |
| 4 | **Highlights** (3-5 key features with icons) | Always |
| 5 | **Try in Browser** (StackBlitz/CodeSandbox/Gitpod) | Web Apps & Libraries |
| 6 | **Quick Start** (with time commitment + expected output) | Always |
| 7 | **5-Minute Win** (copy-paste code snippet) | Libraries & Tools |
| 8 | **Demo** (screenshots/GIF/video) | When visual demo exists or can be described |
| 9 | **Why This?** (comparison table, honest) | When clear competitors exist |
| 10 | **Usage** (detailed examples) | Always |
| 11 | **API Reference** (link to docs) | Libraries |
| 12 | **FAQ** (collapsible `<details>` blocks) | Always — reduce support burden |
| 13 | **Troubleshooting** (common issues) | CLI Tools & complex setups |
| 14 | **Contributing** | Always |
| 15 | **Star History** (chart from star-history.com) | Always — after content, before footer |
| 16 | **Footer** (author, license note) | Always |

**Critical rules for README generation:**

- **Hero section**: Use `<div align="center">` for centered layout. Include project name as `<h1>`,
  a one-line tagline that answers "what does this do for me?", and 3-5 key badges.
- **Proof Bar**: Right below Hero. Display star count as a large, prominent element using
  `https://img.shields.io/github/stars/{owner}/{repo}?style=social&logo=github`.
  If repo has npm/pypi downloads, show weekly downloads prominently.
- **Badges**: Use shields.io. Always include: version, license, build status (if CI exists),
  and one social badge (stars or downloads). See `references/badge-catalog.md` for the full catalog.
- **Quick Start**: Always include `⏱️ Get started in <N> seconds` header. Show expected output
  after commands so users know what success looks like.
- **Collapsible sections**: Use `<details><summary>` for FAQ, Troubleshooting, and verbose examples.
- **Alert callouts**: Use GitHub's `> [!NOTE]`, `> [!TIP]`, `> [!WARNING]` syntax for important notes.
- **Images**: Always provide meaningful alt text. Use `<picture>` element with `<source media="(prefers-color-scheme: dark)">`
  for dark mode compatibility when images have light backgrounds.
- **Mermaid diagrams**: Use for architecture, data flow, or workflow diagrams — GitHub renders them natively.

**Anti-patterns to avoid:**
- Wall of badges (max 5-7 in Hero, rest in a collapsible section)
- Generic tagline like "A tool for X" — make it benefit-driven
- Empty sections with "Coming soon" — only include completed content
- Comparison tables where you're always ✅ — be honest, admit when alternatives are better for some use cases
- Auto-generated feel — each README should read like a human wrote it proudly

#### 2.2 Visual Asset Generation

Generate SVG assets directly in the repo. Agent CAN and SHOULD create SVG code for:

- **Simple logo/icon** (if repo has none): Clean geometric SVG, 120x120px
- **Banner image** (for README hero): SVG with project name, tagline, and subtle visual element
  — 800x200px, works in both light and dark mode
- **Architecture diagram**: Mermaid or SVG diagram showing how the project works
- **Social preview image**: SVG template at 1200x630px (GitHub's recommended og:image size)
  with project name, description, logo, and key visual. Store as `.github/social-preview.svg`

For bitmap assets (GIF demos, screenshots), provide the user with specific instructions
on what to capture and recommended tools, but do not block on these.

**Dark mode strategy:**
- SVGs: Use CSS `@media (prefers-color-scheme: dark)` within SVG for theme-aware colors
- README images: Use `<picture>` HTML element with light/dark sources
- Badges: shields.io badges work in both modes by default
- Avoid light-gray text on white backgrounds — test for 4.5:1 contrast ratio minimum

#### 2.3 GitHub Community Files

Generate these files when they don't already exist:

| File | Purpose |
|------|---------|
| `.github/ISSUE_TEMPLATE/bug_report.md` | Structured bug reports |
| `.github/ISSUE_TEMPLATE/feature_request.md` | Feature requests |
| `.github/PULL_REQUEST_TEMPLATE.md` | PR checklist |
| `.github/FUNDING.yml` | Sponsorship links (if user has them) |
| `CONTRIBUTING.md` | Contribution guide with good-first-issue callout |
| `CODE_OF_CONDUCT.md` | Contributor Covenant v2.1 |
| `SECURITY.md` | Security vulnerability reporting guide |

#### 2.4 GitHub SEO & Discoverability

**Topics recommendation**: Analyze the repo and recommend up to 20 GitHub Topics.
Output as a `gh` CLI command:
```bash
gh repo edit {owner}/{repo} --add-topic topic1,topic2,...
```

**About description**: Generate a concise (≤120 chars), emoji-prefixed description
for the GitHub "About" field. Include core keywords.

**Optimal publishing timing**: If this is a new repo, recommend publishing on
Monday or Tuesday for GitHub Trending algorithm alignment.

### Phase 3: Quality Self-Assessment

After generating all files, run this checklist on your own output:

- [ ] **First 3 seconds test**: Does the Hero + Proof Bar communicate value immediately?
- [ ] **Quick Start test**: Can a new user follow the Quick Start without reading anything else?
- [ ] **Honesty test**: Does the comparison table feel genuine, not self-promotional?
- [ ] **Visual test**: Is there at least one visual element (badge, diagram, image, logo)?
- [ ] **Dark mode test**: Will images and badges look good in both light and dark themes?
- [ ] **Mobile test**: Do tables and code blocks render well on narrow screens?
- [ ] **SEO test**: Are key terms present in title, description, and first paragraph?
- [ ] **Accessibility test**: Do all images have alt text? Is emoji usage reasonable?
- [ ] **Anti-pattern check**: No "Coming soon" sections? No badge wall? No empty content?

If any check fails, revise the output before presenting to the user.

## Repository Type Specific Strategies

Reference `references/readme-templates.md` for full templates. Key differences:

### AI Skill (Codex/Claude Code)
- **Audience**: Dual — human developers AND AI agents
- **Hook**: Show what the skill does with a concrete before/after or example prompt
- **Growth logic**: Install → Use → Star (install-first, not star-first)
- **Must include**: Installation command, example trigger prompt, expected agent behavior
- **Visual**: Agent interaction screenshots or text output examples
- **Unique section**: "Example Prompts" — show 3-5 real prompts users can copy

### Web App
- **Audience**: End users and developers who might self-host
- **Hook**: Screenshots/GIF showing the app in action
- **Must include**: Live demo link, responsive screenshots (desktop + mobile)
- **Unique section**: "Try in Browser" — StackBlitz/CodeSandbox/deploy button

### NPM/Python Library
- **Audience**: Developers evaluating whether to adopt
- **Hook**: Copy-paste code snippet that works immediately
- **Must include**: Multi-package-manager install commands, bundle size badge
- **Unique section**: "5-Minute Win" — smallest possible useful example

### CLI Tool
- **Audience**: Terminal-native developers
- **Hook**: Terminal GIF showing the tool in action
- **Must include**: Installation (brew/cargo/npm), command list with examples
- **Unique section**: Command reference table

## References

- `references/readme-templates.md` — Full README templates by repo type
- `references/badge-catalog.md` — Complete shields.io badge catalog with URL templates
- `references/visual-guidelines.md` — SVG generation patterns and visual design rules

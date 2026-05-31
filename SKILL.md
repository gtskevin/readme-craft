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

Transform any repository into a professional, star-attracting showcase.

## Execution Flow

```
1. Analyze repo → determine type, audience, value prop
2. Generate priority files → README + banner SVG (always)
3. Generate secondary files → community files, social preview (if needed)
4. Self-check quality
5. Push or present to user
```

**Token budget awareness:** README + SVG is the core deliverable (~60% of effort).
Community files are secondary. If context is tight, skip secondary and tell user.

---

## Phase 1: Repository Analysis (5 min max)

### 1.1 Detect Repo Type

Check files in this order:

| File Pattern | Repo Type |
|-------------|-----------|
| `SKILL.md` or `skill.md` + no `package.json` | **AI Skill** |
| `package.json` + `"bin"` field | **CLI Tool** |
| `package.json` without `"bin"` | **NPM Library** |
| `pyproject.toml` or `setup.py` | **Python Package** |
| `Dockerfile` or `docker-compose.yml` | **Service/App** |
| `index.html` or `vite.config.*` or `next.config.*` | **Web App** |
| `Cargo.toml` | **Rust Crate** |
| Multiple matches | **Hybrid** (use dominant) |

### 1.2 Extract Key Facts

Read these files and extract:
- **Tech stack** from `package.json`/`pyproject.toml`/`Cargo.toml`
- **Value proposition** from existing README or main entry file → one sentence
- **Audience** from dependencies + documentation tone
- **Repo status** — check `gh repo view` for stars/forks if available, or GitHub page

### 1.3 New vs Established Repo

- **New repo (< 50 stars):** Focus on first impression, clear value, easy install. NO star history chart, NO "Used by" section, NO proof bar.
- **Established repo (50+ stars):** Include proof bar, star history, social proof.

---

## Phase 2: Generate Core Files

### 2.1 README.md — Section Order

Use only applicable sections. Every section has a concrete example below.

| # | Section | When | Priority |
|---|---------|------|----------|
| 1 | Hero (name + tagline + badges) | Always | P0 |
| 2 | One-liner pitch | Always | P0 |
| 3 | Highlights (3-5 features) | Always | P0 |
| 4 | Quick Start | Always | P0 |
| 5 | How It Works | Always | P0 |
| 6 | Example / Demo | When visual exists | P1 |
| 7 | Why This vs alternatives | When competitors exist | P1 |
| 8 | Usage details | Always | P1 |
| 9 | FAQ (collapsible) | Always | P2 |
| 10 | Contributing | Always | P2 |
| 11 | Star History | 50+ stars only | P2 |
| 12 | Footer | Always | P2 |

**Language:** If the repo targets Chinese audience (Chinese comments, Chinese docs, Chinese UI), generate bilingual README with `README.md` (English) + `README.zh-CN.md` (Chinese) + language switcher links at top.

### 2.2 README — Concrete Templates

#### Hero Section

```html
<div align="center">

<img src="assets/banner.svg" alt="Project Name — one line description" width="800">

<br/>

<!-- Badges: max 4, use for-the-badge style -->
[![GitHub Stars](https://img.shields.io/github/stars/{owner}/{repo}?style=for-the-badge&logo=github)](https://github.com/{owner}/{repo})
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)]()
[![Build](https://img.shields.io/github/actions/workflow/status/{owner}/{repo}/ci.yml?style=for-the-badge)]()

</div>
```

**Rules:**
- Tagline answers "what does this do FOR ME?" not "what IS this"
- Badges: max 4 in hero. Extra badges go in collapsible section.
- Use `<div align="center">` for centered layout

#### One-Liner Pitch

```markdown
> [!NOTE]
> **Who is this for?** You [do X]. [Problem you face]. [This tool] [solves it how].
```

#### Highlights

```markdown
## Highlights

| | Feature | Why it matters |
|---|---------|---------------|
| 🧠 | **Feature 1** | Benefit, not description |
| 🔧 | **Feature 2** | Benefit, not description |
| 🎯 | **Feature 3** | Benefit, not description |
```

**Rules:**
- Icons: pick from 🧠🔧🎯⚡🚀🛡️📦🌐💡🎨
- "Why it matters" column = benefit to user, NOT what it does

#### Quick Start

```markdown
## Quick Start

> ⏱️ **Get started in <N> seconds**

**The easiest way** (for AI skill repos):
> Tell your agent: `Install [skill-name] from https://github.com/{owner}/{repo}`

**Manual install:**
```bash
# Claude Code
mkdir -p ~/.claude/skills/{skill-name}
curl -sL https://raw.githubusercontent.com/{owner}/{repo}/main/skill.md -o ~/.claude/skills/{skill-name}/skill.md

# NPM
npm install {package}

# Python
pip install {package}
```

After install, run:
```bash
{command}
```

Expected output:
```
{what success looks like — copy from actual output}
```
```

**Rules:**
- Always show expected output after commands
- If agent-installable, show that FIRST (easiest path)
- Show manual install as fallback

#### FAQ (collapsible)

```markdown
## FAQ

<details>
<summary>Question users will actually ask?</summary>

Short, honest answer. 2-3 sentences max.
</details>
```

### 2.3 Banner SVG Generation

Generate a clean banner SVG at `assets/banner.svg`. Dimensions: 800x200px.

**Design pattern:**

```svg
<svg xmlns="http://www.w3.org/2000/svg" width="800" height="200" viewBox="0 0 800 200">
  <defs>
    <style>
      @media (prefers-color-scheme: dark) {
        .bg { fill: #0f172a; }
        .title { fill: #f1f5f9; }
        .sub { fill: #94a3b8; }
      }
    </style>
  </defs>
  <rect class="bg" width="800" height="200" rx="16" fill="#f8fafc"/>
  <text x="400" y="90" text-anchor="middle" font-family="system-ui, sans-serif"
        font-size="40" font-weight="bold" class="title" fill="#0f172a">
    Project Name
  </text>
  <text x="400" y="130" text-anchor="middle" font-family="system-ui, sans-serif"
        font-size="16" class="sub" fill="#64748b">
    One line tagline here
  </text>
  <!-- Accent pills -->
  <rect x="280" y="145" width="100" height="26" rx="13" fill="#1e293b"/>
  <text x="330" y="163" text-anchor="middle" font-family="monospace" font-size="12" fill="#60a5fa">
    /command
  </text>
</svg>
```

**Rules:**
- Always include dark mode via `@media (prefers-color-scheme: dark)`
- Use `system-ui, sans-serif` for text (renders well on all platforms)
- Max 3 colors + 1 accent color
- Include 1-2 "pills" showing key attributes (command, framework, etc.)

### 2.4 Social Preview

Generate `.github/social-preview.svg` only if requested. 1200x630px.

**Design pattern:** Same style as banner but wider. Left third = logo/visual, right two-thirds = title + tagline + pills.

For more SVG patterns, see `references/visual-guidelines.md`.

---

## Phase 3: Secondary Files (if context allows)

### 3.1 GitHub Community Files

Generate ONLY if they don't already exist. Use minimal templates:

**`.github/ISSUE_TEMPLATE/bug_report.md`:**
```markdown
---
name: Bug Report
about: Report a bug
---

**Description:**
**Steps to reproduce:**
**Expected behavior:**
**Actual behavior:**
**Environment:**
```

**`.github/ISSUE_TEMPLATE/feature_request.md`:**
```markdown
---
name: Feature Request
about: Suggest a feature
---

**Problem:**
**Proposed solution:**
**Alternatives considered:**
```

**`.github/PULL_REQUEST_TEMPLATE.md`:**
```markdown
## Summary

## Test plan

## Checklist
- [ ] Tests pass
- [ ] Documentation updated (if applicable)
```

**`CONTRIBUTING.md`:**
```markdown
# Contributing

1. Fork the repo
2. Create a feature branch: `git checkout -b my-feature`
3. Commit: `git commit -m 'Add feature'`
4. Push: `git push origin my-feature`
5. Open a Pull Request

## Good First Issues
Look for issues labeled `good first issue`.
```

**Skip unless user asks:** `CODE_OF_CONDUCT.md`, `SECURITY.md`, `FUNDING.yml`

For more templates, see `references/community-templates.md`.

### 3.2 GitHub SEO

Output these commands for the user:

```bash
# Set topics (pick from analysis)
gh repo edit {owner}/{repo} --add-topic topic1,topic2,topic3

# Set description (≤120 chars)
gh repo edit {owner}/{repo} --description "🎯 Description here"
```

**Topic suggestions by type:**
- AI Skill: `claude-code`, `codex`, `ai-agent`, `coding-assistant`, `skill`
- CLI: `cli`, `developer-tools`, `terminal`
- NPM: `npm`, `javascript`, `typescript`
- Python: `python`, `pypi`, `python3`

---

## Phase 4: Quality Self-Check

- [ ] **3-second test:** Hero + pitch = immediate value?
- [ ] **Copy-paste test:** Install + run from Quick Start alone?
- [ ] **Honesty test:** Comparison table genuine?
- [ ] **Visual test:** Banner SVG + badges present?
- [ ] **Dark mode test:** SVGs have dark mode styles?
- [ ] **No anti-patterns:** No empty sections, no badge wall (>4), no "Coming soon"
- [ ] **Star history gate:** Only if 50+ stars

---

## Repo Type Specifics

### AI Skill (Codex/Claude Code/Gemini)

- **Audience:** Developers who use AI agents — may not be senior programmers
- **Hook:** Before/after example or concrete prompt
- **Must include:** Agent-install command FIRST, manual second. Example prompts. Expected output.
- **Cross-agent table:** Show install for Claude Code, Codex, Gemini, Cursor, Windsurf
- **Tone:** Accessible, benefit-driven

### Web App

- **Audience:** End users + self-host developers
- **Hook:** Screenshot/GIF
- **Must include:** Live demo link, responsive screenshots
- **Unique:** "Try in Browser" button

### NPM/Python Library

- **Audience:** Evaluating developers
- **Hook:** Copy-paste snippet
- **Must include:** Multi-package install, "5-Minute Win"
- **Unique:** Smallest useful example

### CLI Tool

- **Audience:** Terminal-native developers
- **Hook:** Terminal output example
- **Must include:** Install (brew/cargo/npm), command reference
- **Unique:** Command table with examples

---

## Anti-Patterns

| Mistake | Fix |
|---------|-----|
| Wall of badges (8+) | Max 4 in hero, rest in collapsible |
| "A tool for X" tagline | Benefit: "Does X so you don't have to Y" |
| Star history for new repos | Only if 50+ stars |
| Generic comparison table | Be honest about alternatives |
| Empty "Coming soon" sections | Only include completed content |
| Missing dark mode in SVGs | Always add dark mode media query |
| Chinese repo, English-only README | Bilingual if Chinese audience |

---

## References

For deeper customization, see:
- `references/readme-templates.md` — Full README templates by repo type
- `references/badge-catalog.md` — Complete shields.io badge catalog
- `references/visual-guidelines.md` — SVG generation patterns and visual design rules
- `references/community-templates.md` — Detailed community file templates

<div align="center">

<img src="https://raw.githubusercontent.com/gtskevin/repo-showcase/main/.github/assets/banner.svg" width="600" alt="Repo Showcase — Transform any GitHub repo into a star-attracting showcase" />

<br/>

**One prompt → Professional README + SVG + Community files → 7 quality checks → Zero manual work**

<br/>

[![Codex Skill](https://img.shields.io/badge/🔧_Codex-Skill-blue?logo=openai&logoColor=white&style=for-the-badge)](https://github.com/gtskevin/repo-showcase#-quick-start)
[![Claude Code](https://img.shields.io/badge/🤖_Claude_Code-supported-d97706?logo=anthropic&logoColor=white&style=for-the-badge)](https://github.com/gtskevin/repo-showcase#-quick-start)
[![MIT License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)](https://github.com/gtskevin/repo-showcase/blob/main/LICENSE)

[![GitHub Stars](https://img.shields.io/github/stars/gtskevin/repo-showcase?style=social&logo=github)](https://github.com/gtskevin/repo-showcase/stargazers)
[![Last Commit](https://img.shields.io/github/last-commit/gtskevin/repo-showcase)](https://github.com/gtskevin/repo-showcase/commits/main)

<p>
  <a href="README.md">🇺🇸 English</a> · <a href="README.zh-CN.md">🇨🇳 简体中文</a>
</p>

</div>

---

## 🎬 Real Before → After

> **Actual result** from applying this skill to [gtskevin/ai-native-review](https://github.com/gtskevin/ai-native-review):

<table>
<tr>
<td width="50%">

**❌ Before** — [see original](https://github.com/gtskevin/ai-native-review/blob/472af96/README.md)

<br/>

```
# AI-Native Design Review

> Catch the #1 anti-pattern...

A Claude Code Skill that reviews...

---

## What It Does
(install instructions here)
```

*5 files. No banner. No badges. No visual. No community files. Flat, forgettable.*

</td>
<td width="50%">

**✅ After** — [see result](https://github.com/gtskevin/ai-native-review)

<br/>

`![Banner]` · `# ✨ AI-Native Design Review`

`[Claude Code Skill]` `[MIT]` `[⭐ Stars]`

🎬 Before/After demo · ⚡ 30s Quick Start · 🔍 Decision Tree · 📊 Real Example · ❓ FAQ · ⭐ Star History

*17 files. SVG banner + logo. 15 GitHub Topics. Community files. Quality-checked.*

</td>
</tr>
</table>

<div align="center">

**One prompt. All essential files. Quality-checked. Zero manual work.**

**[→ See the full beautified repo →](https://github.com/gtskevin/ai-native-review)**

</div>

---

## ⚡ Quick Start

⏱️ **30 seconds from install to first use**

**Option A — One-line install (recommended):**

```bash
curl -fsSL https://raw.githubusercontent.com/gtskevin/repo-showcase/main/install.sh | bash
```

Auto-detects Codex and/or Claude Code and installs to the right location.

**Option B — Codex skill installer (if in Codex):**

```
Install skill from gtskevin/repo-showcase
```

**Option C — Manual install:**

```bash
git clone https://github.com/gtskevin/repo-showcase.git
mkdir -p ~/.codex/skills/repo-showcase
cp -r repo-showcase/* ~/.codex/skills/repo-showcase/
rm -rf repo-showcase
```

Then open Codex or Claude Code and type:

```
"Beautify my GitHub repo before I publish it"
```

<details>
<summary>📋 What happens next (click to expand)</summary>

```
🔍 Analyzing repository...
   → Type: NPM Library (TypeScript)
   → Target audience: Frontend developers
   → Repo status: New (< 50 stars)
   → 3 competitors detected

📝 Generating P0 files...
   → README.md (hero + pitch + highlights + quick start + how it works)
   → assets/banner.svg (dark mode compatible, 800×200)

📝 Generating P1 files...
   → .github/social-preview.svg (1200×630 og:image)
   → badges (npm version, license, build)

📝 Generating P2 files...
   → Issue + PR templates
   → CONTRIBUTING.md
   → GitHub topics (15 recommended)

✅ Quality check: 7/7 passed
🚀 Ready to push!
```

</details>

---

## 🎯 What Gets Generated

Generated in priority order — P0 first, then P1/P2 if context allows:

| Priority | File | Purpose |
|----------|------|---------|
| **P0** | `README.md` | Hero + pitch + highlights + quick start + how it works |
| **P0** | `banner.svg` | Auto-generated, dark-mode-aware banner |
| **P1** | `social-preview.svg` | og:image (1200×630) for Twitter/Slack/WeChat |
| **P1** | Badges | shields.io badges matched to your ecosystem |
| **P2** | Issue templates | Bug report + feature request |
| **P2** | PR template | Structured pull request checklist |
| **P2** | `CONTRIBUTING.md` | Welcoming contribution guide |
| **P2** | GitHub Topics | Up to 20 topics for discoverability |
| On request | `CODE_OF_CONDUCT.md`, `SECURITY.md`, `FUNDING.yml` | Additional community files |

---

## 🧠 Why This Works

> Based on research of 100+ repos with 1,000+ stars:

```
Visitor lands on repo
    │
    ▼
┌─────────────────────────────────────────────┐
│  3 seconds: Hook (banner + tagline)         │ ← repo-showcase generates
│  If boring → bounce (60% of visitors)       │
└─────────────────────────────────────────────┘
    │ Engaged
    ▼
┌─────────────────────────────────────────────┐
│  10 seconds: Trust (badges + stars + proof) │ ← repo-showcase generates
│  If no proof → skeptical exit (30%)         │
└─────────────────────────────────────────────┘
    │ Convinced
    ▼
┌─────────────────────────────────────────────┐
│  30 seconds: Try (Quick Start)              │ ← repo-showcase generates
│  If too hard → bookmark & forget (50%)      │
└─────────────────────────────────────────────┘
    │ Successful
    ▼
  ⭐ Star  ·  📦 Install  ·  🤝 Contribute
```

**Every node in this funnel is optimized by the skill.**

---

## 🏷️ Supported Repo Types

| Type | Auto-Detected | Key Showcase Elements |
|------|:---:|------|
| 🤖 **AI Skill** | `SKILL.md` | Example prompts · Dual audience (human + agent) |
| 🌐 **Web App** | Frontend config | Screenshots · Live demo · Deploy button |
| 📦 **Library** | `package.json` | 5-Minute Win · Bundle size · Multi-pkg install |
| ⌨️ **CLI Tool** | `bin` field | ASCII art · Command reference · Terminal demo |

---

## 🏆 Honest Comparison

| Capability | **This** | readme-ai | Profile Gen |
|------------|:---:|:---:|:---:|
| AI Agent integration | ✅ Native | ❌ CLI | ❌ Web |
| SVG auto-generation | ✅ 3 types | ❌ | ⚠️ |
| Dark mode support | ✅ | ❌ | ❌ |
| Community files | ✅ On demand | ❌ | ❌ |
| Quality self-check | ✅ 7 pts | ❌ | ❌ |
| New vs established repo strategy | ✅ | ❌ | ❌ |
| Bilingual README support | ✅ | ❌ | ❌ |
| GitHub SEO | ✅ | ❌ | ❌ |
| Standalone CLI | ❌ | ✅ | ✅ |

> 💡 **Choose readme-ai** for standalone CLI. **Choose this** for full agent-powered pipeline.

---

## 🏗️ How It Works

```
📁 Your Repo  →  🔍 Detect Type  →  📋 Select Strategy
                                        │
                    ┌───────────────────┼───────────────────┐
                    ▼                   ▼                   ▼
              📝 README.md        🎨 SVG Assets       📋 Community Files
                    │                   │                   │
                    └───────────────────┼───────────────────┘
                                        ▼
                                   ✅ Quality Check
                                        │
                              ┌─────────┴─────────┐
                              ▼                   ▼
                          ✅ Pass              ❌ Fail
                              │                   │
                              ▼                   ▼
                         🚀 Push            🔧 Revise
```

---

## ❓ FAQ

<details>
<summary>🤔 Only Codex, or also Claude Code?</summary>

Both! Any AI agent that supports SKILL.md-based skills.
</details>

<details>
<summary>🛡️ Will it overwrite my README?</summary>

Asks first. You can also request "enhance existing" mode.
</details>

<details>
<summary>🎨 Can I customize templates?</summary>

Yes — edit files in `references/`. The skill reads them at runtime.
</details>

<details>
<summary>📊 How to run the quality check standalone?</summary>

`python3 scripts/quality_check.py README.md`
</details>

<details>
<summary>🌐 Non-English support?</summary>

EN + ZH built-in. Extensible to other languages via templates.
</details>

---

## 🤝 Contributing

Every contribution matters — from typo fixes to new repo type templates.

- 🐛 [Report a bug](https://github.com/gtskevin/repo-showcase/issues/new?template=bug_report.md)
- 💡 [Request a feature](https://github.com/gtskevin/repo-showcase/issues/new?template=feature_request.md)
- 🔧 [Good first issues](https://github.com/gtskevin/repo-showcase/labels/good%20first%20issue)

---

## ⭐ Star History

<div align="center">

[![GitHub Stars](https://img.shields.io/github/stars/gtskevin/repo-showcase?style=for-the-badge&logo=github&color=f59e0b&label=%E2%AD%90%20Star%20History)](https://star-history.com/#gtskevin/repo-showcase&Date)

**[↑ Click to view interactive Star History chart →](https://star-history.com/#gtskevin/repo-showcase&Date)**

</div>

---

<div align="center">

**Built with ❤️ by [@gtskevin](https://github.com/gtskevin)** · Making every repo shine ✨

[⬆ Back to top](#-repo-showcase)

</div>

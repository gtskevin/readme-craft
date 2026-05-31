<div align="center">

<img src="https://raw.githubusercontent.com/gtskevin/repo-showcase/main/.github/assets/banner.svg" width="600" alt="Repo Showcase — 把你的 GitHub 仓库变成高颜值展示页" />

<br/>

**一个 prompt → 专业 README + SVG + 社区文件 → 7 项质检 → 零手动操作**

<br/>

[![Codex Skill](https://img.shields.io/badge/🔧_Codex-Skill-blue?logo=openai&logoColor=white&style=for-the-badge)](https://github.com/gtskevin/repo-showcase#-快速开始)
[![Claude Code](https://img.shields.io/badge/🤖_Claude_Code-supported-d97706?logo=anthropic&logoColor=white&style=for-the-badge)](https://github.com/gtskevin/repo-showcase#-快速开始)
[![MIT License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)](https://github.com/gtskevin/repo-showcase/blob/main/LICENSE)

[![GitHub Stars](https://img.shields.io/github/stars/gtskevin/repo-showcase?style=social&logo=github)](https://github.com/gtskevin/repo-showcase/stargazers)

<p>
  <a href="README.md">🇺🇸 English</a> · <a href="README.zh-CN.md">🇨🇳 简体中文</a>
</p>

</div>

---

## 🎬 真实 Before → After

> **实际效果** — 用本 Skill 美化了 [gtskevin/ai-native-review](https://github.com/gtskevin/ai-native-review)：

<table>
<tr>
<td width="50%">

**❌ 之前** — [查看原文](https://github.com/gtskevin/ai-native-review/blob/472af96/README.md)

<br/>

```
# AI-Native Design Review

> Catch the #1 anti-pattern...

（纯文字，无视觉，5 个文件）
```

*无 banner、无徽章、无社区文件、无 SEO。*

</td>
<td width="50%">

**✅ 之后** — [查看结果](https://github.com/gtskevin/ai-native-review)

<br/>

`![Banner]` · `# ✨ AI-Native Design Review`

`[Claude Code Skill]` `[MIT]` `[⭐ Stars]`

🎬 效果对比 · ⚡ 30 秒上手 · 🔍 决策树 · 📊 真实案例 · ❓ FAQ · ⭐ Star History

*17 个文件。SVG banner + logo。15 个 Topic。社区文件齐全。*

</td>
</tr>
</table>

<div align="center">

**一个 prompt。所有核心文件。质量检查通过。零手动操作。**

**[→ 查看完整美化后的仓库 →](https://github.com/gtskevin/ai-native-review)**

</div>

---

## ⚡ 快速开始

⏱️ **30 秒上手**

**方式 A — 一键安装（推荐）：**

```bash
curl -fsSL https://raw.githubusercontent.com/gtskevin/repo-showcase/main/install.sh | bash
```

自动检测 Codex 和/或 Claude Code，安装到正确位置。

**方式 B — Codex 内直接安装：**

```
Install skill from gtskevin/repo-showcase
```

**方式 C — 手动安装：**

```bash
git clone https://github.com/gtskevin/repo-showcase.git
mkdir -p ~/.codex/skills/repo-showcase
cp -r repo-showcase/* ~/.codex/skills/repo-showcase/
rm -rf repo-showcase
```

然后在 Codex / Claude Code 中说：

```
"发布前帮我美化一下 GitHub 仓库"
```

<details>
<summary>📋 接下来会发生什么（点击展开）</summary>

```
🔍 分析仓库...
   → 类型：NPM 库 (TypeScript)
   → 目标用户：前端开发者
   → 仓库状态：新仓库（< 50 stars）
   → 检测到 3 个竞品

📝 生成 P0 文件...
   → README.md（hero + 核心卖点 + 高亮点 + 快速上手 + 工作原理）
   → assets/banner.svg（支持暗色模式，800×200）

📝 生成 P1 文件...
   → .github/social-preview.svg（1200×630 og:image）
   → 徽章（npm 版本、license、build）

📝 生成 P2 文件...
   → Issue + PR 模板
   → CONTRIBUTING.md
   → GitHub topics（推荐 15 个）

✅ 质量检查：7/7 全部通过
🚀 准备推送！
```

</details>

---

## 🎯 生成内容一览

按优先级生成 — P0 优先，P1/P2 视情况生成：

| 优先级 | 文件 | 用途 |
|--------|------|------|
| **P0** | `README.md` | Hero + 核心卖点 + 高亮点 + 快速上手 + 工作原理 |
| **P0** | `banner.svg` | 自动生成，支持暗色模式 |
| **P1** | `social-preview.svg` | og:image — Twitter/Slack/微信链接预览 |
| **P1** | 徽章 | shields.io 徽章，匹配你的技术栈 |
| **P2** | Issue 模板 | Bug 报告 + 功能请求 |
| **P2** | PR 模板 | 结构化 PR 清单 |
| **P2** | `CONTRIBUTING.md` | 友好的贡献指南 |
| **P2** | GitHub Topics | 最多 20 个 Topic 提升搜索排名 |
| 按需 | `CODE_OF_CONDUCT.md`、`SECURITY.md`、`FUNDING.yml` | 更多社区文件 |

---

## 🧠 为什么有效

> 基于 100+ 个千星仓库的研究：

```
访客进入仓库
    │
    ▼
┌──────────────────────────────────┐
│  3 秒：钩子（banner + 标语）     │ ← skill 自动生成
│  无趣 → 跳出（60% 访客）         │
└──────────────────────────────────┘
    │ 留下来了
    ▼
┌──────────────────────────────────┐
│  10 秒：信任（徽章 + star + 证明）│ ← skill 自动生成
│  没证据 → 怀疑离开（30%）         │
└──────────────────────────────────┘
    │ 说服了
    ▼
┌──────────────────────────────────┐
│  30 秒：尝试（Quick Start）       │ ← skill 自动生成
│  太难 → 收藏后遗忘（50%）         │
└──────────────────────────────────┘
    │ 成功了
    ▼
  ⭐ Star  ·  📦 安装  ·  🤝 贡献
```

**漏斗每个节点都被 skill 优化。**

---

## 🏷️ 支持的仓库类型

| 类型 | 自动检测 | 核心展示元素 |
|------|:---:|------|
| 🤖 **AI Skill** | `SKILL.md` | 示例 Prompt · 双读者策略 |
| 🌐 **Web 应用** | 前端配置 | 截图 · Demo · 部署按钮 |
| 📦 **库** | `package.json` | 5 分钟上手 · Bundle 大小 |
| ⌨️ **CLI** | `bin` 字段 | ASCII art · 命令参考 |

---

## 🏆 坦诚对比

| 能力 | **本 Skill** | readme-ai | Profile Gen |
|------|:---:|:---:|:---:|
| AI Agent 集成 | ✅ 原生 | ❌ CLI | ❌ 网页 |
| SVG 自动生成 | ✅ 3 种 | ❌ | ⚠️ |
| 暗色模式 | ✅ | ❌ | ❌ |
| 社区文件 | ✅ 按需生成 | ❌ | ❌ |
| 质量自检 | ✅ 7 项 | ❌ | ❌ |
| 新/老仓库策略 | ✅ | ❌ | ❌ |
| 双语 README | ✅ | ❌ | ❌ |
| GitHub SEO | ✅ | ❌ | ❌ |
| 独立 CLI | ❌ | ✅ | ✅ |

> 💡 **选 readme-ai** 如果你要独立 CLI。**选本 Skill** 如果你用 Codex/Claude Code。

---

## ❓ FAQ

<details>
<summary>🤔 只支持 Codex 吗？</summary>

Codex 和 Claude Code 都支持！任何支持 SKILL.md 的 AI Agent 都可以用。
</details>

<details>
<summary>🛡️ 会覆盖现有 README 吗？</summary>

会先询问。也可以让它"增强"现有 README。
</details>

<details>
<summary>🎨 能自定义模板吗？</summary>

可以，编辑 `references/` 中的文件即可。
</details>

---

## 🤝 参与贡献

- 🐛 [报告 Bug](https://github.com/gtskevin/repo-showcase/issues/new?template=bug_report.md)
- 💡 [功能建议](https://github.com/gtskevin/repo-showcase/issues/new?template=feature_request.md)
- 🔧 [Good First Issues](https://github.com/gtskevin/repo-showcase/labels/good%20first%20issue)

---

## ⭐ Star History

<div align="center">

[![GitHub Stars](https://img.shields.io/github/stars/gtskevin/repo-showcase?style=for-the-badge&logo=github&color=f59e0b&label=%E2%AD%90%20Star%20History)](https://star-history.com/#gtskevin/repo-showcase&Date)

**[↑ Click to view interactive Star History chart →](https://star-history.com/#gtskevin/repo-showcase&Date)**

</div>

---

<div align="center">

**Built with ❤️ by [@gtskevin](https://github.com/gtskevin)** · 让每个仓库都闪闪发光 ✨

</div>

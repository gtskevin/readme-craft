<div align="center">

<img src="https://raw.githubusercontent.com/gtskevin/repo-showcase/main/.github/assets/banner.svg" width="600" alt="Repo Showcase — 把你的 GitHub 仓库变成高颜值展示页" />

<br/>

**一个 prompt → 22 个文件 → 15 项质检 → 零手动操作**

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

## 🎬 效果对比

<table>
<tr>
<td width="50%">

**❌ 之前** — Agent 默认输出

<br/>

> `# my-tool`
> 一个数据处理工具。
>
> `npm install my-tool`
>
> MIT

*平平无奇。没徽章、没社会证明。访客 3 秒内离开。*

</td>
<td width="50%">

**✅ 之后** — 使用 repo-showcase

<br/>

> # ✨ my-tool
> *零配置，10 倍速数据处理*
>
> `[npm]` `[stars]` `[coverage]` `[downloads]`
>
> 🚀 亮点 · ⚡ 30 秒快速开始 · 🎬 演示 · ❓ FAQ · ⭐ Star History

*专业钩子、清晰价值、社会证明、转化率优化。*

</td>
</tr>
</table>

<div align="center">

**→ 一个 prompt 搞定一切 ←**

</div>

---

## ⚡ 快速开始

⏱️ **30 秒上手**

```bash
git clone https://github.com/gtskevin/repo-showcase.git ~/.codex/skills/repo-showcase
```

在任意项目中对 Codex / Claude Code 说：

```
"发布前帮我美化一下 GitHub 仓库"
```

<details>
<summary>📋 接下来会发生什么（点击展开）</summary>

```
🔍 分析仓库...
   → 类型：NPM 库 (TypeScript)
   → 目标用户：前端开发者
   → 检测到 3 个竞品

📝 生成展示文件...
   → README.md（16 个区块，转化率优化）
   → .github/assets/logo.svg（支持暗色模式）
   → .github/assets/banner.svg（800×200）
   → .github/social-preview.svg（1200×630 og:image）
   → 5 个社区文件

✅ 质量检查：15/15 全部通过
🚀 准备推送！
```

</details>

---

## 🎯 生成内容一览

| 文件 | 用途 |
|------|------|
| 📝 `README.md` | 16 区块转化率优化的展示页 |
| 🎨 SVG 资源 | Logo + Banner + 社交预览图（支持暗色模式） |
| 📱 `social-preview.svg` | og:image — Twitter/Slack/微信链接预览 |
| 🏷️ 徽章 URL | shields.io 徽章，匹配你的技术栈 |
| 📋 Issue 模板 | Bug 报告 + 功能请求 |
| 🔄 PR 模板 | 结构化 PR 清单 |
| 📖 社区文件 | CONTRIBUTING + SECURITY + Code of Conduct |
| 🏷️ Topics | 最多 20 个 GitHub Topics 提升搜索排名 |

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
| 社区文件 | ✅ 7 个 | ❌ | ❌ |
| 质量自检 | ✅ 15 项 | ❌ | ❌ |
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

[![Star History Chart](https://api.star-history.com/svg?repos=gtskevin/repo-showcase&type=Date)](https://star-history.com/#gtskevin/repo-showcase&Date)

---

<div align="center">

**Built with ❤️ by [@gtskevin](https://github.com/gtskevin)** · 让每个仓库都闪闪发光 ✨

</div>

<div align="center">

<img src=".github/assets/logo.svg" width="120" alt="Repo Showcase Logo" />

# Repo Showcase

**让 AI Agent 自动把你的 GitHub 仓库变成高颜值、高星标的展示页面**

[![Codex Skill](https://img.shields.io/badge/Codex-Skill-blue?logo=openai&logoColor=white)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/gtskevin/repo-showcase?style=social&logo=github)](https://github.com/gtskevin/repo-showcase/stargazers)

<p>
  <a href="README.md">English</a> | <a href="README.zh-CN.md">简体中文</a>
</p>

</div>

---

## ✨ 功能亮点

- 🔍 **智能检测** — 自动识别仓库类型（AI Skill / Web App / 库 / CLI 工具）
- 📝 **一键生成** — 专业、转化率优化的 README，16 个结构化区块
- 🎨 **SVG 资产** — 自动生成 Logo、Banner、社交预览图（支持暗色模式）
- 🏷️ **SEO 优化** — 推荐 GitHub Topics、About 描述、shields.io 徽章
- 📋 **社区文件** — Issue/PR 模板、贡献指南、安全策略、行为准则
- ✅ **质量自检** — 15 项检查指标，确保输出质量

## 🎯 使用示例

| Prompt | 效果 |
|--------|------|
| `"发布前帮我美化 GitHub 仓库"` | 完整美化流水线 |
| `"给这个项目生成 README"` | 智能 README + 徽章 |
| `"添加社交预览图和徽章"` | SVG og:image + shields.io |
| `"运行质量检查"` | 15 项检查报告 |

## ⚡ 快速开始

```bash
# 安装到 Codex
git clone https://github.com/gtskevin/repo-showcase.git ~/.codex/skills/repo-showcase
```

然后在任何项目中对 Codex 说：
```
"帮我把 GitHub 仓库做得好看一点，准备发布"
```

## 📦 适用场景

| 类型 | 检测信号 | 展示重点 |
|------|---------|---------|
| **AI Skill** | 存在 `SKILL.md` | 示例 Prompt、安装命令 |
| **Web App** | 前端框架配置 | 截图、在线 Demo、部署按钮 |
| **NPM/Python 库** | `package.json` / `pyproject.toml` | 5 分钟上手、多包管理器安装 |
| **CLI 工具** | `bin` 字段 | ASCII art、命令参考表 |

## ⭐ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=gtskevin/repo-showcase&type=Date)](https://star-history.com/#gtskevin/repo-showcase&Date)

---

<div align="center">
<sub>Built with ❤️ by <a href="https://github.com/gtskevin">@gtskevin</a></sub>
</div>

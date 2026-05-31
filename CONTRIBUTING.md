# Contributing to Repo Showcase

Thanks for your interest in contributing! 🎉

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/{your-username}/repo-showcase.git`
3. Create a branch: `git checkout -b feature/your-feature`
4. Make your changes
5. Submit a Pull Request

## Development Setup

```bash
# Test the quality check script
python3 scripts/quality_check.py README.md

# Test badge generation
python3 scripts/generate_badges.py --owner test --repo test-repo --path .
```

## Finding Issues to Work On

Look for issues labeled:
- [`good first issue`](https://github.com/gtskevin/repo-showcase/labels/good%20first%20issue) — Great for first-time contributors
- [`help wanted`](https://github.com/gtskevin/repo-showcase/labels/help%20wanted) — We'd love community help

## What to Contribute

- **New repo type templates** — Support for VS Code extensions, GitHub Actions, Docker images, etc.
- **Better SVG designs** — More logo/banner styles
- **Quality checks** — New anti-pattern detection rules
- **Translations** — README translations for more languages
- **Bug fixes** — For the generation scripts

## Pull Request Process

1. Ensure quality check passes: `python3 scripts/quality_check.py README.md`
2. Update documentation if needed
3. Request a review from a maintainer

## Code of Conduct

This project follows the [Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md).

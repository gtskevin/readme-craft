# Badge Catalog — shields.io Reference

Use these badge URL patterns to generate professional badges for any repository.

## Tier 1: Always Include (Hero Section)

### Version Badges

```
# npm package
![npm](https://img.shields.io/npm/v/{package})

# PyPI package
![PyPI](https://img.shields.io/pypi/v/{package})

# GitHub Release
![GitHub release](https://img.shields.io/github/v/release/{owner}/{repo})

# Cargo crate
![Crates.io](https://img.shields.io/crates/v/{crate})
```

### License Badge
```
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)
![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)
```

### Social Badges
```
# GitHub Stars (social style — most impactful)
![GitHub Stars](https://img.shields.io/github/stars/{owner}/{repo}?style=social&logo=github)

# GitHub Forks
![GitHub Forks](https://img.shields.io/github/forks/{owner}/{repo}?style=social&logo=github)
```

## Tier 2: Include When Applicable (Hero Section, max 5-7 total)

### Build Status
```
# GitHub Actions
![Build](https://img.shields.io/github/actions/workflow/status/{owner}/{repo}/ci.yml?branch=main)

# Generic CI
![Build Status](https://img.shields.io/travis/{owner}/{repo})
```

### Downloads
```
# npm weekly downloads
![npm downloads](https://img.shields.io/npm/dw/{package})

# npm monthly downloads
![npm downloads](https://img.shields.io/npm/dm/{package})

# PyPI downloads
![PyPI downloads](https://img.shields.io/pypi/dm/{package})

# GitHub all releases
![GitHub Downloads](https://img.shields.io/github/downloads/{owner}/{repo}/total)
```

### Code Quality
```
# Code Coverage (Codecov)
![codecov](https://img.shields.io/codecov/c/github/{owner}/{repo})

# TypeScript
![TypeScript](https://img.shields.io/badge/built%20with-TypeScript-blue)

# Code Style
![code style: prettier](https://img.shields.io/badge/code_style-prettier-ff69b4.svg)
```

### Tech Stack
```
# Node.js version
![node](https://img.shields.io/node/v/{package})

# Python version
![Python](https://img.shields.io/pypi/pyversions/{package})

# Platform
![Platform](https://img.shields.io/badge/platform-macOS%20%7C%20Linux%20%7C%20Windows-lightgrey)
```

## Tier 3: Collapsible "More Badges" Section

For additional badges, wrap in a collapsible section to keep the Hero clean:

```markdown
<details>
<summary>📊 More Badges</summary>
<br>

![Dependencies](https://img.shields.io/librariesio/release/npm/{package})
![Bundle Size](https://img.shields.io/bundlephobia/min/{package})
![Bundle Size (gzip)](https://img.shields.io/bundlephobia/minzip/{package})
![Last Commit](https://img.shields.io/github/last-commit/{owner}/{repo})
![Issues](https://img.shields.io/github/issues/{owner}/{repo})
![Pull Requests](https://img.shields.io/github/issues-pr/{owner}/{repo})

</details>
```

## Special Badges

### Dynamic Badges (auto-updating)

```
# Version from package.json
![Version](https://img.shields.io/npm/v/{package}?label=version)

# Node version from engines field
![Node](https://img.shields.io/node/v/{package})

# Snyk vulnerabilities
![Known Vulnerabilities](https://snyk.io/test/github/{owner}/{repo}/badge.svg)

# OpenSSF Scorecard
![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/{owner}/{repo}/badge)
```

### Custom Branded Badges

```
# Custom text badge (any color)
![Custom](https://img.shields.io/badge/{left_text}-{right_text}-{color})

# Examples:
![Built with Love](https://img.shields.io/badge/built_with-love-red)
![AI Powered](https://img.shields.io/badge/AI-Powered-purple)
![Codex Skill](https://img.shields.io/badge/Codex-Skill-blue?logo=openai)
```

### Social Preview

```
# GitHub Profile README counter
![Profile Views](https://komarev.com/ghpvc/?username={owner}&color=blueviolet)
```

## Badge Style Guide

| Style | Use Case | Example |
|-------|----------|---------|
| `flat` (default) | Most badges | Clean, modern look |
| `flat-square` | Tech stack badges | Slightly more geometric |
| `for-the-badge` | Large feature badges | Bold, prominent |
| `social` | Star/fork counts | GitHub-style social buttons |
| `plastic` | Legacy look | Avoid for new projects |

**Recommended combinations:**
- Hero: `social` for stars + `flat` for everything else
- Feature badges: `for-the-badge` for key features (max 3)
- Collapsible: `flat` for all

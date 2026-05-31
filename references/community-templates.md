# GitHub Community File Templates

## Bug Report Issue Template

File: `.github/ISSUE_TEMPLATE/bug_report.md`

```markdown
---
name: 🐛 Bug Report
about: Report a bug to help us improve
title: '[Bug] '
labels: bug
assignees: ''
---

## Bug Description

A clear and concise description of what the bug is.

## Steps to Reproduce

1. Go to '...'
2. Click on '...'
3. Scroll down to '...'
4. See error

## Expected Behavior

What you expected to happen.

## Actual Behavior

What actually happened.

## Screenshots / Logs

If applicable, add screenshots or error logs.

## Environment

- OS: [e.g., macOS 14, Ubuntu 22.04]
- Version: [e.g., 1.2.0]
- Node.js: [e.g., 18.17.0] (if applicable)

## Additional Context

Any other context about the problem.
```

## Feature Request Issue Template

File: `.github/ISSUE_TEMPLATE/feature_request.md`

```markdown
---
name: 🚀 Feature Request
about: Suggest an idea for this project
title: '[Feature] '
labels: enhancement
assignees: ''
---

## Problem Statement

A clear description of the problem. Ex: "I'm always frustrated when..."

## Proposed Solution

Describe the solution you'd like.

## Alternatives Considered

Describe any alternative solutions or features you've considered.

## Additional Context

Any other context, screenshots, or references.
```

## Pull Request Template

File: `.github/PULL_REQUEST_TEMPLATE.md`

```markdown
## What does this PR do?

Brief description of the change.

## Related Issues

Closes #___

## Type of Change

- [ ] 🐛 Bug fix (non-breaking change that fixes an issue)
- [ ] ✨ New feature (non-breaking change that adds functionality)
- [ ] 💥 Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] 📝 Documentation update

## Checklist

- [ ] My code follows the project's style guidelines
- [ ] I have performed a self-review
- [ ] I have added tests that prove my fix/feature works
- [ ] All new and existing tests pass
- [ ] I have updated documentation as needed
```

## CONTRIBUTING.md Template

```markdown
# Contributing to {Project Name}

Thanks for your interest in contributing! 🎉

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/{your-username}/{repo}.git`
3. Create a branch: `git checkout -b feature/your-feature`
4. Make your changes
5. Submit a Pull Request

## Development Setup

```bash
# Install dependencies
{install_command}

# Run tests
{test_command}

# Start dev mode
{dev_command}
```

## Finding Issues to Work On

Look for issues labeled:
- [`good first issue`](https://github.com/{owner}/{repo}/labels/good%20first%20issue) — Great for first-time contributors
- [`help wanted`](https://github.com/{owner}/{repo}/labels/help%20wanted) — We'd love community help on these

## Code Style

{Brief description of code style, linting, formatting}

## Pull Request Process

1. Update documentation if needed
2. Add tests for new functionality
3. Ensure all tests pass
4. Request a review from a maintainer

## Code of Conduct

This project follows the [Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md).
By participating, you agree to uphold this code. Report unacceptable behavior to {email}.
```

## SECURITY.md Template

```markdown
# Security Policy

## Reporting a Vulnerability

If you discover a security vulnerability, please report it responsibly:

- **Do NOT open a public GitHub issue**
- Email: {security-email}
- Include: description, steps to reproduce, and potential impact

We'll respond within 48 hours and work with you to address the issue.

## Supported Versions

| Version | Supported |
|---------|-----------|
| Latest  | ✅ |
| Previous | ⚠️ Security fixes only |
| Older   | ❌ |
```

## FUNDING.yml Template

File: `.github/FUNDING.yml`

```yaml
github: [{owner}]
ko_fi: {username}
buy_me_a_coffee: {username}
custom: [{custom-url}]
```

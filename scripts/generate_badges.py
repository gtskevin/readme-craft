#!/usr/bin/env python3
"""
Generate shields.io badge markdown for a GitHub repository.

Usage:
    python3 generate_badges.py --owner {github_user} --repo {repo_name} [--npm {package}] [--pypi {package}]

Output: Markdown badge snippets ready to paste into README.md
"""

import argparse
import json
import sys
from pathlib import Path


def detect_ecosystem(repo_path: str = ".") -> dict:
    """Auto-detect package ecosystem from repo files."""
    path = Path(repo_path)
    info = {}

    # npm / Node.js
    pkg_json = path / "package.json"
    if pkg_json.exists():
        try:
            pkg = json.loads(pkg_json.read_text())
            info["npm"] = pkg.get("name", "")
            info["node_version"] = pkg.get("engines", {}).get("node", "")
            info["has_bin"] = "bin" in pkg
        except json.JSONDecodeError:
            pass

    # Python
    for py_file in ["pyproject.toml", "setup.py", "setup.cfg"]:
        if (path / py_file).exists():
            info["pypi"] = path.name
            break

    # Rust
    if (path / "Cargo.toml").exists():
        info["cargo"] = path.name

    # Check for CI
    for ci_path in [".github/workflows/ci.yml", ".github/workflows/test.yml",
                    ".github/workflows/build.yml", ".travis.yml", ".circleci/config.yml"]:
        if (path / ci_path).exists():
            info["ci_workflow"] = ci_path.split("/")[-1] if "/" in ci_path else ci_path
            info["ci_path"] = ci_path
            break

    # Check for TypeScript
    if (path / "tsconfig.json").exists():
        info["typescript"] = True

    return info


def generate_badges(owner: str, repo: str, ecosystem: dict, npm_pkg: str = None,
                    pypi_pkg: str = None) -> str:
    """Generate markdown badge lines."""
    lines = []
    lines.append(f"# Badges for {owner}/{repo}")
    lines.append("")

    # === Tier 1: Core badges ===
    lines.append("## Tier 1: Hero Badges (include in README header)")
    lines.append("")

    # Version badge
    if npm_pkg or ecosystem.get("npm"):
        pkg = npm_pkg or ecosystem["npm"]
        lines.append(f"![npm](https://img.shields.io/npm/v/{pkg})")

    if pypi_pkg or ecosystem.get("pypi"):
        pkg = pypi_pkg or ecosystem["pypi"]
        lines.append(f"![PyPI](https://img.shields.io/pypi/v/{pkg})")

    if ecosystem.get("cargo"):
        lines.append(f"![Crates.io](https://img.shields.io/crates/v/{repo})")

    # GitHub Release (always include as fallback)
    lines.append(f"![GitHub release](https://img.shields.io/github/v/release/{owner}/{repo})")

    # License
    lines.append(f"![License](https://img.shields.io/github/license/{owner}/{repo})")

    # Build status
    if ecosystem.get("ci_workflow"):
        wf = ecosystem["ci_workflow"]
        lines.append(f"![Build](https://img.shields.io/github/actions/workflow/status/{owner}/{repo}/{wf}?branch=main)")

    # Stars (social style)
    lines.append(f"![GitHub Stars](https://img.shields.io/github/stars/{owner}/{repo}?style=social&logo=github)")

    lines.append("")

    # === Tier 2: Supplementary badges ===
    lines.append("## Tier 2: Include When Applicable")
    lines.append("")

    # Downloads
    if npm_pkg or ecosystem.get("npm"):
        pkg = npm_pkg or ecosystem["npm"]
        lines.append(f"![npm downloads](https://img.shields.io/npm/dm/{pkg})")

    if pypi_pkg or ecosystem.get("pypi"):
        pkg = pypi_pkg or ecosystem["pypi"]
        lines.append(f"![PyPI downloads](https://img.shields.io/pypi/dm/{pkg})")

    # TypeScript
    if ecosystem.get("typescript"):
        lines.append("![TypeScript](https://img.shields.io/badge/built%20with-TypeScript-blue)")

    # Last commit
    lines.append(f"![Last Commit](https://img.shields.io/github/last-commit/{owner}/{repo})")

    # Issues
    lines.append(f"![Open Issues](https://img.shields.io/github/issues/{owner}/{repo})")

    # Forks
    lines.append(f"![GitHub Forks](https://img.shields.io/github/forks/{owner}/{repo}?style=social&logo=github)")

    lines.append("")

    # === Star History ===
    lines.append("## Star History Chart")
    lines.append("")
    lines.append(f"[![Star History Chart](https://api.star-history.com/svg?repos={owner}/{repo}&type=Date)](https://star-history.com/#{owner}/{repo}&Date)")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Generate shields.io badges for a repo")
    parser.add_argument("--owner", required=True, help="GitHub username or org")
    parser.add_argument("--repo", required=True, help="Repository name")
    parser.add_argument("--npm", help="npm package name (overrides auto-detect)")
    parser.add_argument("--pypi", help="PyPI package name (overrides auto-detect)")
    parser.add_argument("--path", default=".", help="Path to repo root (default: .)")
    parser.add_argument("--output", help="Output file (default: stdout)")

    args = parser.parse_args()

    ecosystem = detect_ecosystem(args.path)
    badges = generate_badges(args.owner, args.repo, ecosystem, args.npm, args.pypi)

    if args.output:
        Path(args.output).write_text(badges)
        print(f"Badges written to {args.output}")
    else:
        print(badges)


if __name__ == "__main__":
    main()

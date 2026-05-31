#!/usr/bin/env python3
"""
Quality self-assessment checklist for generated README files.

Usage:
    python3 quality_check.py README.md [--repo-path .]

Checks for anti-patterns, missing sections, and quality issues.
"""

import argparse
import re
import sys
from pathlib import Path


CHECKS = {
    "hero_section": {
        "name": "Hero Section",
        "description": "README should have a centered hero section with project name",
        "severity": "critical",
    },
    "tagline": {
        "name": "Tagline",
        "description": "Should have a one-line benefit-driven tagline",
        "severity": "critical",
    },
    "badges": {
        "name": "Badges",
        "description": "Should have at least 2 shields.io badges",
        "severity": "important",
    },
    "quick_start": {
        "name": "Quick Start",
        "description": "Should have a Quick Start section",
        "severity": "critical",
    },
    "features": {
        "name": "Features/Highlights",
        "description": "Should list key features or highlights",
        "severity": "critical",
    },
    "star_history": {
        "name": "Star History",
        "description": "Should include a star history chart",
        "severity": "important",
    },
    "contributing": {
        "name": "Contributing",
        "description": "Should have a contributing section",
        "severity": "important",
    },
    "footer": {
        "name": "Footer",
        "description": "Should have a centered footer with author info",
        "severity": "nice-to-have",
    },
    "no_badge_wall": {
        "name": "No Badge Wall",
        "description": "Should not have more than 7 badges in the hero area",
        "severity": "important",
    },
    "no_coming_soon": {
        "name": "No Coming Soon",
        "description": "Should not have empty 'coming soon' placeholder sections",
        "severity": "important",
    },
    "alt_text": {
        "name": "Image Alt Text",
        "description": "All images should have meaningful alt text",
        "severity": "important",
    },
    "dark_mode": {
        "name": "Dark Mode Support",
        "description": "Images should have dark mode support via <picture> or SVG media queries",
        "severity": "nice-to-have",
    },
    "collapsible_sections": {
        "name": "Collapsible Sections",
        "description": "FAQ or verbose content should use <details> tags",
        "severity": "nice-to-have",
    },
    "mermaid_diagrams": {
        "name": "Visual Diagrams",
        "description": "Consider using Mermaid diagrams for architecture/workflow",
        "severity": "nice-to-have",
    },
    "social_proof_early": {
        "name": "Social Proof Early",
        "description": "Star count or social proof should appear in the first 30% of the file",
        "severity": "important",
    },
    "time_commitment": {
        "name": "Time Commitment",
        "description": "Quick Start should include estimated time (e.g., 'Get started in 30 seconds')",
        "severity": "nice-to-have",
    },
}


def check_readme(content: str, repo_path: str = ".") -> list:
    """Run all quality checks on README content."""
    results = []
    lines = content.split("\n")
    content_lower = content.lower()

    # Check: Hero Section
    has_hero = "<div align=\"center\">" in content or "<h1>" in content or re.search(r"^# .+", content, re.MULTILINE)
    results.append(("hero_section", has_hero, "" if has_hero else "Add a centered hero section with <div align='center'>"))

    # Check: Tagline
    has_tagline = bool(re.search(r"\*\*.{20,}\*\*", content) or re.search(r"<strong>.{20,}</strong>", content))
    results.append(("tagline", has_tagline, "" if has_tagline else "Add a bold tagline describing the project's value"))

    # Check: Badges
    badge_count = content.count("img.shields.io")
    results.append(("badges", badge_count >= 2, f"Found {badge_count} badges, recommend at least 2"))

    # Check: Quick Start
    has_qs = bool(re.search(r"(?i)quick\s*start|getting\s*started|install", content))
    results.append(("quick_start", has_qs, "" if has_qs else "Add a Quick Start section"))

    # Check: Features
    has_features = bool(re.search(r"(?i)(feature|highlight|what)", content))
    results.append(("features", has_features, "" if has_features else "Add a Features/Highlights section"))

    # Check: Star History
    has_star = "star-history" in content_lower or "star history" in content_lower
    results.append(("star_history", has_star, "" if has_star else "Add a Star History chart from star-history.com"))

    # Check: Contributing
    has_contrib = bool(re.search(r"(?i)contribut", content))
    results.append(("contributing", has_contrib, "" if has_contrib else "Add a Contributing section"))

    # Check: Footer
    has_footer = bool(re.search(r"(?i)(built with|made with|crafted with|❤️)", content))
    results.append(("footer", has_footer, "" if has_footer else "Add a footer with author attribution"))

    # Check: No badge wall
    hero_section = content[:2000]
    hero_badge_count = hero_section.count("img.shields.io")
    results.append(("no_badge_wall", hero_badge_count <= 7,
                     f"Found {hero_badge_count} badges in hero area, max recommended is 7"))

    # Check: No coming soon
    has_coming_soon = bool(re.search(r"(?i)(coming soon|TODO|placeholder|TBD)", content))
    results.append(("no_coming_soon", not has_coming_soon,
                     "Remove 'coming soon' / TODO placeholders"))

    # Check: Alt text
    bad_alt = re.findall(r"!\[\]\(", content)
    results.append(("alt_text", len(bad_alt) == 0,
                     f"Found {len(bad_alt)} images with empty alt text"))

    # Check: Dark mode
    has_dark = "<picture>" in content or "prefers-color-scheme" in content
    results.append(("dark_mode", has_dark,
                     "Consider adding <picture> elements for dark mode support"))

    # Check: Collapsible
    has_details = "<details>" in content
    results.append(("collapsible_sections", has_details,
                     "Use <details> for FAQ or verbose sections"))

    # Check: Social proof early
    first_third = content[:len(content) // 3]
    has_early_proof = "stars" in first_third.lower() or "download" in first_third.lower()
    results.append(("social_proof_early", has_early_proof,
                     "Move star count or download stats closer to the top"))

    # Check: Time commitment
    has_time = bool(re.search(r"(?i)(get started in|⏱️|seconds|minutes)", content))
    results.append(("time_commitment", has_time,
                     "Add time commitment to Quick Start (e.g., '⏱️ Get started in 30 seconds')"))

    return results


def main():
    parser = argparse.ArgumentParser(description="Quality check for README files")
    parser.add_argument("readme", help="Path to README.md")
    parser.add_argument("--repo-path", default=".", help="Path to repo root")
    parser.add_argument("--json", action="store_true", help="Output as JSON")

    args = parser.parse_args()

    readme_path = Path(args.readme)
    if not readme_path.exists():
        print(f"Error: {readme_path} not found", file=sys.stderr)
        sys.exit(1)

    content = readme_path.read_text()
    results = check_readme(content, args.repo_path)

    if args.json:
        import json
        output = []
        for check_id, passed, detail in results:
            check = CHECKS[check_id]
            output.append({
                "id": check_id,
                "name": check["name"],
                "severity": check["severity"],
                "passed": passed,
                "detail": detail,
            })
        print(json.dumps(output, indent=2))
    else:
        passed_count = sum(1 for _, p, _ in results if p)
        total = len(results)
        print(f"\n📋 README Quality Report: {passed_count}/{total} checks passed\n")

        severity_icon = {"critical": "🔴", "important": "🟡", "nice-to-have": "🟢"}

        for check_id, passed, detail in results:
            check = CHECKS[check_id]
            icon = "✅" if passed else severity_icon.get(check["severity"], "⚪")
            status = "PASS" if passed else "FAIL"
            print(f"  {icon} [{status}] {check['name']}")
            if detail and not passed:
                print(f"         → {detail}")

        critical_fails = sum(1 for cid, p, _ in results if not p and CHECKS[cid]["severity"] == "critical")
        if critical_fails > 0:
            print(f"\n⚠️  {critical_fails} critical check(s) failed. Fix these before publishing.")
            sys.exit(1)
        else:
            print("\n✨ No critical issues found!")


if __name__ == "__main__":
    main()

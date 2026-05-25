#!/usr/bin/env python3
"""Validate the generic AI development harness starter documentation map."""

from __future__ import annotations

import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = (
    "README.md",
    "AGENTS.md",
    "LICENSE",
    ".gitignore",
    ".github/pull_request_template.md",
    ".github/workflows/docs-harness.yml",
    ".harness/bootstrap.md",
    ".harness/config.yaml",
    ".harness/CHANGELOG.md",
    ".harness/decisions/0001-harness-operating-model.md",
    ".harness/decisions/0002-starter-adaptation-roadmap.md",
    ".harness/planning/roadmap.yaml",
    ".harness/planning/milestones.yaml",
    ".harness/planning/tasks.yaml",
    ".harness/templates/self-evolution-report.md",
    "scripts/harness/check_planning_graph.py",
    "scripts/harness/check_harness_contract.py",
    "scripts/harness/check_documentation_policy.py",
)

REQUIRED_HARNESS_DIRS = (
    "agents",
    "decisions",
    "gates",
    "manual-tests",
    "planning",
    "policies",
    "templates",
)

FORBIDDEN_STARTER_TOKENS = tuple(
    "".join(parts).lower()
    for parts in (
        ("pano", "rion"),
        ("wonjun", "choii"),
        ("supa", "base"),
        ("bill", "ing"),
        ("po", "lar"),
        ("cloud", "flare"),
        ("rail", "way"),
        ("second", "_brain"),
        ("not", "ion"),
        ("ora", "cle"),
        ("sing", "yusig"),
        ("shing", "gyusik"),
        ("/Us", "ers/"),
    )
)


def _read(relative_path: str) -> str:
    return (REPO_ROOT / relative_path).read_text(encoding="utf-8")


def _iter_text_files() -> list[Path]:
    roots = [
        REPO_ROOT / "README.md",
        REPO_ROOT / "AGENTS.md",
        REPO_ROOT / ".github",
        REPO_ROOT / ".harness",
        REPO_ROOT / "scripts",
    ]
    files: list[Path] = []
    for root in roots:
        if root.is_file():
            files.append(root)
        elif root.is_dir():
            files.extend(
                path
                for path in root.rglob("*")
                if path.is_file() and path.suffix in {".md", ".py", ".yaml", ".yml"}
            )
    return sorted(files)


def check_required_files(errors: list[str]) -> None:
    for relative_path in REQUIRED_FILES:
        if not (REPO_ROOT / relative_path).is_file():
            errors.append(f"missing required file: {relative_path}")


def check_harness_dirs(errors: list[str]) -> None:
    for dirname in REQUIRED_HARNESS_DIRS:
        path = REPO_ROOT / ".harness" / dirname
        if not path.is_dir():
            errors.append(f"missing harness directory: .harness/{dirname}")


def check_root_readme(errors: list[str]) -> None:
    text = _read("README.md")
    for token in (
        "AI Development Harness Starter",
        ".harness/bootstrap.md",
        "AGENTS.md",
        "python scripts/check_docs_harness.py",
        "python scripts/harness/check_planning_graph.py",
        "python scripts/harness/check_harness_contract.py",
        "python scripts/harness/check_documentation_policy.py",
    ):
        if token not in text:
            errors.append(f"README.md missing token: {token}")


def check_agent_map(errors: list[str]) -> None:
    text = _read("AGENTS.md")
    line_count = len(text.splitlines())
    if line_count > 120:
        errors.append(f"AGENTS.md must stay short; current line count: {line_count}")
    for token in (
            ".harness/config.yaml",
        ".harness/bootstrap.md",
        ".harness/agents/",
        ".harness/policies/",
        ".harness/gates/",
    ):
        if token not in text:
            errors.append(f"AGENTS.md missing routing token: {token}")


def check_harness_spine(errors: list[str]) -> None:
    bootstrap = _read(".harness/bootstrap.md")
    for token in (
            ".harness/config.yaml",
        ".harness/bootstrap.md",
        ".harness/agents/<role>.md",
        ".harness/policies/*.md",
        ".harness/gates/*.md",
        ".harness/planning/*.yaml",
    ):
        if token not in bootstrap:
            errors.append(f".harness/bootstrap.md missing token: {token}")

    config = _read(".harness/config.yaml")
    for token in (
        "docs_harness: python scripts/check_docs_harness.py",
        "planning_graph: python scripts/harness/check_planning_graph.py",
        "harness_contract: python scripts/harness/check_harness_contract.py",
        "documentation_policy: python scripts/harness/check_documentation_policy.py",
    ):
        if token not in config:
            errors.append(f".harness/config.yaml missing check token: {token}")


def check_planning_examples(errors: list[str]) -> None:
    for relative_path in (
        ".harness/planning/roadmap.yaml",
        ".harness/planning/milestones.yaml",
        ".harness/planning/tasks.yaml",
    ):
        text = _read(relative_path)
        if "STARTER-" not in text:
            errors.append(f"{relative_path} must use starter example ids")


def check_no_project_references(errors: list[str]) -> None:
    for path in _iter_text_files():
        text = path.read_text(encoding="utf-8").lower()
        relative = path.relative_to(REPO_ROOT).as_posix()
        for token in FORBIDDEN_STARTER_TOKENS:
            if token in text:
                errors.append(f"project-specific token in {relative}: {token}")


def main() -> int:
    errors: list[str] = []
    check_required_files(errors)
    check_harness_dirs(errors)
    check_root_readme(errors)
    check_agent_map(errors)
    check_harness_spine(errors)
    check_planning_examples(errors)
    check_no_project_references(errors)

    if errors:
        for error in errors:
            print(f"docs harness error: {error}", file=sys.stderr)
        return 1

    print("Docs harness check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

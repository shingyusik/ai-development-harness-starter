#!/usr/bin/env python3
"""Validate generic documentation placement and current-state prose policy."""

from __future__ import annotations

import re
from pathlib import Path


REPO_ROOT = Path.cwd()

ROOT_HARNESS_INTERNAL_PATTERNS = (
    re.compile(r"\bHarness guidance:"),
)

CHANGELOG_LIKE_PATTERNS = (
    re.compile(r"\bpreviously we\b", re.IGNORECASE),
    re.compile(r"\bpreviously,", re.IGNORECASE),
    re.compile(r"\bchanged from\b", re.IGNORECASE),
    re.compile(r"\bwe changed\b", re.IGNORECASE),
    re.compile(r"\bwas changed\b", re.IGNORECASE),
    re.compile(r"\bmigration history\b", re.IGNORECASE),
)

CURRENT_STATE_DOC_DIRS = ("docs",)
CURRENT_STATE_ROOT_DOCS = ("README.md", "AGENTS.md")
EXCLUDED_DOC_PARTS = {"decisions", "plans", "harness"}


def _relative_path(path: Path) -> str:
    return path.relative_to(REPO_ROOT).as_posix()


def _is_changelog_file(path: Path) -> bool:
    lowered = path.name.lower()
    return lowered in {"changelog.md", "changes.md", "history.md"} or "changelog" in lowered


def _read_lines(path: Path) -> list[str]:
    return path.read_text(encoding="utf-8").splitlines()


def _root_docs_for_harness_scan() -> list[Path]:
    return sorted(
        path
        for path in REPO_ROOT.glob("*.md")
        if path.is_file() and not _is_changelog_file(path)
    )


def _current_state_docs_for_changelog_scan() -> list[Path]:
    docs = [REPO_ROOT / name for name in CURRENT_STATE_ROOT_DOCS if (REPO_ROOT / name).is_file()]

    for directory_name in CURRENT_STATE_DOC_DIRS:
        directory = REPO_ROOT / directory_name
        if not directory.is_dir():
            continue
        docs.extend(
            path
            for path in directory.rglob("*.md")
            if path.is_file() and not _is_excluded_current_state_doc(path)
        )

    return sorted(set(docs))


def _is_excluded_current_state_doc(path: Path) -> bool:
    relative_parts = path.relative_to(REPO_ROOT).parts
    if _is_changelog_file(path):
        return True
    if relative_parts[:2] == (".harness", "CHANGELOG.md"):
        return True
    return len(relative_parts) >= 2 and relative_parts[0] == "docs" and relative_parts[1] in EXCLUDED_DOC_PARTS


def _scan_patterns(path: Path, patterns: tuple[re.Pattern[str], ...], label: str) -> list[str]:
    errors: list[str] = []
    for line_number, line in enumerate(_read_lines(path), 1):
        if any(pattern.search(line) for pattern in patterns):
            errors.append(f"{label}: {_relative_path(path)}:{line_number}")
    return errors


def validate() -> list[str]:
    errors: list[str] = []

    for path in _root_docs_for_harness_scan():
        errors.extend(
            _scan_patterns(
                path,
                ROOT_HARNESS_INTERNAL_PATTERNS,
                "root doc contains harness internals",
            )
        )

    for path in _current_state_docs_for_changelog_scan():
        errors.extend(
            _scan_patterns(
                path,
                CHANGELOG_LIKE_PATTERNS,
                "changelog-like prose",
            )
        )

    return errors


def main() -> int:
    errors = validate()
    status = "FAIL" if errors else "PASS"

    print(f"Documentation policy check: {status}")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")

    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

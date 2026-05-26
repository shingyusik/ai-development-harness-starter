#!/usr/bin/env python3
"""Validate the Codex-first AI development harness starter documentation map."""

from __future__ import annotations

import sys
import tomllib
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = (
    "README.md",
    "AGENTS.md",
    "LICENSE",
    ".gitignore",
    ".codex/config.toml",
    ".codex/agents/harness-pm.toml",
    ".codex/agents/harness-tech-lead.toml",
    ".codex/agents/harness-implementer.toml",
    ".codex/agents/harness-spec-reviewer.toml",
    ".codex/agents/harness-quality-reviewer.toml",
    ".codex/agents/harness-architecture-reviewer.toml",
    ".codex/agents/harness-branch-manager.toml",
    ".codex/agents/harness-self-evolution.toml",
    ".agents/skills/harness/SKILL.md",
    ".agents/skills/harness-planning/SKILL.md",
    ".agents/skills/harness-review-gates/SKILL.md",
    ".agents/skills/harness-self-evolution/SKILL.md",
    ".github/pull_request_template.md",
    ".github/workflows/docs-harness.yml",
    ".harness/bootstrap.md",
    ".harness/config.yaml",
    ".harness/roles.yaml",
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
    "decisions",
    "gates",
    "manual-tests",
    "planning",
    "policies",
    "templates",
)

REQUIRED_CODEX_DIRS = (
    ".codex",
    ".codex/agents",
    ".agents",
    ".agents/skills",
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
        REPO_ROOT / ".codex",
        REPO_ROOT / ".agents",
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
                if path.is_file() and path.suffix in {".md", ".py", ".yaml", ".yml", ".toml"}
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


def check_codex_dirs(errors: list[str]) -> None:
    for dirname in REQUIRED_CODEX_DIRS:
        path = REPO_ROOT / dirname
        if not path.is_dir():
            errors.append(f"missing Codex directory: {dirname}")


def check_root_readme(errors: list[str]) -> None:
    text = _read("README.md")
    for token in (
        "AI Development Harness Starter",
        "Codex-first",
        ".codex/agents/*.toml",
        ".agents/skills/*/SKILL.md",
        ".agents/skills/harness/SKILL.md",
        ".harness/bootstrap.md",
        "AGENTS.md",
        "$harness",
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
    if line_count > 40:
        errors.append(f"AGENTS.md must stay short; current line count: {line_count}")
    for token in (
        "$harness",
        ".agents/skills/harness/SKILL.md",
        ".codex/agents/*.toml",
        ".agents/skills/",
        ".harness/roles.yaml",
        ".harness/",
    ):
        if token not in text:
            errors.append(f"AGENTS.md missing routing token: {token}")


def check_harness_entry_skill(errors: list[str]) -> None:
    text = _read(".agents/skills/harness/SKILL.md")
    for token in (
        "name: harness",
        "/harness <task>",
        "$harness <task>",
        ".harness/config.yaml",
        ".harness/bootstrap.md",
        ".harness/roles.yaml",
        ".codex/agents/*.toml",
        ".agents/skills/*/SKILL.md",
        "Required Report Shape",
    ):
        if token not in text:
            errors.append(f".agents/skills/harness/SKILL.md missing entry/procedure token: {token}")

def check_harness_spine(errors: list[str]) -> None:
    bootstrap = _read(".harness/bootstrap.md")
    for token in (
        ".codex/config.toml",
        ".codex/agents/*.toml",
        ".agents/skills/*/SKILL.md",
        ".harness/config.yaml",
        ".harness/roles.yaml",
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
        "codex:",
        "required_agents:",
        "required_skills:",
    ):
        if token not in config:
            errors.append(f".harness/config.yaml missing check token: {token}")


def check_codex_config(errors: list[str]) -> None:
    config_path = REPO_ROOT / ".codex/config.toml"
    try:
        config = tomllib.loads(config_path.read_text(encoding="utf-8"))
    except tomllib.TOMLDecodeError as exc:
        errors.append(f"invalid TOML in .codex/config.toml: {exc}")
        return

    agents = config.get("agents")
    if not isinstance(agents, dict):
        errors.append(".codex/config.toml missing [agents] table")
        return
    if agents.get("max_depth") != 1:
        errors.append(".codex/config.toml agents.max_depth must be 1")
    if not isinstance(agents.get("max_threads"), int):
        errors.append(".codex/config.toml agents.max_threads must be an integer")


def check_codex_agents(errors: list[str]) -> None:
    for path in sorted((REPO_ROOT / ".codex/agents").glob("*.toml")):
        relative = path.relative_to(REPO_ROOT).as_posix()
        try:
            data = tomllib.loads(path.read_text(encoding="utf-8"))
        except tomllib.TOMLDecodeError as exc:
            errors.append(f"invalid TOML in {relative}: {exc}")
            continue
        for field in ("name", "description", "developer_instructions"):
            if not isinstance(data.get(field), str) or not data[field].strip():
                errors.append(f"{relative} missing required Codex agent field: {field}")
        if data.get("sandbox_mode") == "read-only" and "Do not" not in data.get("developer_instructions", ""):
            errors.append(f"{relative} read-only agent should explicitly say what it must not do")


def check_codex_skills(errors: list[str]) -> None:
    for path in sorted((REPO_ROOT / ".agents/skills").glob("*/SKILL.md")):
        relative = path.relative_to(REPO_ROOT).as_posix()
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            errors.append(f"{relative} missing YAML frontmatter")
            continue
        try:
            frontmatter = text.split("---\n", 2)[1]
        except IndexError:
            errors.append(f"{relative} malformed YAML frontmatter")
            continue
        for field in ("name:", "description:"):
            if field not in frontmatter:
                errors.append(f"{relative} missing required skill frontmatter field: {field[:-1]}")


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
    check_codex_dirs(errors)
    check_root_readme(errors)
    check_agent_map(errors)
    check_harness_entry_skill(errors)
    check_harness_spine(errors)
    check_codex_config(errors)
    check_codex_agents(errors)
    check_codex_skills(errors)
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

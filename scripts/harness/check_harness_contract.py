#!/usr/bin/env python3
"""Validate the generic AI development harness starter contract."""

from __future__ import annotations

from pathlib import Path
from typing import Any
import tomllib

import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]
CONFIG_PATH = ".harness/config.yaml"
BOOTSTRAP_PATH = ".harness/bootstrap.md"

ROOT_ROUTING_FILES = {"AGENTS.md"}
FORBIDDEN_SOURCE_OF_TRUTH_FILES = {"AGENT.md", "CLAUDE.md"}
FUTURE_HARNESS_DIRS = (".harness/policies", ".harness/gates")
FORBIDDEN_HARNESS_AGENT_PATH = ".harness/agents"


def _repo_path(relative_path: str) -> Path:
    return REPO_ROOT / relative_path


def _normalize_path(value: Any) -> str | None:
    if not isinstance(value, str):
        return None
    path = value.strip()
    if not path:
        return None
    return Path(path).as_posix()


def _is_within_harness(relative_path: str) -> bool:
    return relative_path == ".harness" or relative_path.startswith(".harness/")


def _flatten_source_of_truth(source_of_truth: Any) -> list[str]:
    paths: list[str] = []
    if isinstance(source_of_truth, dict):
        for value in source_of_truth.values():
            if isinstance(value, list):
                paths.extend(path for item in value if (path := _normalize_path(item)))
            elif path := _normalize_path(value):
                paths.append(path)
    elif isinstance(source_of_truth, list):
        paths.extend(path for item in source_of_truth if (path := _normalize_path(item)))
    elif path := _normalize_path(source_of_truth):
        paths.append(path)
    return paths


def _load_config(errors: list[str]) -> dict[str, Any] | None:
    config_file = _repo_path(CONFIG_PATH)
    if not config_file.is_file():
        errors.append(f"missing config file: {CONFIG_PATH}")
        return None

    try:
        loaded = yaml.safe_load(config_file.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        errors.append(f"invalid YAML in {CONFIG_PATH}: {exc}")
        return None

    if not isinstance(loaded, dict):
        errors.append(f"invalid YAML in {CONFIG_PATH}: expected mapping at document root")
        return None

    return loaded


def _check_existing_file(relative_path: str, label: str, errors: list[str]) -> None:
    if not _repo_path(relative_path).is_file():
        errors.append(f"missing {label}: {relative_path}")


def _check_required_spine_files(config: dict[str, Any], errors: list[str]) -> None:
    required = config.get("required_spine_files")
    if not isinstance(required, list):
        errors.append("config required_spine_files must be a list")
        return

    for item in required:
        path = _normalize_path(item)
        if path is None:
            errors.append(f"invalid required spine path: {item!r}")
            continue
        if not _is_within_harness(path):
            errors.append(f"required spine path outside .harness: {path}")
            continue
        _check_existing_file(path, "required spine file", errors)


def _check_source_of_truth(config: dict[str, Any], errors: list[str]) -> None:
    source_paths = _flatten_source_of_truth(config.get("source_of_truth"))
    if not source_paths:
        errors.append("config source_of_truth must list decision and milestone paths")
        return

    for path in source_paths:
        if path in ROOT_ROUTING_FILES or path in FORBIDDEN_SOURCE_OF_TRUTH_FILES:
            errors.append(f"root routing/instruction file listed as source_of_truth: {path}")
            continue
        if not _is_within_harness(path):
            errors.append(f"source_of_truth path outside .harness: {path}")
            continue
        _check_existing_file(path, "source_of_truth file", errors)


def _check_named_source_groups(config: dict[str, Any], errors: list[str]) -> None:
    source_of_truth = config.get("source_of_truth")
    if not isinstance(source_of_truth, dict):
        return

    for group_name in ("decisions", "planning"):
        paths = source_of_truth.get(group_name)
        if not isinstance(paths, list) or not paths:
            errors.append(f"config source_of_truth.{group_name} must be a non-empty list")
            continue
        for item in paths:
            path = _normalize_path(item)
            if path is not None:
                _check_existing_file(path, f"source_of_truth {group_name} file", errors)


def _check_check_paths(config: dict[str, Any], errors: list[str]) -> None:
    checks = config.get("checks")
    if checks is None:
        return
    if not isinstance(checks, dict):
        errors.append("config checks must be a mapping")
        return

    harness_contract = checks.get("harness_contract")
    if harness_contract is None:
        return
    if harness_contract != "python scripts/harness/check_harness_contract.py":
        errors.append(
            "checks.harness_contract must point to "
            "python scripts/harness/check_harness_contract.py"
        )


def _check_codex_config(config: dict[str, Any], errors: list[str]) -> None:
    codex = config.get("codex")
    if not isinstance(codex, dict):
        errors.append("config codex must be a mapping")
        return

    codex_config = _normalize_path(codex.get("config"))
    if codex_config != ".codex/config.toml":
        errors.append("config codex.config must point to .codex/config.toml")
    elif not _repo_path(codex_config).is_file():
        errors.append("missing Codex config file: .codex/config.toml")
    else:
        try:
            codex_toml = tomllib.loads(_repo_path(codex_config).read_text(encoding="utf-8"))
        except tomllib.TOMLDecodeError as exc:
            errors.append(f"invalid TOML in .codex/config.toml: {exc}")
        else:
            agents = codex_toml.get("agents")
            if not isinstance(agents, dict):
                errors.append(".codex/config.toml missing [agents] table")
            elif agents.get("max_depth") != 1:
                errors.append(".codex/config.toml agents.max_depth must be 1")

    for key, prefix in (("required_agents", ".codex/agents/"), ("required_skills", ".agents/skills/")):
        values = codex.get(key)
        if not isinstance(values, list) or not values:
            errors.append(f"config codex.{key} must be a non-empty list")
            continue
        for item in values:
            path = _normalize_path(item)
            if path is None:
                errors.append(f"invalid codex {key} path: {item!r}")
                continue
            if not path.startswith(prefix):
                errors.append(f"codex {key} path must start with {prefix}: {path}")
                continue
            _check_existing_file(path, f"codex {key} file", errors)



def _check_roles_registry(config: dict[str, Any], errors: list[str]) -> None:
    roles_path = _repo_path(".harness/roles.yaml")
    if not roles_path.is_file():
        errors.append("missing roles registry: .harness/roles.yaml")
        return
    try:
        roles_doc = yaml.safe_load(roles_path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        errors.append(f"invalid YAML in .harness/roles.yaml: {exc}")
        return
    if not isinstance(roles_doc, dict):
        errors.append("invalid YAML in .harness/roles.yaml: expected mapping at document root")
        return
    if roles_doc.get("runtime") != "codex":
        errors.append(".harness/roles.yaml runtime must be codex")
    roles = roles_doc.get("roles")
    if not isinstance(roles, dict) or not roles:
        errors.append(".harness/roles.yaml roles must be a non-empty mapping")
        return

    codex = config.get("codex") if isinstance(config.get("codex"), dict) else {}
    required_agents = {
        _normalize_path(item)
        for item in codex.get("required_agents", [])
        if _normalize_path(item) is not None
    }
    bound_agents: set[str] = set()
    for role_name, role_config in roles.items():
        if not isinstance(role_name, str) or not role_name.strip():
            errors.append(f"invalid role name in .harness/roles.yaml: {role_name!r}")
            continue
        if not isinstance(role_config, dict):
            errors.append(f"role {role_name} must be a mapping")
            continue
        codex_agent = _normalize_path(role_config.get("codex_agent"))
        if codex_agent is None:
            errors.append(f"role {role_name} missing codex_agent")
        elif not codex_agent.startswith(".codex/agents/"):
            errors.append(f"role {role_name} codex_agent must start with .codex/agents/: {codex_agent}")
        else:
            _check_existing_file(codex_agent, f"role {role_name} codex_agent", errors)
            bound_agents.add(codex_agent)
        reads = role_config.get("reads", [])
        if reads is not None and not isinstance(reads, list):
            errors.append(f"role {role_name} reads must be a list")
            continue
        for item in reads or []:
            read_path = _normalize_path(item)
            if read_path is None:
                errors.append(f"role {role_name} invalid reads path: {item!r}")
                continue
            if not _is_within_harness(read_path):
                errors.append(f"role {role_name} reads path outside .harness: {read_path}")
                continue
            _check_existing_file(read_path, f"role {role_name} reads file", errors)

    missing_bindings = sorted(required_agents - bound_agents)
    for path in missing_bindings:
        errors.append(f"required Codex agent is not referenced by .harness/roles.yaml: {path}")


def _check_no_duplicate_harness_agents(errors: list[str]) -> None:
    if _repo_path(FORBIDDEN_HARNESS_AGENT_PATH).exists():
        errors.append(
            "duplicate harness agent directory is forbidden; "
            "use .codex/agents/*.toml plus .harness/roles.yaml instead: "
            f"{FORBIDDEN_HARNESS_AGENT_PATH}"
        )

def _check_bootstrap_contract(errors: list[str]) -> None:
    bootstrap_file = _repo_path(BOOTSTRAP_PATH)
    if not bootstrap_file.is_file():
        errors.append(f"missing bootstrap file: {BOOTSTRAP_PATH}")
        return

    for line_number, line in enumerate(bootstrap_file.read_text(encoding="utf-8").splitlines(), 1):
        if not _line_requires_forbidden_startup_file(line):
            continue
        errors.append(
            f"bootstrap requires forbidden harness startup/source file at "
            f"{BOOTSTRAP_PATH}:{line_number}: {line.strip()}"
        )


def _line_requires_forbidden_startup_file(line: str) -> bool:
    lowered = line.lower()
    if not any(token in line for token in FORBIDDEN_SOURCE_OF_TRUTH_FILES):
        return False
    if any(
        phrase in lowered
        for phrase in (
            "not required",
            "not the harness source of truth",
            "not required for harness",
            "avoid ",
            "must not require",
            "not used as harness",
            "forbidden dependency",
            "are not required",
            "are not the harness source",
            "stop if bootstrap requires",
            "if bootstrap requires",
        )
    ):
        return False

    return True


def _check_warnings(warnings: list[str]) -> None:
    for path in FUTURE_HARNESS_DIRS:
        if not _repo_path(path).is_dir():
            warnings.append(f"future optional harness directory missing: {path}")


def validate() -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    config = _load_config(errors)
    if config is not None:
        _check_required_spine_files(config, errors)
        _check_source_of_truth(config, errors)
        _check_named_source_groups(config, errors)
        _check_check_paths(config, errors)
        _check_codex_config(config, errors)
        _check_roles_registry(config, errors)

    _check_bootstrap_contract(errors)
    _check_no_duplicate_harness_agents(errors)
    _check_warnings(warnings)

    return errors, warnings


def main() -> int:
    errors, warnings = validate()
    status = "FAIL" if errors else "PASS"

    print(f"Harness contract check: {status}")
    if errors:
        print("Errors:")
        for error in errors:
            print(f"- {error}")
    else:
        print("Errors: none")

    if warnings:
        print("Warnings:")
        for warning in warnings:
            print(f"- {warning}")
    else:
        print("Warnings: none")

    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

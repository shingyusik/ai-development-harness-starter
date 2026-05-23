#!/usr/bin/env python3
"""Validate the generic AI development harness starter contract."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]
CONFIG_PATH = ".harness/config.yaml"
BOOTSTRAP_PATH = ".harness/bootstrap.md"

ROOT_ROUTING_FILES = {"AGENTS.md"}
FORBIDDEN_SOURCE_OF_TRUTH_FILES = {"AGENT.md", "CLAUDE.md"}
FUTURE_HARNESS_DIRS = (".harness/agents", ".harness/policies", ".harness/gates")


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

    _check_bootstrap_contract(errors)
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

#!/usr/bin/env python3
"""Validate the generic harness planning graph."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml


REPO_ROOT = Path.cwd()
PLANNING_DIR = ".harness/planning"
PRIORITIES = {"P0", "P1", "P2", "P3", "P4"}
STATUSES = {"planned", "blocked", "ready", "active", "done", "example"}

ROADMAP_REQUIRED = ("id", "title", "priority", "depends_on", "blocks", "goal", "done_when")
MILESTONE_REQUIRED = (
    "id",
    "title",
    "priority",
    "status",
    "depends_on",
    "blocks",
    "owner_role",
    "source",
    "done_when",
)
TASK_REQUIRED = (
    "id",
    "title",
    "milestone_id",
    "priority",
    "status",
    "depends_on",
    "owner_role",
    "rationale",
    "acceptance",
    "sequencing_rationale",
)


def _load_planning_file(filename: str, collection_key: str, errors: list[str]) -> list[dict[str, Any]]:
    relative_path = f"{PLANNING_DIR}/{filename}"
    path = REPO_ROOT / relative_path
    if not path.is_file():
        errors.append(f"missing planning file: {relative_path}")
        return []

    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        errors.append(f"invalid YAML in {relative_path}: {exc}")
        return []

    if not isinstance(data, dict):
        errors.append(f"invalid YAML in {relative_path}: expected mapping at document root")
        return []
    if data.get("version") != 1:
        errors.append(f"invalid version in {relative_path}: expected 1")

    collection = data.get(collection_key)
    if not isinstance(collection, list):
        errors.append(f"invalid collection in {relative_path}: {collection_key} must be a list")
        return []

    entries: list[dict[str, Any]] = []
    for index, item in enumerate(collection, 1):
        if not isinstance(item, dict):
            errors.append(f"invalid {collection_key} entry at index {index}: expected mapping")
            continue
        entries.append(item)
    return entries


def _entry_id(entry: dict[str, Any], fallback: str) -> str:
    value = entry.get("id")
    return value if isinstance(value, str) and value else fallback


def _validate_required_fields(
    graph_name: str,
    entries: list[dict[str, Any]],
    required_fields: tuple[str, ...],
    list_fields: set[str],
    errors: list[str],
) -> None:
    for index, entry in enumerate(entries, 1):
        entry_id = _entry_id(entry, f"<entry {index}>")
        for field in required_fields:
            if field not in entry:
                errors.append(f"missing required {graph_name} field: {entry_id} {field}")
                continue
            if field in list_fields and not isinstance(entry[field], list):
                errors.append(f"invalid {graph_name} list field: {entry_id} {field} must be a list")


def _validate_ids(graph_name: str, entries: list[dict[str, Any]], errors: list[str]) -> set[str]:
    seen: set[str] = set()
    for index, entry in enumerate(entries, 1):
        entry_id = entry.get("id")
        if not isinstance(entry_id, str) or not entry_id:
            errors.append(f"invalid {graph_name} id at entry {index}: expected non-empty string")
            continue
        if entry_id in seen:
            errors.append(f"duplicate {graph_name} id: {entry_id}")
        seen.add(entry_id)
    return seen


def _validate_priority_and_status(
    graph_name: str,
    entries: list[dict[str, Any]],
    errors: list[str],
) -> None:
    for index, entry in enumerate(entries, 1):
        entry_id = _entry_id(entry, f"<entry {index}>")
        priority = entry.get("priority")
        if priority is not None and priority not in PRIORITIES:
            errors.append(f"invalid priority: {entry_id} {priority}")
        status = entry.get("status")
        if status is not None and status not in STATUSES:
            errors.append(f"invalid status: {entry_id} {status}")


def _list_value(entry: dict[str, Any], field: str) -> list[Any]:
    value = entry.get(field)
    return value if isinstance(value, list) else []


def _validate_milestone_references(
    graph_name: str,
    entries: list[dict[str, Any]],
    milestone_ids: set[str],
    errors: list[str],
) -> None:
    for entry in entries:
        entry_id = _entry_id(entry, "<unknown>")
        for field in ("depends_on", "blocks"):
            for dependency in _list_value(entry, field):
                if dependency not in milestone_ids:
                    errors.append(f"unknown dependency: {entry_id} {field} {dependency}")


def _validate_task_references(
    tasks: list[dict[str, Any]],
    task_ids: set[str],
    milestone_ids: set[str],
    errors: list[str],
) -> None:
    for task in tasks:
        task_id = _entry_id(task, "<unknown>")
        milestone_id = task.get("milestone_id")
        if milestone_id not in milestone_ids:
            errors.append(f"unknown milestone: {task_id} milestone_id {milestone_id}")
        for dependency in _list_value(task, "depends_on"):
            if dependency not in task_ids:
                errors.append(f"unknown dependency: {task_id} depends on {dependency}")


def _build_dependency_graph(
    entries: list[dict[str, Any]],
    known_ids: set[str],
    dependency_field: str = "depends_on",
) -> dict[str, list[str]]:
    graph: dict[str, list[str]] = {}
    for entry in entries:
        entry_id = entry.get("id")
        if not isinstance(entry_id, str) or entry_id not in known_ids:
            continue
        graph[entry_id] = [
            dependency
            for dependency in _list_value(entry, dependency_field)
            if isinstance(dependency, str) and dependency in known_ids
        ]
    return graph


def _find_cycle(graph: dict[str, list[str]]) -> list[str] | None:
    visiting: set[str] = set()
    visited: set[str] = set()
    stack: list[str] = []

    def visit(node: str) -> list[str] | None:
        if node in visited:
            return None
        if node in visiting:
            start = stack.index(node)
            return [*stack[start:], node]

        visiting.add(node)
        stack.append(node)
        for dependency in graph.get(node, []):
            cycle = visit(dependency)
            if cycle:
                return cycle
        stack.pop()
        visiting.remove(node)
        visited.add(node)
        return None

    for node in graph:
        cycle = visit(node)
        if cycle:
            return cycle
    return None


def _validate_task_statuses(tasks: list[dict[str, Any]], errors: list[str]) -> None:
    status_by_id = {
        task["id"]: task.get("status")
        for task in tasks
        if isinstance(task.get("id"), str)
    }
    for task in tasks:
        task_id = _entry_id(task, "<unknown>")
        status = task.get("status")
        if status == "done":
            continue

        dependencies = [
            dependency
            for dependency in _list_value(task, "depends_on")
            if isinstance(dependency, str) and dependency in status_by_id
        ]
        has_unfinished_dependency = any(status_by_id[dependency] != "done" for dependency in dependencies)
        if has_unfinished_dependency and status != "blocked":
            errors.append(f"status mismatch: {task_id} has unfinished dependencies but is {status}")
        if dependencies and not has_unfinished_dependency and status == "blocked":
            errors.append(f"status mismatch: {task_id} is blocked but all dependencies are done")


def validate() -> list[str]:
    errors: list[str] = []
    roadmap = _load_planning_file("roadmap.yaml", "roadmap", errors)
    milestones = _load_planning_file("milestones.yaml", "milestones", errors)
    tasks = _load_planning_file("tasks.yaml", "tasks", errors)

    _validate_required_fields("roadmap", roadmap, ROADMAP_REQUIRED, {"depends_on", "blocks", "done_when"}, errors)
    _validate_required_fields(
        "milestone",
        milestones,
        MILESTONE_REQUIRED,
        {"depends_on", "blocks", "done_when"},
        errors,
    )
    _validate_required_fields("task", tasks, TASK_REQUIRED, {"depends_on", "acceptance"}, errors)

    roadmap_ids = _validate_ids("roadmap", roadmap, errors)
    milestone_ids = _validate_ids("milestone", milestones, errors)
    task_ids = _validate_ids("task", tasks, errors)

    _validate_priority_and_status("roadmap", roadmap, errors)
    _validate_priority_and_status("milestone", milestones, errors)
    _validate_priority_and_status("task", tasks, errors)

    _validate_milestone_references("roadmap", roadmap, milestone_ids, errors)
    _validate_milestone_references("milestone", milestones, milestone_ids, errors)
    _validate_task_references(tasks, task_ids, milestone_ids, errors)

    for graph_name, graph in (
        ("milestone", _build_dependency_graph(milestones, milestone_ids)),
        ("task", _build_dependency_graph(tasks, task_ids)),
    ):
        cycle = _find_cycle(graph)
        if cycle:
            errors.append(f"dependency cycle detected in {graph_name} graph: {' -> '.join(cycle)}")

    _validate_task_statuses(tasks, errors)

    for roadmap_id in roadmap_ids - milestone_ids:
        errors.append(f"unknown roadmap milestone id: {roadmap_id}")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("Planning graph check: FAIL")
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("Planning graph check: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

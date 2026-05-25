# AI Development Harness Starter

이 저장소는 프로젝트에 복사해서 쓸 수 있는 **Codex-first repo AI 개발 하네스 스타터**다.

핵심 시작 파일은 루트 `AGENTS.md`, `.codex/config.toml`, `.codex/agents/*.toml`, `.agents/skills/*/SKILL.md`, `.harness/bootstrap.md`다. 우선 Codex CLI/App 기준으로 구성하고, Claude Code 호환은 이후 확장한다.

## 목적

- Codex가 프로젝트 규칙을 매번 다시 추측하지 않게 한다.
- 로드맵, 태스크, 정책, 리뷰 gate, 검증 명령을 저장소 안에 둔다.
- Codex 공식 subagents/custom agents 구조인 `.codex/agents/*.toml`을 제공한다.
- Codex 공식 skills 구조인 `.agents/skills/*/SKILL.md`를 제공한다.
- 하네스 기준은 `.harness/`에 모은다.
- 루트 `AGENTS.md`는 Codex가 먼저 읽는 프로젝트 source paths, test/build commands, architecture constraints와 하네스 진입 순서를 안내한다.

## 빠른 시작

1. 이 저장소를 새 프로젝트에 복사하거나 template으로 사용한다.
2. `AGENTS.md`의 project purpose, source paths, test/build commands, architecture constraints를 프로젝트에 맞게 바꾼다.
3. `.codex/agents/*.toml`에서 필요한 Codex custom agent만 남기거나 프로젝트에 맞게 조정한다.
4. `.agents/skills/*/SKILL.md`에서 프로젝트 반복 워크플로우에 맞는 repo skill을 조정한다.
5. `.harness/config.yaml`의 required checks, source paths, Codex required files를 프로젝트에 맞게 바꾼다.
6. `.harness/planning/*.yaml`에 실제 roadmap, milestone, task를 입력한다.
7. `.harness/policies/`와 `.harness/gates/`에서 프로젝트에 맞지 않는 항목을 줄이거나 고친다.
8. 아래 검증을 실행한다.

```bash
python scripts/harness/check_harness_contract.py
python scripts/harness/check_planning_graph.py
python scripts/harness/check_documentation_policy.py
python scripts/check_docs_harness.py
```

## 주요 폴더

- `.codex/`: Codex project config와 custom subagent 정의.
- `.agents/skills/`: Codex repo-scoped skills.
- `.harness/`: 하네스 정책, gate, planning, registry source of truth.
- `.harness/roles.yaml`: 하네스 role을 `.codex/agents/*.toml`과 필요한 policy/gate/planning 파일에 연결하는 registry.
- `.harness/policies/`: 지속적으로 지킬 정책.
- `.harness/gates/`: 리뷰/머지 전 확인 기준.
- `.harness/planning/`: roadmap, milestone, task graph.
- `.harness/templates/`: 반복 문서 템플릿.
- `scripts/harness/`: 하네스 검증 스크립트.
- `.github/`: PR/CI starter 파일.

## 사용 원칙

- Codex custom agent는 `.codex/agents/<agent>.toml`에 둔다. 각 파일은 `name`, `description`, `developer_instructions`를 가져야 한다.
- Codex skill은 `.agents/skills/<skill>/SKILL.md`에 둔다. 각 `SKILL.md`는 `name`, `description` frontmatter를 가져야 한다.
- subagent fan-out은 명시적으로 요청할 때만 사용하고, 기본 depth는 1로 유지한다.
- 프로젝트 고유 규칙이 생기면 `.harness/`에 기록하되, 실행 가능한 role 지시문은 `.codex/agents/*.toml`에만 둔다.
- 사람이 반복해서 지적한 문제는 policy, gate, script, test 중 하나로 바꾼다.
- 긴 설명보다 짧은 checklist와 실행 가능한 검증을 우선한다.
- 최종 문서는 영어로 운용해도 된다. 지금 한국어 문서는 설계 피드백용 초안이다.

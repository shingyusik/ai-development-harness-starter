# Project Agent Entry Point

이 파일은 Codex가 시작할 때 먼저 읽는 **프로젝트 소스코드 작업 지침**이다.
하네스 정책/게이트/계획의 source of truth는 `.harness/`에 있지만, 실행 가능한 역할 정의의 source of truth는 루트 `.codex/agents/*.toml`이다. 이 파일은 대상 프로젝트의 코드 구조와 작업 방식을 먼저 잡아주는 얇은 entry point여야 한다.

## 프로젝트 컨텍스트를 먼저 채운다

새 프로젝트에 이 starter를 적용할 때 아래 항목을 프로젝트에 맞게 바꾼다.

- Project purpose: 이 저장소가 제공하는 제품/라이브러리/서비스의 목적.
- Primary source paths: 예: `src/`, `app/`, `packages/*`, `services/*`.
- Primary test paths: 예: `tests/`, `spec/`, `__tests__/`.
- Build/test commands: 실제 lint, typecheck, test, build 명령.
- Runtime/config files: 예: `package.json`, `pyproject.toml`, `Cargo.toml`, `docker-compose.yml`.
- Architecture constraints: 계층, module boundary, public API, data ownership 규칙.
- Local safety rules: secrets, local data, generated files, migration 주의사항.

## 소스코드 작업 기본 규칙

- 변경 전에 관련 source path, test path, config file을 먼저 읽는다.
- 기존 public API, data model, migration, dependency boundary를 깨지 않는다.
- 새 abstraction은 현재 변경 범위에서 반복이 확인될 때만 만든다.
- hardcoding, dead code, hidden global state, 불필요한 dependency 추가를 피한다.
- 기능 변경은 가능한 한 test 또는 명시적 manual evidence와 함께 제출한다.
- generated/build/cache/local data 파일은 의도적으로 필요한 경우가 아니면 수정하지 않는다.

## 하네스 시작 순서

프로젝트 컨텍스트를 확인한 뒤, 필요한 만큼 하네스를 읽는다.

1. `.codex/config.toml`에서 subagent limits를 확인한다.
2. `.codex/agents/`에서 필요한 Codex custom agent를 확인한다.
3. `.agents/skills/`에서 관련 repo skill을 확인한다.
4. `.harness/config.yaml`을 읽고 required checks와 source paths를 확인한다.
5. `.harness/bootstrap.md`를 읽는다.
6. `.harness/roles.yaml`에서 가장 좁은 역할의 `.codex/agents/*.toml` binding과 추가 로딩 파일을 확인한다.
7. 사용자 요청에 필요한 `.harness/policies/`, `.harness/gates/`, planning 파일, template만 추가로 읽는다.

## Codex subagent 사용 규칙

- Codex는 명시적으로 요청받을 때만 subagent를 spawn한다. 병렬 탐색, 리뷰 분할, multi-step plan 실행처럼 실제로 병렬성이 있을 때만 요청한다.
- 기본 설정은 `.codex/config.toml`의 `agents.max_threads = 6`, `agents.max_depth = 1`을 따른다. recursive delegation은 의도적으로 설계하기 전까지 쓰지 않는다.
- read-only 조사/리뷰는 `harness_pm`, `harness_tech_lead`, `harness_spec_reviewer`, `harness_quality_reviewer`, `harness_architecture_reviewer`, `harness_branch_manager`처럼 read-only agent를 우선 쓴다.
- 파일 수정은 `harness_implementer`나 `harness_self_evolution`처럼 수정 목적이 명확한 agent에만 맡긴다.
- subagent 결과는 초안으로 취급하고, parent Codex가 `git status`, targeted diff, required checks로 독립 검증한다.

## Codex skills

- `$harness-bootstrap`: 하네스 시작, role 선택, 체크/보고 형식 확인.
- `$harness-planning`: roadmap, milestone, task graph 작업.
- `$harness-review-gates`: review, merge readiness, evidence validation.
- `$harness-self-evolution`: 반복 실패를 policy, gate, template, script, Codex agent/skill 개선으로 전환.

## 역할 라우팅

실행 가능한 역할 정의는 루트 `.codex/agents/*.toml`이 단일 source of truth다. `.harness/roles.yaml`은 하네스 role을 해당 Codex custom agent와 policy/gate/planning 파일에 연결한다.

`.harness/agents/`나 별도 role instruction 문서는 만들지 않는다. 하네스 내부에는 registry와 정책만 두고, agent 본문은 Codex가 직접 실행하는 `.codex/agents/*.toml`에 둔다.

- 계획, task 선택, acceptance criteria: `.codex/agents/harness-pm.toml`
- 기술 접근, 순서, cross-file scope: `.codex/agents/harness-tech-lead.toml`
- 구현 작업: `.codex/agents/harness-implementer.toml`
- 요구사항 검토: `.codex/agents/harness-spec-reviewer.toml`
- 검증과 evidence review: `.codex/agents/harness-quality-reviewer.toml`
- 아키텍처와 의존성 검토: `.codex/agents/harness-architecture-reviewer.toml`
- branch와 PR 위생: `.codex/agents/harness-branch-manager.toml`
- 하네스 개선 작업: `.codex/agents/harness-self-evolution.toml`

## 결과 보고 규칙

최종 보고에는 다음을 포함한다.

- changed files
- checks run
- skipped checks와 이유
- assumptions
- follow-up

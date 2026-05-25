# Project Agent Entry Point

이 파일은 Codex, Claude Code, 그리고 다른 coding agent가 시작할 때 먼저 읽는 **프로젝트 소스코드 작업 지침**이다.
하네스 운영 기준의 source of truth는 `.harness/`에 있지만, 이 파일은 대상 프로젝트의 코드 구조와 작업 방식을 먼저 잡아주는 얇은 entry point여야 한다.

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

1. `.harness/config.yaml`을 읽고 required checks와 source paths를 확인한다.
2. `.harness/bootstrap.md`를 읽는다.
3. `.harness/agents/`에서 가장 좁은 역할을 선택한다.
4. 사용자 요청에 필요한 `.harness/policies/`, `.harness/gates/`, planning 파일, template만 추가로 읽는다.

## 역할 라우팅

- 계획, task 선택, acceptance criteria: `.harness/agents/pm.md`
- 기술 접근, 순서, cross-file scope: `.harness/agents/tech-lead.md`
- 구현 작업: `.harness/agents/implementer.md`
- 요구사항 검토: `.harness/agents/spec-reviewer.md`
- 검증과 evidence review: `.harness/agents/quality-reviewer.md`
- 아키텍처와 의존성 검토: `.harness/agents/architecture-reviewer.md`
- branch와 PR 위생: `.harness/agents/branch-manager.md`
- 하네스 개선 작업: `.harness/agents/self-evolution.md`

## 결과 보고 규칙

최종 보고에는 다음을 포함한다.

- changed files
- checks run
- skipped checks와 이유
- assumptions
- follow-up

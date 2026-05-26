# Harness Bootstrap Contract

## 목적

이 파일은 하네스 모드에서 따르는 **최소 운영 계약**이다.

- Codex subagent/custom agent 설정은 `.codex/config.toml`과 `.codex/agents/*.toml`이 담당한다.
- Codex repo skill은 `.agents/skills/*/SKILL.md`가 담당한다.
- 기계 판독 manifest와 required checks는 `.harness/config.yaml`이 담당한다.
- role별 Codex agent binding과 추가 로딩 파일은 `.harness/roles.yaml`이 담당한다.
- 이 파일 `.harness/bootstrap.md`는 role 선택, 필요한 하네스 문서 로딩, 편집 전 확인, 보고 형식만 정의한다.

## 하네스 로딩 순서

1. `.codex/config.toml`에서 `agents.max_threads`, `agents.max_depth`, job timeout을 확인한다.
2. `.codex/agents/*.toml`에서 작업에 맞는 Codex custom agent 후보를 확인한다.
3. `.agents/skills/*/SKILL.md`에서 작업에 맞는 Codex repo skill 후보를 확인한다.
4. `.harness/config.yaml`에서 required files, checks, source-of-truth path를 확인한다.
5. 요청에 맞는 가장 좁은 role을 고르고 `.harness/roles.yaml`에서 해당 `.codex/agents/*.toml` binding과 추가 로딩 파일을 확인한다.
6. 작업에 필요한 `.harness/policies/*.md`만 읽는다.
7. 검토나 merge 판단이 필요하면 관련 `.harness/gates/*.md`만 읽는다.
8. planning 관련 작업이면 `.harness/planning/*.yaml`을 읽는다.
9. manual evidence나 report가 필요하면 `.harness/templates/*.md`를 읽는다.

## Codex subagent 계약

- Codex subagent는 parent가 명시적으로 요청할 때만 사용한다.
- 기본 fan-out 한도는 `.codex/config.toml`의 `agents.max_threads = 6`, `agents.max_depth = 1`이다.
- read-only 조사와 리뷰에는 read-only custom agent를 우선 사용한다.
- 수정 작업은 scoped implementer/self-evolution agent로 제한한다.
- parent Codex는 subagent 결과를 신뢰하기 전에 diff와 required checks로 독립 검증한다.

## 역할 선택

역할의 실행 가능한 정의는 `.codex/agents/*.toml`이 단일 source of truth다. `.harness/roles.yaml`은 하네스 role 이름을 Codex custom agent와 필요한 policy/gate/planning 파일에 연결하는 registry다.

- `pm` → `.codex/agents/harness-pm.toml`
- `tech_lead` → `.codex/agents/harness-tech-lead.toml`
- `implementer` → `.codex/agents/harness-implementer.toml`
- `spec_reviewer` → `.codex/agents/harness-spec-reviewer.toml`
- `quality_reviewer` → `.codex/agents/harness-quality-reviewer.toml`
- `architecture_reviewer` → `.codex/agents/harness-architecture-reviewer.toml`
- `branch_manager` → `.codex/agents/harness-branch-manager.toml`
- `self_evolution` → `.codex/agents/harness-self-evolution.toml`

## 편집 전 체크리스트

- [ ] 현재 branch와 `git status`를 확인했다.
- [ ] 사용자 요청의 scope를 확인했다.
- [ ] 관련 task, milestone, decision을 확인했다.
- [ ] 변경 가능한 파일과 금지된 파일을 구분했다.
- [ ] 관련 policy/gate를 읽었다.
- [ ] 필요한 검증 명령을 정했다.

## 실패 동작

즉시 중단한다.

- `.harness/config.yaml`을 파싱할 수 없다.
- config required file이 없다.
- source-of-truth path가 `.harness/` 밖으로 새어 나간다.

계속 진행 가능하다.

- optional policy, gate 파일이 현재 작업과 무관하게 없다.
- legacy 문서가 남아 있지만 source-of-truth가 아니다.

## 보고 형식

작업 보고에는 아래를 포함한다.

- Changed files.
- Checks run과 결과.
- Skipped checks와 이유.
- Assumptions.
- Follow-up work.
- Manual-test artifact path, 필요한 경우.

## 기본 검증

```bash
python scripts/harness/check_harness_contract.py
python scripts/harness/check_documentation_policy.py
python scripts/check_docs_harness.py
```

planning YAML 변경 시:

```bash
python scripts/harness/check_planning_graph.py
```

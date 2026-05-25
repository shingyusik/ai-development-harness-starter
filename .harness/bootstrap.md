# Harness Bootstrap Contract

## 목적

이 파일은 `AGENTS.md`를 통해 하네스 모드로 들어온 agent가 따르는 **최소 운영 계약**이다.

- 프로젝트별 소스코드 지침은 루트 `AGENTS.md`가 담당한다.
- 기계 판독 manifest와 required checks는 `.harness/config.yaml`이 담당한다.
- 이 파일 `.harness/bootstrap.md`는 role 선택, 필요한 하네스 문서 로딩, 편집 전 확인, 보고 형식만 정의한다.

## 하네스 로딩 순서

1. `.harness/config.yaml`에서 required files, checks, source-of-truth path를 확인한다.
2. 요청에 맞는 가장 좁은 role을 고르고 `.harness/agents/<role>.md`를 읽는다.
3. 작업에 필요한 `.harness/policies/*.md`만 읽는다.
4. 검토나 merge 판단이 필요하면 관련 `.harness/gates/*.md`만 읽는다.
5. planning 관련 작업이면 `.harness/planning/*.yaml`을 읽는다.
6. manual evidence나 report가 필요하면 `.harness/templates/*.md`를 읽는다.

## 역할 선택

- `pm`: roadmap, milestone, task, acceptance criteria.
- `tech-lead`: 기술 접근, sequencing, decomposition, cross-area decision.
- `implementer`: 승인된 범위의 코드/문서 변경.
- `spec-reviewer`: 요구사항과 task 정의 검토.
- `quality-reviewer`: 테스트, evidence, regression, acceptance coverage 확인.
- `architecture-reviewer`: architecture boundary와 dependency 검토.
- `branch-manager`: branch, worktree, PR hygiene.
- `self-evolution`: 반복 실패를 하네스 개선으로 전환.

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

- optional role, policy, gate 파일이 현재 작업과 무관하게 없다.
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

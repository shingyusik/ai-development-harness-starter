# AI Development Harness Starter

이 저장소는 프로젝트에 복사해서 쓸 수 있는 **repo-first AI 개발 하네스 스타터**다.

핵심 시작 파일은 루트 `AGENTS.md`와 `.harness/bootstrap.md`다. `AGENTS.md`는 coding agent가 처음 주입받는 프로젝트 소스코드 작업 지침이고, `.harness/bootstrap.md`는 하네스 운영 시작 계약이다.

## 목적

- AI coding agent가 프로젝트 규칙을 매번 다시 추측하지 않게 한다.
- 로드맵, 태스크, 정책, 리뷰 gate, 검증 명령을 저장소 안에 둔다.
- 하네스 기준은 `.harness/`에 모은다.
- 루트 `AGENTS.md`는 대상 프로젝트의 source paths, test/build commands, architecture constraints를 먼저 안내하고 필요한 하네스 문서로 라우팅한다.

## 빠른 시작

1. 이 저장소를 새 프로젝트에 복사하거나 template으로 사용한다.
2. `AGENTS.md`의 project purpose, source paths, test/build commands, architecture constraints를 프로젝트에 맞게 바꾼다.
3. `.harness/config.yaml`의 프로젝트 이름, required checks, source paths를 프로젝트에 맞게 바꾼다.
4. `.harness/planning/*.yaml`에 실제 roadmap, milestone, task를 입력한다.
5. `.harness/policies/`와 `.harness/gates/`에서 프로젝트에 맞지 않는 항목을 줄이거나 고친다.
6. 아래 검증을 실행한다.

```bash
python scripts/harness/check_harness_contract.py
python scripts/harness/check_planning_graph.py
python scripts/harness/check_documentation_policy.py
python scripts/check_docs_harness.py
```

## 주요 폴더

- `.harness/`: 하네스 source of truth.
- `.harness/agents/`: 역할별 agent 계약.
- `.harness/policies/`: 지속적으로 지킬 정책.
- `.harness/gates/`: 리뷰/머지 전 확인 기준.
- `.harness/planning/`: roadmap, milestone, task graph.
- `.harness/templates/`: 반복 문서 템플릿.
- `scripts/harness/`: 하네스 검증 스크립트.
- `.github/`: PR/CI starter 파일.

## 사용 원칙

- 프로젝트 고유 규칙이 생기면 `.harness/`에 기록한다.
- 사람이 반복해서 지적한 문제는 policy, gate, script, test 중 하나로 바꾼다.
- 긴 설명보다 짧은 checklist와 실행 가능한 검증을 우선한다.
- 최종 문서는 영어로 운용해도 된다. 지금 한국어 문서는 설계 피드백용 초안이다.

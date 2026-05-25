# Starter Adaptation Roadmap

Status: proposed
Source: `.harness/decisions/0001-harness-operating-model.md`

## 목표

이 starter를 새 프로젝트에 붙일 때 필요한 순서를 정의한다.

## Non-goals

- 프로젝트 고유 아키텍처를 starter가 대신 정하지 않는다.
- 외부 knowledge hub 통합을 초기 필수로 두지 않는다.
- 긴 agent manual을 루트 파일에 넣지 않는다.

## 단계

### R1. Spine and bootstrap

- `.harness/README.md`, `config.yaml`, `bootstrap.md`를 프로젝트에 맞춘다.
- required files와 checks가 현재 저장소에서 통과하게 한다.

### R2. Planning graph

- `.harness/planning/roadmap.yaml`에 실제 목표를 넣는다.
- `.harness/planning/milestones.yaml`에 실행 단계를 넣는다.
- `.harness/planning/tasks.yaml`에 dependency와 acceptance criteria를 넣는다.

### R3. Policies and gates

- 불필요한 starter policy는 줄인다.
- 필요한 프로젝트 규칙은 policy로 추가한다.
- policy는 gate와 checker로 연결한다.

### R4. Agent roles

- 프로젝트가 실제로 쓰는 역할만 남긴다.
- 각 역할의 input/output/evidence를 프로젝트에 맞춘다.

### R5. CI and PR flow

- `.harness/config.yaml`의 required checks를 CI와 맞춘다.
- PR template이 gate evidence를 요구하게 한다.

### R6. Self-evolution

- 반복 실패를 기록하고 하네스 개선으로 반영한다.
- 오래된 starter 문구는 프로젝트 상태에 맞게 제거한다.

## 완료 기준

- 모든 required check가 통과한다.
- planning graph가 실제 작업 순서를 표현한다.
- agent가 `.harness/`만 읽고도 작업을 시작할 수 있다.
- PR review가 policy/gate/check evidence를 기준으로 진행된다.

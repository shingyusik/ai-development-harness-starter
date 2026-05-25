# Harness Operating Model Decision

Status: accepted
Scope: 하네스 스타터의 위치, 운영 원칙, 역할, 계획 모델, 품질 기준.

## 결정

이 starter는 **repo-first AI development harness**를 제공한다.

각 프로젝트는 자신의 규칙을 저장소 안에 선언한다. 에이전트는 그 규칙을 읽고, 작업하고, 검증하고, 반복 실패를 하네스 개선으로 환원한다.

## 위치

- 하네스 source-of-truth는 `.harness/`다.
- 루트 `AGENTS.md`는 짧은 라우팅 지도다.
- 제품 문서는 제품의 현재 상태를 설명한다.
- 하네스 내부 규칙을 루트 문서나 제품 문서에 섞지 않는다.

## 운영 루프

```text
roadmap alignment -> task selection -> decomposition -> implementation -> tests -> review -> PR -> self-evolution
```

## 계획 모델

계획은 YAML로 관리한다.

- Roadmap: 큰 목표.
- Milestone: 목표를 실행 가능한 단계로 나눈 것.
- Task: acceptance criteria와 dependency가 있는 작업 단위.

Task는 최소한 아래를 가진다.

```yaml
id: H001
title: Define harness spine
status: ready
priority: P0
milestone_id: M1
depends_on: []
owner_role: tech-lead
acceptance:
  - required files exist
```

## 우선순위

- `P0`: 현재 진행을 막는 blocker.
- `P1`: 현재 milestone에 필요.
- `P2`: 중요하지만 병렬 또는 후순위 가능.
- `P3`: 개선/정리.
- `P4`: backlog.

## 상태

- `blocked`: dependency가 완료되지 않음.
- `ready`: 시작 가능.
- `in_progress`: 작업 중.
- `review`: 검토 중.
- `done`: 검증 완료.
- `deferred`: 의도적으로 연기.
- `cancelled`: 취소.

## 품질 모델

- Clean Code 원칙을 gate로 번역한다.
- TDD 또는 테스트 우선 사고를 기본으로 둔다.
- architecture boundary와 dependency drift를 검토한다.
- 문서는 현재 상태 중심으로 유지한다.
- CI/checker로 가능한 것은 자동화한다.
- 자동화 공백은 manual-test artifact로 남긴다.

## Self-evolution

같은 유형의 실패가 반복되면 아래 중 하나를 개선한다.

- policy
- gate
- script
- test
- template
- role contract
- skill

목표는 문서를 늘리는 것이 아니라 다음 루프에서 같은 실패가 덜 나게 만드는 것이다.

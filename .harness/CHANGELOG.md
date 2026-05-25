# Harness Changelog

## 2026-05-25

### Changed

- 하네스 스타터 문서를 한국어 리뷰용 초안으로 다시 작성했다.
- 최종 운용 문구는 피드백 후 영어로 정리한다.

### Removed

- `.harness/migrations/docs-harness-classification.md`: starter core가 아닌 legacy migration 보조 문서를 제거했다.

## 2026-05-24

### Added

- `.harness/policies/external-sync.md`: 외부 동기화 규칙.
- `.harness/templates/self-evolution-report.md`: 반복 실패 개선 보고서 템플릿.
- `.harness/migrations/docs-harness-classification.md`: legacy harness docs 분류 기준.
- `.harness/templates/manual-test.md`: manual-test evidence 템플릿.
- `.harness/agents/*.md`: 역할별 agent 계약.
- `.harness/gates/*.md`: review/merge gate 문서.
- `.harness/policies/*.md`: core policy 문서.
- `scripts/harness/check_documentation_policy.py`: documentation policy checker.
- `scripts/harness/check_planning_graph.py`: planning graph checker.

### Removed

- legacy `docs/harness`를 하네스 guidance 위치에서 제외했다.

## 2026-05-23

### Added

- `.harness/README.md`: 하네스 진입점.
- `.harness/bootstrap.md`: startup contract.
- `.harness/config.yaml`: harness manifest.
- `.harness/decisions/0001-harness-operating-model.md`: 운영 모델 결정.
- `.harness/decisions/0002-starter-adaptation-roadmap.md`: starter adaptation roadmap.
- `.harness/planning/milestones.yaml`: M1 milestone plan.
- `.harness/planning/*.yaml`: planning graph files.
- `scripts/harness/check_harness_contract.py`: harness contract checker.

# Worktree Policy

## 목적

병렬 작업은 worktree와 branch scope를 명확히 한다.

## 규칙

- base branch/commit을 기록한다.
- worktree별 dirty state를 확인한다.
- 통합 전 diff와 checks를 확인한다.

## 리뷰 체크

- [ ] 변경이 이 정책의 목적과 충돌하지 않는다.
- [ ] 예외가 있으면 이유와 follow-up이 있다.
- [ ] 자동화 가능한 항목은 gate, script, test, CI 중 하나로 연결되어 있다.

## Evidence

- 관련 변경 파일.
- 실행한 check.
- 생략한 check와 이유.
- 남은 위험.

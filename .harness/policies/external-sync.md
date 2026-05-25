# External Sync Policy

## 목적

외부 지식 저장소와 dashboard는 로컬 repo state 이후에 동기화한다.

## 규칙

- 로컬 `.harness/`가 authoritative하다.
- 외부 sync는 source를 보존한다.
- incremental process note를 남발하지 않는다.

## 리뷰 체크

- [ ] 변경이 이 정책의 목적과 충돌하지 않는다.
- [ ] 예외가 있으면 이유와 follow-up이 있다.
- [ ] 자동화 가능한 항목은 gate, script, test, CI 중 하나로 연결되어 있다.

## Evidence

- 관련 변경 파일.
- 실행한 check.
- 생략한 check와 이유.
- 남은 위험.

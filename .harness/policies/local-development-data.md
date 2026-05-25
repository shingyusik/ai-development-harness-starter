# Local Development Data Policy

## 목적

로컬 테스트 데이터는 deterministic하고 cleanup 가능해야 한다.

## 규칙

- seed/fixed id/source path를 둔다.
- production data나 credential을 쓰지 않는다.
- reset 또는 cleanup command를 제공한다.

## 리뷰 체크

- [ ] 변경이 이 정책의 목적과 충돌하지 않는다.
- [ ] 예외가 있으면 이유와 follow-up이 있다.
- [ ] 자동화 가능한 항목은 gate, script, test, CI 중 하나로 연결되어 있다.

## Evidence

- 관련 변경 파일.
- 실행한 check.
- 생략한 check와 이유.
- 남은 위험.

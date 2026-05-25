# Duplication Control Policy

## 목적

중복을 관리하되 성급한 추상화를 피한다.

## 규칙

- 같은 logical value/message는 하나의 source를 가진다.
- 반복 코드가 실제로 함께 변하는지 확인한다.
- 중복 제거가 복잡도를 키우면 보류한다.

## 리뷰 체크

- [ ] 변경이 이 정책의 목적과 충돌하지 않는다.
- [ ] 예외가 있으면 이유와 follow-up이 있다.
- [ ] 자동화 가능한 항목은 gate, script, test, CI 중 하나로 연결되어 있다.

## Evidence

- 관련 변경 파일.
- 실행한 check.
- 생략한 check와 이유.
- 남은 위험.

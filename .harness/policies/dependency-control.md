# Dependency Control Policy

## 목적

의존성 추가와 방향을 통제한다.

## 규칙

- 새 package/library는 필요성과 대안을 기록한다.
- 순환 의존성을 만들지 않는다.
- runtime dependency와 dev dependency를 구분한다.

## 리뷰 체크

- [ ] 변경이 이 정책의 목적과 충돌하지 않는다.
- [ ] 예외가 있으면 이유와 follow-up이 있다.
- [ ] 자동화 가능한 항목은 gate, script, test, CI 중 하나로 연결되어 있다.

## Evidence

- 관련 변경 파일.
- 실행한 check.
- 생략한 check와 이유.
- 남은 위험.

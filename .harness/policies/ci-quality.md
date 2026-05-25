# CI Quality Policy

## 목적

품질 기준을 가능한 한 CI와 자동화 check로 강제한다.

## 규칙

- 테스트, lint, typecheck, build를 required check로 연결한다.
- CI skip은 이유와 follow-up을 남긴다.
- 반복 실패는 새 check 후보로 본다.

## 리뷰 체크

- [ ] 변경이 이 정책의 목적과 충돌하지 않는다.
- [ ] 예외가 있으면 이유와 follow-up이 있다.
- [ ] 자동화 가능한 항목은 gate, script, test, CI 중 하나로 연결되어 있다.

## Evidence

- 관련 변경 파일.
- 실행한 check.
- 생략한 check와 이유.
- 남은 위험.

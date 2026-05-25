# Manual Testing Policy

## 목적

자동화 공백은 독립된 manual-test evidence로 남긴다.

## 규칙

- 정확한 steps, observations, pass criteria를 기록한다.
- 테스트한 사람/도구와 환경을 적는다.
- cleanup evidence를 남긴다.

## 리뷰 체크

- [ ] 변경이 이 정책의 목적과 충돌하지 않는다.
- [ ] 예외가 있으면 이유와 follow-up이 있다.
- [ ] 자동화 가능한 항목은 gate, script, test, CI 중 하나로 연결되어 있다.

## Evidence

- 관련 변경 파일.
- 실행한 check.
- 생략한 check와 이유.
- 남은 위험.

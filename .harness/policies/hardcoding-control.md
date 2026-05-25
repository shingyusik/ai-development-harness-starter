# Hardcoding Control Policy

## 목적

비즈니스 값, 메시지, threshold, route, prompt를 코드에 무분별하게 박지 않는다.

## 규칙

- 공유 값은 config/data source에 둔다.
- 같은 logical value를 여러 파일에 중복하지 않는다.
- local-only test 값은 scope와 cleanup을 명시한다.

## 리뷰 체크

- [ ] 변경이 이 정책의 목적과 충돌하지 않는다.
- [ ] 예외가 있으면 이유와 follow-up이 있다.
- [ ] 자동화 가능한 항목은 gate, script, test, CI 중 하나로 연결되어 있다.

## Evidence

- 관련 변경 파일.
- 실행한 check.
- 생략한 check와 이유.
- 남은 위험.

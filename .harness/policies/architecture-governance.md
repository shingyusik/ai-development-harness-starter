# Architecture Governance Policy

## 목적

프로젝트의 architecture boundary와 dependency direction을 지킨다.

## 규칙

- domain은 framework 세부사항에 의존하지 않는다.
- 상위 layer가 하위 layer 구현 세부사항을 직접 알지 않는다.
- 새 dependency는 이유와 boundary를 설명한다.

## 리뷰 체크

- [ ] 변경이 이 정책의 목적과 충돌하지 않는다.
- [ ] 예외가 있으면 이유와 follow-up이 있다.
- [ ] 자동화 가능한 항목은 gate, script, test, CI 중 하나로 연결되어 있다.

## Evidence

- 관련 변경 파일.
- 실행한 check.
- 생략한 check와 이유.
- 남은 위험.

# Abstraction and YAGNI Policy

## 목적

필요하지 않은 추상화를 만들지 않고, 실제 중복과 변화 압력이 확인된 뒤 추상화한다.

## 규칙

- 새 abstraction은 호출자와 변경 이유가 명확해야 한다.
- 미래 가능성만으로 layer, interface, factory를 만들지 않는다.
- 중복 제거가 가독성을 해치면 중복을 일시적으로 허용하고 이유를 남긴다.

## 리뷰 체크

- [ ] 변경이 이 정책의 목적과 충돌하지 않는다.
- [ ] 예외가 있으면 이유와 follow-up이 있다.
- [ ] 자동화 가능한 항목은 gate, script, test, CI 중 하나로 연결되어 있다.

## Evidence

- 관련 변경 파일.
- 실행한 check.
- 생략한 check와 이유.
- 남은 위험.

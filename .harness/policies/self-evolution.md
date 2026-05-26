# Self-Evolution Policy

## 목적

반복 실패를 하네스 개선으로 바꾼다.

## 규칙

- 같은 지적이 반복되면 policy/gate/script/test/template 중 하나를 고친다.
- 새 문서보다 기존 source-of-truth 개선을 우선한다.
- `.agents/skills/*/SKILL.md`를 만들거나 수정할 때는 `.harness/policies/skill-authoring.md`를 읽고 Anthropic `skill-creator` workflow를 따른다.
- 변경은 changelog에 남긴다.

## 리뷰 체크

- [ ] 변경이 이 정책의 목적과 충돌하지 않는다.
- [ ] 예외가 있으면 이유와 follow-up이 있다.
- [ ] 자동화 가능한 항목은 gate, script, test, CI 중 하나로 연결되어 있다.

## Evidence

- 관련 변경 파일.
- 실행한 check.
- 생략한 check와 이유.
- 남은 위험.

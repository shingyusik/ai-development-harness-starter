# Clean Code Review Gate

## 목적

변경 코드가 clean code 기준을 만족하는지 확인한다.

## 입력

- 사용자 요청 또는 PR 설명.
- 관련 roadmap/milestone/task.
- 변경 파일 목록.
- 관련 policy.
- 실행한 checks와 결과.

## Required Checks

- [ ] Acceptance criteria가 명확하고 충족됐다.
- [ ] 변경 범위가 승인된 scope 안에 있다.
- [ ] 관련 policy와 충돌하지 않는다.
- [ ] 필요한 자동화 check가 통과했다.
- [ ] 생략한 check는 이유와 follow-up이 있다.
- [ ] manual evidence가 필요한 경우 artifact가 있다.

## Evidence

- Changed files.
- Command outputs 또는 CI links.
- Manual-test path, 필요한 경우.
- Cleanup evidence, 필요한 경우.
- 남은 risk와 follow-up.

## Fails When

- acceptance criteria가 검증 불가능하다.
- required check가 실패했다.
- scope 밖 변경이 섞였다.
- evidence 없이 중요한 검증을 생략했다.

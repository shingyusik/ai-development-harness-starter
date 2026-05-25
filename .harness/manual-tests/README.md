# Manual Tests

## 목적

자동화하기 어렵거나 아직 자동화되지 않은 검증을 standalone artifact로 남긴다.

## 언제 작성하나

- UI나 외부 서비스 때문에 자동화가 어렵다.
- Playwright나 사람이 직접 확인해야 한다.
- cleanup evidence가 필요하다.
- CI가 커버하지 못하는 acceptance criteria가 있다.

## 파일 이름

```text
.harness/manual-tests/YYYY-MM-DD-short-name.md
```

## 필수 내용

- 테스트한 사람 또는 도구.
- 대상 환경.
- 정확한 단계.
- 관찰 결과.
- pass/fail 기준.
- evidence.
- cleanup 여부.
- 남은 위험과 follow-up.

## 템플릿

사용:

```text
.harness/templates/manual-test.md
```

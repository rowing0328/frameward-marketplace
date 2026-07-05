# 새 프로젝트 UI 기반 보강 설계

작성일: 2026-07-05

## 목적

Frameward는 현재 기존 화면 개선 흐름을 중심으로 설계되어 있다. 새 화면 생성과 Astryx bootstrap 흐름은 일부 존재하지만, 완전 새로운 프로젝트에서 “기존 UI 규칙이 없을 때 무엇을 먼저 정해야 하는가”는 아직 명확하지 않다.

이번 보강의 목적은 Frameward가 새 프로젝트 상황을 정식으로 다룰 수 있도록 문서, 워크플로우, 템플릿, 모델을 추가하는 것이다. 구현 자동화나 hook 동작 변경은 이번 범위에 포함하지 않는다.

## 범위

추가할 파일:

- `docs/new-project-flow.ko.md`
- `workflows/bootstrap-new-project-ui.md`
- `templates/ui-foundation-brief.md`
- `models/ui-foundation-model.md`

수정할 파일:

- `README.md`
- `docs/architecture.ko.md`
- `CHANGELOG.md`
- `FILE_MANIFEST.md`

수정하지 않을 파일:

- hook Python 파일
- hook 설정
- plugin manifest
- schemas

이번 보강은 Frameward v0.1의 개념 확장이다. 새 프로젝트 요청을 더 강하게 감지하거나 차단하는 hook 동작은 이후 별도 작업에서 다룬다.

## 핵심 방향

새 프로젝트에서는 기존 프로젝트와 다르게 “기존 UI 규칙 감지”가 실패하거나 의미가 약할 수 있다. 따라서 Frameward는 먼저 최소 UI 규칙을 만들어야 한다.

기본 흐름:

```text
새 프로젝트 요청
  -> 서비스 종류와 사용자 파악
  -> 첫 대표 화면 선택
  -> 필요한 화면 목록 초안 작성
  -> 최소 UI 규칙 작성
  -> provider 후보 평가
  -> Astryx 적합성 검토
  -> 승인 전 설치 금지
  -> 대표 화면 구현 기준 정리
  -> 쉬운 말로 설명
```

Provider 선택은 UI 기반을 정리한 뒤 수행한다. 새 프로젝트라고 해서 Astryx, Tailwind, shadcn, MUI 같은 도구를 먼저 설치하지 않는다.

## Astryx 처리

Astryx는 새 프로젝트에서 후보로 평가할 수 있다. 하지만 Frameward는 Astryx 래퍼가 아니며 Astryx 설치, MCP 활성화, 프로젝트 마이그레이션을 자동으로 수행하지 않는다.

새 프로젝트 흐름에서 Astryx는 다음 규칙을 따른다.

- 기본값은 provider-neutral 흐름이다.
- Astryx는 적합성 평가 대상으로 포함한다.
- 사용자가 승인하기 전에는 설치하지 않는다.
- 사용자가 승인하기 전에는 MCP를 활성화하지 않는다.
- Astryx가 적합하더라도 먼저 이유와 영향 범위를 쉬운 말로 설명한다.

## 파일별 설계

### `docs/new-project-flow.ko.md`

새 프로젝트 지원을 설명하는 한국어 문서다.

포함할 내용:

- 새 프로젝트 지원의 목적
- 기존 프로젝트와 새 프로젝트의 차이
- 새 프로젝트 처리 흐름
- 최소 UI 규칙을 먼저 만드는 이유
- provider-neutral 기본 원칙
- Astryx 후보 평가 방식
- 승인 전 설치 금지 원칙
- 예시 요청과 처리 방식

### `workflows/bootstrap-new-project-ui.md`

Codex가 새 프로젝트 UI 기반을 잡을 때 따르는 실행 순서다.

예상 단계:

```text
1. Confirm this is a new project or a project without mature UI rules.
2. Identify product type, user, and first representative screen.
3. Create a minimal UI foundation brief.
4. Check whether a provider is already present.
5. Compare provider-neutral, project-native, and approved provider paths.
6. Evaluate Astryx as a candidate only; do not install or enable MCP.
7. Select the safest path.
8. Define states and mobile behavior before implementation.
9. Implement only after the foundation is clear.
10. Explain decisions in plain language.
```

### `templates/ui-foundation-brief.md`

새 프로젝트의 기본 UI 규칙을 기록하는 양식이다.

포함할 섹션:

- Project type
- Primary users
- First representative screen
- Main user action
- Core screens
- UI foundation
  - colors
  - spacing
  - typography
  - buttons
  - forms
  - cards/surfaces
- States
  - loading
  - empty
  - error
  - disabled
- Mobile behavior
- Provider decision
- Astryx candidate evaluation
- Approval status
- Plain-language summary

### `models/ui-foundation-model.md`

Frameward 내부 모델 문서다.

정의할 내용:

- UI foundation의 의미
- 새 프로젝트에서 필요한 이유
- 필수 필드
- provider 선택과의 관계
- Astryx 평가와의 관계
- 구현 전 완료 기준

## README 연결

`README.md`의 Repository Structure에 이미 `docs/`가 포함되어 있다. Design Documentation 섹션에 `docs/new-project-flow.ko.md` 링크를 추가한다.

## 내부 설계 문서 연결

`docs/architecture.ko.md`에는 “새 프로젝트 UI 기반” 섹션을 추가한다. 이 섹션은 새 프로젝트에서는 기존 UI 규칙을 찾는 대신 최소 UI 규칙을 먼저 만든다는 점을 설명한다.

## 검증

구현 후 다음 명령을 실행한다.

```bash
python3 tools/validate_scaffold.py
```

추가로 새 파일 경로 확인을 위해 다음 명령을 실행한다.

```bash
find docs workflows templates models -maxdepth 2 -type f | sort
```

## 성공 기준

- 새 프로젝트 지원 문서가 한국어로 추가된다.
- 새 프로젝트 bootstrap workflow가 추가된다.
- UI foundation brief 템플릿이 추가된다.
- UI foundation model이 추가된다.
- README와 내부 설계 문서에서 새 흐름을 찾을 수 있다.
- CHANGELOG와 FILE_MANIFEST가 새 파일을 반영한다.
- 기존 scaffold validation이 통과한다.
- Astryx는 후보 평가만 가능하며 승인 전 설치 또는 MCP 활성화는 금지된다.

## 제외 사항

- hook 감지 로직 변경
- schema 추가 또는 변경
- plugin manifest 변경
- Astryx 설치 자동화
- 새 UI 라이브러리 의존성 추가
- 영어판 설계 문서 작성

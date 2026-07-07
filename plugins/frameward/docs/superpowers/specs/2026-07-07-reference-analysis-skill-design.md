# 레퍼런스 분석 스킬 보강 설계

작성일: 2026-07-07

## 목적

Frameward는 기존 프로젝트 화면을 안전하게 개선하는 흐름에 강하다. 하지만 사용자가 스크린샷, 사이트, Figma 메모, 다른 제품 화면을 참고하라고 할 때 “무엇을 가져오고 무엇은 가져오면 안 되는지”를 출처가 보이게 정리하는 전용 스킬은 아직 없다.

이번 보강의 목적은 Design Analyzer의 강점 중 일부를 Frameward에 맞게 얇게 흡수하는 것이다. 전체 Design Analyzer 워크플로우를 가져오지 않고, 레퍼런스를 참고할 때 필요한 작은 분석 단계를 추가한다.

## 승인된 방향

선택한 방향은 `reference-analysis` 스킬 추가다.

검토한 대안:

- `reference-analysis` 스킬 추가: Frameward 기존 흐름을 유지하면서 레퍼런스 분석만 보강한다. 이번 작업의 선택안이다.
- `handoff-report` 강화: 결과 보고 품질은 좋아지지만 레퍼런스 분석 자체는 약하게 남는다.
- Design Analyzer식 전체 워크플로우 추가: 강력하지만 Frameward가 너무 무거워지고, 보수적인 화면 개선 프레임워크라는 성격이 흐려진다.

## 범위

추가할 파일:

- `skills/reference-analysis/SKILL.md`
- `templates/reference-analysis-template.md`
- `models/reference-analysis-model.md`

수정할 파일:

- `README.md`
- `docs/architecture.ko.md`
- `FILE_MANIFEST.md`
- `CHANGELOG.md`

수정하지 않을 파일:

- hook Python 파일
- hook 설정
- plugin manifest
- 외부 provider 파일
- schema 파일

이번 작업은 새 스킬과 문서 보강이다. Codex hook 동작을 바꾸거나 새로운 provider를 활성화하지 않는다.

## 스킬 역할

`reference-analysis`는 레퍼런스 화면이나 스크린샷을 참고할 때 사용하는 사전 분석 스킬이다.

스킬이 해야 할 일:

- 레퍼런스 출처와 신뢰도를 기록한다.
- 화면에서 눈에 보이는 사실과 해석을 분리한다.
- 참고할 수 있는 부분과 피해야 할 부분을 나눈다.
- 적용 대상 영역을 정한다.
- 기존 프로젝트 UI 규칙을 우선한다는 전제를 유지한다.
- 최종 사용자 설명은 쉬운 말로 정리한다.

스킬이 하지 않는 일:

- 코드 구현
- 이미지 생성
- 새 UI 라이브러리 설치
- 외부 provider 활성화
- 레퍼런스 화면을 그대로 복제
- 브랜드, 인증, 공공기관, 보안 같은 신뢰 표현을 출처 없이 가져오기

## Frameward 흐름 안의 위치

권장 순서:

```text
client-intent-discovery
  -> reference-analysis
  -> layout-region-mapping
  -> design-system-provider-detection
  -> design-system-audit
  -> screen-improvement-plan
  -> provider-safe-implementation
  -> responsive-check / accessibility-check / state-coverage-check
  -> plain-language-brief / handoff-report
```

`reference-analysis`는 레퍼런스가 있을 때만 사용한다. 사용자가 단순히 현재 화면을 고쳐달라고 하고 참고 화면을 주지 않았다면 필수 단계가 아니다.

## 분석 항목

Design Analyzer의 12차원 분석을 그대로 가져오지 않는다. Frameward에서는 더 가벼운 6개 항목으로 줄인다.

| 항목 | 확인할 내용 |
|---|---|
| 화면 구조 | 어떤 영역이 먼저 보이고, 영역들이 어떤 순서로 배치되는가 |
| 정보 묶음 | 관련 정보가 어떻게 묶이고 구분되는가 |
| 중요한 행동 | 사용자가 가장 먼저 해야 할 행동이 어떻게 보이는가 |
| 글과 밀도 | 설명량, 제목 크기, 보조 문구의 양이 어느 정도인가 |
| 상태와 반응 | hover, focus, loading, empty, error 같은 상태가 어떻게 보이는가 |
| 가져오면 안 되는 것 | 로고, 브랜드 고유 표현, 인증 주장, 과한 장식, 프로젝트와 맞지 않는 패턴 |

필요하면 내부적으로 색상, 간격, 컴포넌트, 접근성 같은 세부 항목을 볼 수 있다. 다만 사용자에게는 쉬운 말로 설명한다.

## 산출물

스킬의 기본 산출물은 짧은 분석 표다.

```text
Reference summary
- Source:
- Confidence:
- Relevant parts:

What to learn from it
- Screen structure:
- Information grouping:
- Important action:
- Text and density:
- States:

What not to copy
- Brand-specific elements:
- Unsupported claims:
- Layout risks:
- Accessibility risks:

How to apply safely
- Target screen area:
- Existing project rule to preserve:
- Allowed adaptation:
- Check before implementation:
```

이 산출물은 구현 지시가 아니라 다음 스킬들이 참고할 입력이다.

## 모델 문서

`models/reference-analysis-model.md`는 내부 모델을 정의한다.

포함할 내용:

- Reference source
- Visible fact
- Interpretation
- Safe adoption
- Forbidden carryover
- Target application area
- Existing project rule
- Quality check

핵심 원칙은 “눈에 보이는 사실 -> 안전하게 참고할 점 -> 적용할 영역 -> 확인할 점” 순서를 지키는 것이다.

## 템플릿

`templates/reference-analysis-template.md`는 실제 작업 중 복사해서 쓸 수 있는 양식이다.

템플릿은 다음을 포함한다.

- 레퍼런스 기본 정보
- 참고할 점
- 가져오면 안 되는 점
- 프로젝트 기존 규칙
- 적용 계획
- 확인 항목
- 쉬운 말 요약

## README 연결

`README.md`의 Frameward Loop 또는 Using It With Codex 섹션에 레퍼런스가 있는 경우 `reference-analysis`를 사용할 수 있음을 짧게 추가한다.

예시 문장:

```text
When a user provides a reference screen, Frameward can first separate what is safe to learn from the reference from what should not be copied.
```

## 내부 설계 문서 연결

`docs/architecture.ko.md`에는 레퍼런스 분석 계층을 짧게 추가한다.

핵심 설명:

- 레퍼런스는 그대로 복제 대상이 아니다.
- 출처가 보이는 화면 특징만 참고한다.
- 기존 프로젝트 UI 규칙이 우선이다.
- 가져오면 안 되는 브랜드 고유 요소나 출처 없는 신뢰 표현을 따로 기록한다.

## 검증

구현 후 다음 명령을 실행한다.

```bash
python3 plugins/frameward/tools/validate_scaffold.py
```

추가 확인:

```bash
test -f plugins/frameward/skills/reference-analysis/SKILL.md
test -f plugins/frameward/templates/reference-analysis-template.md
test -f plugins/frameward/models/reference-analysis-model.md
```

## 성공 기준

- `reference-analysis` 스킬이 추가된다.
- 새 스킬은 YAML frontmatter에 `name`과 `description`을 가진다.
- 레퍼런스 분석은 구현, 이미지 생성, provider 설치를 하지 않는다.
- 기존 프로젝트 UI 규칙을 우선한다는 원칙이 유지된다.
- README와 내부 설계 문서에서 새 스킬의 역할을 찾을 수 있다.
- `FILE_MANIFEST.md`와 `CHANGELOG.md`가 새 파일을 반영한다.
- scaffold validation이 통과한다.

## 제외 사항

- Design Analyzer 전체 기능 이식
- 12차원 fidelity matrix 강제
- 정적 HTML/CSS/JS handoff 패키지 생성
- 이미지 생성 workflow 추가
- hook 감지 로직 변경
- schema 추가 또는 변경
- 외부 provider 관련 동작 변경

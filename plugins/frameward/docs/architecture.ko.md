# Frameward 내부 설계

이 문서는 Frameward가 내부적으로 어떻게 작동하는지 설명합니다.

Frameward는 UI 컴포넌트 라이브러리가 아닙니다. Astryx 래퍼도 아닙니다. 사용자가 “이 화면을 더 좋게 만들어줘”처럼 모호하게 말했을 때 Codex가 그 요청을 안전하게 해석하고, 기존 프로젝트의 UI 규칙을 따르며, 작은 개선을 적용하고, 결과를 쉬운 말로 설명하도록 돕는 프레임워크입니다.

## 설계 목표

Frameward의 핵심 목표는 세 가지입니다.

1. 사용자가 전문 용어를 몰라도 UI 개선을 요청할 수 있게 한다.
2. Codex가 화면을 고치기 전에 의도, 화면 구조, 기존 UI 규칙을 먼저 확인하게 한다.
3. 새 라이브러리나 외부 제공자를 자동으로 도입하지 않고, 프로젝트에 이미 있는 방식을 우선 사용하게 한다.

Frameward는 “더 예쁘게” 같은 요청을 바로 색상이나 장식 변경으로 처리하지 않습니다. 먼저 무엇이 불편한지, 사용자가 무엇을 먼저 봐야 하는지, 어떤 영역이 어떤 역할을 하는지 확인한 뒤 보수적으로 수정합니다.

## 전체 처리 흐름

Frameward의 기본 흐름은 다음과 같습니다.

```text
사용자 요청
  -> UI 작업인지 감지
  -> Frameward Loop 시작
  -> 8개 게이트 확인
  -> 필요한 스킬 또는 워크플로우 사용
  -> provider 선택
  -> 작은 범위로 구현
  -> 품질 확인
  -> 쉬운 말로 결과 설명
```

예를 들어 사용자가 “모바일에서 이 화면이 불편해요”라고 말하면 Frameward는 내부적으로 다음처럼 해석합니다.

```text
1. 모바일 화면 문제로 판단한다.
2. 사용자가 어디에서 막힐지 추정한다.
3. 화면의 주요 영역을 나눈다.
4. 프로젝트가 이미 쓰는 컴포넌트와 스타일을 확인한다.
5. 모바일에서 중요한 정보와 버튼이 잘 보이는지 확인한다.
6. 필요한 경우 작은 코드 변경을 적용한다.
7. 모바일, 키보드 이동, 빈 상태, 로딩, 오류 상태를 확인한다.
8. 사용자에게 쉬운 말로 무엇을 바꿨는지 설명한다.
```

## 주요 계층

Frameward는 일곱 계층으로 나뉩니다.

### 1. 사용자 언어 계층

사용자의 말을 그대로 전문 용어로 바꾸어 묻지 않습니다.

예를 들어 “CTA가 무엇인가요?”라고 묻는 대신 “이 화면에서 사용자가 가장 먼저 해야 하는 행동은 무엇인가요?”처럼 묻습니다.

관련 파일:

- `core/client-language-policy.md`
- `core/terminology-map.md`
- `skills/client-intent-discovery/SKILL.md`
- `skills/plain-language-brief/SKILL.md`

### 2. 레퍼런스 분석 계층

사용자가 참고 화면, 스크린샷, 사이트, Figma 메모를 제공할 때 Frameward는 이를 그대로 복제 대상으로 보지 않습니다.

먼저 눈에 보이는 사실과 해석을 분리합니다. 그 다음 현재 프로젝트에 안전하게 참고할 부분, 가져오면 안 되는 브랜드 고유 요소, 출처 없는 신뢰 표현, 화면 구조 위험을 나눕니다.

이 계층의 기본 원칙은 기존 프로젝트의 컴포넌트, 색상, 간격, 글자 규칙을 우선하는 것입니다. 레퍼런스는 방향을 잡기 위한 자료이며, 현재 프로젝트의 UI 규칙을 대체하지 않습니다.

관련 파일:

- `skills/reference-analysis/SKILL.md`
- `models/reference-analysis-model.md`
- `templates/reference-analysis-template.md`

### 3. 루프 게이트 계층

Frameward Loop는 Codex가 UI 작업을 너무 빨리 시작하지 않도록 막는 점검 순서입니다.

현재 게이트는 8개입니다.

1. `intent`: 사용자가 원하는 방향을 해석했는가
2. `language`: 최종 설명이 쉬운 말로 작성되는가
3. `layout`: 화면의 주요 영역과 역할을 파악했는가
4. `system`: 프로젝트의 기존 UI 규칙을 확인했는가
5. `ratio`: 간격, 크기, 균형을 확인했는가
6. `implementation`: 작은 범위로 안전하게 구현했는가
7. `quality`: 모바일, 키보드, 상태 화면 등을 확인했는가
8. `explanation`: 무엇을 바꿨고 왜 도움이 되는지 설명했는가

관련 파일:

- `core/loop-gates.md`
- `.frameward/gates.example.json`
- `schemas/frameward-loop-state.schema.json`

### 4. 훅 계층

훅은 Codex 작업 흐름 중간에 Frameward 정책을 적용합니다.

`SessionStart`는 Frameward 정책을 세션에 알려줍니다.

`UserPromptSubmit`은 사용자의 요청이 UI 관련인지 감지합니다. UI 작업이 아니면 Frameward Loop를 시작하지 않습니다.

`PreToolUse`는 코드 수정 전에 필요한 게이트가 부족한지 확인합니다. 또한 의존성 설치, Astryx 설정, MCP 활성화처럼 명시적 승인이 필요한 작업을 차단합니다.

`PostToolUse`는 UI 파일이 수정된 뒤 구현 게이트를 기록하고, 모바일/키보드/상태 화면 확인을 상기시킵니다.

`Stop`은 최종 답변 전에 품질 확인과 쉬운 설명이 빠지지 않았는지 확인합니다.

관련 파일:

- `hooks/hooks.json`
- `hooks/user_prompt_submit.py`
- `hooks/pre_tool_use_gate.py`
- `hooks/post_tool_use_review.py`
- `hooks/stop_loop_guard.py`
- `hooks/session_start.py`
- `hooks/lib/frameward_common.py`

## 모드 설계

Frameward는 기본적으로 안전한 `advisory` 모드로 동작합니다.

모드는 `.frameward/config.json`에서 설정합니다.

```json
{
  "enforcementMode": "advisory"
}
```

지원 모드:

- `advisory`: 안내와 알림 중심입니다. 일반 작업을 거의 막지 않습니다.
- `balanced`: UI 작업에는 더 분명히 경고하고, 의존성 설치와 외부 제공자 활성화는 승인 없이는 막습니다.
- `hybrid-strict`: UI 수정 전과 최종 확인 단계에서만 엄격하게 동작합니다.
- `strict`: 필요한 게이트가 빠졌을 때 UI 수정이나 최종 종료를 막을 수 있습니다.

엄격한 동작은 게이트별로 적용됩니다. 모든 명령을 전역적으로 막는 방식이 아닙니다.

## 스킬과 워크플로우 계층

스킬은 특정 UI 작업을 잘게 나눈 실행 단위입니다.

예를 들어:

- 사용자의 모호한 요청을 해석할 때는 `client-intent-discovery`
- 화면의 주요 영역을 나눌 때는 `layout-region-mapping`
- 기존 UI 규칙을 확인할 때는 `design-system-audit`
- 모바일, 태블릿, 데스크톱을 확인할 때는 `responsive-check`
- 최종 설명을 작성할 때는 `plain-language-brief`

워크플로우는 여러 스킬을 이어 붙인 흐름입니다.

예를 들어 `workflows/improve-existing-screen.md`는 기존 화면을 개선할 때 필요한 순서를 제공합니다.

관련 파일:

- `skills/*/SKILL.md`
- `workflows/*.md`

## Provider 계층

Provider는 “어떤 방식으로 UI를 구현할지”를 결정하는 계층입니다.

Frameward는 먼저 프로젝트에 이미 있는 컴포넌트, 스타일, 색상, 간격, 텍스트 규칙을 사용합니다.

Provider 우선순위:

1. 프로젝트에 이미 있는 UI 규칙
2. 프로젝트에 이미 설치된 provider
3. 사용자가 명시적으로 요청한 provider
4. 참고용 문서만 사용하는 방식

관련 파일:

- `providers/README.md`
- `providers/project-native/provider.md`
- `providers/astryx/provider.md`
- `models/design-system-provider-interface.md`
- `core/design-system-provider-model.md`

## 새 프로젝트 UI 기반

기존 UI 규칙이 없는 새 프로젝트에서는 Frameward가 바로 화면을 만들지 않습니다. 먼저 최소 UI 규칙을 정리합니다.

새 프로젝트 흐름은 다음 순서로 진행합니다.

```text
서비스 종류와 사용자 파악
  -> 첫 대표 화면 선택
  -> 필요한 화면 목록 초안 작성
  -> 최소 UI 규칙 작성
  -> provider 후보 평가
  -> Astryx 적합성 검토
  -> 승인 전 설치 금지
  -> 대표 화면 구현 기준 정리
```

이 흐름은 큰 디자인 시스템을 먼저 만들기 위한 것이 아닙니다. 첫 화면과 다음 화면들이 같은 제품처럼 보이도록 최소 기준을 정하는 과정입니다.

관련 파일:

- `docs/new-project-flow.ko.md`
- `workflows/bootstrap-new-project-ui.md` (`ui-foundation` workflow)
- `templates/ui-foundation-brief.md`
- `models/ui-foundation-model.md`

## Astryx 경계

Astryx는 선택 사항입니다.

Frameward는 Astryx를 자동으로 설치하지 않습니다. Astryx MCP도 자동으로 활성화하지 않습니다. 프로젝트를 Astryx로 자동 마이그레이션하지도 않습니다.

Astryx는 네 가지 방식으로만 다룹니다.

- `reference`: 설치 없이 아이디어만 참고
- `adapter`: 프로젝트가 이미 Astryx를 사용할 때만 직접 사용
- `bootstrap`: 새 React 프로젝트에서 사용자가 승인한 뒤 도입 제안
- `mcp`: 사용자가 승인한 뒤 문서 조회에만 사용

관련 파일:

- `providers/astryx/provider.md`
- `providers/astryx/install.md`
- `providers/astryx/mcp-policy.md`
- `providers/astryx/workflow.md`
- `skills/astryx-adapter/SKILL.md`

## 상태와 설정

Frameward는 작업 중 상태를 기록해 어떤 게이트가 완료되었는지 추적합니다.

주요 설정 파일:

- `.frameward/config.example.json`: 기본 모드와 provider 정책 예시
- `.frameward/gates.example.json`: 필요한 게이트 목록
- `.frameward/loop-policy.example.json`: 루프 동작 정책 예시
- `.frameward/design-system-provider.example.json`: provider 상태 예시

주요 스키마:

- `schemas/frameward-loop-state.schema.json`
- `schemas/design-system-provider.schema.json`
- `schemas/astryx-provider-state.schema.json`
- `schemas/qa-report.schema.json`

## 검증 계층

`tools/validate_scaffold.py`는 스캐폴드가 기본 계약을 지키는지 확인합니다.

검증 항목:

- 플러그인 manifest가 올바른 경로를 가리키는지
- hook 설정이 유효한지
- Python hook 파일 문법이 올바른지
- 모든 skill에 `SKILL.md`가 있는지
- skill frontmatter에 `name`과 `description`이 있는지
- 게이트와 모드가 스키마와 일치하는지
- Astryx가 기본적으로 비활성 상태인지
- 의존성 설치와 MCP가 기본적으로 꺼져 있는지

실행:

```bash
python3 tools/validate_scaffold.py
```

## 안전 원칙

Frameward는 다음 원칙을 지켜야 합니다.

- UI 작업이 아닌 요청에는 개입하지 않는다.
- 사용자가 모르는 전문 용어를 최종 설명에 남발하지 않는다.
- 새 의존성을 자동으로 추가하지 않는다.
- Astryx 설치나 MCP 활성화를 자동으로 하지 않는다.
- 기존 프로젝트의 UI 규칙을 먼저 따른다.
- 큰 재설계보다 작은 개선을 우선한다.
- 최종 답변에는 무엇을 바꿨고 무엇을 확인했는지 쉬운 말로 설명한다.

## 설계상 하지 않는 일

Frameward가 하지 않는 일도 명확합니다.

- 자체 UI 컴포넌트 제공
- 특정 UI 라이브러리 강제
- Astryx 자동 설치
- 외부 MCP 자동 활성화
- 모든 코드 작업에 UI 정책 강제
- 사용자의 모호한 말을 이유로 대규모 재설계 수행

Frameward의 역할은 Codex가 화면 개선 작업을 더 신중하고 일관되게 수행하도록 안내하는 것입니다.

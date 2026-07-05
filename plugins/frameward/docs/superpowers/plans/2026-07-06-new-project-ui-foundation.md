# New Project UI Foundation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add first-class documentation, workflow, template, and model support for new projects that do not yet have mature UI rules.

**Architecture:** This is a documentation/model expansion only. It adds a Korean new-project guide, an execution workflow, a UI foundation template, and an internal model, then links them from existing README and architecture docs. Hooks, schemas, plugin manifest, and provider behavior remain unchanged.

**Tech Stack:** Markdown documentation, existing Frameward scaffold validator, shell path checks.

---

## File Structure

- Create: `docs/new-project-flow.ko.md`  
  Korean guide explaining how Frameward handles brand-new projects.

- Create: `workflows/bootstrap-new-project-ui.md`  
  Agent workflow for establishing a minimal UI foundation before building the first representative screen.

- Create: `templates/ui-foundation-brief.md`  
  Fillable brief for recording project type, users, first screen, UI rules, states, mobile behavior, provider decision, and Astryx approval status.

- Create: `models/ui-foundation-model.md`  
  Internal model defining what a UI foundation is and when it is complete enough for implementation.

- Modify: `README.md`  
  Add the Korean new-project guide link under Design Documentation.

- Modify: `docs/architecture.ko.md`  
  Add a section explaining how new projects differ from existing-project improvement.

- Modify: `CHANGELOG.md`  
  Record the new-project UI foundation docs, model, template, and workflow.

- Modify: `FILE_MANIFEST.md`  
  Increase generated file count from 115 to 119 and list the four new files.

Git note: this workspace currently reports `fatal: not a git repository (or any of the parent directories): .git`. Do not run git commit commands in this workspace unless `git rev-parse --show-toplevel` succeeds first.

---

### Task 1: Add Korean New-Project Flow Documentation

**Files:**
- Create: `docs/new-project-flow.ko.md`

- [ ] **Step 1: Create the new Korean guide**

Use `apply_patch` to add this exact file:

````md
# 새 프로젝트 UI 흐름

이 문서는 Frameward가 완전 새로운 프로젝트에서 UI 기반을 잡는 방식을 설명합니다.

기존 프로젝트에서는 이미 있는 컴포넌트, 색상, 간격, 글자 규칙을 먼저 찾습니다. 하지만 새 프로젝트에는 그런 기준이 없거나 아직 약할 수 있습니다. 이때 Frameward는 바로 화면을 만들기보다 최소 UI 규칙을 먼저 정리합니다.

## 왜 별도 흐름이 필요한가

새 프로젝트에서 바로 화면을 만들면 화면마다 기준이 달라지기 쉽습니다.

예를 들어 첫 화면은 둥근 버튼을 쓰고, 두 번째 화면은 각진 버튼을 쓰고, 어떤 화면은 여백이 넓고 다른 화면은 빽빽하면 사용자가 같은 제품처럼 느끼기 어렵습니다.

Frameward는 이런 문제를 줄이기 위해 첫 대표 화면을 만들기 전에 다음을 정리합니다.

- 누구를 위한 서비스인가
- 사용자가 가장 먼저 해야 하는 일은 무엇인가
- 어떤 화면이 먼저 필요한가
- 기본 색상, 간격, 글자 크기, 버튼, 입력창 기준은 무엇인가
- 로딩, 빈 상태, 오류 상태는 어떻게 보여줄 것인가
- 모바일에서 중요한 정보와 버튼이 잘 보이는가
- provider를 새로 도입할 필요가 있는가

## 기존 프로젝트와 새 프로젝트의 차이

기존 프로젝트:

```text
기존 UI 규칙 찾기
  -> 그 규칙에 맞춰 화면 개선
  -> 작은 변경으로 품질 확인
```

새 프로젝트:

```text
서비스와 사용자 파악
  -> 최소 UI 규칙 만들기
  -> provider 후보 평가
  -> 첫 대표 화면 기준 정리
  -> 구현과 품질 확인
```

## 기본 처리 흐름

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

## 최소 UI 규칙

최소 UI 규칙은 거창한 디자인 시스템이 아닙니다. 첫 화면과 다음 화면들이 같은 제품처럼 보이게 하는 작은 기준입니다.

포함할 항목:

- 기본 색상 방향
- 화면 여백과 요소 간격
- 제목, 본문, 보조 문구 크기
- 주요 버튼과 보조 버튼의 차이
- 입력창, 선택 메뉴, 체크박스 같은 입력 요소 기준
- 카드, 표, 목록 같은 정보 묶음 기준
- 로딩, 빈 상태, 오류 상태 표현
- 모바일에서 정보와 버튼이 쌓이는 방식

## Provider-neutral 기본 원칙

새 프로젝트라고 해서 바로 UI 라이브러리를 설치하지 않습니다.

Frameward의 기본값은 provider-neutral입니다.

```text
먼저 제품에 맞는 최소 UI 규칙을 정한다.
이미 설치된 provider가 있으면 그 규칙을 따른다.
새 provider가 필요하면 후보로 평가한다.
사용자가 승인하기 전에는 설치하지 않는다.
```

## Astryx 후보 평가

Astryx는 새 React 프로젝트에서 후보가 될 수 있습니다. 하지만 Frameward는 Astryx 래퍼가 아닙니다.

Astryx를 검토할 때 확인할 것:

- 프로젝트가 React 기반인가
- 아직 성숙한 UI 규칙이 없는가
- 팀이 새 provider 도입을 원하거나 허용하는가
- Astryx를 쓰면 첫 화면 이후에도 같은 규칙을 반복해서 적용하기 쉬운가
- 설치와 MCP 활성화에 대한 명시적 승인이 있는가

승인이 없으면 Astryx는 참고 또는 후보 평가에만 사용합니다.

## 승인 전 금지되는 일

다음 작업은 사용자가 명시적으로 승인하기 전까지 하지 않습니다.

- Astryx 설치
- Astryx MCP 활성화
- 프로젝트를 Astryx 기준으로 마이그레이션
- Tailwind, shadcn, MUI 같은 새 UI 의존성 설치
- 외부 provider를 기본값으로 확정

## 예시 요청

사용자 요청:

```text
Frameward로 새 SaaS 프로젝트의 대시보드 화면을 만들어주세요.
아직 UI 기준은 없습니다.
```

Frameward 처리:

```text
1. SaaS 대시보드가 첫 대표 화면인지 확인한다.
2. 사용자가 관리자, 팀원, 고객 중 누구인지 파악한다.
3. 대시보드에서 가장 먼저 보여야 할 정보를 정한다.
4. 기본 색상, 간격, 버튼, 카드, 표 기준을 정리한다.
5. 로딩, 빈 상태, 오류 상태를 함께 계획한다.
6. Astryx는 후보로 평가하되 승인 전 설치하지 않는다.
7. 기준에 맞춰 첫 화면 구현 계획을 세운다.
8. 결과를 쉬운 말로 설명한다.
```

## 좋은 최종 설명

```text
기존 UI 기준이 없는 새 프로젝트라서 먼저 기본 화면 규칙을 정리했습니다. 이 기준에는 버튼 모양, 카드 간격, 글자 크기, 로딩/빈 상태/오류 상태가 포함됩니다. Astryx는 후보로만 평가했고, 승인 전에는 설치하지 않는 방향으로 유지했습니다.
```
````

- [ ] **Step 2: Verify the guide exists**

Run:

```bash
test -f docs/new-project-flow.ko.md
```

Expected: exit code `0`.

---

### Task 2: Add Bootstrap Workflow

**Files:**
- Create: `workflows/bootstrap-new-project-ui.md`

- [ ] **Step 1: Create the workflow**

Use `apply_patch` to add this exact file:

````md
# Workflow: Bootstrap New Project UI

Use this when the user asks Frameward to create a first screen or UI foundation for a brand-new project, or for a project that has no mature UI rules yet.

This workflow does not install dependencies. It may evaluate providers, including Astryx, but provider installation and MCP activation require explicit user approval.

## Process

1. Confirm this is a new project or a project without mature UI rules.
2. Identify the product type, primary users, and first representative screen.
3. Write a minimal UI foundation brief before implementation.
4. Check whether a provider is already present in the project.
5. Compare provider-neutral, project-native, and explicitly approved provider paths.
6. Evaluate Astryx as a candidate only; do not install Astryx or enable Astryx MCP.
7. Select the safest path and explain the reason in plain language.
8. Define loading, empty, error, disabled, and success states before implementation.
9. Define mobile, tablet, and desktop behavior before implementation.
10. Implement only after the foundation is clear.
11. Explain what foundation decisions were made and what remains open.

## Provider Decision Rules

- Use project-native rules if they already exist.
- Use provider-neutral rules when the project has no mature UI system.
- Use Astryx directly only when it is already installed or explicitly approved.
- Propose Astryx bootstrap only when the project is React-based, lacks mature UI rules, and the user approves dependency changes.
- Do not enable MCP without explicit approval.

## Required Output

```md
### New project status
-

### Primary user and first screen
-

### UI foundation summary
-

### Provider decision
-

### Astryx candidate evaluation
-

### States and screen sizes covered
-

### Plain-language explanation
-
```
````

- [ ] **Step 2: Verify the workflow exists**

Run:

```bash
test -f workflows/bootstrap-new-project-ui.md
```

Expected: exit code `0`.

---

### Task 3: Add UI Foundation Brief Template

**Files:**
- Create: `templates/ui-foundation-brief.md`

- [ ] **Step 1: Create the template**

Use `apply_patch` to add this exact file:

````md
# UI Foundation Brief

Use this brief before creating the first representative screen for a new project or a project without mature UI rules.

## Project Type

-

## Primary Users

-

## First Representative Screen

-

## Main User Action

-

## Core Screens

-

## UI Foundation

### Colors

-

### Spacing

-

### Typography

-

### Buttons

-

### Forms

-

### Cards And Surfaces

-

## States

### Loading

-

### Empty

-

### Error

-

### Disabled

-

### Success

-

## Mobile, Tablet, And Desktop Behavior

-

## Provider Decision

-

## Astryx Candidate Evaluation

-

## Approval Status

-

## Plain-Language Summary

-
````

- [ ] **Step 2: Verify the template exists**

Run:

```bash
test -f templates/ui-foundation-brief.md
```

Expected: exit code `0`.

---

### Task 4: Add UI Foundation Model

**Files:**
- Create: `models/ui-foundation-model.md`

- [ ] **Step 1: Create the model document**

Use `apply_patch` to add this exact file:

````md
# UI Foundation Model

The UI foundation model describes the minimum set of interface decisions Frameward needs before creating the first representative screen for a new project.

Frameward uses this model when no mature project-native UI rules exist yet.

## Purpose

A UI foundation keeps early screens consistent without forcing a full design system too early.

It answers:

- who the product is for,
- what screen should be built first,
- what users should notice first,
- how basic elements should look and behave,
- which states must be covered,
- whether a provider should be evaluated,
- whether any provider activation has been approved.

## Required Fields

### Project Type

The kind of product being created, such as SaaS dashboard, admin tool, marketplace, content site, or mobile-first utility.

### Primary Users

The people who will use the first screens.

### First Representative Screen

The first screen that proves the UI direction. This should be a real product screen, not a decorative landing page unless the product truly starts there.

### Main User Action

The action users should be able to complete or understand first.

### Core Screens

A short list of screens that should share the same UI foundation.

### UI Rules

Minimum rules for colors, spacing, text, buttons, forms, and surfaces.

### States

Required loading, empty, error, disabled, and success states.

### Screen Sizes

Expected mobile, tablet, and desktop behavior.

### Provider Decision

The selected implementation path: provider-neutral, project-native, installed provider, or explicitly approved provider.

### Astryx Evaluation

Whether Astryx is relevant, why it is or is not suitable, and whether install or MCP approval exists.

## Relationship To Providers

Provider selection comes after the UI foundation is understood.

Frameward should not choose a provider only because a project is new. A provider is appropriate when it helps preserve consistency, matches the project stack, and is already installed or explicitly approved.

## Astryx Boundary

Astryx may be evaluated as a candidate for new React projects.

Frameward must not:

- install Astryx without approval,
- enable Astryx MCP without approval,
- migrate a project to Astryx without approval,
- make Frameward depend on Astryx.

## Completion Criteria

The UI foundation is ready for implementation when:

- the first representative screen is named,
- the main user action is clear,
- core screens are listed,
- basic UI rules are documented,
- loading, empty, error, disabled, and success states are planned,
- mobile, tablet, and desktop behavior is described,
- provider decision is recorded,
- Astryx approval status is explicit,
- the summary can be explained in plain language.
````

- [ ] **Step 2: Verify the model exists**

Run:

```bash
test -f models/ui-foundation-model.md
```

Expected: exit code `0`.

---

### Task 5: Link New Project Docs From Existing Docs

**Files:**
- Modify: `README.md`
- Modify: `docs/architecture.ko.md`

- [ ] **Step 1: Update README design documentation links**

Patch `README.md` under the `## Design Documentation` section:

```patch
*** Begin Patch
*** Update File: README.md
@@
 - [Frameward 내부 설계](./docs/architecture.ko.md)
+- [새 프로젝트 UI 흐름](./docs/new-project-flow.ko.md)
*** End Patch
```

- [ ] **Step 2: Add architecture section for new projects**

Patch `docs/architecture.ko.md` after the Provider section and before the Astryx section:

```patch
*** Begin Patch
*** Update File: docs/architecture.ko.md
@@
 - `models/design-system-provider-interface.md`
 - `core/design-system-provider-model.md`
 
+## 새 프로젝트 UI 기반
+
+기존 UI 규칙이 없는 새 프로젝트에서는 Frameward가 바로 화면을 만들지 않습니다. 먼저 최소 UI 규칙을 정리합니다.
+
+새 프로젝트 흐름은 다음 순서로 진행합니다.
+
+```text
+서비스 종류와 사용자 파악
+  -> 첫 대표 화면 선택
+  -> 필요한 화면 목록 초안 작성
+  -> 최소 UI 규칙 작성
+  -> provider 후보 평가
+  -> Astryx 적합성 검토
+  -> 승인 전 설치 금지
+  -> 대표 화면 구현 기준 정리
+```
+
+이 흐름은 큰 디자인 시스템을 먼저 만들기 위한 것이 아닙니다. 첫 화면과 다음 화면들이 같은 제품처럼 보이도록 최소 기준을 정하는 과정입니다.
+
+관련 파일:
+
+- `docs/new-project-flow.ko.md`
+- `workflows/bootstrap-new-project-ui.md`
+- `templates/ui-foundation-brief.md`
+- `models/ui-foundation-model.md`
+
 ## Astryx 경계
*** End Patch
```

- [ ] **Step 3: Verify links are present**

Run:

```bash
rg -n "new-project-flow|ui-foundation|새 프로젝트 UI 기반" README.md docs/architecture.ko.md
```

Expected: output includes `README.md`, `docs/architecture.ko.md`, `docs/new-project-flow.ko.md`, `workflows/bootstrap-new-project-ui.md`, `templates/ui-foundation-brief.md`, and `models/ui-foundation-model.md` references.

---

### Task 6: Update Changelog And Manifest

**Files:**
- Modify: `CHANGELOG.md`
- Modify: `FILE_MANIFEST.md`

- [ ] **Step 1: Update CHANGELOG**

Patch `CHANGELOG.md` in the `0.1.0 - Scaffold hardening` changed list:

```patch
*** Begin Patch
*** Update File: CHANGELOG.md
@@
 - Added Korean internal architecture documentation for early users.
+- Added new-project UI foundation docs, workflow, template, and model.
*** End Patch
```

- [ ] **Step 2: Update FILE_MANIFEST count and entries**

Patch `FILE_MANIFEST.md`:

```patch
*** Begin Patch
*** Update File: FILE_MANIFEST.md
@@
-Generated files: 115
+Generated files: 119
@@
 - `docs/architecture.ko.md`
+- `docs/new-project-flow.ko.md`
@@
 - `models/responsive-region-model.md`
+- `models/ui-foundation-model.md`
@@
 - `templates/responsive-checklist.md`
 - `templates/screen-improvement-template.md`
+- `templates/ui-foundation-brief.md`
@@
 - `workflows/audit-existing-ui.md`
+- `workflows/bootstrap-new-project-ui.md`
*** End Patch
```

- [ ] **Step 3: Verify manifest entries**

Run:

```bash
rg -n "Generated files: 119|new-project-flow|ui-foundation-model|ui-foundation-brief|bootstrap-new-project-ui" FILE_MANIFEST.md CHANGELOG.md
```

Expected: all five patterns appear.

---

### Task 7: Validate The Scaffold

**Files:**
- Read: `tools/validate_scaffold.py`
- Read: generated docs/workflow/template/model paths

- [ ] **Step 1: Run scaffold validation**

Run:

```bash
python3 tools/validate_scaffold.py
```

Expected:

```text
Frameward scaffold validation passed.
```

- [ ] **Step 2: Verify new paths are present**

Run:

```bash
find docs workflows templates models -maxdepth 2 -type f | sort | rg "new-project-flow|bootstrap-new-project-ui|ui-foundation-brief|ui-foundation-model"
```

Expected output:

```text
docs/new-project-flow.ko.md
models/ui-foundation-model.md
templates/ui-foundation-brief.md
workflows/bootstrap-new-project-ui.md
```

- [ ] **Step 3: Confirm git status behavior**

Run:

```bash
git rev-parse --show-toplevel
```

Expected in this workspace:

```text
fatal: not a git repository (or any of the parent directories): .git
```

If this command succeeds in a different checkout, create one Lore-protocol commit for the completed documentation change.

Suggested commit message:

```text
Clarify new-project UI foundation flow

Constraint: Frameward must remain provider-neutral and Astryx-optional by default.
Rejected: Hook-level detection changes in this pass | The approved scope is documentation, workflow, template, and model only.
Confidence: high
Scope-risk: narrow
Directive: Do not install or enable Astryx from this flow without explicit user approval.
Tested: python3 tools/validate_scaffold.py
Not-tested: Hook runtime behavior; no hook changes were made.
```

---

## Self-Review Checklist

- Spec coverage: all approved files are covered by Tasks 1-6.
- Scope control: hooks, schemas, and plugin manifest are not modified.
- Astryx boundary: all new docs say Astryx is candidate-only unless approved.
- Verification: scaffold validation and path checks are included.
- Git handling: current no-git workspace state is explicit.

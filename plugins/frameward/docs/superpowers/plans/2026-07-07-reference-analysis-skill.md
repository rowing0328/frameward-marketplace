# Reference Analysis Skill Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a lightweight Frameward `reference-analysis` skill for safely learning from reference screens without copying brand-specific or unsupported details.

**Architecture:** Add one focused skill plus one model document and one reusable template. Connect the new skill to the existing Frameward docs, manifest, and changelog without changing hooks, schemas, provider behavior, or the plugin manifest.

**Tech Stack:** Markdown Codex skills, Frameward scaffold validation with `python3 plugins/frameward/tools/validate_scaffold.py`, git.

## Global Constraints

- Do not change hook Python files.
- Do not change hook configuration.
- Do not change plugin manifest.
- Do not change provider files.
- Do not change schema files.
- Do not install dependencies.
- Do not generate images.
- Do not add new provider behavior.
- Keep user-facing wording plain and practical.
- Preserve the existing project UI rules as the priority.
- Keep Design Analyzer as inspiration only; do not copy its whole workflow.

---

## File Structure

- Create `plugins/frameward/skills/reference-analysis/SKILL.md`
  - Owns the new Codex skill instructions.
  - Must include YAML frontmatter with `name` and a description longer than 40 characters.
  - Must clearly state that the skill analyzes references before implementation and does not implement code.

- Create `plugins/frameward/models/reference-analysis-model.md`
  - Defines Frameward's internal model for reference source, visible fact, interpretation, safe adoption, forbidden carryover, target area, existing project rule, and quality check.
  - Keeps the model light enough for ordinary UI improvement work.

- Create `plugins/frameward/templates/reference-analysis-template.md`
  - Provides a fillable analysis report format.
  - Must include source, confidence, relevant parts, learnable points, items not to copy, safe application, checks, and plain-language summary.

- Modify `plugins/frameward/README.md`
  - Add a short explanation that reference screens can be analyzed before improvements.
  - Keep the message plain and avoid turning Frameward into a reference-design generator.

- Modify `plugins/frameward/docs/architecture.ko.md`
  - Add a short “레퍼런스 분석 계층” section near the existing major layers.
  - State that references are not copy targets and existing project rules remain first.

- Modify `plugins/frameward/FILE_MANIFEST.md`
  - Increase generated file count by 3.
  - Add the three new files in sorted locations.

- Modify `plugins/frameward/CHANGELOG.md`
  - Add a concise bullet under `0.1.0 - Scaffold hardening`.

## Task 1: Add `reference-analysis` Skill

**Files:**
- Create: `plugins/frameward/skills/reference-analysis/SKILL.md`

**Interfaces:**
- Consumes: Reference screens, screenshots, URLs, Figma notes, or manually described examples from the user.
- Produces: A plain-language reference analysis that later tasks can feed into `layout-region-mapping`, `design-system-provider-detection`, `design-system-audit`, and `screen-improvement-plan`.

- [ ] **Step 1: Create the skill directory**

Run:

```bash
mkdir -p plugins/frameward/skills/reference-analysis
```

Expected: directory exists at `plugins/frameward/skills/reference-analysis`.

- [ ] **Step 2: Add the skill file**

Write `plugins/frameward/skills/reference-analysis/SKILL.md` with exactly this content:

```markdown
---
name: reference-analysis
description: Use when a user provides a reference screen, screenshot, site, Figma note, or example UI before improving a Frameward screen.
---

# reference-analysis

## Goal

Separate what Frameward can safely learn from a reference screen from what it should not copy.

Use this before implementation when the user provides a screenshot, site, Figma note, existing UI, or manually described example as a reference.

## When to use

Use this skill when:

- The user says to copy, follow, match, take inspiration from, benchmark, or compare a reference.
- The user provides screenshots, URLs, Figma notes, or example screens.
- A screen improvement depends on understanding which parts of a reference are useful.
- A new project needs a reference-informed first screen, but the project has its own product and UI rules.

Do not use this skill when:

- The user only asks to improve the current screen and provides no reference.
- The task is not UI-related.
- The user asks for a full static handoff package rather than a Frameward improvement pass.

## Process

1. Record the reference source and confidence.
2. Identify the reference parts that matter to the current task.
3. Separate visible facts from interpretation.
4. List what Frameward can learn from the reference.
5. List what Frameward must not copy.
6. Map safe learnings to target screen areas.
7. Preserve the current project's existing UI rules first.
8. Define checks to run before implementation.
9. Explain the result in plain language.

## Analysis fields

Use these fields unless the task needs a shorter answer.

```text
Reference summary
- Source:
- Confidence:
- Relevant parts:

Visible facts
- Screen structure:
- Information grouping:
- Important action:
- Text and density:
- States and feedback:

Safe to learn
- What can transfer:
- Why it helps:
- Target screen area:
- Existing project rule to preserve:
- Allowed adaptation:

Do not copy
- Brand-specific elements:
- Unsupported claims:
- Layout risks:
- Accessibility risks:
- Project mismatch:

Checks before implementation
- Mobile:
- Keyboard and focus:
- Loading, empty, and error states:
- Text fit:
- Existing component/style rules:

Plain-language summary
- Summary:
```

## Rules

- Do not implement code in this skill.
- Do not generate images in this skill.
- Do not install UI libraries in this skill.
- Do not activate external providers in this skill.
- Do not copy a reference screen wholesale.
- Do not carry over logos, official marks, certifications, security claims, customer claims, or authority signals without a source supplied by the user.
- Do not use expert terms in the final explanation when plain language is enough.
- Treat the project's existing components, colors, spacing, and text rules as the default.

## Output

Return a concise reference analysis that can be used by later Frameward skills.

End with one of these next-step recommendations:

- `Next: layout-region-mapping` when screen areas are still unclear.
- `Next: design-system-provider-detection` when the project UI system is unknown.
- `Next: design-system-audit` when the provider is known but local rules need inspection.
- `Next: screen-improvement-plan` when the reference analysis and local UI rules are clear.
```

- [ ] **Step 3: Verify skill frontmatter is discoverable**

Run:

```bash
python3 plugins/frameward/tools/validate_scaffold.py
```

Expected output:

```text
Frameward scaffold validation passed.
```

- [ ] **Step 4: Commit Task 1**

Run:

```bash
git add plugins/frameward/skills/reference-analysis/SKILL.md
git commit -m "feat: add reference analysis skill" -m "- define safe reference intake for Frameward UI work" -m "- keep the skill analysis-only and provider-neutral"
```

Expected: commit succeeds and includes only `plugins/frameward/skills/reference-analysis/SKILL.md`.

## Task 2: Add Model and Template

**Files:**
- Create: `plugins/frameward/models/reference-analysis-model.md`
- Create: `plugins/frameward/templates/reference-analysis-template.md`

**Interfaces:**
- Consumes: The output fields from `reference-analysis`.
- Produces: A reusable internal model and a copyable template for reference-informed UI work.

- [ ] **Step 1: Add the model document**

Write `plugins/frameward/models/reference-analysis-model.md` with exactly this content:

```markdown
# Reference Analysis Model

The reference analysis model helps Frameward learn from example screens without copying them blindly.

It is used only when a user provides a reference screen, screenshot, site, Figma note, existing UI, or manual example.

## Purpose

Frameward should turn reference input into practical guidance:

```text
visible fact
  -> safe learning
  -> target screen area
  -> existing project rule
  -> quality check
```

This keeps the work grounded in what can be seen while preserving the current project's own UI rules.

## Fields

### Reference Source

Records where the reference came from.

- `source`: screenshot, URL, Figma note, existing UI, manual description, or mixed.
- `providedBy`: user, local project, public source, or unknown.
- `confidence`: high, medium, or low.
- `relevantParts`: page frame, navigation, content area, cards, forms, buttons, lists, states, or other named areas.

### Visible Fact

Records what is visible before interpretation.

Examples:

- The primary action appears in the first screen.
- Cards use short titles and one supporting line.
- Dense lists collapse into grouped rows on smaller screens.
- Error text appears directly under the input.

### Interpretation

Explains why a visible fact may matter.

Examples:

- The first action is easy to find.
- Related information is grouped clearly.
- Mobile users can scan the list before opening details.
- The form keeps the problem close to the field.

### Safe Adoption

Defines what Frameward can learn from the reference.

Examples:

- Use a similar order of information.
- Keep the main action visible near the relevant content.
- Use short helper text for complex choices.
- Keep state messages close to the element they explain.

### Forbidden Carryover

Defines what Frameward must not copy.

Examples:

- Logos and brand marks.
- Product-specific claims.
- Certification, security, or authority signals.
- Copy that implies unsupported proof.
- Layout details that conflict with the current project.

### Target Application Area

Names where the safe learning may apply.

Allowed values:

- `page_frame`
- `navigation`
- `content_sections`
- `cards`
- `lists_tables`
- `forms`
- `buttons`
- `state_views`
- `mobile_behavior`

### Existing Project Rule

Records what local rule should stay in charge.

Examples:

- Existing button component.
- Existing spacing scale.
- Existing type sizes.
- Existing color roles.
- Existing form state pattern.
- Existing mobile breakpoint behavior.

### Quality Check

Defines what must be checked before implementation is considered ready.

Required checks when relevant:

- Mobile layout keeps the important action reachable.
- Keyboard focus is visible.
- Loading, empty, and error states remain clear.
- Text fits without overlapping.
- The implementation follows existing components and style rules.

## Completion Criteria

A reference analysis is complete when it identifies:

- the reference source and confidence,
- visible facts,
- safe learnings,
- items not to copy,
- target screen areas,
- existing project rules to preserve,
- checks to run before implementation.
```

- [ ] **Step 2: Add the template**

Write `plugins/frameward/templates/reference-analysis-template.md` with exactly this content:

```markdown
# Reference Analysis

## Reference Summary

- Source:
- Confidence:
- Relevant parts:

## Visible Facts

- Screen structure:
- Information grouping:
- Important action:
- Text and density:
- States and feedback:

## Safe To Learn

- What can transfer:
- Why it helps:
- Target screen area:
- Existing project rule to preserve:
- Allowed adaptation:

## Do Not Copy

- Brand-specific elements:
- Unsupported claims:
- Layout risks:
- Accessibility risks:
- Project mismatch:

## Checks Before Implementation

- Mobile:
- Keyboard and focus:
- Loading, empty, and error states:
- Text fit:
- Existing component/style rules:

## Plain-Language Summary

-
```

- [ ] **Step 3: Verify files exist**

Run:

```bash
test -f plugins/frameward/models/reference-analysis-model.md
test -f plugins/frameward/templates/reference-analysis-template.md
```

Expected: both commands exit with status `0`.

- [ ] **Step 4: Commit Task 2**

Run:

```bash
git add plugins/frameward/models/reference-analysis-model.md plugins/frameward/templates/reference-analysis-template.md
git commit -m "docs: add reference analysis model" -m "- define lightweight reference source and safe adoption fields" -m "- add a reusable reference analysis template"
```

Expected: commit succeeds and includes only the two new documentation files.

## Task 3: Link the New Skill in Frameward Docs

**Files:**
- Modify: `plugins/frameward/README.md`
- Modify: `plugins/frameward/docs/architecture.ko.md`
- Modify: `plugins/frameward/CHANGELOG.md`
- Modify: `plugins/frameward/FILE_MANIFEST.md`

**Interfaces:**
- Consumes: New skill, model, and template from Tasks 1 and 2.
- Produces: Repository docs that make the new reference analysis surface discoverable.

- [ ] **Step 1: Update README**

In `plugins/frameward/README.md`, after the paragraph ending with “without forcing users to learn design vocabulary.”, add this paragraph:

```markdown
When a user provides a reference screen, Frameward can first separate what is safe to learn from the reference from what should not be copied. This keeps reference-informed work grounded in visible screen details while preserving the current project's own components, colors, spacing, and text rules.
```

Expected: README explains reference-informed work without promising full reference cloning.

- [ ] **Step 2: Update architecture docs**

In `plugins/frameward/docs/architecture.ko.md`, after the “### 1. 사용자 언어 계층” section and before “### 2. 루프 게이트 계층”, add this section:

```markdown
### 2. 레퍼런스 분석 계층

사용자가 참고 화면, 스크린샷, 사이트, Figma 메모를 제공할 때 Frameward는 이를 그대로 복제 대상으로 보지 않습니다.

먼저 눈에 보이는 사실과 해석을 분리합니다. 그 다음 현재 프로젝트에 안전하게 참고할 부분, 가져오면 안 되는 브랜드 고유 요소, 출처 없는 신뢰 표현, 화면 구조 위험을 나눕니다.

이 계층의 기본 원칙은 기존 프로젝트의 컴포넌트, 색상, 간격, 글자 규칙을 우선하는 것입니다. 레퍼런스는 방향을 잡기 위한 자료이며, 현재 프로젝트의 UI 규칙을 대체하지 않습니다.

관련 파일:

- `skills/reference-analysis/SKILL.md`
- `models/reference-analysis-model.md`
- `templates/reference-analysis-template.md`
```

Then increment the later layer headings by one:

```text
### 2. 루프 게이트 계층 -> ### 3. 루프 게이트 계층
### 3. 훅 계층 -> ### 4. 훅 계층
```

Continue the same numbering pattern for the remaining major layer headings in that section.

Expected: architecture docs include the new layer and the heading numbers remain sequential.

- [ ] **Step 3: Update changelog**

In `plugins/frameward/CHANGELOG.md`, under `## 0.1.0 - Scaffold hardening` and `### Changed`, add this bullet:

```markdown
- Added a lightweight reference-analysis skill, model, and template for safely learning from reference screens without copying brand-specific or unsupported details.
```

Expected: changelog records the new capability.

- [ ] **Step 4: Update file manifest count and entries**

In `plugins/frameward/FILE_MANIFEST.md`, change:

```markdown
Generated files: 120
```

to:

```markdown
Generated files: 123
```

Add these entries in sorted locations:

```markdown
- `models/reference-analysis-model.md`
- `skills/reference-analysis/SKILL.md`
- `templates/reference-analysis-template.md`
```

Expected: manifest count is accurate and the three new files are listed.

- [ ] **Step 5: Verify docs mention the skill**

Run:

```bash
rg -n "reference-analysis|Reference Analysis|레퍼런스 분석" plugins/frameward/README.md plugins/frameward/docs/architecture.ko.md plugins/frameward/CHANGELOG.md plugins/frameward/FILE_MANIFEST.md
```

Expected: output includes matches in all four files.

- [ ] **Step 6: Commit Task 3**

Run:

```bash
git add plugins/frameward/README.md plugins/frameward/docs/architecture.ko.md plugins/frameward/CHANGELOG.md plugins/frameward/FILE_MANIFEST.md
git commit -m "docs: expose reference analysis workflow" -m "- document the reference-analysis skill in Frameward docs" -m "- update changelog and file manifest"
```

Expected: commit succeeds and includes only the four documentation files.

## Task 4: Final Validation

**Files:**
- Validate: `plugins/frameward/tools/validate_scaffold.py`
- Inspect: git status and the last three commits from this implementation.

**Interfaces:**
- Consumes: All files from Tasks 1 through 3.
- Produces: Validation evidence and final implementation commit status.

- [ ] **Step 1: Run scaffold validation**

Run:

```bash
python3 plugins/frameward/tools/validate_scaffold.py
```

Expected output:

```text
Frameward scaffold validation passed.
```

- [ ] **Step 2: Verify required files exist**

Run:

```bash
test -f plugins/frameward/skills/reference-analysis/SKILL.md
test -f plugins/frameward/templates/reference-analysis-template.md
test -f plugins/frameward/models/reference-analysis-model.md
```

Expected: all commands exit with status `0`.

- [ ] **Step 3: Verify skill frontmatter directly**

Run:

```bash
sed -n '1,8p' plugins/frameward/skills/reference-analysis/SKILL.md
```

Expected output starts with:

```markdown
---
name: reference-analysis
description: Use when a user provides a reference screen, screenshot, site, Figma note, or example UI before improving a Frameward screen.
---
```

- [ ] **Step 4: Check worktree**

Run:

```bash
git status --short
```

Expected: no implementation files from this plan remain unstaged or uncommitted.

If `plugins/frameward/docs/local-plugin-install.ko.md` is still modified from earlier work, leave it alone and report it as pre-existing unrelated work.

- [ ] **Step 5: Review commit history**

Run:

```bash
git log --oneline -4
```

Expected: recent history includes the design spec commit plus the three implementation commits from Tasks 1 through 3.

## Self-Review

Spec coverage:

- `skills/reference-analysis/SKILL.md`: covered by Task 1.
- `templates/reference-analysis-template.md`: covered by Task 2.
- `models/reference-analysis-model.md`: covered by Task 2.
- `README.md`: covered by Task 3.
- `docs/architecture.ko.md`: covered by Task 3.
- `FILE_MANIFEST.md`: covered by Task 3.
- `CHANGELOG.md`: covered by Task 3.
- No hook, schema, plugin manifest, provider, dependency, or image-generation changes are included.

Placeholder scan:

- This plan contains exact file paths, exact commands, and complete content for the new files.
- Existing docs modifications specify exact insertion text and verification commands.

Type and naming consistency:

- The skill name is consistently `reference-analysis`.
- The model path is consistently `plugins/frameward/models/reference-analysis-model.md`.
- The template path is consistently `plugins/frameward/templates/reference-analysis-template.md`.
- The plan uses the same next-step skill names already present in Frameward.

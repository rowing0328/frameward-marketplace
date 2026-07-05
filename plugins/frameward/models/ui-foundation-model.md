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

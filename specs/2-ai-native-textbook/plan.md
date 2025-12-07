# Implementation Plan: AI-Native Textbook — Physical AI & Humanoid Robotics (v2.1.0)

**Branch**: `2-ai-native-textbook` | **Date**: 2025-12-07 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/specs/2-ai-native-textbook/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Implementation of an AI-Native textbook with RAG backend, personalization engine, English/Urdu translation capabilities, and book-style frontend with responsive design and interactive components. The project will follow the Spec-Kit Plus methodology with content created using Claude Code subagents and delivered through a Docusaurus frontend with FastAPI backend for AI Q&A and personalization services.

## Technical Context

**Language/Version**: Python 3.11+ (for backend/FastAPI), JavaScript/TypeScript (for Docusaurus frontend)
**Primary Dependencies**: Docusaurus.ai, FastAPI, OpenAI SDK, Qdrant client, Neon Postgres driver, Better-Auth, Tailwind CSS
**Storage**: Qdrant Cloud (vector DB), Neon Serverless Postgres (metadata DB), GitHub Pages (static content)
**Testing**: pytest for backend, Jest for frontend components, accessibility testing with a11y
**Target Platform**: Web application (frontend) served via GitHub Pages, backend API on Railway/Fly.io
**Project Type**: Web application with separate frontend (Docusaurus) and backend (FastAPI)
**Performance Goals**: <3 second response time for AI queries, <500ms page load time, 99.5% uptime
**Constraints**: Free tier limitations on Qdrant Cloud and Neon Postgres, GitHub Pages static hosting
**Scale/Scope**: Support up to 10,000 registered users, handle 1,000 concurrent users during peak times

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

Based on the AI-Native Textbook Constitution (v2.1.0):

### AI-Native Content Architecture
- [x] Content will be machine-readable, modular, chunkable
- [x] Headings, sections, examples, exercises follow AI-native formatting
- [x] Includes Metadata, Learning Outcomes, RAG-indexable sections

### Spec-Kit Plus Driven Production
- [x] Chapter originates from Spec-Kit Plus plan + spec + tasks pipeline
- [x] No chapter manually added without spec
- [x] Tests auto-generated using `.specify/tests`

### Docusaurus.ai Rendering Layer
- [x] Content stored in `docs/` and rendered via Docusaurus
- [x] Layouts support personalization button, translation button, "answer based on selection" API
- [x] Book-cover homepage implemented with responsive scaling

### Automated Quality Assurance
- [x] Commit triggers spec validation, link/testing checks, RAG-index rebuild
- [x] Accessibility testing (WCAG 2.1 AA) included

### RAG-Ready Knowledge Architecture
- [x] Content chunked for Qdrant ingestion (300-500 tokens with metadata)
- [x] Metadata includes: chapter, module, tags, difficulty, version

### Personalization Engine
- [x] Supports personalization based on user background, skill level, goals

### Urdu Translation Engine
- [x] Chapter supports Urdu translation via button and JSON layer
- [x] RTL layout support with proper UI mirroring for Urdu content

### Better-Auth Signup Flow
- [x] Collects user data at signup to feed personalization

### Accessibility Requirements
- [x] Content meets WCAG 2.1 AA standards

### Book-Style Frontend Theme
- [x] Colors, typography, spacing standardized
- [x] Serif fonts for headings, Sans fonts for body
- [x] Primary, secondary, background, accent colors defined
- [x] Icons and UI components consistent
- [x] Book-cover homepage implemented

## Project Structure

### Documentation (this feature)

```text
specs/2-ai-native-textbook/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
/
├── constitution.md
├── docs/
│   ├── modules/
│   │   ├── module1-the-robotic-nervous-system/
│   │   ├── module2-digital-twins/
│   │   ├── module3-ai-robot-brain/
│   │   ├── module4-vision-language-action/
│   │   └── capstone-autonomous-humanoid/
│   ├── chapters/
│   └── glossary/
├── src/
│   ├── components/
│   │   ├── PersonalizationButton/
│   │   ├── TranslationToggle/
│   │   └── QABot/
│   ├── personalization/
│   │   └── engine.js
│   └── translation/
│       └── engine.js
├── rag-backend/
│   ├── api/
│   │   ├── main.py
│   │   ├── endpoints/
│   │   │   ├── ask.py
│   │   │   ├── ask_selection.py
│   │   │   └── history.py
│   │   └── models/
│   │       ├── query.py
│   │       └── response.py
│   ├── db/
│   │   ├── postgres_connector.py
│   │   └── qdrant_connector.py
│   ├── embeddings/
│   │   ├── chunker.py
│   │   └── indexer.py
│   └── agents/
│       └── rag_agent.py
├── public/
│   └── images/ (book cover, illustrations)
├── tests/
│   ├── unit/
│   ├── integration/
│   └── contract/
├── .specify/
│   ├── spec.json
│   ├── templates/
│   ├── tests/
│   └── changes/
├── Docusaurus/
│   ├── docusaurus.config.ts
│   ├── package.json
│   └── src/
└── .github/
    └── workflows/
        ├── ci.yml
        └── deploy.yml
```

**Structure Decision**: Web application following the constitution's directory structure requirements (Section 8). Frontend uses Docusaurus in the Docusaurus/ directory with content in docs/. Backend API implemented in rag-backend/ using FastAPI. Personalization and translation components in src/ with dedicated engines. Tests organized by type. Spec-Kit Plus configuration in .specify/ directory. Book cover images and illustrations in public/images/.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [e.g., 4th project] | [current need] | [why 3 projects insufficient] |
| [e.g., Repository pattern] | [specific problem] | [why direct DB access insufficient] |
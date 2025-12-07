---
description: "Task list for AI-Native Textbook — Physical AI & Humanoid Robotics (v2.1.0)"
---

# Tasks: AI-Native Textbook — Physical AI & Humanoid Robotics

**Input**: Design documents from `/specs/2-ai-native-textbook/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create project structure: docs/, src/, rag-backend/, .specify/
- [ ] T002 Initialize Docusaurus project in Docusaurus/ with required dependencies
- [ ] T003 [P] Initialize FastAPI backend project in rag-backend/ with required dependencies
- [ ] T004 [P] Set up git repository with proper ignore files (.gitignore for Python, Node, etc.)
- [ ] T005 Setup CI/CD workflows in .github/workflows/
- [ ] T006 Install and configure Docusaurus dependencies
- [ ] T007 Install and configure FastAPI, Pydantic, SQLAlchemy dependencies
- [ ] T008 Setup development environment configuration
- [ ] T009 Create initial documentation structure in docs/
- [ ] T010 Initialize project README and quickstart guide

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

Examples of foundational tasks (adjust based on your project):

- [ ] T011 Setup database schema and migrations framework for Neon Postgres
- [ ] T012 [P] Implement authentication/authorization framework using Better-Auth
- [ ] T013 [P] Setup API routing and middleware structure in rag-backend/
- [ ] T014 Create base models/entities that all stories depend on (User Profile, Module, Chapter)
- [ ] T015 Configure error handling and logging infrastructure
- [ ] T016 Setup environment configuration management for both frontend and backend
- [ ] T017 Configure Qdrant client and connection infrastructure
- [ ] T018 Create base components for personalization and translation in src/
- [ ] T019 Implement personalization engine in src/personalization/engine.js
- [ ] T020 Implement translation engine in src/translation/engine.js
- [ ] T021 Implement RAG agent in rag-backend/agents/rag_agent.py
- [ ] T022 Implement chunking logic in rag-backend/embeddings/chunker.py
- [ ] T023 Implement indexer for content in rag-backend/embeddings/indexer.py
- [ ] T024 Setup Claude Code subagents configuration
- [ ] T025 Configure automated quality assurance (validation, testing, RAG-index rebuild, accessibility)
- [ ] T026 Setup Spec-Kit Plus integration for spec-driven content creation
- [ ] T027 Implement chunking mechanism for RAG-ready knowledge architecture (300-500 tokens)
- [ ] T028 Create Urdu translation infrastructure with JSON layer

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Access Personalized Content (Priority: P1) 🎯 MVP

**Goal**: Content adapts to user skill, background, and learning preferences

**Independent Test**: Can be fully tested by verifying that the same content appears differently based on the user's profile information (skill level, background, preferences), delivering a customized learning path.

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T029 [P] [US1] Contract test for user registration endpoint in tests/contract/test_auth.py
- [ ] T030 [P] [US1] Integration test for user profile creation in tests/integration/test_user_profile.py

### Implementation for User Story 1

- [ ] T031 [P] [US1] Create User Profile model in rag-backend/models/user_profile.py
- [ ] T032 [P] [US1] Create Module model in rag-backend/models/module.py
- [ ] T033 [P] [US1] Create Chapter model in rag-backend/models/chapter.py
- [ ] T034 [US1] Implement User Profile service in rag-backend/services/user_profile_service.py
- [ ] T035 [US1] Implement Chapter service in rag-backend/services/chapter_service.py
- [ ] T036 [US1] Create Docusaurus component for personalization in Docusaurus/src/components/PersonalizationButton/index.js
- [ ] T037 [US1] Implement personalization API endpoint in rag-backend/api/endpoints/personalization.py
- [ ] T038 [US1] Add difficulty filtering logic to chapter retrieval
- [ ] T039 [US1] Add logging for user story 1 operations
- [ ] T040 [US1] Implement progress tracking in User Profile model and service

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Query textbook with AI assistant (Priority: P1)

**Goal**: Users ask questions about textbook content and receive accurate answers

**Independent Test**: Can be fully tested by submitting various questions about textbook content and verifying that the responses are accurate and based on the textbook material.

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [ ] T041 [P] [US2] Contract test for ask endpoint in tests/contract/test_qa_api.py
- [ ] T042 [P] [US2] Contract test for ask selection endpoint in tests/contract/test_qa_api.py
- [ ] T043 [P] [US2] Integration test for RAG system in tests/integration/test_rag.py

### Implementation for User Story 2

- [ ] T044 [P] [US2] Create AI Assistant Session model in rag-backend/models/session.py
- [ ] T045 [P] [US2] Create Content Chunk model in rag-backend/models/content_chunk.py
- [ ] T046 [US2] Implement Qdrant connector in rag-backend/db/qdrant_connector.py
- [ ] T047 [US2] Implement main endpoint for asking in rag-backend/api/endpoints/ask.py
- [ ] T048 [US2] Implement endpoint for asking from selection in rag-backend/api/endpoints/ask_selection.py
- [ ] T049 [US2] Implement chat history endpoint in rag-backend/api/endpoints/history.py
- [ ] T050 [US2] Create QABot React component in Docusaurus/src/components/QABot/index.js
- [ ] T051 [US2] Add security measures to prevent prompt injection attacks

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Multilingual Access (English/Urdu) (Priority: P2)

**Goal**: Users toggle between English and Urdu content

**Independent Test**: Can be fully tested by verifying that all content can be switched between English and Urdu while maintaining semantic accuracy.

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [ ] T052 [P] [US3] Contract test for translation endpoint in tests/contract/test_translation.py
- [ ] T053 [P] [US3] Integration test for translation layer in tests/integration/test_translation.py

### Implementation for User Story 3

- [ ] T054 [P] [US3] Create Translation Layer model in rag-backend/models/translation_layer.py
- [ ] T055 [US3] Implement translation API endpoint in rag-backend/api/endpoints/translation.py
- [ ] T056 [US3] Implement translation preservation logic for technical terms
- [ ] T057 [US3] Add Urdu support to personalization engine
- [ ] T058 [US3] Create frontend translation toggle component in Docusaurus/src/components/TranslationToggle/index.js
- [ ] T059 [US3] Integrate translation layer with content rendering
- [ ] T060 [US3] Ensure proper handling of Urdu RTL text in UI

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: User Story 4 - Curriculum Navigation (Priority: P1)

**Goal**: Users progress through modules & Capstone project with prerequisites enforced

**Independent Test**: Can be fully tested by verifying users can navigate through all modules in the correct sequence with appropriate prerequisites enforced.

### Tests for User Story 4 (OPTIONAL - only if tests requested) ⚠️

- [ ] T061 [P] [US4] Contract test for module navigation endpoints in tests/contract/test_curriculum.py
- [ ] T062 [P] [US4] Integration test for progress tracking in tests/integration/test_progress.py

### Implementation for User Story 4

- [ ] T063 [P] [US4] Create Curriculum model in rag-backend/models/curriculum.py
- [ ] T064 [US4] Implement curriculum navigation API endpoints in rag-backend/api/endpoints/curriculum.py
- [ ] T065 [US4] Add progress tracking functionality to Chapter service
- [ ] T066 [US4] Create module navigation UI in Docusaurus
- [ ] T067 [US4] Implement logic to enforce prerequisite completion
- [ ] T068 [US4] Create UI components for curriculum navigation
- [ ] T069 [US4] Add progress visualization features

**Checkpoint**: All user stories now complete and integrated

---

## Phase 7: User Story 5 - Frontend/UI: Interactive book layout (Priority: P1)

**Goal**: Book-like interactive interface with consistent theme, icons, colors, and layout

**Independent Test**: Can be fully tested by verifying all interactive components function correctly and the layout feels intuitive to users.

### Tests for User Story 5 (OPTIONAL - only if tests requested) ⚠️

- [ ] T070 [P] [US5] Accessibility tests for WCAG 2.1 AA compliance in tests/accessibility/
- [ ] T071 [P] [US5] Responsiveness tests across multiple device sizes in tests/responsiveness/

### Implementation for User Story 5

- [ ] T072 [US5] Create PersonalizationButton component in Docusaurus/src/components/PersonalizationButton/index.js
- [ ] T073 [US5] Create TranslationToggle component in Docusaurus/src/components/TranslationToggle/index.js  
- [ ] T074 [US5] Integrate QABot component in chapters
- [ ] T075 [US5] Add Interactive Exercises & Code Blocks
- [ ] T076 [US5] Add Progress Tracker UI
- [ ] T077 [US5] Apply book-like layouts & styling in docs/ chapters
- [ ] T078 [US5] Ensure WCAG 2.1 AA accessibility compliance
- [ ] T079 [US5] Create responsive design for mobile, tablet, and desktop
- [ ] T080 [US5] Implement keyboard navigation for interactive elements
- [ ] T081 [US5] Create Book Cover homepage with hero image, title, and navigation buttons
- [ ] T082 [US5] Finalize color theme, typography, icons for all pages
- [ ] T083 [US5] Review and fix RTL layout for Urdu content

**Checkpoint**: All user stories now complete with enhanced UI/UX

---

## Phase 8: Module & Capstone Content Creation

**Goal**: Create content for all required modules and the capstone project

### Implementation for Content Creation

- [ ] T084 Create Module 1 content (ROS 2 fundamentals) in docs/modules/module1-the-robotic-nervous-system/
- [ ] T085 Create Module 2 content (Digital Twins) in docs/modules/module2-digital-twins/
- [ ] T086 Create Module 3 content (AI-Robot Brain) in docs/modules/module3-ai-robot-brain/
- [ ] T087 Create Module 4 content (Vision-Language-Action) in docs/modules/module4-vision-language-action/
- [ ] T088 Create Capstone content (Autonomous Humanoid) in docs/modules/capstone-autonomous-humanoid/
- [ ] T089 Draft Module 1 content with exercises/examples
- [ ] T090 Draft Module 2 content with exercises/examples
- [ ] T091 Draft Module 3 content with exercises/examples
- [ ] T092 Draft Module 4 content with exercises/examples
- [ ] T093 Draft Capstone content with exercises/examples
- [ ] T094 Refine Module 1–4 and Capstone content
- [ ] T095 Create Urdu translation for all modules and Capstone
- [ ] T096 RAG index content for all modules and Capstone
- [ ] T097 Update Docusaurus sidebar with modules, chapters, and Capstone

---

## Phase 9: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T098 [P] Documentation updates in docs/
- [ ] T099 Code cleanup and refactoring
- [ ] T100 Performance optimization across all stories
- [ ] T101 Additional unit tests (if requested) in tests/unit/
- [ ] T102 Security hardening
- [ ] T103 Run quickstart.md validation
- [ ] T104 Accessibility audit and fixes
- [ ] T105 UI/UX consistency review
- [ ] T106 Performance testing and optimization
- [ ] T107 Content accuracy verification
- [ ] T108 Final validation checklist

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Content Creation (Phase 8)**: Depends on foundational and US1-5 completion
- **Polish (Final Phase)**: Depends on all desired user stories and content being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1-2 but should be independently testable
- **User Story 4 (P1)**: Can start after Foundational (Phase 2) - Integrates with US1 functionality
- **User Story 5 (P1)**: Can start after Foundational (Phase 2) - May integrate with US1-4 but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members
- Content creation for different modules can run in parallel after foundational work is complete

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together (if tests requested):
Task: "Contract test for user registration endpoint in tests/contract/test_auth.py"
Task: "Integration test for user profile creation in tests/integration/test_user_profile.py"

# Launch all models for User Story 1 together:
Task: "Create User Profile model in rag-backend/models/user_profile.py"
Task: "Create Module model in rag-backend/models/module.py"
Task: "Create Chapter model in rag-backend/models/chapter.py"
```

---

## Implementation Strategy

### MVP First (User Stories 1-4 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. Complete Phase 4: User Story 2
5. Complete Phase 5: User Story 3
6. Complete Phase 6: User Story 4
7. **STOP and VALIDATE**: Test all user stories independently and together
8. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Stories 1-4 → Test independently and together → Deploy/Demo (MVP!)
3. Add User Story 5 → Enhanced UI/UX → Test and deploy
4. Add Content Modules → Test and deploy
5. Each addition adds value without breaking previous functionality

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
   - Developer E: User Story 5
3. After user stories complete, begin content creation in parallel
4. Modules can be worked on simultaneously by different team members

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
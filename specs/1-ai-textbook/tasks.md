---
description: "Task list for Physical AI & Humanoid Robotics Textbook - All Modules and Capstone"
---

# Tasks: Physical AI & Humanoid Robotics — AI-Native Textbook

**Input**: Design documents from `/specs/1-ai-textbook/`
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

- [X] T001 Create project structure per implementation plan in root directory
- [X] T002 Initialize Docusaurus project in Docusaurus/ with required dependencies
- [X] T003 [P] Initialize FastAPI backend project in rag-backend/ with required dependencies
- [X] T004 [P] Set up git repository with proper ignore files (.gitignore for Python, Node, etc.)
- [X] T005 Setup CI/CD workflows in .github/workflows/

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

Examples of foundational tasks (adjust based on your project):

- [X] T006 Setup database schema and migrations framework for Neon Postgres
- [X] T007 [P] Implement authentication/authorization framework using Better-Auth
- [X] T008 [P] Setup API routing and middleware structure in rag-backend/
- [X] T009 Create base models/entities that all stories depend on (User Profile, Module, Chapter)
- [X] T010 Configure error handling and logging infrastructure
- [X] T011 Setup environment configuration management for both frontend and backend
- [X] T012 Setup Qdrant client and connection infrastructure
- [X] T013 Create base components for personalization and translation in src/
- [X] T014 Implement personalization engine in src/personalization/engine.js
- [X] T015 Implement translation engine in src/translation/engine.js
- [X] T016 Implement RAG agent in rag-backend/agents/rag_agent.py
- [X] T017 Implement chunking logic in rag-backend/embeddings/chunker.py
- [X] T018 Implement indexer for content in rag-backend/embeddings/indexer.py
- [X] T019 Setup Claude Code subagents configuration

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Access Personalized Textbook Content (Priority: P1) 🎯 MVP

**Goal**: Enable textbooks that adapt to user's background and learning preferences

**Independent Test**: Can be fully tested by registering with different background information and verifying that the content variants adjust appropriately (beginner vs. advanced versions).

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [X] T020 [P] [US1] Contract test for user registration endpoint in tests/contract/test_auth.py
- [X] T021 [P] [US1] Integration test for user profile creation in tests/integration/test_user_profile.py

### Implementation for User Story 1

- [X] T022 [P] [US1] Create User Profile model in rag-backend/models/user_profile.py
- [X] T023 [P] [US1] Create Module model in rag-backend/models/module.py
- [X] T024 [P] [US1] Create Chapter model in rag-backend/models/chapter.py
- [X] T025 [US1] Implement User Profile service in rag-backend/services/user_profile_service.py
- [X] T026 [US1] Implement Chapter service in rag-backend/services/chapter_service.py
- [X] T027 [US1] Create Docusaurus component for personalization in Docusaurus/src/components/PersonalizationButton/index.js
- [X] T028 [US1] Implement personalization API endpoint in rag-backend/api/endpoints/personalization.py
- [X] T029 [US1] Add difficulty filtering logic to chapter retrieval
- [X] T030 [US1] Add logging for user story 1 operations
- [X] T031 [US1] Implement progress tracking in User Profile model and service

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Query Textbook with AI Assistant (Priority: P1)

**Goal**: Provide AI-powered Q&A functionality with textbook content

**Independent Test**: Can be fully tested by asking various questions about the textbook content and verifying that the AI assistant provides accurate answers based on the indexed material.

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [X] T032 [P] [US2] Contract test for ask endpoint in tests/contract/test_qa_api.py
- [X] T033 [P] [US2] Contract test for ask selection endpoint in tests/contract/test_qa_api.py
- [X] T034 [P] [US2] Integration test for RAG system in tests/integration/test_rag.py

### Implementation for User Story 2

- [X] T035 [P] [US2] Create AI Assistant Session model in rag-backend/models/session.py
- [X] T036 [P] [US2] Create Content Chunk model in rag-backend/models/content_chunk.py
- [X] T037 [US2] Implement Qdrant connector in rag-backend/db/qdrant_connector.py
- [X] T038 [US2] Implement main endpoint for asking in rag-backend/api/endpoints/ask.py
- [X] T039 [US2] Implement endpoint for asking from selection in rag-backend/api/endpoints/ask_selection.py
- [X] T040 [US2] Implement chat history endpoint in rag-backend/api/endpoints/history.py
- [X] T041 [US2] Create QABot React component in Docusaurus/src/components/QABot/index.js
- [X] T042 [US2] Add accessibility testing for QABot component to ensure WCAG 2.1 AA compliance

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Access Textbook in Multiple Languages (Priority: P2)

**Goal**: Enable textbook access in multiple languages, specifically Urdu

**Independent Test**: Can be fully tested by switching between English and Urdu language options and verifying the content translates accurately while preserving technical terminology.

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [X] T043 [P] [US3] Contract test for translation endpoint in tests/contract/test_translation.py
- [X] T044 [P] [US3] Integration test for translation layer in tests/integration/test_translation.py

### Implementation for User Story 3

- [X] T045 [P] [US3] Create Translation Layer model in rag-backend/models/translation_layer.py
- [X] T046 [US3] Implement translation API endpoint in rag-backend/api/endpoints/translation.py
- [X] T047 [US3] Create TranslationToggle React component in Docusaurus/src/components/TranslationToggle/index.js
- [X] T048 [US3] Add translation preservation logic for code and technical terms
- [X] T049 [US3] Implement Urdu language support in the personalization engine

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: User Story 4 - Navigate Through Structured Robotics Curriculum (Priority: P1)

**Goal**: Enable users to follow a structured curriculum that builds knowledge systematically from ROS 2 fundamentals to advanced concepts

**Independent Test**: Can be fully tested by navigating through the curriculum modules sequentially and verifying that each builds appropriately on previous knowledge.

### Tests for User Story 4 (OPTIONAL - only if tests requested) ⚠️

- [X] T050 [P] [US4] Contract test for module navigation endpoints in tests/contract/test_curriculum.py
- [X] T051 [P] [US4] Integration test for progress tracking in tests/integration/test_progress.py

### Implementation for User Story 4

- [X] T052 [US4] Create curriculum navigation API endpoints in rag-backend/api/endpoints/curriculum.py
- [X] T053 [US4] Add progress tracking functionality to Chapter service
- [X] T054 [US4] Create module navigation UI in Docusaurus
- [X] T055 [US4] Implement logic to enforce prerequisite completion

**Checkpoint**: All user stories now complete and integrated

---

## Phase 7: Module 1 Creation - The Robotic Nervous System (ROS 2)

**Goal**: Create the content for Module 1 on ROS 2 fundamentals

### Implementation for Module 1

- [X] T056 Create directory structure for module in docs/modules/module1-the-robotic-nervous-system/
- [X] T057 Generate chapter outline using Claude Code in docs/modules/module1-the-robotic-nervous-system/outline.md (m1-t1)
- [X] T058 Write full chapter draft with ROS 2 concepts, nodes, topics, services in docs/modules/module1-the-robotic-nervous-system/chapter-draft.md (m1-t2)
- [X] T059 Refine chapter content for clarity and pedagogical value in docs/modules/module1-the-robotic-nervous-system/chapter-refined.md (m1-t3)
- [X] T060 Generate Urdu translation of chapter content in docs/modules/module1-the-robotic-nervous-system/chapter-urdu.md (m1-t4)
- [X] T061 Process chapter through RAG indexing (chunking and embedding) in rag-backend/ (m1-t5)
- [X] T062 Create beginner, intermediate, and advanced content variants based on user skill level (m1-t6)
- [X] T063 Run Spec-Kit Plus tests for content structure, accessibility, and code correctness (m1-t7)
- [X] T064 Deploy chapter to Docusaurus and verify rendering, personalization, and translation buttons (m1-t8)
- [X] T065 Update Docusaurus sidebar to include new chapter

---

## Phase 8: Module 2 Creation - Digital Twins (Gazebo + Unity)

**Goal**: Create the content for Module 2 on Digital Twins

### Implementation for Module 2

- [X] T066 Create directory structure for module in docs/modules/module2-digital-twins/
- [X] T067 Generate chapter outline using Claude Code in docs/modules/module2-digital-twins/outline.md (m2-t1)
- [X] T068 Write full chapter draft with Gazebo physics, Unity rendering, and sensor simulations in docs/modules/module2-digital-twins/chapter-draft.md (m2-t2)
- [X] T069 Refine chapter content for clarity and pedagogical value in docs/modules/module2-digital-twins/chapter-refined.md (m2-t3)
- [X] T070 Generate Urdu translation of chapter content in docs/modules/module2-digital-twins/chapter-urdu.md (m2-t4)
- [X] T071 Process chapter through RAG indexing (chunking and embedding) in rag-backend/ (m2-t5)
- [X] T072 Create beginner, intermediate, and advanced content variants based on user skill level (m2-t6)
- [X] T073 Run Spec-Kit Plus tests for content structure, accessibility, and code correctness (m2-t7)
- [X] T074 Deploy chapter to Docusaurus and verify rendering, personalization, and translation buttons (m2-t8)
- [X] T075 Update Docusaurus sidebar to include new chapter

---

## Phase 9: Module 3 Creation - AI-Robot Brain (NVIDIA Isaac)

**Goal**: Create the content for Module 3 on AI-Robot Brain

### Implementation for Module 3

- [X] T076 Create directory structure for module in docs/modules/module3-ai-robot-brain/
- [X] T077 Generate chapter outline using Claude Code in docs/modules/module3-ai-robot-brain/outline.md (m3-t1)
- [X] T078 Write full chapter draft with Isaac Sim, Isaac ROS, VSLAM, Nav2 path planning in docs/modules/module3-ai-robot-brain/chapter-draft.md (m3-t2)
- [X] T079 Refine chapter content for clarity and pedagogical value in docs/modules/module3-ai-robot-brain/chapter-refined.md (m3-t3)
- [X] T080 Generate Urdu translation of chapter content in docs/modules/module3-ai-robot-brain/chapter-urdu.md (m3-t4)
- [X] T081 Process chapter through RAG indexing (chunking and embedding) in rag-backend/ (m3-t5)
- [X] T082 Create beginner, intermediate, and advanced content variants based on user skill level (m3-t6)
- [X] T083 Run Spec-Kit Plus tests for content structure, accessibility, and code correctness (m3-t7)
- [X] T084 Deploy chapter to Docusaurus and verify rendering, personalization, and translation buttons (m3-t8)
- [X] T085 Update Docusaurus sidebar to include new chapter

---

## Phase 10: Module 4 Creation - Vision-Language-Action (VLA)

**Goal**: Create the content for Module 4 on Vision-Language-Action

### Implementation for Module 4

- [X] T086 Create directory structure for module in docs/modules/module4-vision-language-action/
- [X] T087 Generate chapter outline using Claude Code in docs/modules/module4-vision-language-action/outline.md (m4-t1)
- [X] T088 Write full chapter draft with Whisper voice input, LLM planning, ROS2 action graphs in docs/modules/module4-vision-language-action/chapter-draft.md (m4-t2)
- [X] T089 Refine chapter content for clarity and pedagogical value in docs/modules/module4-vision-language-action/chapter-refined.md (m4-t3)
- [X] T090 Generate Urdu translation of chapter content in docs/modules/module4-vision-language-action/chapter-urdu.md (m4-t4)
- [X] T091 Process chapter through RAG indexing (chunking and embedding) in rag-backend/ (m4-t5)
- [X] T092 Create beginner, intermediate, and advanced content variants based on user skill level (m4-t6)
- [X] T093 Run Spec-Kit Plus tests for content structure, accessibility, and code correctness (m4-t7)
- [X] T094 Deploy chapter to Docusaurus and verify rendering, personalization, and translation buttons (m4-t8)
- [X] T095 Update Docusaurus sidebar to include new chapter

---

## Phase 11: Capstone Creation - Autonomous Humanoid

**Goal**: Create the content for the capstone project

### Implementation for Capstone

- [X] T096 Create directory structure for capstone in docs/modules/capstone-autonomous-humanoid/
- [X] T097 Generate capstone outline using Claude Code in docs/modules/capstone-autonomous-humanoid/outline.md (capstone-t1)
- [X] T098 Write full capstone draft with voice-to-action, object recognition, navigation, and integration in docs/modules/capstone-autonomous-humanoid/chapter-draft.md (capstone-t2)
- [X] T099 Refine capstone content for clarity and pedagogical value in docs/modules/capstone-autonomous-humanoid/chapter-refined.md (capstone-t3)
- [X] T100 Generate Urdu translation of capstone content in docs/modules/capstone-autonomous-humanoid/chapter-urdu.md (capstone-t4)
- [X] T101 Process capstone through RAG indexing (chunking and embedding) in rag-backend/ (capstone-t5)
- [X] T102 Create beginner, intermediate, and advanced content variants based on user skill level (capstone-t6)
- [X] T103 Run Spec-Kit Plus tests for content structure, accessibility, and code correctness (capstone-t7)
- [X] T104 Deploy capstone to Docusaurus and verify full integrations (capstone-t8)
- [X] T105 Update Docusaurus sidebar to include capstone chapter

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T106 [P] Documentation updates in docs/
- [X] T107 Code cleanup and refactoring
- [X] T108 Performance optimization across all stories
- [X] T109 [P] Additional unit tests (if requested) in tests/unit/
- [X] T110 Security hardening
- [X] T111 Run quickstart.md validation

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Module Creation Phases (7-11)**: Depends on foundational and US1-4 completion
- **Polish (Final Phase)**: Depends on all desired user stories and modules being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 4 (P1)**: Can start after Foundational (Phase 2) - Integrates with US1 functionality

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
- Module creation phases can potentially run in parallel after foundational work is complete

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
3. Add Module 1 → Test and deploy
4. Add Module 2 → Test and deploy
5. Add Module 3 → Test and deploy
6. Add Module 4 → Test and deploy
7. Add Capstone → Test and deploy
8. Each addition adds value without breaking previous functionality

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
3. After user stories complete, begin module creation in parallel
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
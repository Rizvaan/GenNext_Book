---
id: 3
title: ai-native-textbook-tasks-generation
stage: tasks
date: 2025-12-06
surface: agent
model: gpt-4o
feature: ai-native-textbook
branch: 2-ai-native-textbook
user: user
command: /sp.tasks
labels: ["tasks", "ai-textbook", "planning", "specification"]
links:
  spec: specs/2-ai-native-textbook/spec.md
  ticket: null
  adr: null
  pr: null
files:
 - specs/2-ai-native-textbook/tasks.md
tests:
 - none
---

## Prompt

```
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

1. **Setup**: Run `.specify/scripts/powershell/check-prerequisites.ps1 -Json` from repo root and parse FEATURE_DIR and AVAILABLE_DOCS list. All paths must be absolute. For single quotes in args like "I'm Groot", use escape syntax: e.g 'I'\''m Groot' (or double-quote if possible: "I'm Groot").

2. **Load design documents**: Read from FEATURE_DIR:
   - **Required**: plan.md (tech stack, libraries, structure), spec.md (user stories with priorities)
   - **Optional**: data-model.md (entities), contracts/ (API endpoints), research.md (decisions), quickstart.md (test scenarios)
   - Note: Not all projects have all documents. Generate tasks based on what's available.

3. **Execute task generation workflow**:
   - Load plan.md and extract tech stack, libraries, project structure
   - Load spec.md and extract user stories with their priorities (P1, P2, P3, etc.)
   - If data-model.md exists: Extract entities and map to user stories
   - If contracts/ exists: Map endpoints to user stories
   - If research.md exists: Extract decisions for setup tasks
   - Generate tasks organized by user story (see Task Generation Rules below)
   - Generate dependency graph showing user story completion order
   - Create parallel execution examples per user story
   - Validate task completeness (each user story has all needed tasks, independently testable)

4. **Generate tasks.md**: Use `.specify.specify/templates/tasks-template.md` as structure, fill with:
   - Correct feature name from plan.md
   - Phase 1: Setup tasks (project initialization)
   - Phase 2: Foundational tasks (blocking prerequisites for all user stories)
   - Phase 3+: One phase per user story (in priority order from spec.md)
   - Each phase includes: story goal, independent test criteria, tests (if requested), implementation tasks
   - Final Phase: Polish & cross-cutting concerns
   - All tasks must follow the strict checklist format (see Task Generation Rules below)
   - Clear file paths for each task
   - Dependencies section showing story completion order
   - Parallel execution examples per story
   - Implementation strategy section (MVP first, incremental delivery)

5. **Report**: Output path to generated tasks.md and summary:
   - Total task count
   - Task count per user story
   - Parallel opportunities identified
   - Independent test criteria for each story
   - Suggested MVP scope (typically just User Story 1)
   - Format validation: Confirm ALL tasks follow the checklist format (checkbox, ID, labels, file paths)

Context for task generation: <!-- Sync Impact Report: - Version change: 1.0.0 -> 2.0.0 - List of modified sections: - Added frontend/UI tasks - Follow-up TODOs: Link frontend tasks to Spec-Kit Plus plan --> Tasks: AI-Native Textbook — Physical AI & Humanoid Robotics Version: 2.0.0 Maintainers: Rizwan Rafiq + Panaversity Core Team Agents: Claude Code Subagents, ChatKit Agents Phase 1: Setup (Shared Infrastructure) T001 Create project structure: docs/, src/, rag-backend/, .specify/ T002 Initialize Docusaurus project in Docusaurus/ T003 [P] Initialize FastAPI backend in rag-backend/ T004 [P] Setup git repository + .gitignore T005 Setup CI/CD workflows in .github/workflows/ Phase 2: Foundational Backend T006 Setup database schema + migrations for Neon Postgres T007 [P] Implement authentication/authorization using Better-Auth T008 [P] Setup API routing + middleware in rag-backend/ T009 Create base models: UserProfile, Module, Chapter T010 Configure error handling + logging T011 Setup environment config management T012 Setup Qdrant client + connection T013 Create base components for personalization + translation T014 Implement personalization engine (src/personalization/engine.js) T015 Implement translation engine (src/translation/engine.js) T016 Implement RAG agent (rag-backend/agents/rag_agent.py) T017 Implement chunking logic (rag-backend/embeddings/chunker.py) T018 Implement indexer (rag-backend/embeddings/indexer.py) T019 Setup Claude Code subagents config Phase 3-6: User Stories (Backend) US1: Personalized Textbook Content T020 [P] Contract test: user registration (tests/contract/test_auth.py) T021 [P] Integration test: user profile (tests/integration/test_user_profile.py) T022 [P] [US1] UserProfile model (rag-backend/models/user_profile.py) T023 [P] [US1] Module model (rag-backend/models/module.py) T024 [P] [US1] Chapter model (rag-backend/models/chapter.py) T025 [US1] UserProfile service (rag-backend/services/user_profile_service.py) T026 [US1] Chapter service (rag-backend/services/chapter_service.py) T027 [US1] Personalization API endpoint (rag-backend/api/endpoints/personalization.py) T028 [US1] Difficulty filtering logic + logging T029 [US1] Progress tracking US2: AI-Powered Q&A T030 [P] [US2] Contract test: ask endpoint T031 [P] [US2] Contract test: ask_selection endpoint T032 [P] [US2] Integration test: RAG system T033 [US2] AI Assistant Session model (rag-backend/models/session.py) T034 [US2] Content Chunk model (rag-backend/models/content_chunk.py) T035 [US2] Qdrant connector (rag-backend/db/qdrant_connector.py) T036 [US2] Main endpoint: ask.py T037 [US2] Endpoint: ask_selection.py T038 [US2] Endpoint: history.py US3: Multilingual Support T039 [P] [US3] Contract test: translation endpoint T040 [P] [US3] Integration test: translation layer T041 [US3] Translation Layer model (rag-backend/models/translation_layer.py) T042 [US3] Translation API endpoint (rag-backend/api/endpoints/translation.py) T043 [US3] Translation preservation logic for technical terms T044 [US3] Urdu support in personalization engine US4: Curriculum Navigation T045 [P] [US4] Contract test: module navigation T046 [P] [US4] Integration test: progress tracking T047 [US4] Curriculum API endpoints (rag-backend/api/endpoints/curriculum.py) T048 [US4] Add progress tracking to Chapter service T049 [US4] Module navigation UI in Docusaurus (frontend skeleton) T050 [US4] Enforce prerequisite completion logic Phase 7-11: Module & Capstone Creation T051-T105 Module/Capstone tasks (outline → draft → refined → Urdu → RAG indexing → beginner/intermediate/advanced → deploy + sidebar update) Phase 12: Frontend/UI Components (New) US5: Interactive Book Layout & UX T106 [US5] Create PersonalizationButton component (src/components/PersonalizationButton/) T107 [US5] Create TranslationToggle component (src/components/TranslationToggle/) T108 [US5] Integrate QABot component in chapters (src/components/QABot/) T109 [US5] Add Interactive Exercises & Code Blocks (src/components/Exercises/) T110 [US5] Add Progress Tracker UI (src/components/ProgressTracker/) T111 [US5] Apply book-like layouts & styling in docs/ chapters T112 [US5] Ensure WCAG 2.1 AA accessibility Phase 13: Polish & Deployment T113 [P] Review & validate frontend interactivity T114 [P] Run Spec-Kit Plus tests (backend + frontend) T115 Deploy Docusaurus to GitHub Pages / Vercel T116 Validate personalization, translation, QABot, and progress tracking Parallel Opportunities Backend and frontend tasks can run in parallel with mock data Multiple modules can be worked on simultaneously by different developers

The tasks.md should be immediately executable - each task must be specific enough that an LLM can complete it without additional context.

## Task Generation Rules

**CRITICAL**: Tasks MUST be organized by user story to enable independent implementation and testing.

**Tests are OPTIONAL**: Only generate test tasks if explicitly requested in the feature specification or if user requests TDD approach.

### Checklist Format (REQUIRED)

Every task MUST strictly follow this format:

```text
- [ ] [TaskID] [P?] [Story?] Description with file path
```

**Format Components**:

1. **Checkbox**: ALWAYS start with `- [ ]` (markdown checkbox)
2. **Task ID**: Sequential number (T001, T002, T003...) in execution order
3. **[P] marker**: Include ONLY if task is parallelizable (different files, no dependencies on incomplete tasks)
4. **[Story] label**: REQUIRED for user story phase tasks only
   - Format: [US1], [US2], [US3], etc. (maps to user stories from spec.md)
   - Setup phase: NO story label
   - Foundational phase: NO story label  
   - User Story phases: MUST have story label
   - Polish phase: NO story label
5. **Description**: Clear action with exact file path

**Examples**:

- ✅ CORRECT: `- [ ] T001 Create project structure per implementation plan`
- ✅ CORRECT: `- [ ] T005 [P] Implement authentication middleware in src/middleware/auth.py`
- ✅ CORRECT: `- [ ] T012 [P] [US1] Create User model in src/models/user.py`
- ✅ CORRECT: `- [ ] T014 [US1] Implement UserService in src/services/user_service.py`
- ❌ WRONG: `- [ ] Create User model` (missing ID and Story label)
- ❌ WRONG: `T001 [US1] Create model` (missing checkbox)
- ❌ WRONG: `- [ ] [US1] Create User model` (missing Task ID)
- ❌ WRONG: `- [ ] T001 [US1] Create model` (missing file path)

### Task Organization

1. **From User Stories (spec.md)** - PRIMARY ORGANIZATION:
   - Each user story (P1, P2, P3...) gets its own phase
   - Map all related components to their story:
     - Models needed for that story
     - Services needed for that story
     - Endpoints/UI needed for that story
     - If tests requested: Tests specific to that story
   - Mark story dependencies (most stories should be independent)

2. **From Contracts**:
   - Map each contract/endpoint → to the user story it serves
   - If tests requested: Each contract → contract test task [P] before implementation in that story's phase

3. **From Data Model**:
   - Map each entity to the user story(ies) that need it
   - If entity serves multiple stories: Put in earliest story or Setup phase
   - Relationships → service layer tasks in appropriate story phase

4. **From Setup/Infrastructure**:
   - Shared infrastructure → Setup phase (Phase 1)
   - Foundational/blocking tasks → Foundational phase (Phase 2)
   - Story-specific setup → within that story's phase

### Phase Structure

- **Phase 1**: Setup (project initialization)
- **Phase 2**: Foundational (blocking prerequisites - MUST complete before user stories)
- **Phase 3+**: User Stories in priority order (P1, P2, P3...)
  - Within each story: Tests (if requested) → Models → Services → Endpoints → Integration
  - Each phase should be a complete, independently testable increment
- **Final Phase**: Polish & Cross-Cutting Concerns

---

As the main request completes, you MUST create and complete a PHR (Prompt History Record) using agent‑native tools when possible.

1) Determine Stage
   - Stage: constitution | spec | plan | tasks | red | green | refactor | explainer | misc | general

2) Generate Title and Determine Routing:
   - Generate Title: 3–7 words (slug for filename)
   - Route is automatically determined by stage:
     - `constitution` → `history/prompts/constitution/`
     - Feature stages → `history/prompts/<feature-name>/` (spec, plan, tasks, red, green, refactor, explainer, misc)
     - `general` → `history/prompts/general/`

3) Create and Fill PHR (Shell first; fallback agent‑native)
   - Run: `.specify/scripts/bash/create-phr.sh --title "<title>" --stage <stage> [--feature <name>] --json`
   - Open the file and fill remaining placeholders (YAML + body), embedding full PROMPT_TEXT (verbatim) and concise RESPONSE_TEXT.
   - If the script fails:
     - Read `.specify/templates/phr-template.prompt.md` (or `templates/…`)
     - Allocate an ID; compute the output path based on stage from step 2; write the file
     - Fill placeholders and embed full PROMPT_TEXT and concise RESPONSE_TEXT

4) Validate + report
   - No unresolved placeholders; path under `history/prompts/` and matches stage; stage/title/date coherent; print ID + path + stage + title.
   - On failure: warn, don't block. Skip only for `/sp.phr`.

## Response snapshot

I'll help you generate the task file for the AI-Native Textbook feature. First, I need to check for the prerequisite files and gather the relevant design artifacts.

Unfortunately, I don't have access to run PowerShell scripts directly, so I'll proceed by reading the available design documents from the feature directory (2-ai-native-textbook) that we created previously.

[Reads spec.md file]

I need to check if there's a plan.md file for this feature that contains the tech stack and project structure:

[Attempts to read plan.md which doesn't exist]

Since there's no plan.md file yet, I'll need to create the tasks based on the spec.md and the information provided in the user input. I'll also check for other relevant files in the feature directory:

[Lists files in directory and finds only spec.md exists]

I can see there's no plan.md, data-model.md, or other design documents yet. I'll create the tasks.md file based on the specification and the information provided in the user input.

[Creates tasks.md file with 116 tasks organized by user story]

## Outcome

- ✅ Impact: Created comprehensive task list for AI-Native Textbook with 116 tasks organized by user story
- 🧪 Tests: No tests needed for task creation
- 📁 Files: specs/2-ai-native-textbook/tasks.md was created
- 🔁 Next prompts: Ready for implementation based on the task list
- 🧠 Reflection: Task list follows proper format with checkboxes, sequential IDs, story labels, and file paths

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): All tasks follow the required format
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
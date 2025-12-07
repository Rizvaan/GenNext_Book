---
id: 4
title: Create comprehensive tasks for ai textbook
stage: tasks
date: 2025-12-05
surface: agent
model: Qwen
feature: 1-ai-textbook
branch: 1-ai-textbook
user: user
command: /sp.tasks
labels: [tasks,ai-textbook,robotics,all-modules]
links:
  spec: specs/1-ai-textbook/spec.md
  plan: specs/1-ai-textbook/plan.md
  ticket: null
  adr: null
  pr: null
files:
 - specs/1-ai-textbook/tasks.md
tests:
 - none
---

## Prompt

```
---
description: Generate an actionable, dependency-ordered tasks.md for the feature based on available design artifacts.
---

## User Input

```text
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

Context for task generation: # sp.tasks - Physical AI & Humanoid Robotics Textbook version: 2.0.0 tasks: # ---------------- Module 1 ---------------- - id: m1-t1 name: "Generate Chapter Outline" agent: "claude-code" description: "Create detailed AI-native chapter outline with sections, RAG metadata." output: "module1_outline.md" dependencies: [] - id: m1-t2 name: "Write Full Chapter Draft" agent: "claude-code" description: "Generate full chapter content including ROS2 nodes, topics, services, URDF diagrams, code examples." output: "module1_draft.md" dependencies: ["m1-t1"] - id: m1-t3 name: "Rewrite and Improve Clarity" agent: "rewriter" description: "Enhance clarity, structure, tone of draft chapter." output: "module1_rewritten.md" dependencies: ["m1-t2"] - id: m1-t4 name: "Generate Urdu Translation" agent: "translator" description: "Translate chapter into Urdu, preserving code and technical terms." output: "module1_urdu.md" dependencies: ["m1-t3"] - id: m1-t5 name: "RAG Indexing" agent: "rag-indexer" description: "Chunk content for Qdrant embedding and retrieval." output: "module1_rag.json" dependencies: ["m1-t3"] - id: m1-t6 name: "Personalize Content Variants" agent: "claude-code" description: "Generate beginner, intermediate, and advanced variants." output: "module1_personalized.md" dependencies: ["m1-t3"] - id: m1-t7 name: "Test Chapter" agent: "tester" description: "Run tests for content structure, accessibility, code correctness, and RAG completeness." output: "module1_test_report.json" dependencies: ["m1-t3", "m1-t5", "m1-t6"] - id: m1-t8 name: "Deploy Chapter to Docusaurus" agent: "claude-code" description: "Publish chapter to docs/ and verify rendering, translation, and personalization." output: "module1_published.md" dependencies: ["m1-t3", "m1-t4", "m1-t6", "m1-t7"] # ---------------- Module 2 ---------------- - id: m2-t1 name: "Generate Chapter Outline" agent: "claude-code" description: "Create chapter outline for Digital Twins module." output: "module2_outline.md" dependencies: [] - id: m2-t2 name: "Write Full Chapter Draft" agent: "claude-code" description: "Generate full chapter including Gazebo physics, Unity rendering, and sensor simulations." output: "module2_draft.md" dependencies: ["m2-t1"] - id: m2-t3 name: "Rewrite and Improve Clarity" agent: "rewriter" description: "Enhance clarity and pedagogy." output: "module2_rewritten.md" dependencies: ["m2-t2"] - id: m2-t4 name: "Generate Urdu Translation" agent: "translator" description: "Translate content preserving technical accuracy." output: "module2_urdu.md" dependencies: ["m2-t3"] - id: m2-t5 name: "RAG Indexing" agent: "rag-indexer" description: "Chunk content for embeddings." output: "module2_rag.json" dependencies: ["m2-t3"] - id: m2-t6 name: "Personalize Content Variants" agent: "claude-code" description: "Create beginner, intermediate, and advanced variants." output: "module2_personalized.md" dependencies: ["m2-t3"] - id: m2-t7 name: "Test Chapter" agent: "tester" description: "Validate structure, accessibility, code, RAG." output: "module2_test_report.json" dependencies: ["m2-t3", "m2-t5", "m2-t6"] - id: m2-t8 name: "Deploy Chapter to Docusaurus" agent: "claude-code" description: "Publish chapter and verify integrations." output: "module2_published.md" dependencies: ["m2-t3", "m2-t4", "m2-t6", "m2-t7"] # ---------------- Module 3 ---------------- - id: m3-t1 name: "Generate Chapter Outline" agent: "claude-code" description: "Outline AI-Robot Brain (NVIDIA Isaac) module." output: "module3_outline.md" dependencies: [] - id: m3-t2 name: "Write Full Chapter Draft" agent: "claude-code" description: "Generate content with Isaac Sim, Isaac ROS, VSLAM, Nav2 path planning." output: "module3_draft.md" dependencies: ["m3-t1"] - id: m3-t3 name: "Rewrite and Improve Clarity" agent: "rewriter" description: "Improve teaching clarity and examples." output: "module3_rewritten.md" dependencies: ["m3-t2"] - id: m3-t4 name: "Generate Urdu Translation" agent: "translator" description: "Create Urdu variant preserving technical terms." output: "module3_urdu.md" dependencies: ["m3-t3"] - id: m3-t5 name: "RAG Indexing" agent: "rag-indexer" description: "Prepare content for RAG embedding." output: "module3_rag.json" dependencies: ["m3-t3"] - id: m3-t6 name: "Personalize Content Variants" agent: "claude-code" description: "Create personalized content variants." output: "module3_personalized.md" dependencies: ["m3-t3"] - id: m3-t7 name: "Test Chapter" agent: "tester" description: "Validate structure, accessibility, code, RAG." output: "module3_test_report.json" dependencies: ["m3-t3", "m3-t5", "m3-t6"] - id: m3-t8 name: "Deploy Chapter to Docusaurus" agent: "claude-code" description: "Publish module 3 and verify integrations." output: "module3_published.md" dependencies: ["m3-t3", "m3-t4", "m3-t6", "m3-t7"] # ---------------- Module 4 ---------------- - id: m4-t1 name: "Generate Chapter Outline" agent: "claude-code" description: "Outline Vision-Language-Action module." output: "module4_outline.md" dependencies: [] - id: m4-t2 name: "Write Full Chapter Draft" agent: "claude-code" description: "Generate content including Whisper voice input, LLM planning, ROS2 action graphs." output: "module4_draft.md" dependencies: ["m4-t1"] - id: m4-t3 name: "Rewrite and Improve Clarity" agent: "rewriter" description: "Enhance readability and structure." output: "module4_rewritten.md" dependencies: ["m4-t2"] - id: m4-t4 name: "Generate Urdu Translation" agent: "translator" description: "Create Urdu translation." output: "module4_urdu.md" dependencies: ["m4-t3"] - id: m4-t5 name: "RAG Indexing" agent: "rag-indexer" description: "Chunk and index content." output: "module4_rag.json" dependencies: ["m4-t3"] - id: m4-t6 name: "Personalize Content Variants" agent: "claude-code" description: "Generate beginner/intermediate/advanced variants." output: "module4_personalized.md" dependencies: ["m4-t3"] - id: m4-t7 name: "Test Chapter" agent: "tester" description: "Run Spec-Kit tests for structure, code, accessibility, and RAG." output: "module4_test_report.json" dependencies: ["m4-t3", "m4-t5", "m4-t6"] - id: m4-t8 name: "Deploy Chapter to Docusaurus" agent: "claude-code" description: "Publish module 4 and verify integrations." output: "module4_published.md" dependencies: ["m4-t3", "m4-t4", "m4-t6", "m4-t7"] # ---------------- Capstone ---------------- - id: capstone-t1 name: "Generate Capstone Outline" agent: "claude-code" description: "Create outline for Autonomous Humanoid capstone project." output: "capstone_outline.md" dependencies: [] - id: capstone-t2 name: "Write Capstone Chapter Draft" agent: "claude-code" description: "Generate full capstone content with voice-to-action, object recognition, navigation, and integration." output: "capstone_draft.md" dependencies: ["capstone-t1"] - id: capstone-t3 name: "Rewrite Capstone for Clarity" agent: "rewriter" description: "Improve readability and structure of capstone." output: "capstone_rewritten.md" dependencies: ["capstone-t2"] - id: capstone-t4 name: "Generate Urdu Translation" agent: "translator" description: "Translate capstone into Urdu preserving technical accuracy." output: "capstone_urdu.md" dependencies: ["capstone-t3"] - id: capstone-t5 name: "RAG Indexing" agent: "rag-indexer" description: "Chunk and index capstone content for Qdrant embeddings." output: "capstone_rag.json" dependencies: ["capstone-t3"] - id: capstone-t6 name: "Personalize Content Variants" agent: "claude-code" description: "Generate beginner, intermediate, and advanced capstone variants." output: "capstone_personalized.md" dependencies: ["capstone-t3"] - id: capstone-t7 name: "Test Capstone Chapter" agent: "tester" description: "Run tests for structure, code correctness, accessibility, and RAG completeness." output: "capstone_test_report.json" dependencies: ["capstone-t3", "capstone-t5", "capstone-t6"] - id: capstone-t8 name: "Deploy Capstone to Docusaurus" agent: "claude-code" description: "Publish capstone chapter and verify full integrations." output: "capstone_published.md" dependencies: ["capstone-t3", "capstone-t4", "capstone-t6", "capstone-t7"]

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
```

## Response snapshot

I have successfully generated a comprehensive tasks.md file for the Physical AI & Humanoid Robotics Textbook project, incorporating all modules and the capstone. The tasks are organized according to the specifications and requirements from the design artifacts.

## Outcome

- ✅ Impact: Created comprehensive task list with 111 individual tasks covering all modules and user stories
- 🧪 Tests: Identified optional test tasks that can be implemented based on requirements
- 📁 Files: Updated specs/1-ai-textbook/tasks.md with properly structured tasks for all modules
- 🔁 Next prompts: Ready for task execution following the dependency-ordered structure
- 🧠 Reflection: Successfully organized tasks by user stories and modules with proper phase structure and parallel execution opportunities

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): Not applicable
- Prompt variant (if applicable): Not applicable
- Next experiment (smallest change to try): Not applicable
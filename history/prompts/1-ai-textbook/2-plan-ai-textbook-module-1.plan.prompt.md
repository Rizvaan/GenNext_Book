---
id: 2
title: Plan ai textbook module 1
stage: plan
date: 2025-12-05
surface: agent
model: Qwen
feature: 1-ai-textbook
branch: 1-ai-textbook
user: user
command: /sp.plan
labels: [plan,ai-textbook,robotics,module1]
links:
  spec: specs/1-ai-textbook/spec.md
  ticket: null
  adr: null
  pr: null
files:
 - specs/1-ai-textbook/plan.md
 - specs/1-ai-textbook/research.md
 - specs/1-ai-textbook/data-model.md
 - specs/1-ai-textbook/quickstart.md
 - specs/1-ai-textbook/contracts/qa-service-api-contract.md
tests:
 - none
---

## Prompt

```
---
description: Execute the implementation planning workflow using the plan template to generate design artifacts.
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

1. **Setup**: Run `.specify/scripts/powershell/setup-plan.ps1 -Json` from repo root and parse JSON for FEATURE_SPEC, IMPL_PLAN, SPECS_DIR, BRANCH. For single quotes in args like "I'm Groot", use escape syntax: e.g 'I'\''m Groot' (or double-quote if possible: "I'm Groot").

2. **Load context**: Read FEATURE_SPEC and `.specify/memory/constitution.md`. Load IMPL_PLAN template (already copied).

3. **Execute plan workflow**: Follow the structure in IMPL_PLAN template to:
   - Fill Technical Context (mark unknowns as "NEEDS CLARIFICATION")
   - Fill Constitution Check section from constitution
   - Evaluate gates (ERROR if violations unjustified)
   - Phase 0: Generate research.md (resolve all NEEDS CLARIFICATION)
   - Phase 1: Generate data-model.md, contracts/, quickstart.md
   - Phase 1: Update agent context by running the agent script
   - Re-evaluate Constitution Check post-design

4. **Stop and report**: Command ends after Phase 2 planning. Report branch, IMPL_PLAN path, and generated artifacts.

## Phases

### Phase 0: Outline & Research

1. **Extract unknowns from Technical Context** above:
   - For each NEEDS CLARIFICATION → research task
   - For each dependency → best practices task
   - For each integration → patterns task

2. **Generate and dispatch research agents**:

   ```text
   For each unknown in Technical Context:
     Task: "Research {unknown} for {feature context}"
   For each technology choice:
     Task: "Find best practices for {tech} in {domain}"
   ```

3. **Consolidate findings** in `research.md` using format:
   - Decision: [what was chosen]
   - Rationale: [why chosen]
   - Alternatives considered: [what else evaluated]

**Output**: research.md with all NEEDS CLARIFICATION resolved

### Phase 1: Design & Contracts

**Prerequisites:** `research.md` complete

1. **Extract entities from feature spec** → `data-model.md`:
   - Entity name, fields, relationships
   - Validation rules from requirements
   - State transitions if applicable

2. **Generate API contracts** from functional requirements:
   - For each user action → endpoint
   - Use standard REST/GraphQL patterns
   - Output OpenAPI/GraphQL schema to `/contracts/`

3. **Agent context update**:
   - Run `.specify/scripts/powershell/update-agent-context.ps1 -AgentType qwen`
   - These scripts detect which AI agent is in use
   - Update the appropriate agent-specific context file
   - Add only new technology from current plan
   - Preserve manual additions between markers

**Output**: data-model.md, /contracts/*, quickstart.md, agent-specific file

## Key rules

- Use absolute paths
- ERROR on gate failures or unresolved clarifications

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


/sp.plan # sp.plan - Physical AI & Humanoid Robotics Textbook
version: 2.0.0
module: module1
title: "The Robotic Nervous System (ROS 2)"
description: |
  This module introduces the robotic nervous system using ROS 2. 
  Students will learn nodes, topics, services, URDF, and agent integration.
workflow:
  - step: 1
    name: "Chapter Outline Generation"
    agent: "claude-code"
    deliverable: "chapter outline"
    instructions: |
      - Generate a detailed chapter outline for Module 1.
      - Include sections: Overview, Technical Explanation, Code Examples, Exercises, Mini-Projects.
      - Add RAG-ready metadata for each section.
      - Ensure AI-native formatting (chunkable, semantic headings).
  - step: 2
    name: "Chapter Draft Creation"
    agent: "claude-code"
    deliverable: "draft chapter"
    instructions: |
      - Use the approved outline to write full chapter content.
      - Include ROS2 Nodes, Topics, Services with example code in Python.
      - Explain URDF for humanoids.
      - Include diagrams as placeholders (to be rendered in Docusaurus).
      - Chunk content for RAG indexing (400 tokens, 50 token overlap).
  - step: 3
    name: "Subagent Task Assignment"
    agent: "subagents"
    deliverable: "specialized content"
    instructions: |
      - "chapter-writer": Enhance explanations for beginners.
      - "rewriter": Improve clarity, structure, and style.
      - "tester": Validate code examples for syntax correctness.
      - "rag-indexer": Prepare embeddings for Qdrant ingestion.
      - "translator": Generate Urdu translation variants.
  - step: 4
    name: "Personalization Layer"
    agent: "claude-code"
    deliverable: "personalized content variants"
    instructions: |
      - Create three variants based on user skill level: beginner, intermediate, advanced.
      - Adjust examples and exercises to match user background (hardware/software experience).
  - step: 5
    name: "Integration & Testing"
    agent: "tester"
    deliverable: "tested chapter"
    instructions: |
      - Run Spec-Kit Plus tests for content structure, links, accessibility.
      - Verify RAG indexing is complete and correct.
      - Ensure translation and personalization layers are properly generated.
  - step: 6
    name: "Docusaurus Deployment"
    agent: "claude-code"
    deliverable: "live chapter"
    instructions: |
      - Deploy chapter to docs/ using Docusaurus.ai.
      - Verify rendering, code blocks, diagrams, and AI-native formatting.
      - Confirm that personalization and translation buttons are functional.
```

## Response snapshot

I've successfully executed the implementation planning workflow for the Physical AI & Humanoid Robotics Textbook, Module 1. Here's what was accomplished:

1. **Setup phase**: Successfully ran the setup-plan PowerShell script which created the plan.md file and provided necessary paths.

2. **Context loading**: Read the feature specification and constitution files to understand requirements.

3. **Plan template completion**:
   - Filled the Technical Context section with project details
   - Completed the Constitution Check section, verifying alignment with all constitutional principles
   - Updated the Project Structure section with the planned directory structure
   - Added a summary and module-specific implementation details

4. **Phase 0 (Research)**: Created research.md with decisions on implementation approach, ROS 2 content, URDF focus, and agent integration.

5. **Phase 1 (Design & Contracts)**:
   - Created data-model.md with all necessary entities and relationships
   - Generated API contracts for the Q&A service in the contracts/ directory
   - Created a comprehensive quickstart.md guide for developers
   - Updated the agent context by running the update-agent-context script

All required artifacts have been successfully generated and the implementation plan is complete. The project is now ready for the next phase, which would typically be creating the detailed task list with `/sp.tasks`.

## Outcome

- ✅ Impact: Created comprehensive implementation plan and design artifacts for Module 1 of the AI-Native textbook
- 🧪 Tests: Created research, data models, contracts, and quickstart guide
- 📁 Files: Created/updated plan.md, research.md, data-model.md, quickstart.md, contracts/qa-service-api-contract.md; updated Qwen context
- 🔁 Next prompts: Ready for /sp.tasks to generate implementation tasks
- 🧠 Reflection: Successfully aligned implementation with constitutional requirements and project specifications

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): Not applicable
- Prompt variant (if applicable): Not applicable
- Next experiment (smallest change to try): Not applicable
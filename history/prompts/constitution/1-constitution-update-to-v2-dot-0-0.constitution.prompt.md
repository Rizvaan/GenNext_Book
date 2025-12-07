---
id: 1
title: constitution-update-to-v2-dot-0-0
stage: constitution
date: 2025-12-06
surface: agent
model: gpt-4o
feature: none
branch: main
user: user
command: /sp.constitution
labels: ["constitution", "governance", "template-sync"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
 - .specify/spec.json
 - .specify/templates/plan-template.md
 - .specify/templates/spec-template.md
 - .specify/templates/tasks-template.md
tests:
 - none
---

## Prompt

```
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

You are updating the project constitution at `.specify/memory/constitution.md`. This file is a TEMPLATE containing placeholder tokens in square brackets (e.g. `[PROJECT_NAME]`, `[PRINCIPLE_1_NAME]`). Your job is to (a) collect/derive concrete values, (b) fill the template precisely, and (c) propagate any amendments across dependent artifacts.

Follow this execution flow:

1. Load the existing constitution template at `.specify/memory/constitution.md`.
   - Identify every placeholder token of the form `[ALL_CAPS_IDENTIFIER]`.
   **IMPORTANT**: The user might require less or more principles than the ones used in the template. If a number is specified, respect that - follow the general template. You will update the doc accordingly.

2. Collect/derive values for placeholders:
   - If user input (conversation) supplies a value, use it.
   - Otherwise infer from existing repo context (README, docs, prior constitution versions if embedded).
   - For governance dates: `RATIFICATION_DATE` is the original adoption date (if unknown ask or mark TODO), `LAST_AMENDED_DATE` is today if changes are made, otherwise keep previous.
   - `CONSTITUTION_VERSION` must increment according to semantic versioning rules:
     - MAJOR: Backward incompatible governance/principle removals or redefinitions.
     - MINOR: New principle/section added or materially expanded guidance.
     - PATCH: Clarifications, wording, typo fixes, non-semantic refinements.
   - If version bump type ambiguous, propose reasoning before finalizing.

3. Draft the updated constitution content:
   - Replace every placeholder with concrete text (no bracketed tokens left except intentionally retained template slots that the project has chosen not to define yet—explicitly justify any left).
   - Preserve heading hierarchy and comments can be removed once replaced unless they still add clarifying guidance.
   - Ensure each Principle section: succinct name line, paragraph (or bullet list) capturing non‑negotiable rules, explicit rationale if not obvious.
   - Ensure Governance section lists amendment procedure, versioning policy, and compliance review expectations.

4. Consistency propagation checklist (convert prior checklist into active validations):
   - Read `.specify/templates/plan-template.md` and ensure any "Constitution Check" or rules align with updated principles.
   - Read `.specify/templates/spec-template.md` for scope/requirements alignment—update if constitution adds/removes mandatory sections or constraints.
   - Read `.specify/templates/tasks-template.md` and ensure task categorization reflects new or removed principle-driven task types (e.g., observability, versioning, testing discipline).
   - Read each command file in `.specify/templates/commands/*.md` (including this one) to verify no outdated references (agent-specific names like CLAUDE only) remain when generic guidance is required.
   - Read any runtime guidance docs (e.g., `README.md`, `docs/quickstart.md`, or agent-specific guidance files if present). Update references to principles changed.

5. Produce a Sync Impact Report (prepend as an HTML comment at top of the constitution file after update):
   - Version change: old → new
   - List of modified principles (old title → new title if renamed)
   - Added sections
   - Removed sections
   - Templates requiring updates (✅ updated / ⚠ pending) with file paths
   - Follow-up TODOs if any placeholders intentionally deferred.

6. Validation before final output:
   - No remaining unexplained bracket tokens.
   - Version line matches report.
   - Dates ISO format YYYY-MM-DD.
   - Principles are declarative, testable, and free of vague language ("should" → replace with MUST/SHOULD rationale where appropriate).

7. Write the completed constitution back to `.specify/memory/constitution.md` (overwrite).

8. Output a final summary to the user with:
   - New version and bump rationale.
   - Any files flagged for manual follow-up.
   - Suggested commit message (e.g., `docs: amend constitution to vX.Y.Z (principle additions + governance update)`).

Formatting & Style Requirements:

- Use Markdown headings exactly as in the template (do not demote/promote levels).
- Wrap long rationale lines to keep readability (<100 chars ideally) but do not hard enforce with awkward breaks.
- Keep a single blank line between sections.
- Avoid trailing whitespace.

If the user supplies partial updates (e.g., only one principle revision), still perform validation and version decision steps.

If critical info missing (e.g., ratification date truly unknown), insert `TODO(<FIELD_NAME>): explanation` and include in the Sync Impact Report under deferred items.

Do not create a new template; always operate on the existing `.specify/memory/constitution.md` file.

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


/sp.constitution <!-- 
Sync Impact Report: 
- Version change: 0.1.0 -> 2.0.0 
- List of modified principles: 
  - Complete rewrite of the constitution with 10 new sections
- Added sections: 
  - Purpose of This Constitution
  - Governance Rules
  - Versioning & Amendments
  - Core Principles (9 mandatory principles)
  - Technical Architecture Rules
  - Chapter Design Rules
  - Robotics Course Standards
  - Agent Systems
  - Directory Structure
  - Enforcement Rules
- Removed sections: 
  - Original template placeholders
- Templates requiring updates: 
  - ✅ .specify/templates/plan-template.md
  - ✅ .specify/templates/spec-template.md
  - ✅ .specify/templates/tasks-template.md
- Follow-up TODOs: None
--> 

# Constitution for the **AI-Native Textbook: Physical AI & Humanoid Robotics**

**Version:** 2.0.0  
**Ratified:** 2025-12-05  
**Last Amended:** 2025-12-05  
**Maintainers:**  
- **Primary Author:** *Rizwan Rafiq*  
- **Core Maintainers:** Panaversity Team (Zia, Rehan, Junaid, Wania)  
- **AI Agents:** Spec-Kit Plus Autonomous Agents, Claude Code Subagents, ChatKit Agents  

---

# 0. Purpose of This Constitution
This constitution defines the **governance**, **architecture**, **workflow**, and **automation rules** for the creation of the AI-Native textbook:

### **Physical AI & Humanoid Robotics**  
A foundational book designed using:
- **Docusaurus.ai** (Claude Code authoring mode)  
- **Spec-Kit Plus** for planning, specs, testing  
- **AI Agents** (Claude Code Subagents + ChatKit Agents)  
- **Integrated RAG systems** for interactive learning  

This constitution is the **supreme governing document** for this repository.  
All contributors — human or AI — MUST follow it exactly.

---

# 1. Governance Rules

## 1.1. Repository Purpose
This repository contains:
1. A fully AI-native textbook built using **Docusaurus.ai**  
2. Automated writing workflows using **Spec-Kit Plus**  
3. A complete RAG backend using:
   - OpenAI ChatKit Agents  
   - FastAPI  
   - Neon Serverless Postgres  
   - Qdrant Cloud  
4. Personalization + Translation engines  
5. Claude Code subagents for reusable intelligence  

## 1.2. Allowed Tools
The following tools are officially recognized:

### **Authoring & Automation**
- Docusaurus.ai  
- Spec-Kit Plus  
- Claude Code + Subagents  
- GitHub Actions CI/CD  

### **Backend**
- FastAPI  
- ChatKit/OpenAI Agents  
- Neon Serverless Postgres  
- Qdrant Cloud Free Tier  

### **Optional Bonus**
- Better-Auth (for signup/signin + user metadata)  
- Urdu Language Engine  
- Personalization Engine  

## 1.3. Authority Hierarchy
1. **This Constitution**
2. `.specify/spec.json` rules  
3. Chapter-level spec files  
4. AI Agents + builders  
5. Human maintainers (override only by amendment)

Human contributors **cannot violate** constitutional rules without submitting an amendment.

---

# 2. Versioning & Amendments

## 2.1. Semantic Versioning
- **MAJOR** — Breaking changes to workflow or structure  
- **MINOR** — New capabilities, principles, or systems  
- **PATCH** — Textual cleanup, wording fixes  

## 2.2. Amendment Process
1. Proposal created (`.specify/changes/proposal-XYZ.md`)  
2. 7-day review period  
3. Majority approval  
4. Version bump applied  

---

# 3. Core Principles (Mandatory)

## **3.1. AI-Native Content Architecture**
- All content MUST be machine-readable, modular, chunkable.  
- Headings, sections, examples, exercises MUST follow AI-native formatting.  
- Each chapter must include Metadata, Learning Outcomes, RAG-indexable sections.

## **3.2. Spec-Kit Plus Driven Book Production**
- Every chapter MUST originate from a **Spec-Kit Plus plan + spec + tasks** pipeline.  
- No chapter may be manually added without a spec.  
- Tests MUST be autogenerated using `.specify/tests`.

## **3.3. Docusaurus.ai as the Rendering Layer**
- All book content is stored in `docs/` and rendered via Docusaurus.  
- All layouts and UI components MUST support:
  - personalization button  
  - translation button  
  - "answer based on this selection" API  

## **3.4. Automated Quality Assurance**
- Every commit triggers:
  - spec validation  
  - link/testing checks  
  - RAG-index rebuild  
  - accessibility testing (WCAG 2.1 AA)  

## **3.5. RAG-Ready Knowledge Architecture**
- All content MUST be chunked for Qdrant ingestion.  
- Chunking rules: 300–500 token chunks with metadata:
  - chapter  
  - module  
  - tags  
  - difficulty  
  - version  

## **3.6. Personalization Engine**
The book MUST support personalization based on:
- user background  
- skill level  
- learning goals  
- hardware/software experience  

## **3.7. Urdu Translation Engine**
- Every chapter MUST support Urdu translation via:
  - a translation button  
  - a translation JSON layer  

## **3.8. Better-Auth Signup Flow**
At signup, the system MUST collect:
- software background  
- hardware experience  
- preferred language  
- learning style  
- robotics experience  

This data feeds the personalization engine.

## **3.9. Accessibility Requirements**
All content MUST meet **WCAG 2.1 AA** standards.

---

# 4. Technical Architecture Rules

## 4.1. RAG Backend Standards
The RAG system MUST use:

### **Database**
- Qdrant Cloud (vector DB)  
- Neon Postgres (metadata DB)  

### **Backend**
- FastAPI  
- ChatKit/OpenAI Agents  
- Functions:
  - `ask_book(question)`  
  - `ask_from_selection(question, selected_text)`  
  - `chat_history()`  

## 4.2. Deployment Rules
- Docusaurus deployed on GitHub Pages or Vercel  
- Backend deployed on:
  - Railway  
  - Fly.io  
  - Render  
  - or any free-tier server  

## 4.3. Indexing Rules
Index MUST be updated on:
- chapter creation  
- chapter edit  
- version bump  

---

# 5. Chapter Design Rules

Every chapter MUST include:

1. **Frontmatter Metadata**
2. **Learning Outcomes**
3. **AI-native structured sections**
4. **RAG-chunkable blocks**
5. **Code examples**
6. **Exercises**
7. **Mini-projects**
8. **Assessment questions**
9. **Glossary terms**
10. **Personalization-ready variants**

---

# 6. Robotics Course Standards (Content Rules)

The book MUST cover:

## **Module 1: Robotic Nervous System (ROS 2)**
- Nodes, Topics, Services  
- rclpy agent integration  
- URDF for humanoids  

## **Module 2: Digital Twin (Gazebo + Unity)**
- Physics simulation  
- Sensor simulation  
- High fidelity rendering  

## **Module 3: AI-Robot Brain (NVIDIA Isaac)**
- Isaac Sim  
- Isaac ROS  
- SLAM  
- Nav2  

## **Module 4: Vision-Language-Action (VLA)**
- Whisper voice commands  
- LLM planning  
- Action graph generation  

## **Capstone: Autonomous Humanoid**
- Voice command → planning → navigation → manipulation workflow  

---

# 7. Agent Systems

## 7.1. Claude Code Subagents
The repo MUST include reusable intelligence agents for:
- chapter writing  
- content rewriting  
- Urdu translation  
- indexing  
- testing  
- planning  

## 7.2. ChatKit Agents
These agents MUST:
- answer based only on book data  
- support queries with and without selection  
- maintain user history  

---

# 8. Directory Structure (Enforced)

/
├── constitution.md
├── docs/
│ ├── modules/
│ ├── chapters/
│ └── glossary/
├── src/
│ ├── components/
│ ├── personalization/
│ └── translation/
├── rag-backend/
│ ├── api/
│ ├── db/
│ ├── embeddings/
│ └── agents/
└── .specify/
├── spec.json
├── templates/
├── tests/
└── changes/


---

# 9. Enforcement Rules

## 9.1. Violations
Any violation of this constitution MUST block:
- merge  
- release  
- publish  

## 9.2. Responsibility
AI agents MUST correct violations automatically.

---

# 10. Closing Clause
This constitution defines the principles, practices, rules, and automations that make this project a **true Panaversity-grade AI-Native Textbook**.

All contributors — human or AI — MUST comply.
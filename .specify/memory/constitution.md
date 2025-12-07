<!--
Sync Impact Report:
- Version change: 2.0.0 -> 2.1.0
- Updated for: Frontend improvements, responsive design, multilingual support, book cover homepage, polished theme and UI/UX
-->

# Constitution for the **AI-Native Textbook: Physical AI & Humanoid Robotics**

**Version:** 2.1.0
**Ratified:** 2025-12-07
**Last Amended:** 2025-12-07
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
- **Multilingual content** (English + Urdu)
- **Book-like UI with responsive design**

This constitution is the **supreme governing document**. All contributors — human or AI — MUST follow it exactly.

---

# 1. Governance Rules

## 1.1. Repository Purpose
Contains:
1. AI-native textbook using **Docusaurus.ai**
2. Automated workflows via **Spec-Kit Plus**
3. RAG backend:
   - OpenAI ChatKit Agents
   - FastAPI
   - Neon Postgres
   - Qdrant Cloud
4. Personalization & translation engines
5. Book-like frontend with polished theme
6. Claude Code subagents for reusable intelligence

## 1.2. Allowed Tools

### **Authoring & Automation**
- Docusaurus.ai
- Spec-Kit Plus
- Claude Code + Subagents
- GitHub Actions CI/CD

### **Backend**
- FastAPI
- ChatKit/OpenAI Agents
- Neon Postgres
- Qdrant Cloud Free Tier

### **Frontend**
- React + Tailwind CSS
- Lucide / Tabler Icons
- Custom book-style components
- i18n / RTL support libraries

### **Optional Bonus**
- Better-Auth (signup/signin + user metadata)
- Urdu Language Engine
- Personalization Engine

## 1.3. Authority Hierarchy
1. **This Constitution**
2. `.specify/spec.json` rules
3. Chapter-level spec files
4. AI Agents + builders
5. Human maintainers (override only via amendment)

---

# 2. Versioning & Amendments

## 2.1. Semantic Versioning
- **MAJOR** — Breaking changes to workflow or structure
- **MINOR** — New capabilities, principles, or systems
- **PATCH** — Text cleanup, wording, theme/UI improvements

## 2.2. Amendment Process
1. Proposal created (`.specify/changes/proposal-XYZ.md`)
2. 7-day review
3. Majority approval
4. Version bump applied

---

# 3. Core Principles

## 3.1. AI-Native Content Architecture
- Modular, chunkable, AI-readable content.
- Includes metadata, learning outcomes, RAG-indexable sections.

## 3.2. Spec-Kit Plus Driven Book Production
- All chapters originate from Spec-Kit Plus plan + spec + tasks.

## 3.3. Docusaurus.ai as Rendering Layer
- Layouts/UI components MUST support:
  - Personalization button
  - Translation button
  - Book cover homepage
  - Responsive design
  - Interactive exercises

## 3.4. Automated Quality Assurance
- Commits trigger:
  - Spec validation
  - RAG indexing
  - Accessibility testing (WCAG 2.1 AA)
  - UI/UX and theme verification

## 3.5. RAG-Ready Knowledge Architecture
- Chunk 300–500 tokens with metadata (chapter, module, tags, difficulty, version).

## 3.6. Personalization Engine
- Adapts content based on:
  - User background
  - Skill level
  - Learning goals

## 3.7. Urdu Translation Engine
- Content toggle between English ↔ Urdu
- Correct RTL handling for Urdu

## 3.8. Better-Auth Signup Flow
- Collects:
  - Software/hardware background
  - Preferred language
  - Learning style

## 3.9. Accessibility & Responsiveness
- WCAG 2.1 AA standards
- Fully responsive: desktop, tablet, mobile

---

# 4. Technical Architecture Rules

## 4.1. RAG Backend Standards
- FastAPI, Qdrant Cloud, Neon Postgres
- Functions:
  - `ask_book(question)`
  - `ask_from_selection(question, selected_text)`
  - `chat_history()`

## 4.2. Deployment Rules
- Docusaurus: GitHub Pages / Vercel
- Backend: Railway / Fly.io / Render / free-tier

## 4.3. Indexing Rules
- Index updated on chapter creation/edit or version bump

---

# 5. Chapter Design Rules

Every chapter MUST include:

1. Metadata
2. Learning Outcomes
3. AI-native sections
4. RAG-chunkable blocks
5. Code examples
6. Exercises
7. Mini-projects
8. Assessment questions
9. Glossary terms
10. Personalization-ready variants
11. Translation-ready variants (English + Urdu)

---

# 6. Robotics Course Standards

Covers modules:

1. ROS 2 fundamentals
2. Digital Twin (Gazebo + Unity)
3. AI-Robot Brain (Isaac Sim/ROS)
4. Vision-Language-Action (Whisper + LLM + Action Graph)
5. Capstone: Autonomous Humanoid

---

# 7. Agent Systems

## 7.1. Claude Code Subagents
- Writing, rewriting, translation, indexing, testing, planning

## 7.2. ChatKit Agents
- AI Q&A based on textbook
- Maintains user history

---

# 8. Directory Structure

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
├── public/
│ └── images/ (book cover, illustrations)
└── .specify/
├── spec.json
├── templates/
├── tests/
└── changes/


---

# 9. Enforcement Rules

- Violations block merge/release/publish
- AI agents correct violations automatically

---

# 10. Closing Clause
Defines principles, practices, rules, automations that make this a **Panaversity-grade AI-Native Textbook**. All contributors — human or AI — MUST comply.
---
id: 1
title: Create ai textbook spec
stage: spec
date: 2025-12-05
surface: agent
model: Qwen
feature: 1-ai-textbook
branch: 1-ai-textbook
user: user
command: /sp.specify
labels: [spec,ai-textbook,robotics]
links:
  spec: specs/1-ai-textbook/spec.md
  ticket: null
  adr: null
  pr: null
files:
 - specs/1-ai-textbook/spec.md
 - specs/1-ai-textbook/checklists/requirements.md
tests:
 - none
---

## Prompt

```
---
description: Create or update the feature specification from a natural language feature description.
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

The text the user typed after `/sp.specify` in the triggering message **is** the feature description. Assume you always have it available in this conversation even if `{ "name": "Physical AI & Humanoid Robotics — AI-Native Textbook", "version": "2.0.0", "description": "A fully AI-native textbook built using Docusaurus.ai, Spec-Kit Plus, Claude Code, and OpenAI ChatKit Agents. This file defines the authoritative spec rules for automated writing, planning, content generation, testing, RAG indexing, translations, personalization, and robotics curriculum structure.", "governance": { "constitution": "constitution.md", "maintainers": [ "Rizwan Rafiq", "Panaversity Team" ], "aiAgents": { "enabled": true, "agents": [ "Claude Code Subagents", "Spec-Kit Orchestrator", "ChatKit RAG Agents" ] } }, "project": { "framework": "docusaurus.ai", "output": "docs/", "backend": "rag-backend/", "languages": ["en", "ur-PK"], "deployment": { "frontend": "GitHub Pages", "backend": "Railway/Fly.io", "databases": { "vector": "Qdrant Cloud", "postgres": "Neon Serverless Postgres" } } }, "bookStructure": { "modules": [ { "id": "module1", "title": "The Robotic Nervous System (ROS 2)", "chapters": [ "introduction-to-ros2", "nodes-topics-services", "urdf-for-humanoids", "python-agent-to-ros-controllers" ] }, { "id": "module2", "title": "Digital Twins (Gazebo + Unity)", "chapters": [ "gazebo-physics", "unity-rendering", "sensor-simulation", "digital-twin-design" ] }, { "id": "module3", "title": "AI-Robot Brain (NVIDIA Isaac)", "chapters": [ "isaac-sim-basics", "isaac-ros", "vslam", "nav2-path-planning" ] }, { "id": "module4", "title": "Vision-Language-Action (VLA)", "chapters": [ "whisper-voice-input", "llm-cognitive-planning", "ros2-action-graphs", "end-to-end-vla-systems" ] }, { "id": "capstone", "title": "Capstone: Autonomous Humanoid", "chapters": [ "voice-to-action-pipeline", "object-recognition", "navigation-obstacle-avoidance", "final-integration" ] } ], "supportFiles": ["glossary", "appendix", "assessment"] }, "specKit": { "templates": { "plan": ".specify/templates/plan-template.md", "spec": ".specify/templates/spec-template.md", "tasks": ".specify/templates/tasks-template.md" }, "defaults": { "priority": "high", "agent": "claude-code", "deliverable": "chapter" } }, "contentRules": { "aiNative": true, "chunking": { "enabled": true, "tokens": 400, "overlap": 50, "metadata": ["chapter", "module", "tags", "difficulty", "version"] }, "frontmatterRequired": true, "learningOutcomesRequired": true, "sections": [ "overview", "technical explanation", "code examples", "diagrams", "exercises", "mini projects", "assessment" ], "glossaryTerms": true, "wcagAccessibility": "2.1AA" }, "personalization": { "enabled": true, "strategy": "background-aware", "inputs": [ "software experience", "hardware experience", "robotics exposure", "preferred language", "learning pace", "career goals" ], "variants": [ "beginner version", "intermediate version", "advanced version" ] }, "translation": { "enabled": true, "languages": ["ur-PK"], "humanReadable": true, "rules": { "preserveCodeBlocks": true, "preserveTechnicalTerms": true, "createGlossaryAuto": true } }, "rag": { "enabled": true, "embeddingModel": "text-embedding-3-large", "vectorDB": "qdrant", "postgres": "neon", "indexOn": [ "chapter creation", "chapter update", "release" ], "api": { "ask": "/api/ask", "askSelection": "/api/ask/selection", "history": "/api/history" } }, "testing": { "specTests": true, "brokenLinkCheck": true, "spellcheck": true, "indexQualityCheck": true, "integrationTests": { "frontend": true, "backend": true }, "accessibility": true }, "agents": { "subagents": [ { "name": "chapter-writer", "role": "Generate full chapters from spec files" }, { "name": "rewriter", "role": "Enhance clarity, structure, tone" }, { "name": "translator", "role": "Generate Urdu variants" }, { "name": "rag-indexer", "role": "Chunk and index content in Qdrant" }, { "name": "tester", "role": "Run Spec-Kit tests" } ] }, "ci": { "onCommit": [ "validate-specs", "run-tests", "rebuild-rag-index", "deploy-preview" ], "onMergeMain": [ "full-build", "deploy-docs", "deploy-backend" ] } }` appears literally below. Do not ask the user to repeat it unless they provided an empty command.

Given that feature description, do this:

1. **Generate a concise short name** (2-4 words) for the branch:
   - Analyze the feature description and extract the most meaningful keywords
   - Create a 2-4 word short name that captures the essence of the feature
   - Use action-noun format when possible (e.g., "add-user-auth", "fix-payment-bug")
   - Preserve technical terms and acronyms (OAuth2, API, JWT, etc.)
   - Keep it concise but descriptive enough to understand the feature at a glance
   - Examples:
     - "I want to add user authentication" → "user-auth"
     - "Implement OAuth2 integration for the API" → "oauth2-api-integration"
     - "Create a dashboard for analytics" → "analytics-dashboard"
     - "Fix payment processing timeout bug" → "fix-payment-timeout"

2. **Check for existing branches before creating new one**:
   
   a. First, fetch all remote branches to ensure we have the latest information:
      ```bash
      git fetch --all --prune
      ```
   
   b. Find the highest feature number across all sources for the short-name:
      - Remote branches: `git ls-remote --heads origin | grep -E 'refs/heads/[0-9]+-<short-name>$'`
      - Local branches: `git branch | grep -E '^[* ]*[0-9]+-<short-name>$'`
      - Specs directories: Check for directories matching `specs/[0-9]+-<short-name>`
   
   c. Determine the next available number:
      - Extract all numbers from all three sources
      - Find the highest number N
      - Use N+1 for the new branch number
   
   d. Run the script `.specify/scripts/powershell/create-new-feature.ps1 -Json "{ "name": "Physical AI & Humanoid Robotics — AI-Native Textbook", "version": "2.0.0", "description": "A fully AI-native textbook built using Docusaurus.ai, Spec-Kit Plus, Claude Code, and OpenAI ChatKit Agents. This file defines the authoritative spec rules for automated writing, planning, content generation, testing, RAG indexing, translations, personalization, and robotics curriculum structure.", "governance": { "constitution": "constitution.md", "maintainers": [ "Rizwan Rafiq", "Panaversity Team" ], "aiAgents": { "enabled": true, "agents": [ "Claude Code Subagents", "Spec-Kit Orchestrator", "ChatKit RAG Agents" ] } }, "project": { "framework": "docusaurus.ai", "output": "docs/", "backend": "rag-backend/", "languages": ["en", "ur-PK"], "deployment": { "frontend": "GitHub Pages", "backend": "Railway/Fly.io", "databases": { "vector": "Qdrant Cloud", "postgres": "Neon Serverless Postgres" } } }, "bookStructure": { "modules": [ { "id": "module1", "title": "The Robotic Nervous System (ROS 2)", "chapters": [ "introduction-to-ros2", "nodes-topics-services", "urdf-for-humanoids", "python-agent-to-ros-controllers" ] }, { "id": "module2", "title": "Digital Twins (Gazebo + Unity)", "chapters": [ "gazebo-physics", "unity-rendering", "sensor-simulation", "digital-twin-design" ] }, { "id": "module3", "title": "AI-Robot Brain (NVIDIA Isaac)", "chapters": [ "isaac-sim-basics", "isaac-ros", "vslam", "nav2-path-planning" ] }, { "id": "module4", "title": "Vision-Language-Action (VLA)", "chapters": [ "whisper-voice-input", "llm-cognitive-planning", "ros2-action-graphs", "end-to-end-vla-systems" ] }, { "id": "capstone", "title": "Capstone: Autonomous Humanoid", "chapters": [ "voice-to-action-pipeline", "object-recognition", "navigation-obstacle-avoidance", "final-integration" ] } ], "supportFiles": ["glossary", "appendix", "assessment"] }, "specKit": { "templates": { "plan": ".specify/templates/plan-template.md", "spec": ".specify/templates/spec-template.md", "tasks": ".specify/templates/tasks-template.md" }, "defaults": { "priority": "high", "agent": "claude-code", "deliverable": "chapter" } }, "contentRules": { "aiNative": true, "chunking": { "enabled": true, "tokens": 400, "overlap": 50, "metadata": ["chapter", "module", "tags", "difficulty", "version"] }, "frontmatterRequired": true, "learningOutcomesRequired": true, "sections": [ "overview", "technical explanation", "code examples", "diagrams", "exercises", "mini projects", "assessment" ], "glossaryTerms": true, "wcagAccessibility": "2.1AA" }, "personalization": { "enabled": true, "strategy": "background-aware", "inputs": [ "software experience", "hardware experience", "robotics exposure", "preferred language", "learning pace", "career goals" ], "variants": [ "beginner version", "intermediate version", "advanced version" ] }, "translation": { "enabled": true, "languages": ["ur-PK"], "humanReadable": true, "rules": { "preserveCodeBlocks": true, "preserveTechnicalTerms": true, "createGlossaryAuto": true } }, "rag": { "enabled": true, "embeddingModel": "text-embedding-3-large", "vectorDB": "qdrant", "postgres": "neon", "indexOn": [ "chapter creation", "chapter update", "release" ], "api": { "ask": "/api/ask", "askSelection": "/api/ask/selection", "history": "/api/history" } }, "testing": { "specTests": true, "brokenLinkCheck": true, "spellcheck": true, "indexQualityCheck": true, "integrationTests": { "frontend": true, "backend": true }, "accessibility": true }, "agents": { "subagents": [ { "name": "chapter-writer", "role": "Generate full chapters from spec files" }, { "name": "rewriter", "role": "Enhance clarity, structure, tone" }, { "name": "translator", "role": "Generate Urdu variants" }, { "name": "rag-indexer", "role": "Chunk and index content in Qdrant" }, { "name": "tester", "role": "Run Spec-Kit tests" } ] }, "ci": { "onCommit": [ "validate-specs", "run-tests", "rebuild-rag-index", "deploy-preview" ], "onMergeMain": [ "full-build", "deploy-docs", "deploy-backend" ] } }"` with the calculated number and short-name:
      - Pass `--number N+1` and `--short-name "your-short-name"` along with the feature description
      - Bash example: `.specify/scripts/powershell/create-new-feature.ps1 -Json "{ "name": "Physical AI & Humanoid Robotics — AI-Native Textbook", "version": "2.0.0", "description": "A fully AI-native textbook built using Docusaurus.ai, Spec-Kit Plus, Claude Code, and OpenAI ChatKit Agents. This file defines the authoritative spec rules for automated writing, planning, content generation, testing, RAG indexing, translations, personalization, and robotics curriculum structure.", "governance": { "constitution": "constitution.md", "maintainers": [ "Rizwan Rafiq", "Panaversity Team" ], "aiAgents": { "enabled": true, "agents": [ "Claude Code Subagents", "Spec-Kit Orchestrator", "ChatKit RAG Agents" ] } }, "project": { "framework": "docusaurus.ai", "output": "docs/", "backend": "rag-backend/", "languages": ["en", "ur-PK"], "deployment": { "frontend": "GitHub Pages", "backend": "Railway/Fly.io", "databases": { "vector": "Qdrant Cloud", "postgres": "Neon Serverless Postgres" } } }, "bookStructure": { "modules": [ { "id": "module1", "title": "The Robotic Nervous System (ROS 2)", "chapters": [ "introduction-to-ros2", "nodes-topics-services", "urdf-for-humanoids", "python-agent-to-ros-controllers" ] }, { "id": "module2", "title": "Digital Twins (Gazebo + Unity)", "chapters": [ "gazebo-physics", "unity-rendering", "sensor-simulation", "digital-twin-design" ] }, { "id": "module3", "title": "AI-Robot Brain (NVIDIA Isaac)", "chapters": [ "isaac-sim-basics", "isaac-ros", "vslam", "nav2-path-planning" ] }, { "id": "module4", "title": "Vision-Language-Action (VLA)", "chapters": [ "whisper-voice-input", "llm-cognitive-planning", "ros2-action-graphs", "end-to-end-vla-systems" ] }, { "id": "capstone", "title": "Capstone: Autonomous Humanoid", "chapters": [ "voice-to-action-pipeline", "object-recognition", "navigation-obstacle-avoidance", "final-integration" ] } ], "supportFiles": ["glossary", "appendix", "assessment"] }, "specKit": { "templates": { "plan": ".specify/templates/plan-template.md", "spec": ".specify/templates/spec-template.md", "tasks": ".specify/templates/tasks-template.md" }, "defaults": { "priority": "high", "agent": "claude-code", "deliverable": "chapter" } }, "contentRules": { "aiNative": true, "chunking": { "enabled": true, "tokens": 400, "overlap": 50, "metadata": ["chapter", "module", "tags", "difficulty", "version"] }, "frontmatterRequired": true, "learningOutcomesRequired": true, "sections": [ "overview", "technical explanation", "code examples", "diagrams", "exercises", "mini projects", "assessment" ], "glossaryTerms": true, "wcagAccessibility": "2.1AA" }, "personalization": { "enabled": true, "strategy": "background-aware", "inputs": [ "software experience", "hardware experience", "robotics exposure", "preferred language", "learning pace", "career goals" ], "variants": [ "beginner version", "intermediate version", "advanced version" ] }, "translation": { "enabled": true, "languages": ["ur-PK"], "humanReadable": true, "rules": { "preserveCodeBlocks": true, "preserveTechnicalTerms": true, "createGlossaryAuto": true } }, "rag": { "enabled": true, "embeddingModel": "text-embedding-3-large", "vectorDB": "qdrant", "postgres": "neon", "indexOn": [ "chapter creation", "chapter update", "release" ], "api": { "ask": "/api/ask", "askSelection": "/api/ask/selection", "history": "/api/history" } }, "testing": { "specTests": true, "brokenLinkCheck": true, "spellcheck": true, "indexQualityCheck": true, "integrationTests": { "frontend": true, "backend": true }, "accessibility": true }, "agents": { "subagents": [ { "name": "chapter-writer", "role": "Generate full chapters from spec files" }, { "name": "rewriter", "role": "Enhance clarity, structure, tone" }, { "name": "translator", "role": "Generate Urdu variants" }, { "name": "rag-indexer", "role": "Chunk and index content in Qdrant" }, { "name": "tester", "role": "Run Spec-Kit tests" } ] }, "ci": { "onCommit": [ "validate-specs", "run-tests", "rebuild-rag-index", "deploy-preview" ], "onMergeMain": [ "full-build", "deploy-docs", "deploy-backend" ] } }" --json --number 5 --short-name "user-auth" "Add user authentication"`
      - PowerShell example: `.specify/scripts/powershell/create-new-feature.ps1 -Json "{ "name": "Physical AI & Humanoid Robotics — AI-Native Textbook", "version": "2.0.0", "description": "A fully AI-native textbook built using Docusaurus.ai, Spec-Kit Plus, Claude Code, and OpenAI ChatKit Agents. This file defines the authoritative spec rules for automated writing, planning, content generation, testing, RAG indexing, translations, personalization, and robotics curriculum structure.", "governance": { "constitution": "constitution.md", "maintainers": [ "Rizwan Rafiq", "Panaversity Team" ], "aiAgents": { "enabled": true, "agents": [ "Claude Code Subagents", "Spec-Kit Orchestrator", "ChatKit RAG Agents" ] } }, "project": { "framework": "docusaurus.ai", "output": "docs/", "backend": "rag-backend/", "languages": ["en", "ur-PK"], "deployment": { "frontend": "GitHub Pages", "backend": "Railway/Fly.io", "databases": { "vector": "Qdrant Cloud", "postgres": "Neon Serverless Postgres" } } }, "bookStructure": { "modules": [ { "id": "module1", "title": "The Robotic Nervous System (ROS 2)", "chapters": [ "introduction-to-ros2", "nodes-topics-services", "urdf-for-humanoids", "python-agent-to-ros-controllers" ] }, { "id": "module2", "title": "Digital Twins (Gazebo + Unity)", "chapters": [ "gazebo-physics", "unity-rendering", "sensor-simulation", "digital-twin-design" ] }, { "id": "module3", "title": "AI-Robot Brain (NVIDIA Isaac)", "chapters": [ "isaac-sim-basics", "isaac-ros", "vslam", "nav2-path-planning" ] }, { "id": "module4", "title": "Vision-Language-Action (VLA)", "chapters": [ "whisper-voice-input", "llm-cognitive-planning", "ros2-action-graphs", "end-to-end-vla-systems" ] }, { "id": "capstone", "title": "Capstone: Autonomous Humanoid", "chapters": [ "voice-to-action-pipeline", "object-recognition", "navigation-obstacle-avoidance", "final-integration" ] } ], "supportFiles": ["glossary", "appendix", "assessment"] }, "specKit": { "templates": { "plan": ".specify/templates/plan-template.md", "spec": ".specify/templates/spec-template.md", "tasks": ".specify/templates/tasks-template.md" }, "defaults": { "priority": "high", "agent": "claude-code", "deliverable": "chapter" } }, "contentRules": { "aiNative": true, "chunking": { "enabled": true, "tokens": 400, "overlap": 50, "metadata": ["chapter", "module", "tags", "difficulty", "version"] }, "frontmatterRequired": true, "learningOutcomesRequired": true, "sections": [ "overview", "technical explanation", "code examples", "diagrams", "exercises", "mini projects", "assessment" ], "glossaryTerms": true, "wcagAccessibility": "2.1AA" }, "personalization": { "enabled": true, "strategy": "background-aware", "inputs": [ "software experience", "hardware experience", "robotics exposure", "preferred language", "learning pace", "career goals" ], "variants": [ "beginner version", "intermediate version", "advanced version" ] }, "translation": { "enabled": true, "languages": ["ur-PK"], "humanReadable": true, "rules": { "preserveCodeBlocks": true, "preserveTechnicalTerms": true, "createGlossaryAuto": true } }, "rag": { "enabled": true, "embeddingModel": "text-embedding-3-large", "vectorDB": "qdrant", "postgres": "neon", "indexOn": [ "chapter creation", "chapter update", "release" ], "api": { "ask": "/api/ask", "askSelection": "/api/ask/selection", "history": "/api/history" } }, "testing": { "specTests": true, "brokenLinkCheck": true, "spellcheck": true, "indexQualityCheck": true, "integrationTests": { "frontend": true, "backend": true }, "accessibility": true }, "agents": { "subagents": [ { "name": "chapter-writer", "role": "Generate full chapters from spec files" }, { "name": "rewriter", "role": "Enhance clarity, structure, tone" }, { "name": "translator", "role": "Generate Urdu variants" }, { "name": "rag-indexer", "role": "Chunk and index content in Qdrant" }, { "name": "tester", "role": "Run Spec-Kit tests" } ] }, "ci": { "onCommit": [ "validate-specs", "run-tests", "rebuild-rag-index", "deploy-preview" ], "onMergeMain": [ "full-build", "deploy-docs", "deploy-backend" ] } }" -Json -Number 5 -ShortName "user-auth" "Add user authentication"`
   
   **IMPORTANT**:
   - Check all three sources (remote branches, local branches, specs directories) to find the highest number
   - Only match branches/directories with the exact short-name pattern
   - If no existing branches/directories found with this short-name, start with number 1
   - You must only ever run this script once per feature
   - The JSON is provided in the terminal as output - always refer to it to get the actual content you're looking for
   - The JSON output will contain BRANCH_NAME and SPEC_FILE paths
   - For single quotes in args like "I'm Groot", use escape syntax: e.g 'I'\''m Groot' (or double-quote if possible: "I'm Groot")

3. Load `.specify/templates/spec-template.md` to understand required sections.

4. Follow this execution flow:

    1. Parse user description from Input
       If empty: ERROR "No feature description provided"
    2. Extract key concepts from description
       Identify: actors, actions, data, constraints
    3. For unclear aspects:
       - Make informed guesses based on context and industry standards
       - Only mark with [NEEDS CLARIFICATION: specific question] if:
         - The choice significantly impacts feature scope or user experience
         - Multiple reasonable interpretations exist with different implications
         - No reasonable default exists
       - **LIMIT: Maximum 3 [NEEDS CLARIFICATION] markers total**
       - Prioritize clarifications by impact: scope > security/privacy > user experience > technical details
    4. Fill User Scenarios & Testing section
       If no clear user flow: ERROR "Cannot determine user scenarios"
    5. Generate Functional Requirements
       Each requirement must be testable
       Use reasonable defaults for unspecified details (document assumptions in Assumptions section)
    6. Define Success Criteria
       Create measurable, technology-agnostic outcomes
       Include both quantitative metrics (time, performance, volume) and qualitative measures (user satisfaction, task completion)
       Each criterion must be verifiable without implementation details
    7. Identify Key Entities (if data involved)
    8. Return: SUCCESS (spec ready for planning)

5. Write the specification to SPEC_FILE using the template structure, replacing placeholders with concrete details derived from the feature description (arguments) while preserving section order and headings.

6. **Specification Quality Validation**: After writing the initial spec, validate it against quality criteria:

   a. **Create Spec Quality Checklist**: Generate a checklist file at `FEATURE_DIR/checklists/requirements.md` using the checklist template structure with these validation items:

      ```markdown
      # Specification Quality Checklist: [FEATURE NAME]
      
      **Purpose**: Validate specification completeness and quality before proceeding to planning
      **Created**: [DATE]
      **Feature**: [Link to spec.md]
      
      ## Content Quality
      
      - [ ] No implementation details (languages, frameworks, APIs)
      - [ ] Focused on user value and business needs
      - [ ] Written for non-technical stakeholders
      - [ ] All mandatory sections completed
      
      ## Requirement Completeness
      
      - [ ] No [NEEDS CLARIFICATION] markers remain
      - [ ] Requirements are testable and unambiguous
      - [ ] Success criteria are measurable
      - [ ] Success criteria are technology-agnostic (no implementation details)
      - [ ] All acceptance scenarios are defined
      - [ ] Edge cases are identified
      - [ ] Scope is clearly bounded
      - [ ] Dependencies and assumptions identified
      
      ## Feature Readiness
      
      - [ ] All functional requirements have clear acceptance criteria
      - [ ] User scenarios cover primary flows
      - [ ] Feature meets measurable outcomes defined in Success Criteria
      - [ ] No implementation details leak into specification
      
      ## Notes
      
      - Items marked incomplete require spec updates before `/sp.clarify` or `/sp.plan`
      ```

   b. **Run Validation Check**: Review the spec against each checklist item:
      - For each item, determine if it passes or fails
      - Document specific issues found (quote relevant spec sections)

   c. **Handle Validation Results**:

      - **If all items pass**: Mark checklist complete and proceed to step 6

      - **If items fail (excluding [NEEDS CLARIFICATION])**:
        1. List the failing items and specific issues
        2. Update the spec to address each issue
        3. Re-run validation until all items pass (max 3 iterations)
        4. If still failing after 3 iterations, document remaining issues in checklist notes and warn user

      - **If [NEEDS CLARIFICATION] markers remain**:
        1. Extract all [NEEDS CLARIFICATION: ...] markers from the spec
        2. **LIMIT CHECK**: If more than 3 markers exist, keep only the 3 most critical (by scope/security/UX impact) and make informed guesses for the rest
        3. For each clarification needed (max 3), present options to user in this format:

           ```markdown
           ## Question [N]: [Topic]
           
           **Context**: [Quote relevant spec section]
           
           **What we need to know**: [Specific question from NEEDS CLARIFICATION marker]
           
           **Suggested Answers**:
           
           | Option | Answer | Implications |
           |--------|--------|--------------|
           | A      | [First suggested answer] | [What this means for the feature] |
           | B      | [Second suggested answer] | [What this means for the feature] |
           | C      | [Third suggested answer] | [What this means for the feature] |
           | Custom | Provide your own answer | [Explain how to provide custom input] |
           
           **Your choice**: _[Wait for user response]_
           ```

        4. **CRITICAL - Table Formatting**: Ensure markdown tables are properly formatted:
           - Use consistent spacing with pipes aligned
           - Each cell should have spaces around content: `| Content |` not `|Content|`
           - Header separator must have at least 3 dashes: `|--------|`
           - Test that the table renders correctly in markdown preview
        5. Number questions sequentially (Q1, Q2, Q3 - max 3 total)
        6. Present all questions together before waiting for responses
        7. Wait for user to respond with their choices for all questions (e.g., "Q1: A, Q2: Custom - [details], Q3: B")
        8. Update the spec by replacing each [NEEDS CLARIFICATION] marker with the user's selected or provided answer
        9. Re-run validation after all clarifications are resolved

   d. **Update Checklist**: After each validation iteration, update the checklist file with current pass/fail status

7. Report completion with branch name, spec file path, checklist results, and readiness for the next phase (`/sp.clarify` or `/sp.plan`).

**NOTE:** The script creates and checks out the new branch and initializes the spec file before writing.

## General Guidelines

## Quick Guidelines

- Focus on **WHAT** users need and **WHY**.
- Avoid HOW to implement (no tech stack, APIs, code structure).
- Written for business stakeholders, not developers.
- DO NOT create any checklists that are embedded in the spec. That will be a separate command.

### Section Requirements

- **Mandatory sections**: Must be completed for every feature
- **Optional sections**: Include only when relevant to the feature
- When a section doesn't apply, remove it entirely (don't leave as "N/A")

### For AI Generation

When creating this spec from a user prompt:

1. **Make informed guesses**: Use context, industry standards, and common patterns to fill gaps
2. **Document assumptions**: Record reasonable defaults in the Assumptions section
3. **Limit clarifications**: Maximum 3 [NEEDS CLARIFICATION] markers - use only for critical decisions that:
   - Significantly impact feature scope or user experience
   - Have multiple reasonable interpretations with different implications
   - Lack any reasonable default
4. **Prioritize clarifications**: scope > security/privacy > user experience > technical details
5. **Think like a tester**: Every vague requirement should fail the "testable and unambiguous" checklist item
6. **Common areas needing clarification** (only if no reasonable default exists):
   - Feature scope and boundaries (include/exclude specific use cases)
   - User types and permissions (if multiple conflicting interpretations possible)
   - Security/compliance requirements (when legally/financially significant)
   - Authentication method: Standard session-based or OAuth2 for web apps
   - Integration patterns: RESTful APIs unless specified otherwise

**Examples of reasonable defaults** (don't ask about these):

- Data retention: Industry-standard practices for the domain
- Performance targets: Standard web/mobile app expectations unless specified
- Error handling: User-friendly messages with appropriate fallbacks
- Authentication method: Standard session-based or OAuth2 for web apps
- Integration patterns: RESTful APIs unless specified otherwise

### Success Criteria Guidelines

Success criteria must be:

1. **Measurable**: Include specific metrics (time, percentage, count, rate)
2. **Technology-agnostic**: No mention of frameworks, languages, databases, or tools
3. **User-focused**: Describe outcomes from user/business perspective, not system internals
4. **Verifiable**: Can be tested/validated without knowing implementation details

**Good examples**:

- "Users can complete checkout in under 3 minutes"
- "System supports 10,000 concurrent users"
- "95% of searches return results in under 1 second"
- "Task completion rate improves by 40%"

**Bad examples** (implementation-focused):

- "API response time is under 200ms" (too technical, use "Users see results instantly")
- "Database can handle 1000 TPS" (implementation detail, use user-facing metric)
- "React components render efficiently" (framework-specific)
- "Redis cache hit rate above 80%" (technology-specific)

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

I'll help you create a feature specification based on the detailed information provided. Let me start by analyzing the feature description and creating a concise short name for the branch.

Based on the description, this is about creating an AI-native textbook for Physical AI & Humanoid Robotics using Docusaurus.ai, Spec-Kit Plus, and various AI agents. A suitable short name would be "ai-textbook".

Now, I need to check for existing branches before creating a new one. Let me first see what branches exist:

I've successfully completed the feature specification creation. Here's a summary of what I did:

1. Created a new feature branch called "1-ai-textbook"
2. Created the required directory structure (specs/1-ai-textbook)
3. Generated a comprehensive specification document with:
   - Multiple user scenarios with priorities
   - Detailed functional requirements
   - Key entities identification
   - Measurable success criteria
4. Created a quality checklist as required

The specification is now ready for the next phase (either /sp.clarify or /sp.plan).

## Outcome

- ✅ Impact: Created feature branch and comprehensive spec for AI-native textbook project
- 🧪 Tests: Created requirements checklist for validation
- 📁 Files: Created specs/1-ai-textbook/spec.md and specs/1-ai-textbook/checklists/requirements.md
- 🔁 Next prompts: Ready for /sp.clarify or /sp.plan
- 🧠 Reflection: Successfully transformed detailed feature description into well-structured specification following all guidelines

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): Not applicable
- Prompt variant (if applicable): Not applicable
- Next experiment (smallest change to try): Not applicable
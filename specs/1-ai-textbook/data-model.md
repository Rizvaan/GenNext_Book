# Data Model: Physical AI & Humanoid Robotics Textbook

## Entities

### User Profile
- **id**: UUID (primary key)
- **email**: String (unique, required)
- **createdAt**: DateTime (required)
- **updatedAt**: DateTime (required)
- **softwareExperience**: Enum ["beginner", "intermediate", "advanced"]
- **hardwareExperience**: Enum ["none", "basic", "intermediate", "advanced"]
- **roboticsExposure**: Enum ["none", "basic", "intermediate", "advanced"]
- **preferredLanguage**: String (default: "en", supports "ur-PK")
- **learningPace**: Enum ["slow", "moderate", "fast"]
- **careerGoals**: Text (optional)
- **currentModule**: String (optional, references Module)
- **progress**: JSON (stores progress by chapter)

### Module
- **id**: String (primary key, e.g., "module1-the-robotic-nervous-system")
- **title**: String (required)
- **description**: Text (required)
- **order**: Integer (required, for curriculum sequence)
- **createdAt**: DateTime (required)
- **updatedAt**: DateTime (required)

### Chapter
- **id**: String (primary key)
- **moduleId**: String (foreign key to Module)
- **title**: String (required)
- **content**: Text (required, markdown format)
- **difficulty**: Enum ["beginner", "intermediate", "advanced"]
- **learningOutcomes**: JSON (list of learning outcomes)
- **tags**: JSON (list of tags for searchability)
- **version**: String (required, for tracking content updates)
- **createdAt**: DateTime (required)
- **updatedAt**: DateTime (required)

### AI Assistant Session
- **id**: UUID (primary key)
- **userId**: UUID (foreign key to User Profile, optional for anon users)
- **sessionId**: UUID (for tracking conversation context)
- **query**: Text (required)
- **response**: Text (required)
- **timestamp**: DateTime (required)
- **sourceContentIds**: JSON (list of content IDs used to generate response)
- **createdAt**: DateTime (required)

### Translation Layer
- **id**: String (primary key, format: "<chapter_id>:<language_code>")
- **chapterId**: String (foreign key to Chapter)
- **languageCode**: String (required, e.g., "ur-PK", "en")
- **translatedContent**: Text (required)
- **createdAt**: DateTime (required)
- **updatedAt**: DateTime (required)

### Content Chunk
- **id**: UUID (primary key)
- **chapterId**: String (foreign key to Chapter)
- **chunkOrder**: Integer (required, for reassembly)
- **content**: Text (required, 300-500 token chunks)
- **metadata**: JSON (chapter, module, tags, difficulty, version)
- **embeddingId**: String (ID in vector database)
- **createdAt**: DateTime (required)
- **updatedAt**: DateTime (required)

## Relationships
- User Profile (1) → (M) AI Assistant Session
- Module (1) → (M) Chapter
- Chapter (1) → (M) Content Chunk
- Chapter (1) → (M) Translation Layer (one chapter can have multiple translations)
# Data Model: AI-Native Textbook — Physical AI & Humanoid Robotics

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

### Exercise
- **id**: String (primary key)
- **chapterId**: String (foreign key to Chapter)
- **title**: String (required)
- **type**: Enum ["multiple-choice", "coding", "short-answer", "project"]
- **content**: Text (required)
- **solution**: Text (required, for auto-grading)
- **difficulty**: Enum ["beginner", "intermediate", "advanced"]
- **createdAt**: DateTime (required)
- **updatedAt**: DateTime (required)

### Progress Tracking
- **id**: UUID (primary key)
- **userId**: UUID (foreign key to User Profile)
- **chapterId**: String (foreign key to Chapter)
- **progressPercentage**: Integer (0-100, required)
- **lastAccessed**: DateTime (required)
- **completed**: Boolean (default: false)
- **createdAt**: DateTime (required)
- **updatedAt**: DateTime (required)

## Relationships
- User Profile (1) → (M) AI Assistant Session
- User Profile (1) → (M) Progress Tracking (across chapters)
- Module (1) → (M) Chapter
- Chapter (1) → (M) Content Chunk
- Chapter (1) → (M) Translation Layer (one chapter can have multiple translations)
- Chapter (1) → (M) Exercise
- User Profile (1) → (M) Progress Tracking
# Quickstart Guide: Physical AI & Humanoid Robotics Textbook

## Setting up the Development Environment

### Prerequisites
- Node.js 18+ (for Docusaurus frontend)
- Python 3.11+ (for backend services)
- Git SCM
- Access to OpenAI API (for AI assistant features)
- Access to Qdrant Cloud (for RAG functionality)

### 1. Clone the Repository
```bash
git clone <repository-url>
cd Nextgen_book
```

### 2. Set up the Frontend (Docusaurus)
```bash
# Navigate to the Docusaurus directory
cd Docusaurus

# Install dependencies
npm install

# Create environment file
cp .env.example .env

# Update .env with your API keys and configuration
# (See Configuration section below)
```

### 3. Set up the Backend (FastAPI)
```bash
# From the project root
cd rag-backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create environment file
cp .env.example .env

# Update .env with your API keys and configuration
# (See Configuration section below)
```

## Configuration

### Environment Variables
Create `.env` files in both the Docusaurus and rag-backend directories with the following variables:

#### For rag-backend/.env:
```env
OPENAI_API_KEY=your_openai_api_key
QDRANT_API_KEY=your_qdrant_api_key
QDRANT_URL=your_qdrant_cluster_url
NEON_DB_URL=your_neon_postgres_connection_string
SECRET_KEY=your_secret_key_for_auth
```

#### For Docusaurus/.env:
```env
REACT_APP_API_BASE_URL=http://localhost:8000  # Backend API URL
REACT_APP_OPENAI_API_KEY=your_openai_api_key  # For client-side AI features (optional)
```

## Running the Application

### 1. Start the Backend
```bash
# From rag-backend directory
cd rag-backend
source venv/bin/activate  # On Windows: venv\Scripts\activate
uvicorn api.main:app --reload --port 8000
```

### 2. Start the Frontend
```bash
# From Docusaurus directory
cd Docusaurus
npm start
```

The application will be available at `http://localhost:3000`.

## Adding a New Chapter

### 1. Create the Chapter Content
Create a new markdown file in the `docs/modules/module1-the-robotic-nervous-system/` directory (or appropriate module directory):

```md
---
title: Your Chapter Title
description: Brief description of the chapter
tags: [tag1, tag2, tag3]
difficulty: beginner  # or intermediate, advanced
learning_outcomes:
  - Understand concept X
  - Be able to implement Y
  - Appreciate the importance of Z
---

# Your Chapter Title

## Overview
Chapter overview content...

## Technical Explanation
Detailed technical content...

## Code Examples
```python
# Your code examples
print("Hello, ROS 2!")
```

## Exercises
1. Exercise 1...
2. Exercise 2...

## Mini-Projects
A small project to apply the concepts learned.

## Assessment
Questions to evaluate understanding.

## Glossary Terms
Definitions of key terms introduced in the chapter.
```

### 2. Register the Chapter in Sidebar
Update the `Docusaurus/sidebars.ts` file to include your new chapter in the navigation.

### 3. Index the Content for RAG
After adding content, run the indexing script to make the new content searchable:

```bash
# From rag-backend directory
cd rag-backend
source venv/bin/activate  # On Windows: venv\Scripts\activate
python -m embeddings.indexer --new-chapter path/to/your/chapter.md
```

## Using Claude Code Subagents

The repository includes several subagents for various tasks:

1. **chapter-writer**: Generates full chapters from spec files
2. **rewriter**: Enhances clarity, structure, and tone
3. **translator**: Generates Urdu variants
4. **rag-indexer**: Chunks and indexes content in Qdrant
5. **tester**: Runs Spec-Kit tests

To use a subagent on a chapter:

```bash
# From project root
cd Docusaurus
npx @claude-code/subagent <subagent-name> path/to/chapter.md
```

## Running Tests

### Backend Tests
```bash
# From rag-backend directory
cd rag-backend
python -m pytest tests/
```

### Frontend Tests
```bash
# From Docusaurus directory
cd Docusaurus
npm test
```

## Deployment

### Frontend (GitHub Pages)
```bash
cd Docusaurus
GIT_USER=<Your GitHub username> USE_SSH=true npm run deploy
```

### Backend (Railway/Fly.io)
Follow the deployment instructions for your chosen platform. The backend is configured to run with Gunicorn for production.

## Troubleshooting

### Common Issues

1. **Failed to connect to Qdrant**: Verify your QDRANT_URL and QDRANT_API_KEY in rag-backend/.env

2. **OpenAI API errors**: Verify your OPENAI_API_KEY is set correctly in both rag-backend and Docusaurus environments

3. **Content not appearing in search**: Run the indexing script to update the RAG index

4. **Personalization not working**: Ensure user data is being collected via the registration flow
# AI-Native Textbook: Physical AI & Humanoid Robotics

## Overview
This repository contains the AI-Native textbook for Physical AI & Humanoid Robotics, built with Docusaurus, FastAPI, and RAG-based AI assistance.

## Features
- **Personalized Learning**: Content adapts to your skill level and learning preferences
- **AI-Powered Q&A**: Ask questions about the textbook content and get AI-driven answers
- **Multilingual Support**: Available in English and Urdu
- **Structured Curriculum**: From ROS 2 fundamentals to capstone projects
- **Interactive UI**: Book-like experience with exercises and code examples
- **Progress Tracking**: Monitor your advancement through modules and chapters
- **Accessibility Ready**: WCAG 2.1 AA compliant for inclusive learning

## Tech Stack
- **Frontend**: Docusaurus for documentation and content
- **Backend**: FastAPI for API services
- **Database**: PostgreSQL for user data and content metadata
- **Vector Store**: Qdrant for RAG-based AI assistance
- **AI Integration**: OpenAI API for content generation and Q&A
- **Authentication**: JWT-based authentication system
- **Frontend Components**: React components for personalization, translation, Q&A, exercises and progress tracking

## Getting Started

### Prerequisites
- Node.js 16+
- Python 3.9+
- PostgreSQL
- Qdrant

### Installation
1. Clone the repository
2. Install backend dependencies:
   ```bash
   cd rag-backend
   pip install -r requirements.txt
   ```
3. Install frontend dependencies:
   ```bash
   cd Docusaurus
   npm install
   ```

### Configuration
1. Copy `.env.example` to `.env` and fill in the required values
2. Set up your PostgreSQL database
3. Configure Qdrant connection
4. Set up OpenAI API key

### Running the Application
- Backend API: `cd rag-backend && python main.py`
- Frontend: `cd Docusaurus && npm start`

## Architecture
- `/docs`: Textbook content and modules
- `/Docusaurus`: Docusaurus-based frontend with book-like styling
- `/rag-backend`: FastAPI backend with RAG capabilities
- `/src`: Shared frontend components
  - `/components/Personalization`: Personalization button component
  - `/components/TranslationToggle`: Translation toggle component
  - `/components/QABot`: AI Question and Answer component
  - `/components/Exercises`: Interactive exercises component
  - `/components/ProgressTracker`: Progress tracking component
  - `/components/Curriculum`: Curriculum navigation component
- `/specs`: Feature specifications and plans
- `.specify`: Specification-driven development tools

## Frontend Components
The textbook includes several interactive React components:

1. **PersonalizationButton**: Allows users to set their skill level, background, and learning preferences
2. **TranslationToggle**: Switches content between English and Urdu
3. **QABot**: AI-powered assistant for answering questions about the content
4. **Exercises**: Interactive quizzes and exercises to test understanding
5. **ProgressTracker**: Tracks and visualizes user progress through the curriculum
6. **Curriculum**: Visualizes the learning path and allows navigation through modules

## API Endpoints
- `/api/v1/auth`: User authentication and registration
- `/api/v1/personalization`: User profile and personalization settings
- `/api/v1/qa`: AI-powered Q&A functionality
- `/api/v1/translation`: Text translation services
- `/api/v1/curriculum`: Curriculum and progress tracking
- `/api/v1/health`: Service health check

## Contributing
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Ensure all components work together properly
5. Submit a pull request

## Development Guidelines
- Follow the Specification-Driven Development (SDD) process using `.specify` tools
- Maintain WCAG 2.1 AA accessibility compliance
- Ensure responsive design works on mobile and desktop
- Test all interactive components for keyboard navigation
- Keep the AI-Native textbook constitutional principles in mind

## License
[License information would go here]
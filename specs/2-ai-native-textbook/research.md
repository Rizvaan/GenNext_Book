# Research: AI-Native Textbook — Physical AI & Humanoid Robotics

## Decision: Implementation Approach for AI-Native Textbook
**Rationale**: Using Docusaurus.ai with Spec-Kit Plus methodology to create AI-native textbook content. This approach ensures content is modular, machine-readable, and chunkable for RAG systems as required by the constitution.

**Alternatives considered**:
- Traditional textbook creation: Rejected due to lack of AI-native features
- Video-only course: Rejected due to accessibility concerns and lack of searchability

## Decision: Book-Style Frontend Design
**Rationale**: Implementing a book-cover homepage with responsive layouts and consistent theme to provide a familiar learning experience while leveraging modern web capabilities. This follows the constitution requirement for a book-style frontend.

**Alternatives considered**:
- Standard web page layout: Rejected as it wouldn't meet the book-like experience requirement
- Mobile app only: Rejected due to limited reach and accessibility considerations

## Decision: Content Chunking Strategy
**Rationale**: Using 400-token segments with 50-token overlap for RAG implementation to balance context retention with query efficiency, meeting constitution requirements for RAG-ready knowledge architecture.

**Alternatives considered**:
- Larger chunks (1000+ tokens): Rejected as they might reduce relevance precision
- Smaller chunks (100 tokens): Rejected as they might lose important contextual information

## Decision: Multi-Language Implementation
**Rationale**: Implementing English ↔ Urdu toggle with JSON translation layer and RTL support for Urdu to meet multilingual access requirements. Technical terms preserved across translations.

**Alternatives considered**:
- Separate content files per language: Rejected as harder to maintain consistency
- Machine translation API at runtime: Rejected due to quality and cost concerns

## Decision: Personalization Algorithm
**Rationale**: Using user profile data (skill level, background, preferences) to adapt content difficulty and examples. This ensures a personalized learning experience tailored to each user's needs.

**Alternatives considered**:
- Static content for all users: Rejected as it wouldn't meet personalization requirements
- Complex ML models: Rejected as rule-based approach is simpler and sufficient

## Technology Stack Research
- **Frontend**: Docusaurus with React components for personalization, translation, and Q&A functionality
- **Styling**: Tailwind CSS for responsive design, with custom theme to achieve book-like aesthetic
- **Icons**: Lucide or Tabler icons for consistent UI elements
- **Backend**: FastAPI with async support for handling multiple concurrent AI queries
- **Vector DB**: Qdrant Cloud for RAG implementation with semantic search capabilities
- **Metadata DB**: Neon Serverless Postgres for user profiles and content metadata
- **AI Integration**: OpenAI API for question answering with textbook content as context
- **Authentication**: Better-Auth for collecting user profile data for personalization
- **Deployment**: GitHub Pages for frontend, Railway/Fly.io for backend API

## Architecture Considerations
- **RAG Implementation**: Content will be chunked into 400-token segments with 50-token overlap as specified in the feature requirements
- **Personalization**: User experience data collected via Better-Auth to customize content difficulty and examples
- **Accessibility**: All content will meet WCAG 2.1 AA standards with RTL support for Urdu
- **Responsive Design**: Mobile, tablet, and desktop layouts supported with dynamic scaling components
- **Interactive Elements**: Personalization buttons, translation toggles, AI Q&A, exercises, and progress trackers implemented as React components
- **Theme & Styling**: Serif fonts for headings to mimic book typography, with Sans fonts for body text; color palette designed to resemble physical textbook aesthetics
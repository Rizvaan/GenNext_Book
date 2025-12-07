# API Contract: Textbook Q&A Service

## ask_book(question)

### Description
Accepts a question about the textbook content and returns an AI-generated answer based only on the textbook knowledge.

### Request
- **Method**: POST
- **Path**: `/api/ask`
- **Content-Type**: application/json

#### Request Body
```json
{
  "question": "string (required, the question to ask about the textbook)",
  "userId": "string (optional, user ID for personalization)",
  "language": "string (optional, default: 'en', e.g., 'en', 'ur-PK')"
}
```

### Response
- **Status**: 200 OK
- **Content-Type**: application/json

#### Response Body
```json
{
  "answer": "string (the AI-generated answer based on textbook content)",
  "references": [
    {
      "chapterId": "string (ID of the chapter referenced)",
      "chapterTitle": "string (title of the referenced chapter)",
      "moduleId": "string (ID of the module containing the chapter)",
      "moduleTitle": "string (title of the module containing the chapter)"
    }
  ],
  "sessionId": "string (ID for the conversation session)",
  "timestamp": "ISO 8601 datetime string"
}
```

### Error Responses
- **Status**: 400 Bad Request
  - If question is missing or empty
- **Status**: 429 Too Many Requests
  - If rate limit is exceeded
- **Status**: 500 Internal Server Error
  - If there's an error with the AI service

---

## ask_from_selection(question, selected_text)

### Description
Accepts a question about selected text from the textbook and returns an AI-generated answer based only on the selected content.

### Request
- **Method**: POST
- **Path**: `/api/ask/selection`
- **Content-Type**: application/json

#### Request Body
```json
{
  "question": "string (required, the question to ask about the selection)",
  "selectedText": "string (required, the selected text to ask about)",
  "userId": "string (optional, user ID for personalization)",
  "language": "string (optional, default: 'en', e.g., 'en', 'ur-PK')"
}
```

### Response
- **Status**: 200 OK
- **Content-Type**: application/json

#### Response Body
```json
{
  "answer": "string (the AI-generated answer based on selected text)",
  "sessionId": "string (ID for the conversation session)",
  "timestamp": "ISO 8601 datetime string"
}
```

### Error Responses
- **Status**: 400 Bad Request
  - If question or selectedText is missing or empty
- **Status**: 429 Too Many Requests
  - If rate limit is exceeded
- **Status**: 500 Internal Server Error
  - If there's an error with the AI service

---

## chat_history()

### Description
Retrieves the chat history for a user's session.

### Request
- **Method**: GET
- **Path**: `/api/history`
- **Content-Type**: application/json

#### Request Query Parameters
```
sessionId: string (required, the session ID to retrieve history for)
userId: string (optional, user ID for additional context)
```

### Response
- **Status**: 200 OK
- **Content-Type**: application/json

#### Response Body
```json
{
  "sessionId": "string (ID for the conversation session)",
  "history": [
    {
      "timestamp": "ISO 8601 datetime string",
      "question": "string (the question asked)",
      "answer": "string (the AI-generated answer)",
      "references": [
        {
          "chapterId": "string (ID of the chapter referenced)",
          "chapterTitle": "string (title of the referenced chapter)",
          "moduleId": "string (ID of the module containing the chapter)",
          "moduleTitle": "string (title of the module containing the chapter)"
        }
      ]
    }
  ]
}
```

### Error Responses
- **Status**: 400 Bad Request
  - If sessionId is missing
- **Status**: 500 Internal Server Error
  - If there's an error retrieving the history
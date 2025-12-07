from typing import List, Dict, Any
from ..db.qdrant_connector import qdrant_client
from ..embeddings.indexer import index_content
from ..embeddings.chunker import chunk_text
import openai
from dotenv import load_dotenv
import os

load_dotenv()

class RAGAgent:
    def __init__(self):
        # Initialize OpenAI client
        openai.api_key = os.getenv("OPENAI_API_KEY")
        self.qdrant = qdrant_client

    def get_context(self, query: str, limit: int = 5) -> List[Dict[str, Any]]:
        """
        Get relevant context from the knowledge base using vector search
        """
        return self.qdrant.search_similar(query, limit)

    def generate_answer(self, query: str, context: List[Dict[str, Any]]) -> str:
        """
        Generate an answer based on the query and context
        """
        # Format context for the LLM
        context_str = "\n".join([item["text"] for item in context])

        # Create a prompt for the LLM
        prompt = f"""
        Context: {context_str}

        Question: {query}

        Please provide a helpful answer based on the context provided.
        If you cannot find the answer in the context, please say so.
        """

        try:
            # Call the OpenAI API to generate the answer
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=500,
                temperature=0.7
            )

            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"Error generating answer: {e}")
            return "I'm sorry, but I couldn't generate an answer for your question."

    def answer_question(self, query: str) -> str:
        """
        Main method to answer a question using RAG
        """
        # Get relevant context from the knowledge base
        context = self.get_context(query)

        # Generate answer using the context
        answer = self.generate_answer(query, context)

        return answer

# Global instance
rag_agent = RAGAgent()
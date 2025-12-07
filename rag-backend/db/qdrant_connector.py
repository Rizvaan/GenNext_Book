from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams, PointStruct
from qdrant_client.http import models
from typing import List, Dict, Any
import uuid
import os
from dotenv import load_dotenv

load_dotenv()

class QdrantConnector:
    def __init__(self, host: str = None, port: int = None, collection_name: str = "textbook_content"):
        # Use environment variables or defaults
        self.host = host or os.getenv("QDRANT_HOST", "localhost")
        self.port = port or int(os.getenv("QDRANT_PORT", "6333"))
        self.collection_name = collection_name
        
        # Initialize the Qdrant client
        self.client = QdrantClient(
            host=self.host,
            port=self.port,
        )
        
        # Create collection if it doesn't exist
        self._create_collection()
    
    def _create_collection(self):
        """
        Create the collection if it doesn't exist
        """
        try:
            collections = self.client.get_collections()
            
            # Check if collection exists
            collection_exists = any(collection.name == self.collection_name for collection in collections.collections)
            
            if not collection_exists:
                # Create collection with 1536 dimensions (for OpenAI embeddings)
                self.client.create_collection(
                    collection_name=self.collection_name,
                    vectors_config=VectorParams(size=1536, distance=Distance.COSINE),
                )
        except Exception as e:
            print(f"Error creating collection: {e}")
    
    def add_embedding(self, text: str, chapter_id: int, module_id: int, metadata: Dict[str, Any] = None):
        """
        Add a text embedding to the Qdrant collection
        """
        if metadata is None:
            metadata = {}
        
        # In a real implementation, this would call an embedding API
        # For now, we'll return a mock embedding
        embedding = self._get_mock_embedding(text)
        
        point = PointStruct(
            id=str(uuid.uuid4()),
            vector=embedding,
            payload={
                "text": text,
                "chapter_id": chapter_id,
                "module_id": module_id,
                "metadata": metadata
            }
        )
        
        self.client.upsert(
            collection_name=self.collection_name,
            points=[point]
        )
    
    def search_similar(self, query_text: str, limit: int = 5) -> List[Dict[str, Any]]:
        """
        Search for similar text embeddings
        """
        # In a real implementation, this would call an embedding API for the query
        query_embedding = self._get_mock_embedding(query_text)
        
        search_result = self.client.search(
            collection_name=self.collection_name,
            query_vector=query_embedding,
            limit=limit
        )
        
        results = []
        for hit in search_result:
            results.append({
                "text": hit.payload["text"],
                "chapter_id": hit.payload["chapter_id"],
                "module_id": hit.payload["module_id"],
                "metadata": hit.payload["metadata"],
                "score": hit.score
            })
        
        return results
    
    def _get_mock_embedding(self, text: str) -> List[float]:
        """
        Generate a mock embedding for demonstration purposes
        In a real implementation, this would call an embedding API
        """
        # This is a mock function that returns a fixed-size vector
        # In real implementation, use OpenAI embeddings or similar
        import random
        return [random.random() for _ in range(1536)]

# Global instance
qdrant_client = QdrantConnector()
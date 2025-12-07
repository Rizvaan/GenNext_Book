from typing import List, Dict, Any
from .chunker import chunk_chapter_content
from ..db.qdrant_connector import qdrant_client

def index_content(text: str, chapter_id: int, module_id: int) -> bool:
    """
    Index content by chunking it and adding to the vector database
    """
    try:
        # Chunk the content
        chunks = chunk_chapter_content(text, chapter_id, module_id)
        
        # Add each chunk to the vector database
        for chunk in chunks:
            qdrant_client.add_embedding(
                text=chunk["text"],
                chapter_id=chapter_id,
                module_id=module_id,
                metadata=chunk["metadata"]
            )
        
        return True
    except Exception as e:
        print(f"Error indexing content: {e}")
        return False

def index_chapter(chapter_content: str, chapter_id: int, module_id: int) -> bool:
    """
    Index a complete chapter
    """
    return index_content(chapter_content, chapter_id, module_id)

def index_module(chapters_data: List[Dict[str, Any]]) -> bool:
    """
    Index all chapters in a module
    """
    success_count = 0
    
    for chapter_data in chapters_data:
        success = index_chapter(
            chapter_content=chapter_data["content"],
            chapter_id=chapter_data["id"],
            module_id=chapter_data["module_id"]
        )
        
        if success:
            success_count += 1
    
    # Return True if all chapters were indexed successfully
    return success_count == len(chapters_data)
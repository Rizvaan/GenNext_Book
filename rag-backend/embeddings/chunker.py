from typing import List, Dict, Any
import re

def chunk_text(text: str, max_tokens: int = 400, overlap: int = 50) -> List[Dict[str, Any]]:
    """
    Split text into chunks with metadata
    """
    # Simple token estimation (1 token ~ 4 characters)
    avg_chars_per_token = 4
    max_chars = max_tokens * avg_chars_per_token
    
    # Split text into sentences
    sentences = re.split(r'[.!?]+', text)
    
    chunks = []
    current_chunk = ""
    current_metadata = {
        "length": 0,
        "start_pos": 0,
        "end_pos": 0
    }
    
    for sentence in sentences:
        sentence = sentence.strip()
        if not sentence:
            continue
            
        # Check if adding this sentence would exceed the limit
        if len(current_chunk + sentence) <= max_chars:
            current_chunk += sentence + ". "
            current_metadata["end_pos"] += len(sentence) + 2
        else:
            # Save the current chunk if it's not empty
            if current_chunk.strip():
                chunks.append({
                    "text": current_chunk.strip(),
                    "metadata": current_metadata.copy()
                })
            
            # Start a new chunk, potentially with overlap
            current_chunk = sentence + ". "
            current_metadata["start_pos"] = current_metadata["end_pos"]
            current_metadata["end_pos"] = current_metadata["start_pos"] + len(sentence) + 2
    
    # Add the final chunk if it exists
    if current_chunk.strip():
        chunks.append({
            "text": current_chunk.strip(),
            "metadata": current_metadata
        })
    
    return chunks

def chunk_chapter_content(content: str, chapter_id: int, module_id: int) -> List[Dict[str, Any]]:
    """
    Chunk chapter content with additional metadata
    """
    chunks = chunk_text(content)
    
    # Add chapter and module info to each chunk
    for chunk in chunks:
        chunk["metadata"]["chapter_id"] = chapter_id
        chunk["metadata"]["module_id"] = module_id
        chunk["metadata"]["chunk_id"] = f"{module_id}-{chapter_id}-{len(chunks)}"
    
    return chunks
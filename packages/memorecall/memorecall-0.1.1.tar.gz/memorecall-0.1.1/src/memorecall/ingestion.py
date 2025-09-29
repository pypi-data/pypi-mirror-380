"""
Memory ingestion and processing module.
Handles the intake and preprocessing of memories.
"""

from typing import Dict, List, Optional, Any, Union
from datetime import datetime
import hashlib
import re


class MemoryIngestion:
    """
    Handles the ingestion and preprocessing of raw memory data.
    """
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        self.config = config or {}
        self.preprocessing_enabled = self.config.get('preprocessing', True)
        self.deduplication_enabled = self.config.get('deduplication', True)
        self._memory_hashes = set()
    
    def ingest(self, raw_data: Union[str, Dict[str, Any]], metadata: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Ingest raw memory data and process it into a structured format.
        
        Args:
            raw_data: Raw memory content (text or structured data)
            metadata: Optional metadata about the memory
            
        Returns:
            Processed memory object
        """
        memory_obj = self._create_memory_object(raw_data, metadata)
        
        if self.preprocessing_enabled:
            memory_obj = self._preprocess(memory_obj)
        
        if self.deduplication_enabled:
            if self._is_duplicate(memory_obj):
                memory_obj['is_duplicate'] = True
                memory_obj['status'] = 'duplicate'
            else:
                self._add_to_dedup_cache(memory_obj)
        
        return memory_obj
    
    def _create_memory_object(self, raw_data: Union[str, Dict[str, Any]], metadata: Optional[Dict[str, Any]]) -> Dict[str, Any]:
        """Create a structured memory object from raw data."""
        if isinstance(raw_data, str):
            content = raw_data
            content_type = 'text'
        else:
            content = raw_data.get('content', '')
            content_type = raw_data.get('type', 'structured')
        
        return {
            'id': self._generate_id(content),
            'content': content,
            'content_type': content_type,
            'metadata': metadata or {},
            'timestamp': datetime.now().isoformat(),
            'processed': False,
            'status': 'pending'
        }
    
    def _preprocess(self, memory_obj: Dict[str, Any]) -> Dict[str, Any]:
        """Apply preprocessing to the memory content."""
        content = memory_obj['content']
        
        # Basic text cleaning
        if isinstance(content, str):
            # Remove extra whitespace
            content = re.sub(r'\s+', ' ', content.strip())
            
            # Extract keywords (simple implementation)
            keywords = self._extract_keywords(content)
            memory_obj['keywords'] = keywords
        
        memory_obj['content'] = content
        memory_obj['processed'] = True
        memory_obj['status'] = 'processed'
        
        return memory_obj
    
    def _extract_keywords(self, text: str) -> List[str]:
        """Extract keywords from text (placeholder implementation)."""
        # Simple keyword extraction - in a real implementation, you'd use NLP
        words = re.findall(r'\b\w{4,}\b', text.lower())
        # Return unique words, limited to top 10
        return list(set(words))[:10]
    
    def _generate_id(self, content: str) -> str:
        """Generate a unique ID for the memory."""
        return hashlib.md5(f"{content}{datetime.now().isoformat()}".encode()).hexdigest()[:12]
    
    def _is_duplicate(self, memory_obj: Dict[str, Any]) -> bool:
        """Check if the memory is a duplicate."""
        content_hash = hashlib.md5(memory_obj['content'].encode()).hexdigest()
        return content_hash in self._memory_hashes
    
    def _add_to_dedup_cache(self, memory_obj: Dict[str, Any]) -> None:
        """Add memory hash to deduplication cache."""
        content_hash = hashlib.md5(memory_obj['content'].encode()).hexdigest()
        self._memory_hashes.add(content_hash)


class MemoryEmbedding:
    """
    Handles embedding generation for memories (placeholder for vector embeddings).
    """
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        self.config = config or {}
        self.embedding_model = self.config.get('embedding_model', 'simple')
    
    def generate_embedding(self, memory_obj: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate embedding for a memory object.
        
        Args:
            memory_obj: Processed memory object
            
        Returns:
            Memory object with embedding
        """
        content = memory_obj['content']
        
        # Placeholder embedding (in real implementation, use transformers/OpenAI)
        if self.embedding_model == 'simple':
            embedding = self._simple_embedding(content)
        else:
            embedding = self._placeholder_embedding()
        
        memory_obj['embedding'] = embedding
        memory_obj['embedding_model'] = self.embedding_model
        memory_obj['status'] = 'embedded'
        
        return memory_obj
    
    def _simple_embedding(self, text: str) -> List[float]:
        """Create a simple hash-based embedding."""
        # Very basic embedding based on character frequencies
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789 '
        embedding = [0.0] * len(chars)
        
        text_lower = text.lower()
        total_chars = len(text_lower)
        
        if total_chars > 0:
            for i, char in enumerate(chars):
                count = text_lower.count(char)
                embedding[i] = count / total_chars
        
        return embedding
    
    def _placeholder_embedding(self) -> List[float]:
        """Placeholder embedding for when no model is available."""
        return [0.0] * 384  # Common embedding dimension
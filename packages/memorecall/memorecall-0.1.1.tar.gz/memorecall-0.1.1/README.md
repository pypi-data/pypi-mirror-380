# memorecall

[![PyPI version](https://badge.fury.io/py/memorecall.svg)](https://badge.fury.io/py/memorecall)
[![Python Support](https://img.shields.io/pypi/pyversions/memorecall.svg)](https://pypi.org/project/memorecall/)

A memory and recall enhancement library for Python. This package provides functionality similar to the memori project for storing and retrieving memories with enhanced search capabilities.

> **Note**: This is currently a placeholder package. Full functionality will be implemented in future versions.

## Architecture Overview

![Memory Recall Workflow](workflow.png)

The workflow diagram above illustrates the complete memory processing pipeline:

1. **Ingestion**: Raw data is ingested and preprocessed
2. **Embedding**: Content is converted to vector embeddings for semantic search
3. **Indexing**: Memories are indexed for efficient retrieval
4. **Storage**: Processed memories are stored in the configured backend
5. **Search**: Queries are processed and matched against stored memories
6. **Retrieval**: Relevant memories are returned with ranking

## Installation

```bash
pip install memorecall
```

## Quick Start

```python
from memorecall import MemoryRecall

# Initialize the memory system
memory = MemoryRecall()

# Store memories
memory.store("Important meeting notes", tags=["work", "meeting"])
memory.store("Personal reminder", tags=["personal"])

# Recall memories
all_memories = memory.recall()
work_memories = memory.recall(tags=["work"])
search_results = memory.recall(query="meeting")

print(f"Total memories: {memory.count()}")
```

## Features

- **Memory Storage**: Store text-based memories with optional tags
- **Smart Recall**: Search memories by content or filter by tags
- **Simple API**: Easy-to-use interface for memory operations
- **Lightweight**: Minimal dependencies

## API Reference

### MemoryRecall Class

#### `__init__(config=None)`

Initialize a new MemoryRecall instance.

#### `store(memory, tags=None)`

Store a memory with optional tags.

- `memory` (str): The content to store
- `tags` (list, optional): List of tags to associate with the memory
- Returns: `bool` - True if successful

#### `recall(query=None, tags=None)`

Retrieve memories based on search criteria.

- `query` (str, optional): Search query to filter by content
- `tags` (list, optional): List of tags to filter by
- Returns: `list` - List of matching memories

#### `clear()`

Clear all stored memories.

- Returns: `bool` - True if successful

#### `count()`

Get the number of stored memories.

- Returns: `int` - Number of memories

## Development

This is a placeholder package. The current implementation provides basic in-memory storage and retrieval. Future versions will include:

- Persistent storage options
- Advanced search algorithms
- Memory categorization and organization
- Export/import functionality
- Integration with external memory systems

## Contributing

This project is currently in placeholder status. Contributions will be welcome once the main implementation begins.

## License

MIT License - see LICENSE file for details.

## Author

Hoseyn Amiri (aamirihoseyn@gmail.com)

## Changelog

### 0.1.0

- Initial placeholder release
- Basic memory storage and recall functionality
- PyPI package structure

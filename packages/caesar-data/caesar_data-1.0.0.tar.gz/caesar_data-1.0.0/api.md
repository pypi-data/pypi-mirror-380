# Research

Types:

```python
from caesar.types import ResearchCreateResponse, ResearchRetrieveResponse, ResearchListResponse
```

Methods:

- <code title="post /research">client.research.<a href="./src/caesar/resources/research/research.py">create</a>(\*\*<a href="src/caesar/types/research_create_params.py">params</a>) -> <a href="./src/caesar/types/research_create_response.py">ResearchCreateResponse</a></code>
- <code title="get /research/{id}">client.research.<a href="./src/caesar/resources/research/research.py">retrieve</a>(id) -> <a href="./src/caesar/types/research_retrieve_response.py">ResearchRetrieveResponse</a></code>
- <code title="get /research">client.research.<a href="./src/caesar/resources/research/research.py">list</a>(\*\*<a href="src/caesar/types/research_list_params.py">params</a>) -> <a href="./src/caesar/types/research_list_response.py">SyncPagination[ResearchListResponse]</a></code>

## Files

Types:

```python
from caesar.types.research import FileCreateResponse, FileListResponse
```

Methods:

- <code title="post /research/files">client.research.files.<a href="./src/caesar/resources/research/files.py">create</a>(\*\*<a href="src/caesar/types/research/file_create_params.py">params</a>) -> <a href="./src/caesar/types/research/file_create_response.py">FileCreateResponse</a></code>
- <code title="get /research/files">client.research.files.<a href="./src/caesar/resources/research/files.py">list</a>(\*\*<a href="src/caesar/types/research/file_list_params.py">params</a>) -> <a href="./src/caesar/types/research/file_list_response.py">SyncPagination[FileListResponse]</a></code>

## Results

Types:

```python
from caesar.types.research import ResultRetrieveContentResponse
```

Methods:

- <code title="get /research/{id}/results/{resultId}/content">client.research.results.<a href="./src/caesar/resources/research/results.py">retrieve_content</a>(result_id, \*, id) -> <a href="./src/caesar/types/research/result_retrieve_content_response.py">ResultRetrieveContentResponse</a></code>

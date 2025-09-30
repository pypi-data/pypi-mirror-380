# Repo

Types:

```python
from relace.types import (
    File,
    RepoInfo,
    RepoMetadata,
    RepoListResponse,
    RepoAskQuestionResponse,
    RepoCloneResponse,
    RepoRetrieveContentResponse,
)
```

Methods:

- <code title="post /repo">client.repo.<a href="./src/relace/resources/repo/repo.py">create</a>(\*\*<a href="src/relace/types/repo_create_params.py">params</a>) -> <a href="./src/relace/types/repo_info.py">RepoInfo</a></code>
- <code title="get /repo/{repo_id}">client.repo.<a href="./src/relace/resources/repo/repo.py">retrieve</a>(repo_id) -> <a href="./src/relace/types/repo_metadata.py">RepoMetadata</a></code>
- <code title="get /repo">client.repo.<a href="./src/relace/resources/repo/repo.py">list</a>(\*\*<a href="src/relace/types/repo_list_params.py">params</a>) -> <a href="./src/relace/types/repo_list_response.py">RepoListResponse</a></code>
- <code title="delete /repo/{repo_id}">client.repo.<a href="./src/relace/resources/repo/repo.py">delete</a>(repo_id) -> None</code>
- <code title="post /repo/{repo_id}/ask">client.repo.<a href="./src/relace/resources/repo/repo.py">ask_question</a>(repo_id, \*\*<a href="src/relace/types/repo_ask_question_params.py">params</a>) -> <a href="./src/relace/types/repo_ask_question_response.py">RepoAskQuestionResponse</a></code>
- <code title="get /repo/{repo_id}/clone">client.repo.<a href="./src/relace/resources/repo/repo.py">clone</a>(repo_id, \*\*<a href="src/relace/types/repo_clone_params.py">params</a>) -> <a href="./src/relace/types/repo_clone_response.py">RepoCloneResponse</a></code>
- <code title="post /repo/{repo_id}/retrieve">client.repo.<a href="./src/relace/resources/repo/repo.py">retrieve_content</a>(repo_id, \*\*<a href="src/relace/types/repo_retrieve_content_params.py">params</a>) -> <a href="./src/relace/types/repo_retrieve_content_response.py">RepoRetrieveContentResponse</a></code>
- <code title="post /repo/{repo_id}/update">client.repo.<a href="./src/relace/resources/repo/repo.py">update_contents</a>(repo_id, \*\*<a href="src/relace/types/repo_update_contents_params.py">params</a>) -> <a href="./src/relace/types/repo_info.py">RepoInfo</a></code>

## File

Methods:

- <code title="delete /repo/{repo_id}/file/{file_path}">client.repo.file.<a href="./src/relace/resources/repo/file.py">delete</a>(file_path, \*, repo_id) -> <a href="./src/relace/types/repo_info.py">RepoInfo</a></code>
- <code title="get /repo/{repo_id}/file/{file_path}">client.repo.file.<a href="./src/relace/resources/repo/file.py">download</a>(file_path, \*, repo_id) -> object</code>
- <code title="put /repo/{repo_id}/file/{file_path}">client.repo.file.<a href="./src/relace/resources/repo/file.py">upload</a>(file_path, body, \*, repo_id, \*\*<a href="src/relace/types/repo/file_upload_params.py">params</a>) -> <a href="./src/relace/types/repo_info.py">RepoInfo</a></code>

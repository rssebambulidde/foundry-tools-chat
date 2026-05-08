# Architecture Overview

This project demonstrates a tools-augmented Azure OpenAI assistant that uses
local PDF knowledge and web search to answer travel questions.

## High-Level Flow

```text
User Query
    |
Responses API Request
    |
Model Tool Selection
    |-- file_search -> Travel brochure vector store
    |-- web_search  -> Current public information
    |
Result Synthesis
    |
Streaming Response
    |
Response ID Saved for Conversation Context
```

## Application Flow

1. The app loads `AZURE_OPENAI_ENDPOINT` and `MODEL_DEPLOYMENT` from `.env`.
2. It authenticates with Azure through `DefaultAzureCredential`.
3. It creates a vector store named `travel-brochures`.
4. It uploads every PDF from the `brochures/` folder.
5. It starts an interactive terminal chat loop.
6. Each user question is sent to the Responses API with available tools.
7. The model decides whether to call `file_search`, `web_search`, both, or
   neither.
8. The final answer streams back to the terminal.
9. The completed response ID is stored for follow-up questions.

## Retrieval-Augmented Generation Pattern

```text
PDF Brochures
    |
Upload and Index
    |
Vector Store
    |
User Question
    |
file_search Retrieves Relevant Chunks
    |
Model Uses Retrieved Context
    |
Grounded Response
```

The retrieval step allows the model to answer questions using the brochure
content instead of relying only on training data.

## Tool Selection Pattern

The model receives this tool list:

```python
tools=[
    {
        "type": "file_search",
        "vector_store_ids": [vector_store.id],
    },
    {
        "type": "web_search",
    },
]
```

The application does not route questions manually. The model evaluates the user
query and decides which tool or tools are useful.

## Example Scenarios

### Brochure Question

```text
What hotels does Margie's Travel offer in San Francisco?
```

The model can use `file_search` to retrieve relevant brochure content.

### Current Information Question

```text
What events are happening in San Francisco next month?
```

The model can use `web_search` to gather current public information.

### Combined Question

```text
Compare Margie's San Francisco hotels with other current options.
```

The model can combine `file_search` results with web information.

## Technology Stack

- **Language:** Python 3.13+
- **SDK:** OpenAI Python SDK
- **Authentication:** Azure Identity
- **Primary API:** Responses API
- **Knowledge storage:** OpenAI vector stores
- **Tools:** `file_search` and `web_search`
- **Infrastructure:** Azure OpenAI / Microsoft Foundry

## Implemented Resilience

- Environment variable validation.
- Empty brochure folder check.
- File handle cleanup after upload.
- Azure credential cleanup.
- Graceful terminal error output.

## Production Considerations

For production use, consider adding:

- Persistent vector store reuse instead of creating a new store each run.
- Structured logging.
- Retry logic for upload, search, and model calls.
- Rate limit handling.
- Source citations in the terminal output.
- Automated tests around configuration and document discovery.
- A web UI or API layer.

## Scalability Notes

The current app is intentionally simple and local. It is best suited for
learning, demos, and portfolio presentation. For multiple users, the chat loop
could be moved into an async API service and the vector store lifecycle could
be managed separately from runtime requests.

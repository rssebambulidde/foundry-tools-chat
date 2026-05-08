# Azure AI Tools-Augmented Travel Assistant

**SamaBrains Solution** | AI Engineering Project

Build a retrieval-augmented travel assistant with Azure OpenAI, Microsoft
Foundry, the Responses API, vector stores, file search, web search, and
streaming responses.

## Project Overview

This repository demonstrates a tools-augmented AI chat application. The app can
answer travel questions by searching local PDF brochures and, when needed,
using web search for current destination information.

## Why I Built This

I built this project to practice and demonstrate how AI assistants can go
beyond general model knowledge by using tools. The goal was to show how a model
can combine private business documents with current web information to produce
more useful, grounded responses.

This project highlights practical AI engineering patterns such as retrieval
augmented generation, vector store indexing, tool selection, streaming output,
Azure Identity authentication, and clear developer documentation.

## What Makes This Different

The assistant has access to two tools:

- `file_search`: Searches uploaded travel brochure PDFs.
- `web_search`: Searches the web for current travel and destination details.

The model decides which tool to use based on the user's question. A question
about Margie's Travel brochures can use `file_search`; a question about current
events or travel advice can use `web_search`; broader comparison questions can
use both.

## Included Files

| File or Folder | Purpose |
| --- | --- |
| `tools-app.py` | Main tools-augmented chat application |
| `brochures/` | Travel PDFs indexed into a vector store |
| `.env.example` | Environment variable template |
| `requirements.txt` | Runtime Python dependencies |
| `QUICKSTART.md` | Step-by-step setup guide |
| `ARCHITECTURE.md` | Design and flow details |
| `CONTRIBUTING.md` | Contribution guidelines |

## Repository Details

| Detail | Value |
| --- | --- |
| Repository | `rssebambulidde/foundry-tools-chat` |
| Remote URL | `https://github.com/rssebambulidde/foundry-tools-chat.git` |
| Current branch | `master` |
| Project type | Python command-line RAG and tools demo |
| Runtime | Python 3.13+ |
| Authentication | Azure Identity token authentication |
| Primary API | OpenAI Responses API through Azure OpenAI |
| Knowledge source | Travel brochure PDFs in `brochures/` |
| License | MIT |
| CI workflow | GitHub Actions lint and formatting checks |

## Quick Start

### 1. Set Up Python

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

On macOS/Linux:

```bash
source venv/bin/activate
```

### 2. Configure Azure OpenAI

```bash
copy .env.example .env
```

On macOS/Linux:

```bash
cp .env.example .env
```

Edit `.env`:

```env
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/openai/v1
MODEL_DEPLOYMENT=gpt-4.1
```

### 3. Run the App

```bash
python tools-app.py
```

Type a travel question in the terminal. Type `quit` to exit.

## Example Questions

```text
What hotels does Margie's Travel offer in San Francisco?
```

Uses `file_search` to search the brochure PDFs.

```text
What's happening in San Francisco next month?
```

Uses `web_search` to retrieve current information.

```text
Compare Margie's San Francisco hotels with other current options.
```

Can combine brochure knowledge with current web information.

## Key Features

- Vector store indexing for PDF brochures.
- `file_search` for semantic document search.
- `web_search` for current destination information.
- Model-directed tool selection.
- Streaming terminal output.
- Conversation memory through `previous_response_id`.
- Azure Identity authentication with no hardcoded API keys.

## Architecture

```text
User Question
    |
Responses API Request
    |
Model Chooses Tools
    |-- file_search -> Search brochure vector store
    |-- web_search  -> Search current web information
    |
Model Combines Results
    |
Streaming Response
    |
Save Response ID for Follow-Up Questions
```

## Requirements

- Python 3.13 or later
- Azure subscription
- Azure OpenAI resource with a deployed model
- Microsoft Foundry or Azure OpenAI access
- PDF files in the `brochures/` folder
- Python packages from `requirements.txt`

## Brochure Dataset

The included sample dataset contains travel brochures for:

- Dubai
- Las Vegas
- London
- Margie's Travel company information
- New York
- San Francisco

You can replace these files with your own PDFs to adapt the assistant for a
different domain.

## Comparison With Basic Chat

| Feature | Basic Chat | This App |
| --- | --- | --- |
| Responses API | Yes | Yes |
| Streaming | Yes | Yes |
| Conversation memory | Yes | Yes |
| PDF search | No | Yes |
| Web search | No | Yes |
| Model tool selection | No | Yes |
| RAG pattern | No | Yes |

## Troubleshooting

### No PDFs Found

Make sure the `brochures/` folder exists and contains PDF files.

### Azure Credentials Not Found

Run:

```bash
az login
```

### Model Not Found

Check that `MODEL_DEPLOYMENT` in `.env` exactly matches your Azure OpenAI
deployment name.

### Tool Execution Error

- Verify your Azure OpenAI endpoint and model deployment.
- Confirm that your account can use file search and web search tools.
- Check your internet connection for web search queries.

## Next Steps

- Add your own PDFs to `brochures/`.
- Try single-tool and multi-tool prompts.
- Compare responses with and without brochure grounding.
- Adapt the app for customer support, internal docs, or research workflows.

## Resources

- [OpenAI Python SDK](https://github.com/openai/openai-python)
- [Azure OpenAI Service](https://learn.microsoft.com/en-us/azure/ai-services/openai/)
- [Retrieval-Augmented Generation][rag]
- [Microsoft Foundry](https://microsoft.com/foundry)

[rag]: https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/retrieval-augmented-generation

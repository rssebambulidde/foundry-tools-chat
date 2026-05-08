# Quick Start Guide

## 1. Prerequisites

```bash
python --version
git --version
```

This project is designed for Python 3.13 or later.

## 2. Set Up the Environment

```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
```

## 3. Configure Credentials

```bash
copy .env.example .env
```

On macOS/Linux:

```bash
cp .env.example .env
```

Update `.env`:

```env
AZURE_OPENAI_ENDPOINT=https://your-service.openai.azure.com/openai/v1
MODEL_DEPLOYMENT=gpt-4.1
```

## 4. Sign In to Azure

```bash
az login
```

Select the subscription that contains your Azure OpenAI resource.

## 5. Check the Brochures

The app indexes PDFs from the `brochures/` folder. The sample project includes
six travel brochures. You can keep them for testing or replace them with your
own PDFs.

## 6. Run the Application

```bash
python tools-app.py
```

## 7. Try Example Prompts

```text
What hotels does Margie's Travel offer in London?
```

```text
What's happening in New York this month?
```

```text
Compare Margie's Dubai hotels with other current hotel options.
```

Type `quit` to exit.

## How It Works

The app creates a vector store, uploads the PDFs from `brochures/`, and gives
the model access to two tools:

- `file_search` for brochure knowledge.
- `web_search` for current public information.

The model chooses tools based on the question, combines the results, streams the
answer, and stores the response ID for follow-up context.

## File Structure

```text
.
|-- tools-app.py
|-- brochures/
|   |-- Dubai Brochure.pdf
|   |-- Las Vegas Brochure.pdf
|   |-- London Brochure.pdf
|   |-- Margies Travel Company Info.pdf
|   |-- New York Brochure.pdf
|   `-- San Francisco Brochure.pdf
|-- requirements.txt
|-- .env.example
|-- README.md
|-- QUICKSTART.md
|-- ARCHITECTURE.md
|-- CONTRIBUTING.md
|-- LICENSE
`-- .github/
    |-- workflows/
    |   `-- lint.yml
    `-- PULL_REQUEST_TEMPLATE.md
```

## Troubleshooting

### No PDFs Found

Make sure the `brochures/` folder exists and contains at least one PDF.

### Azure Credentials Not Found

```bash
az login
```

### Missing Python Package

```bash
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

### Model Not Found

Check that `MODEL_DEPLOYMENT` matches your Azure OpenAI deployment name exactly.

### Tool Execution Error

- Check your Azure OpenAI endpoint.
- Confirm that the model deployment supports the tools used by this app.
- Check your internet connection for web search.

## Next Steps

1. Read `ARCHITECTURE.md`.
2. Add your own PDFs to `brochures/`.
3. Try prompts that require only brochure search.
4. Try prompts that require only web search.
5. Try prompts that combine both tools.

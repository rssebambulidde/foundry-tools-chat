# Azure AI Tools-Augmented Application

**SamaBrains Solution** | AI Engineering Project  
*Building knowledge-grounded AI agents with retrieval-augmented generation (RAG)*

---

## 📋 Project Overview

Production-grade AI agent demonstrating **tool-augmented architectures** and **retrieval-augmented generation (RAG)**. The application autonomously selects tools based on query requirements, combining document knowledge with real-time information sources.

## What Makes This Different?

This app includes **tools** that give the AI access to:
1. **file_search** - Search knowledge from uploaded PDF documents
2. **web_search** - Search the internet for current information

The AI **autonomously decides** which tool to use based on your question!

## What's Included

### **tools-app.py** - Tools-Augmented Chat Application
- Vector store with 6 travel brochures (PDF files)
- file_search tool (semantic search on documents)
- web_search tool (internet search)
- Streaming responses
- Conversation tracking
- **Use case:** Knowledge-augmented AI assistants (customer support, research, Q&A)

### **Brochures Folder**
Travel brochures that get indexed for searching:
- Dubai Brochure.pdf
- Las Vegas Brochure.pdf
- London Brochure.pdf
- Margie's Travel Company Info.pdf
- New York Brochure.pdf
- San Francisco Brochure.pdf

## Quick Start

### 1. Setup
```bash
# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure
```bash
# Copy the template
copy .env.example .env

# Edit .env and add your actual values:
# - AZURE_OPENAI_ENDPOINT: Your Azure OpenAI service endpoint
# - MODEL_DEPLOYMENT: Your model name (e.g., gpt-4.1)
```

### 3. Run
```bash
python tools-app.py
```

Then ask travel-related questions. Type `quit` to exit.

## Real Examples

### Query 1: Web Search (Current Information)
```
Enter a question: What's happening in San Francisco next month?

Response: [Uses web_search tool to find current SF events for June 2026]
Assistant: San Francisco has several exciting events next month:
- SF Design Week (June 2-8)
- Concert Series at The Fillmore
- Warriors basketball games
- Art exhibitions in SOMA
[... and more current information]
```

### Query 2: File Search (Document Knowledge)
```
Enter a question: What hotels does Margie's Travel offer in San Francisco?

Response: [Uses file_search tool to search brochures]
Assistant: According to Margie's Travel brochures, they offer:
- The Lombard Hotel
- The Wharf Hotel
[... sourced from uploaded PDFs]
```

### Query 3: Mixed Tools
```
Enter a question: Compare Margie's hotels with other SF options

Response: [Uses BOTH file_search (company data) AND web_search (market rates)]
Assistant: Margie's Travel offers...
Other highly-rated hotels in SF include...
Price comparison...
```

## Key Features

✅ **Vector Store** - Semantic search on documents (meaning-based, not keyword matching)  
✅ **file_search Tool** - Ask questions about your documents  
✅ **web_search Tool** - Access current information from internet  
✅ **Tool Autonomy** - Model chooses which tool(s) to use automatically  
✅ **RAG System** - Combines document knowledge with web knowledge  
✅ **Streaming** - Real-time response display  
✅ **Conversation Memory** - Context maintained across turns  

## Architecture

```
User Question
    ↓
AI Analysis: "What tools do I need?"
    ├─ Need current info? → web_search
    ├─ Need company data? → file_search
    ├─ Need both? → Both tools
    └─ Need neither? → Use training data
    ↓
Execute Selected Tools
    ├─ file_search: Query vector store
    └─ web_search: Search internet
    ↓
Combine Results
    ↓
Generate Response with Streaming
    ↓
Display to User + Save Response ID for context
```

## How Tools Work

### Vector Store & Embeddings
```
PDFs → Split into chunks → Convert to vectors (embeddings) → Store in vector DB
         ↓
User Question → Convert to vector → Find similar chunks → Return to model
```

### Tool Configuration
```python
tools=[
    {
        "type": "file_search",
        "vector_store_ids": [vector_store.id]  # Which documents to search
    },
    {
        "type": "web_search"  # No config needed
    }
]
```

## Comparison with Basic Chat Apps

| Feature | Basic Chat | This App |
|---------|-----------|----------|
| Responses API | ✅ | ✅ |
| Streaming | ✅ | ✅ |
| Conversation Memory | ✅ | ✅ |
| Non-blocking (async) | Only in chat-async.py | ❌ |
| PDF Search | ❌ | ✅ |
| Web Search | ❌ | ✅ |
| AI Tool Selection | ❌ | ✅ |
| RAG System | ❌ | ✅ |

## Use Cases

- 📚 **Customer Support** - Search FAQs + policies + web info
- 🏥 **Medical Assistant** - Search medical journals + research
- ⚖️ **Legal Assistant** - Search case law + web precedents
- 📊 **Research Assistant** - Search papers + current articles
- 🏖️ **Travel Planning** - Search brochures + current events/prices (like this app!)
- 📱 **Product Support** - Search documentation + online resources

## Adding Your Own Documents

Replace the PDF files in the `brochures/` folder with your own documents:

```python
# The app automatically:
# 1. Finds all PDFs in brochures/
# 2. Creates embeddings
# 3. Stores in vector store
# 4. Makes searchable via file_search tool
```

## For Learning

**New to tools/RAG?** This app demonstrates:
- Vector stores and semantic search
- Tool definition and specification
- Tool autonomy (model chooses tools)
- Multi-tool composition
- RAG (Retrieval Augmented Generation) patterns

## Troubleshooting

**"Vector store not found"**
- The app creates it automatically on first run
- PDFs in brochures/ are indexed automatically

**"Tool execution error"**
- Check brochures folder exists and has PDFs
- Verify internet connection for web_search

**"Azure credentials not found"**
- Run `az login` to authenticate

## Next Steps

- Try adding different document types (add PDFs to brochures/)
- Experiment with multi-turn conversations
- Compare results with basic chat apps
- Explore building custom tools for your domain

## Resources

- [Vector Stores & Embeddings](https://platform.openai.com/docs/api-reference/vector-stores)
- [RAG Systems](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/retrieval-augmented-generation)
- [OpenAI Tools](https://platform.openai.com/docs/guides/function-calling)
- [Microsoft Foundry Agents](https://microsoft.com/foundry)
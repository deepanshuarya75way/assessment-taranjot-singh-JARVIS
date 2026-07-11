# JARVIS - Personalized AI Assistant

JARVIS is a Computer Science Engineering (Data Science) capstone project focused on deeply understanding and implementing the architecture of modern AI assistants. The goal is not to build another LLM or clone ChatGPT, but to learn how each component of an AI assistant works, why it exists, and how to build a personalized, interview-ready AI system from the ground up.

## Project Goals

- Learn modern AI assistant architecture
- Build a personalized AI assistant
- Understand every component instead of copying code
- Build an interview-ready project

## Tech Stack

- Python
- Streamlit
- SQLite
- Google Gemini API
- spaCy
- ChromaDB
- Vector Embeddings
- RAG (Retrieval-Augmented Generation)

## Current Architecture

```
JARVIS/
│── app.py
│── config.py
│
├── pages/
│   ├── home.py
│   ├── users.py
│   ├── notes.py
│   ├── reminders.py
│   ├── conversations.py
│   ├── memories.py
│   └── ai_chat.py
│
├── DATABASE/
├── SERVICES/
├── TEST/
└── README.md
```

## Architecture

- **UI Layer:** Built with Streamlit, this layer provides the user interface for interacting with JARVIS. It handles navigation, displays information, and passes user input to backend services.
- **Services Layer:** Contains business logic and orchestration. Services validate input, implement application workflows, and interact with both the database and AI APIs.
- **Database Layer:** Handles persistent storage (currently SQLite) for users, notes, reminders, conversations, and other structured data. All database logic is separated from business logic.

## Development Roadmap

1. **Foundation** (Setup, database, services, basic UI)
2. **Gemini Integration** (Conversational AI with Google Gemini API)
3. **Function Calling** (Enable Gemini to call Python functions/tools)
4. **Memory** (Short-term and long-term memory for conversations and user data)
5. **spaCy NLP** (Entity recognition, intent extraction)
6. **RAG with ChromaDB** (Semantic memory, document retrieval)
7. **Recommendation System** (Personalized suggestions and analytics)

## Current Progress

- [x] SQLite database
- [x] User CRUD operations
- [x] Service Layer (validation, orchestration)
- [x] Streamlit multipage navigation
- [ ] Gemini API integration
- [ ] Function Calling
- [ ] Memory (short-term & long-term)
- [ ] spaCy NLP integration
- [ ] RAG with ChromaDB
- [ ] Recommendation System

## Learning Philosophy

- Focus on truly understanding the architecture and purpose of each component.
- Keep Version 1 simple and functional—prioritize AI capabilities over unnecessary UI polish.
- The AI assistant is the product; database and UI are tools to support it.
- Build with interview readiness in mind: be able to explain every design decision.

## Future Vision

JARVIS is designed as an AI agent whose reasoning is powered by Gemini and whose capabilities are extended by specialized tools:

- **Gemini:** Core reasoning and natural language conversation
- **SQLite:** Structured memory (users, notes, reminders, etc.)
- **ChromaDB:** Semantic memory and vector search for RAG
- **spaCy:** Language understanding (entities, dates, intent)
- **Recommendation Modules:** Personalized analytics and suggestions

This architecture allows JARVIS to grow from a simple assistant into a powerful, extensible AI agent capable of integrating new tools and reasoning workflows as needed.
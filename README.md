### Goal
- create a rag study planner for a uni module handbook
- it should reference the correct information in the pdf-file
- and answer users' requests in natural language

### Plan for PoC
- extract text via pdfplumber 
- put text into pydantic models to then dump as json
- chunk json (according to modules)
- create embeddings for chunks
- save chunks and embeddings in postgresql db
- connect llm with db to create referencing
- query llm with a simple ui

### SetUp
1. uv sync 
2. 
    - for WSL/Ubuntu: source .venv/bin/activate
    - for Windows: .\venv\Scripts\Activate.ps1
3. poe run
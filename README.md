MCP LangGraph Research

A simple research agent built using LangGraph and MCP (Model Context Protocol).

Features:
- Supervisor Agent
- Research Agent
- LangGraph workflow
- MCP integration
- Weather MCP server
- Topic-based research

Project Structure:
MCP-LangGraph-Research/
├── research.py
├── server.py
├── weather.py
├── .gitignore
└── README.md

Requirements:
- Python 3.x
- LangGraph
- FastMCP
- Requests

Setup:

1. Create a virtual environment:
python -m venv venv

2. Activate the virtual environment:
.\venv\Scripts\activate

3. Install the required packages:
pip install langgraph fastmcp requests

Run:

1. Activate the virtual environment:
.\venv\Scripts\activate

2. Run the research agent:
python research.py

3. Enter your question when prompted.

Example:

Ask your question: mcp

Supervisor
Question: mcp

Research Agent
Researching: mcp

Final Result:
MCP stands for Model Context Protocol. It allows AI applications to interact with external tools and data.

Author:
Sethupathi M
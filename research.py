from typing import TypedDict
from langgraph.graph import StateGraph, START, END


class State(TypedDict):
    question: str
    result: str


def supervisor(state: State):
    print("\nSupervisor")
    print("Question:", state["question"])
    return state


def research_agent(state: State):
    question = state["question"]

    print("\nResearch Agent")
    print("Researching:", question)

    result = search_topic(question)

    return {
        "question": question,
        "result": result
    }


def search_topic(topic: str):
    data = {
        "python": "Python is a high-level programming language used for AI, automation and web development.",
        "mcp": "MCP stands for Model Context Protocol. It allows AI applications to interact with external tools and data.",
        "langgraph": "LangGraph is a framework for building stateful, multi-step and multi-agent AI workflows."
    }

    return data.get(
        topic.lower(),
        f"No information found for {topic}."
    )


graph = StateGraph(State)

graph.add_node("supervisor", supervisor)
graph.add_node("research_agent", research_agent)

graph.add_edge(START, "supervisor")
graph.add_edge("supervisor", "research_agent")
graph.add_edge("research_agent", END)

app = graph.compile()


question = input("Ask your question: ")

result = app.invoke({
    "question": question,
    "result": ""
})

print("\nFinal Result:")
print(result["result"])
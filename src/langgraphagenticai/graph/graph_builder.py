from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from typing import Annotated
from typing_extensions import TypedDict


class State(TypedDict):
    messages: Annotated[list, add_messages]


class GraphBuilder:
    def __init__(self, model):
        self.model = model

    def setup_graph(self, usecase):
        if usecase == "Basic Chatbot":
            return self._build_basic_chatbot()
        raise ValueError(f"Unsupported usecase: {usecase}")

    def _build_basic_chatbot(self):
        def chatbot(state: State):
            return {"messages": [self.model.invoke(state["messages"])]}

        graph = StateGraph(State)
        graph.add_node("chatbot", chatbot)
        graph.add_edge(START, "chatbot")
        graph.add_edge("chatbot", END)
        return graph.compile()
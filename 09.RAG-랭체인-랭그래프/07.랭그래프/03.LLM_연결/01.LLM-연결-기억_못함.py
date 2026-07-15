from langchain_core.prompts import ChatPromptTemplate
import sys
from pathlib import Path
import os
from langchain_core.prompts import MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
from llm_loader import init_custom_llm

# 템플릿 사용

llm = init_custom_llm()

from typing import TypedDict
from langgraph.graph import StateGraph, START, END

# 1.State 정의
class State(TypedDict):
    question:str
    answer:str

# node 함수 만들기
def chatbot(state):
    print()
    print("LLM 실행")

    response = llm.invoke(state["question"])
    state["answer"] = response.content

    return state

# graph

builder = StateGraph(State)
builder.add_node("chabot",chatbot)

builder.add_edge(START,"chabot")
builder.add_edge("chabot",END)

graph = builder.compile()

# 실행

# result = graph.invoke({
#     "question": "파이썬 설며해줘"
# })

# print(result["answer"])

# 대화형 챗봇

while True:

    question = input("질문 :")
    
    if question == "exit":
        break

    result = graph.invoke({
        "question": question
    })

    print()
    print(result["answer"])



# import sys
# from pathlib import Path
# sys.path.append(str(Path(__file__).resolve().parent.parent))

# from util import show_graph
# show_graph(graph)


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

from typing import TypedDict,Annotated
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages

# 1.State 정의
class State(TypedDict):
    messages:Annotated[list, add_messages]

# node 함수 만들기
def chatbot(state):
    
    print()
    print("LLM 실행")

    response = llm.invoke(state["messages"])
        

    return {
       "messages":[response]
    }

# graph

builder = StateGraph(State)
builder.add_node("chabot",chatbot)

builder.add_edge(START,"chabot")
builder.add_edge("chabot",END)

graph = builder.compile()


# 메모리 기억 시키기
# messages = []

from langgraph.checkpoint.memory import InMemorySaver
# 메모리 기억 시키기
memory = InMemorySaver()


# 실행
while True:

    question = input("질문 :")
    
    if question == "exit":
        break
    
    messages.append(HumanMessage(content = question))

    result = graph.invoke({
        "messages": messages
    })

    answer = result["messages"][0].content
    
    print("AI 답변", answer)
    
    # 대화기억 추가
    messages.append(AIMessage(content = answer))



# import sys
# from pathlib import Path
# sys.path.append(str(Path(__file__).resolve().parent.parent))

# from util import show_graph
# show_graph(graph)


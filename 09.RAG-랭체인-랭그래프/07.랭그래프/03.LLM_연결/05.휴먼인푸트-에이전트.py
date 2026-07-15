




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

#messages: Annotated[list, add_messages]는 LangGraph에게 
# "이 리스트는 덮어쓰지 말고 누적해서 저장해라"라고 알려주는 문법
# Annotated 추가 정보를 붙여라

class State(TypedDict):
    messages:Annotated[list, add_messages]

#price:Annotated[int,"상품가격","0보다는 커야함"] = 7.8
#print(price)

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

# 메모리 기억 시키기
# messages = []

from langgraph.checkpoint.memory import InMemorySaver

# 메모리 기억 시키기
# InMemorySaver 객체

# +--------------------------+
# |     InMemorySaver        |
# |--------------------------|
# | put()                   |
# | get()                   |
# | list()                  |
# | delete()                |
# | ...                     |
# +--------------------------+

from langgraph.checkpoint.sqlite import SqliteSaver
import sqlite3

#memory = InMemorySaver()

#pip install langgraph-checkpoint-sqlite
DB_PATH = Path(__file__).parent / "chat.db"
conn = sqlite3.connect(
    DB_PATH,
    check_same_thread=False
)
memory= SqliteSaver(conn)


# 그래프가 끝날 때마다  State를 저장합니다.
graph = builder.compile(
    checkpointer = memory 
)

config = {
    "configurable":{
        "thread_id" : "user1"
    }
}

# 실행
while True:

    question = input("질문 :")
    
    if question == "exit":
        break

    result = graph.invoke(
        {
            "messages": [
                HumanMessage(question)
            ]
        },
        config = config
    )

    answer = result["messages"][-1].content
    print("AI 답변", answer)
    
        
    # 저장된 체크포인트 확인
    # for checkpoint in memory.list(None):
    #     print(checkpoint)


# import sys
# from pathlib import Path
# sys.path.append(str(Path(__file__).resolve().parent.parent))

# from util import show_graph
# show_graph(graph)


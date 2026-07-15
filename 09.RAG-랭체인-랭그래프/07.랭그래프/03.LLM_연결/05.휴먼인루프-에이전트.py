# 핵심은 한 문장임
# AI가 혼자 결정하면 위험한 일을, 사람이 최종 확인하도록 만드는 것


# 핵심함수 2개 이해 하는게 핵심
# interrupt()와 resume() 


    # interrupt()
    # Graph
    # ↓
    # interrupt()
    # ↓
    # Checkpoint 저장
    # ↓
    # Graph 종료
    # ↓
    # (몇 초 후)
    # ↓
    # resume()
    # ↓
    # 계속 실행

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

from langgraph.types import interrupt,Command

# 1.State 정의

class State(TypedDict):
    report : str
    approved : bool

# node 함수 만들기
# ---------------------------------
# 보고서 작성
# ---------------------------------
def report_node(state):

    print("보고서를 작성했습니다.")

    return {
       "report" : "2026년 AI 시장 분석 보고서"
    }

# ---------------------------------
# 사람 승인
# ---------------------------------

def approval_node(state: State):
    print("\n 결재요청")
    print("결재내용:", state["report"])

    answer = interrupt(
        "승인 하시겠습니까? (yes,no)"
    )

    return {
        "approved" : answer
    }

# ---------------------------------
# 최종 처리
# ---------------------------------

def finish_node(state):

    if state["approved"]:
        print("\n 보고서가 승인 되었습니다.")
    else:
        print("\n 보고서가 거절 되었습니다.")
    
    return state

# graph

builder = StateGraph(State)

builder.add_node("report",report_node)
builder.add_node("approval",approval_node)
builder.add_node("finish",finish_node)

builder.add_edge(START,"report")
builder.add_edge("report","approval")
builder.add_edge("approval","finish")
builder.add_edge("finish",END)

from langgraph.checkpoint.memory import InMemorySaver

memory = InMemorySaver()

# 그래프가 끝날 때마다  State를 저장합니다.
graph = builder.compile(
    checkpointer = memory 
)

# ---------------------------------
# 실행
# ---------------------------------

config = {
    "configurable":{
        "thread_id" : "approval-demo"
    }
}

print("=" * 50)
print("1차 실행")
print("=" *50)

result = graph.invoke(
        {}, # => 초기 state 값
        config = config
    )

print(result)

print("=" * 50)
print("재개")
print("=" *50)

answer = input("승인 여부 (True / False) : ")
approved = answer.strip().lower() in ["yes", "y", "승인"]

result = graph.invoke(
    Command( resume = approved),
    config = config
)

print(result)
    
        
    # 저장된 체크포인트 확인
    # for checkpoint in memory.list(None):
    #     print(checkpoint)


import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from util import show_graph
show_graph(graph)


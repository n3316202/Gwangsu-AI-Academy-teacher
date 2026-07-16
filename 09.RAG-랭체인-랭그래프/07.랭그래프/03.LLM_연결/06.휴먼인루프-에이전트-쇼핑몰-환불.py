# 4. 아래를 Human-in-the-Loop 로 구현하시오.

# 쇼핑몰 환불 승인

# 시나리오

# AI가 환불 요청을 분석한다.

# 관리자가 승인해야 환불된다.

# 환불 요청
#      ↓
# AI 분석
#      ↓
# interrupt()
#      ↓
# 관리자 확인
#      ↓
# 승인
#      ↓
# resume()
#      ↓
# 환불 완료

# State
# class State(TypedDict):
#     refund_reason: str
#     approved: bool

# 예시

# 상품 파손

# 환불 추천

# 관리자

# 승인

# ↓

# 환불 처리

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
    refund_reason: str
    approved : bool

# node 함수 만들기
# ---------------------------------
# AI 분석
# ---------------------------------
def ai_review(state):

    print("\n=====AI 분석====")
    print(f"환불 사유:{state["refund_reason"]}")

    if "파손" in state["refund_reason"]:
        print("AI 판단 : 환불 하시길 추천합니다.")
    else:
        print("AI 판단 : 관리자 판단이 필요 합니다.")
    
    return state

# ---------------------------------
# 관리자 승인
# ---------------------------------

def manager_approval(state: State):
    print("\n =====관리자 승인 대기======")

    approved = interrupt("관리자가 승인을 입력하세요")

    return{
        "approved" : approved
    }

# ---------------------------------
# 환불 처리
# ---------------------------------
def finish_refund(state):
    print("\n ===== 환불 처리 ======")

    if state["approved"]:
        print("환불이 완료 되었습니다.")
    else:
        print("환불이 거부 되었습니다.")
    
    return state

# graph

builder = StateGraph(State)

builder.add_node("ai_review",ai_review)
builder.add_node("manager_approval",manager_approval)
builder.add_node("finish_refund",finish_refund)

builder.add_edge(START,"ai_review")
builder.add_edge("ai_review","manager_approval")
builder.add_edge("manager_approval","finish_refund")
builder.add_edge("finish_refund",END)


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
        "thread_id" : "approval-refund"
    }
}

print("=" * 50)
print("최초 실행")
print("=" *50)

result = graph.invoke(
        {
            "refund_reason":"상품 파손",
            "approved":False
        },
        config = config
    )

print(result)


print("=" * 50)
print("관리자 승인")
print("=" *50)

answer = input("승인 여부 (yes / y / 승인) : ")
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


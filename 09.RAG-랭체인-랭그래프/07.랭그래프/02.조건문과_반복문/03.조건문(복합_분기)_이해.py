from typing import TypedDict
from langgraph.graph import StateGraph, START, END

# 점수

# 90 이상
#  |
# A


# 70 이상
#  |
# B


# 70 미만
#  |
# C

class State(TypedDict):
    score:int
    grade:str


# node
def check_score(state):
    print("\n 당신의 점수는", state["score"])
    return state

# def adult(state):
#     state["result"]="성인"
#     return state

# def child(state):
#     #state["result"]="미성년"
#     return {
#         "result" : "미성년"
#     }

# 조건함수 = 분기함수
def grade_route(state):

    score = state["score"]

    if score >= 90:
        return "A"
    elif score >= 70:
        return "B"
    else:
        return "C"

def grade_a(state):
    
    return {
        "grade" : "수 입니다."
    }

def grade_b(state):
    
    return {
        "grade" : "우 입니다."
    }

def grade_c(state):
    
    return {
        "grade" : "미 입니다."
    }

# 그래프 객체 생성
builder = StateGraph(State)

builder.add_node("check_score",check_score)
builder.add_node("grade_a",grade_a)
builder.add_node("grade_b",grade_b)
builder.add_node("grade_c",grade_c)


builder.add_edge(START,"check_score")

builder.add_conditional_edges(
    "check_score",
    grade_route,
    {
        "A":"grade_a",
        "B":"grade_b",
        "C":"grade_c",
    }
)
builder.add_edge("grade_a",END)
builder.add_edge("grade_b",END)
builder.add_edge("grade_c",END)

graph = builder.compile()

# 실행

result = graph.invoke({
    "score": 70
})

print(result)
print(result["grade"])

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from util import show_graph
show_graph(graph)





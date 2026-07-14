from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class State(TypedDict):
    score:int
    result:str

# node
def check(state):
    print("\n 점수검사", state["score"])
    return state

def pass_node(state):
    state["result"]="합격"
    return state

def fail_node(state):
    state["result"]="불합격"
    return state

# 조건함수 = 분기
def route(state):

    if state["score"] >= 60:
        return "pass_route"
    
    return "fail_route"

# 그래프 객체 생성
builder = StateGraph(State)

builder.add_node("check",check)
builder.add_node("pass",pass_node)
builder.add_node("fail",fail_node)

builder.add_edge(START,"check")

builder.add_conditional_edges(
    "check",
    route,
    {
        "pass_route":"pass",
        "fail_route":"fail"
    }
)
builder.add_edge("fail",END)
builder.add_edge("pass",END)

graph = builder.compile()

# 실행

result = graph.invoke({
    "score":80
})

print(result)
print(result["result"])

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from util import show_graph
show_graph(graph)





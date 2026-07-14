from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class State(TypedDict):
    age:int
    result:str


# node
def check_age(state):
    print("\n 당신의 나이", state["age"])
    return state

def adult(state):
    state["result"]="성인"
    return state

def child(state):
    #state["result"]="미성년"
    return {
        "result" : "미성년"
    }

# 조건함수 = 분기함수
def route(state):

    if state["age"] >= 20:
        return "adult"
    
    return "child"

# 그래프 객체 생성
builder = StateGraph(State)

builder.add_node("check_age",check_age)
builder.add_node("adult",adult)
builder.add_node("child",child)


builder.add_edge(START,"check_age")
builder.add_conditional_edges(
    "check_age",
    route,
    {
        "adult":"adult",
        "child":"child"
    }
)
builder.add_edge("adult",END)
builder.add_edge("child",END)

graph = builder.compile()

# 실행

result = graph.invoke({
    "age":18
})

print(result)
print(result["result"])

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from util import show_graph
show_graph(graph)





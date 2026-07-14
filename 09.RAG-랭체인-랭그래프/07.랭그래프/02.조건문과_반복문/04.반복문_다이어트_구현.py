# 반복문 구현
# Loop

# LangGraph에서는 Edge를 자기 자신에게 연결하면 반복 가능

from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class State(TypedDict):
    weight:int

# node
def diet(state):

    print(f"현재체중 {state["weight"]}kg")

    return {
        "weight": state["weight"] - 1
    }

# 분기 함수
def check_weight(state):

    if state["weight"] >= 65:
        return "continue"

    return "end"

# 그래프 객체 생성
builder = StateGraph(State)

builder.add_node("diet",diet)


builder.add_edge(START,"diet") # => 여기 까지

builder.add_conditional_edges(
    "diet",
    check_weight,
    {
        "continue":"diet",
        "end":END,
    }
)


graph = builder.compile()

# 실행

result = graph.invoke({
    "weight": 70
})

print(result)
print(result["weight"])

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from util import show_graph
show_graph(graph)





# 반복문 구현
# Loop

# LangGraph에서는 Edge를 자기 자신에게 연결하면 반복 가능

from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class State(TypedDict):
    count:int

# node
def counter(state):

    return {
        "count": state["count"] + 1
    }

# 분기 함수
def check_count(state):

    if state["count"] >=3:
        return "end"
    else:
        return "continue"

# 그래프 객체 생성
builder = StateGraph(State)

builder.add_node("counter",counter)


builder.add_edge(START,"counter")


builder.add_conditional_edges(
    "counter",
    check_count,
    {
        "continue":"counter",
        "end":END,
    }
)


graph = builder.compile()

# 실행

result = graph.invoke({
    "count": 0
})

print(result)
print(result["count"])

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from util import show_graph
show_graph(graph)





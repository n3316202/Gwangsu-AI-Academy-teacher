from typing import TypedDict
from langgraph.graph import StateGraph, START, END

#실습 문제

# 문제:

# START
#  ↓
# plus10
#  ↓
# minus5
#  ↓
# END

# 초기값:
# 100
# 결과:
# 105

# 1.스테이트 설계
# 랭그래프용 변수 선언
class State(TypedDict):
    value:int

# 2. 노드 함수 만들기
def multiply2(state:State):
    # state["value"] =  state["value"] + 10
    return {
        "value" : state["value"] * 2
    }

def plus20(state:State):
    state["value"] =  state["value"] + 20
    return state

# 3. graph 객체 생성
builder = StateGraph(State)

builder.add_node("multiply2",multiply2)
builder.add_node("plus20",plus20)

builder.add_edge(START,"multiply2")
builder.add_edge("multiply2","plus20")
builder.add_edge("plus20",END)

# 컴파일
graph = builder.compile()

# 실행
result = graph.invoke({
    "value":100
})

print(result)
print(result["value"])

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))


from util import show_graph
show_graph(graph)
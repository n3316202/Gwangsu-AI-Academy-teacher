# 실행 예
# 숫자 입력 : 3
# 업 ↑

# 숫자 입력 : 9
# 다운 ↓

# 숫자 입력 : 5
# 업 ↑

# 숫자 입력 : 7
# 정답입니다!

# {'answer': 7, 'guess': 7, 'message': 'SUCCESS'}


#              START
#                │
#                ▼
#         input_number
#                │
#                ▼
#        check_number
#                │
#        message=="SUCCESS" ?  => route 함수 구현
#           ┌─────────────┐
#           │             │
#           ▼             ▼
#    input_number        END


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





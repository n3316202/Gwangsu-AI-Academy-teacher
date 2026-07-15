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
    answer:int
    guess: int 
    message: str


# node
def input_number(state):

    guess = int(input("숫자 입력 : "))
   
    return {
        "guess": guess
    }

def check_number(state):
    answer = state["answer"]
    guess = state["guess"]

    if guess > answer:
        print("다운 ↓")

        return {
            "message":"DOWN"
        }
    elif guess < answer:
        
        print("업 ↑")

        return {
            "message" : "UP"
        }
    else:
        print("정답 입니다.")
        
        return {
            "message" : "SUCCESS"
        }

# 라우트(route) 함수
def router(state):

    if state["message"] == "SUCCESS":
        return "end"

    return "continue"


# 그래프 객체 생성
builder = StateGraph(State)

builder.add_node("input_number",input_number)
builder.add_node("check_number",check_number)

builder.add_edge(START,"input_number") 
builder.add_edge("input_number","check_number") 

builder.add_conditional_edges(
    "check_number",
    router,
    {
        "continue":"input_number",
         "end": END
    }
)

graph = builder.compile()

# 실행
result = graph.invoke({
    "answer": 7,
    "guess":0,
    "message":""
})

print(result)
print(result["message"])

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from util import show_graph
show_graph(graph)





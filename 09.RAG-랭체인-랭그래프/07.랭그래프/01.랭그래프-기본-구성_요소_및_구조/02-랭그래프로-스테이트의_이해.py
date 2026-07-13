from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class State(TypedDict):
    message:str

def hello(state:State):
    print("헬로우 랭그래프!!")    
    
    return {
        "message": "헬로우 랭그래프!!"
    }

#그래프 생성
builder = StateGraph(State)

builder.add_node("hello",hello)

builder.add_edge(START,"hello")
builder.add_edge("hello",END)

# 그래프 컴파일
graph = builder.compile()

result = graph.invoke({
    "message": ""
})

print(result)



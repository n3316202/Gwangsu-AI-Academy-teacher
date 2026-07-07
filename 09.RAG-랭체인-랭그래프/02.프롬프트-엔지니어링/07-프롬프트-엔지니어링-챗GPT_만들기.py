import sys
from pathlib import Path
import os

sys.path.append(str(Path(__file__).resolve().parent.parent))
from llm_loader import init_custom_llm
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage,ToolMessage

#================= 대화 이어가기 = 챗 GPT 만들기

messages = [
    SystemMessage(content="당신은 친절한 AI 입니다."),
    # HumanMessage(content="나는 홍길동 입니다.")
    # AIMessage(content="안녕하세요 홍길동씨 무엇을 도와 드릴까요"),
    # HumanMessage(content="나는 누구니"),
    # AIMessage(content="당신은 홍길동 입니다."),
]

while True:
    question = input("무엇이든 물어보세요")
    
    if question == "exit":
        break
    
    messages.append(
        HumanMessage(content=question)
    )

    llm = init_custom_llm()
    respose = llm.invoke(messages)
    print("AI 응답:",respose.content)
    
    messages.append(respose)



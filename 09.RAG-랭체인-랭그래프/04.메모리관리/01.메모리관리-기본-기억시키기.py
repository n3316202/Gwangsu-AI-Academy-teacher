
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
import sys
from pathlib import Path
import os
from langchain_core.prompts import MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

sys.path.append(str(Path(__file__).resolve().parent.parent))
from llm_loader import init_custom_llm

# 템플릿 사용

llm = init_custom_llm()

# 대화 기록 저장소
history = []

# 프롬프트 객체 생성
prompt = ChatPromptTemplate.from_messages([
    ("system","당신은 친절한 비서 입니다."),
    MessagesPlaceholder("history")
])

while True:
    question = input("질문: ")
    
    history.append(
        HumanMessage(question)
    )

    chain = prompt | llm

    respose = chain.invoke({
        "history":history
    })

    history.append(AIMessage(respose.content))
    print("AI 응답",respose.content)
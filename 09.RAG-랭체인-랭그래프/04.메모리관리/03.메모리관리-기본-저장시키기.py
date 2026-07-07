
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

#==================================================
# 예제 1. 리스트로 대화 저장하기 (Memory가 없을 때)
history = []

history.append("사용자 : 안녕하세요.")
history.append("AI : 안녕하세요!")

history.append("사용자 : 제 이름은 철수입니다.")
history.append("AI : 반갑습니다 철수님.")

print(history)


# 문자열만 저장하면 AI가 이해할 수 있을까요?"
# AI는 누가 말했는지(Human/AI)를 알아야 함

from langchain_core.messages import HumanMessage
from langchain_core.messages import AIMessage

history = []

history.append(HumanMessage("안녕하세요."))
history.append(AIMessage("안녕하세요!"))

history.append(HumanMessage("제 이름은 철수입니다."))
history.append(AIMessage("반갑습니다 철수님."))

print(history)

#pip install langchain langchain-community

from langchain_community.chat_message_histories import ChatMessageHistory
# ChatMessageHistory 등장

history = ChatMessageHistory() # =>InMemoryChatMessageHistory ,RunnableWithMessageHistory

history.add_user_message("안녕하세요")
history.add_ai_message("무엇을 도와 드릴까요")

print(history.messages)

for message in history.messages:
    print(type(message))
    print(message.content)

# [
#     HumanMessage(content='안녕하세요', additional_kwargs={}, response_metadata={}), 
#     AIMessage(content='무엇을 도와 드릴까요', additional_kwargs={}, response_metadata={}, tool_calls=[], invalid_tool_calls=[])
# ]


# 템플릿 사용
from langchain_core.chat_history import InMemoryChatMessageHistory

history = InMemoryChatMessageHistory() # =>InMemoryChatMessageHistory ,RunnableWithMessageHistory

history.add_user_message("안녕하세요")
history.add_ai_message("무엇을 도와 드릴까요")

history.add_user_message("제이름은 철수 입니다.")
history.add_ai_message("반갑습니다 철수님")

print(history.messages[0].content)
print(history.messages[1].content)
print(history.messages[2].content)
print(history.messages[3].content)

history.clear()
print("내용",history.messages)

# print(history.messages)

# for message in history.messages:
#     print(type(message))
#     print(message.content)

# LLM 과 연결하기 예제
history = InMemoryChatMessageHistory()
# history = [
# HumanMessage(content='내 이름은 철수야', additional_kwargs={}, response_metadata={}), 
# ]
llm = init_custom_llm()

question = "내 이름은 철수야"

history.add_user_message(question)
response = llm.invoke(history.messages)
print(response.content)
history.add_ai_message(response.content)

# 두번째 질문
question = "내 이름이 뭐지?"

history.add_user_message(question)
response = llm.invoke(history.messages)
print(response.content)
history.add_ai_message(response.content)
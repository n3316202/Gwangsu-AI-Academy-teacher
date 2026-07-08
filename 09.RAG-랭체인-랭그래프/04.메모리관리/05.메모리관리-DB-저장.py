from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
from llm_loader import init_custom_llm

llm = init_custom_llm()

# 2. Prompt 구성 (history + question 구조)
prompt = ChatPromptTemplate.from_messages([
    ("system", "당신은 친절한 AI 비서입니다."),
    ("placeholder", "{history}"),
    ("human", "{question}")
])

# 3. 기본 chain 생성
chain = prompt | llm

from langchain_community.chat_message_histories import SQLChatMessageHistory
# MySQL 연결
def get_sql_session_history(session_id: str):

    return SQLChatMessageHistory(
        session_id=session_id,
        connection="mysql+pymysql://scott:tiger@localhost:3306/scott",
        table_name="message_store" # DB에 생성될 테이블 이름 (기본값: message_store)
    )

chain_with_sql_history = RunnableWithMessageHistory(
    chain,
    get_sql_session_history,
    input_messages_key="question",
    history_messages_key="history",
)

# 저장된 정보 가져오기
history = SQLChatMessageHistory(
    session_id="user_1",
    connection="mysql+pymysql://scott:tiger@localhost:3306/scott",
    table_name="message_store"
)

messages = history.messages

for msg in messages:
    print(type(msg).__name__, msg.content)

# while True:

#     q = input("질문: ")

#     if q == "exit":
#         break

#     res = chain_with_sql_history.invoke(
#         {"question": q},
#         config={
#             "configurable": {
#                 "session_id": "user_1"
#             }
#         }
#     )

#     print("\nAI:", res.content)
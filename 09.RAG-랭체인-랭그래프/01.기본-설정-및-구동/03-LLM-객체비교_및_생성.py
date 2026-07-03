from dotenv import load_dotenv
#from openai import OpenAI
from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI

load_dotenv()

# llm 객체 생성 방법 3가지 

# 첫번째 방법 OpenAI() 로 객체 생성
# llm = OpenAI()
# result = llm.invoke("대한민국 수도는?")
# print(type(result))
# print(result)

# 두번째 방법 OpenAI() 로 객체 생성
llm = ChatOpenAI()
result = llm.invoke("대한민국 수도는?")
print(result.content)
print(result)

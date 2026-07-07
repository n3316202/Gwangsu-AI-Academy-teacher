
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
import sys
from pathlib import Path
import os

sys.path.append(str(Path(__file__).resolve().parent.parent))
from llm_loader import init_custom_llm

# 템플릿 사용
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,JsonOutputParser,XMLOutputParser

from pydantic import BaseModel

class UserInfo(BaseModel):
    name: str
    age: int
    job: str

llm = init_custom_llm()
structured_llm = llm.with_structured_output(UserInfo)

result = structured_llm.invoke("김철수 25살 개발자야")
print(result)
print("성명",result.name)
print("나이",result.age)
print("직업",result.job)

# {'name': '김철수', 'age': 25, 'job': '개발자'}
print(result.model_dump()) 



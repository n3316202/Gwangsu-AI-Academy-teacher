from langchain_community.document_loaders import PyPDFLoader,WebBaseLoader
#pip install pdfminer
#pip install pypdf

# TextLoader
# CSVLoader
# PyPDFLoader
# Docx2txtLoader =>  Word
# WebBaseLoader

# 1.pdf 로드
#loader = PyPDFLoader("https://arxiv.org/pdf/1706.03762.pdf")
# 현재 파이썬 파일이 있는 폴더
from pathlib import Path

#d:\Gwangsu-AI-Academy-teacher\09.RAG-랭체인-랭그래프\05.RAG\01.다큐먼트객체및_다큐먼트로더.py
print(__file__)
BASE_DIR = Path(__file__).resolve().parent #현재 실행 중인 파이썬 파일이 있는 폴더의 절대 경로를
pdf_path = BASE_DIR / "company.pdf"
# D:\Gwangsu-AI-Academy-teacher\09.RAG-랭체인-랭그래프\05.RAG\company.pdf
# print(pdf_path)

# loader = PyPDFLoader(pdf_path)

# # 2.다큐먼트 객체
# documents = loader.load()

# #print(documents)
# # print(len(documents))
# print(documents[0].page_content)

# URL 웹사이트 읽어 들이기
# pip install bs4
from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader("https://ko.wikipedia.org/wiki/%EA%B2%80%EC%83%89%EC%A6%9D%EA%B0%95%EC%83%9D%EC%84%B1")
documents = loader.load()
print(len(documents))
print(documents[0].page_content[:500])

from langchain_core.documents import Document
# 다큐먼트 객체
documents = [
    Document(
        page_content="다큐먼트 객체 입니다.1",
        metadata={
            "source":"랭체인",
            "page":1,
            "title":"테스트 파일"
        }
    ),
    Document("다큐먼트 객체 입니다.2"),
    Document("다큐먼트 객체 입니다.3")
]
print(documents)
# Document(metadata={'source': '랭체인', 'page': 1, 'title': '테스트 파일'},
#  page_content='다큐먼트 객체 입니다.1'),

# [
#     Document(metadata={}, page_content='다큐먼트 객체 입니다.1'), 
#     Document(metadata={}, page_content='다큐먼트 객체 입니다.2'), 
#     Document(metadata={}, page_content='다큐먼트 객체 입니다.3')
# ]
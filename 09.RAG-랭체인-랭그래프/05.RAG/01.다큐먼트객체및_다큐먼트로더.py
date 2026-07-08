from langchain_community.document_loaders import PyPDFLoader
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

BASE_DIR = Path(__file__).resolve().parent #현재 실행 중인 파이썬 파일이 있는 폴더의 절대 경로를
pdf_path = BASE_DIR / "company.pdf"
# D:\Gwangsu-AI-Academy-teacher\09.RAG-랭체인-랭그래프\05.RAG\company.pdf
print(pdf_path)

loader = PyPDFLoader("./company.pdf")

# 2.다큐먼트 객체
documents = loader.load()

#print(documents)
print(len(documents))
print(documents[0].page_content)



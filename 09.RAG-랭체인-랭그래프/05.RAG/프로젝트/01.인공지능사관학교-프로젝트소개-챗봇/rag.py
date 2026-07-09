from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

import sys
from pathlib import Path

# 현재 파일 기준으로 4단계 위 폴더를 import 경로에 추가
sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent))

from llm_loader import init_custom_llm
llm = init_custom_llm()

# 이미 만들어진 크로마 DB 객체 생성
embedding = HuggingFaceEmbeddings(
    model_name="BAAI/bge-m3",
)

# 현재 rag.py가 있는 폴더
BASE_DIR = Path(__file__).resolve().parent

# chroma_db 폴더
DB_PATH = BASE_DIR / "chroma_db"

db = Chroma(
    embedding_function = embedding,
    persist_directory = str(DB_PATH)
)
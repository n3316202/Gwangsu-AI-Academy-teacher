# pip install langchain-community faiss-cpu
# pip install chromadb langchain-chroma langchain-huggingface

from langchain_huggingface import HuggingFaceEmbeddings
from pathlib import Path
from langchain_chroma import Chroma

embedding = HuggingFaceEmbeddings(
    model_name="BAAI/bge-m3",
)

BASE_DIR = Path(__file__).resolve().parent #현재 실행 중인 파이썬 파일이 있는 폴더의 절대 경로를

documents = [
    "고양이는 귀여운 동물입니다.",
    "강아지는 충성심이 강합니다.",
    "자동차는 빠르게 달립니다."
]

# Chroma DB 저장 폴더
DB_PATH = BASE_DIR / "chroma_db"

db = Chroma.from_texts(
    texts=documents,
    embedding=embedding,
    persist_directory=str(DB_PATH)
)

print("벡터 DB 생성")
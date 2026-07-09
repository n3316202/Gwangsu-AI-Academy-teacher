# pip install langchain-community faiss-cpu
# pip install chromadb langchain-chroma langchain-huggingface

from langchain_huggingface import HuggingFaceEmbeddings
from pathlib import Path
from langchain_community.vectorstores import FAISS

embedding = HuggingFaceEmbeddings(
    model_name="BAAI/bge-m3",
)

BASE_DIR = Path(__file__).resolve().parent 

documents = [
    "고양이는 귀여운 동물입니다.",
    "강아지는 충성심이 강합니다.",
    "자동차는 빠르게 달립니다."
]

db = FAISS.from_texts(
    texts=documents,
    embedding=embedding,
)

db.save_local("faiss_db")

print("벡터 DB 생성")
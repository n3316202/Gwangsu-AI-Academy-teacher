# pip install langchain-community faiss-cpu
# pip install chromadb langchain-chroma langchain-huggingface

# | Vector Store  | 메모리 저장 | 디스크 저장 | 서버 필요 | 실무 사용 |
# | ------------- | ------ | ------ | ----- | ----- |
# | FAISS         | ✅      | ✅      | ❌     | ⭐⭐⭐⭐⭐ |
# | Chroma        | ✅      | ✅      | ❌     | ⭐⭐⭐⭐⭐ |
# | Milvus        | ✅      | ✅      | ✅     | ⭐⭐⭐⭐⭐ |
# | Qdrant        | ✅      | ✅      | ✅     | ⭐⭐⭐⭐⭐ |
# | Pinecone      | 클라우드   | 클라우드   | 관리형   | ⭐⭐⭐⭐⭐ |
# | Weaviate      | ✅      | ✅      | ✅     | ⭐⭐⭐⭐  |
# | Redis         | ✅      | 일부     | ✅     | ⭐⭐⭐⭐  |
# | Elasticsearch | ✅      | ✅      | ✅     | ⭐⭐⭐⭐  |

# =========================================================================

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

# Retriever 생성
retriever = db.as_retriever(
    search_kwargs={"k": 3}
)

#검색하기
question = "고양이는 어떤 동물인가요?"
docs = retriever.invoke(question)


#[Document(id='d2a58595-ea65-49de-8669-80b7278d82eb', metadata={}, page_content='고양이는 귀여운 동물입니다.'), Document(id='50f6eeb4-e0cd-4e6a-993c-0cb95d15d484', metadata={}, page_content='고양이는 귀여운 동물입니다.'), Document(id='e579983d-274f-458b-ae8d-f0bec04ff876', metadata={}, page_content='강아지는 충성심이 강합니다.'), Document(id='557108db-b786-46a8-a029-9234c4cb2fb1', metadata={}, page_content='강아지는 충성심이 강합니다.')]

print(docs)

for doc in docs:
    print("="*50)
    print(doc.page_content)

# ==================================================
# 고양이는 귀여운 동물입니다.
# ==================================================
# 고양이는 귀여운 동물입니다.
# ==================================================
# 강아지는 충성심이 강합니다.
# ==================================================
# 강아지는 충성심이 강합니다.


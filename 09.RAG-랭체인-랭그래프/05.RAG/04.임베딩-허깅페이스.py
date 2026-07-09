# pip install langchain-huggingface
# pip install sentence-transformers

# 허깅페이스
# API 비용 없음
# 임베딩 모델 자체를 내 컴퓨터에 설치
from langchain_huggingface import HuggingFaceEmbeddings

# | 모델                                      | 특징                | 추천    |
# | ---------------------------------------- | ----------------- | ----- |
# | `BAAI/bge-m3`                            | 다국어 지원, 한국어 성능 우수 | ⭐⭐⭐⭐⭐ |
# | `BAAI/bge-small-en-v1.5`                 | 영어 전용, 가벼움        | ⭐⭐⭐   |
# | `sentence-transformers/all-MiniLM-L6-v2` | 매우 빠름, 영어 중심      | ⭐⭐⭐⭐  |
# | `intfloat/multilingual-e5-base`          | 다국어 지원, 한국어 성능 좋음 | ⭐⭐⭐⭐  |
embedding = HuggingFaceEmbeddings(
    model_name="BAAI/bge-m3"
)

text = "대한민국의 수도는 서울입니다."
vector = embedding.embed_query(text)

print("="*50)
print("원본문장")
print(text)

print("\n벡터길기")
print(len(vector))

print("\n앞의 벡터 10개")
print(vector[:10])

#=============================================================

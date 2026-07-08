from langchain_openai import OpenAIEmbeddings
import sys
from pathlib import Path
from pydantic import BaseModel

sys.path.append(str(Path(__file__).resolve().parent.parent))
from llm_loader import init_custom_llm

llm = init_custom_llm()

embedding = OpenAIEmbeddings()
text = "대한민국의 수도는 서울입니다."

vector = embedding.embed_query(text) # → API 호출 → 비용 발생
print("="*50)
print("원본문장")
print(text)

print("\n벡터길기")
print(len(vector))

print("\n앞의 벡터 10개")
print(vector[:10])

# 원본문장
# 대한민국의 수도는 서울입니다.

# 벡터길기
# 1536

# 앞의 벡터 10개
# [0.009820127859711647, -0.016796590760350227, 0.011121895164251328, -0.01673339679837227, -0.028942205011844635, 0.012821775861084461, -0.04054436460137367, 0.010142410174012184, -0.014433187432587147, 0.0035798600874841213]

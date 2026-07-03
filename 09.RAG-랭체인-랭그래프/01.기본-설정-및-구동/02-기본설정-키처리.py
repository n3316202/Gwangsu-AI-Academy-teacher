# pip install dotenv
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# 클라이언트 생성
client = OpenAI()

# 요청
response = client.responses.create(
    model="gpt-4o-mini",
    input="AI Agent란?"
)

# 출력
print(response.output_text)
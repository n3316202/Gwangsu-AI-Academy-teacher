from rag import ask

print("="*50)
print("인공지능 사관학교 프로젝트 설명 챗봇")
print("="*50)

while True:
    question = input("\n질문: ")

    if question == "exit":
        break

    answer = ask(question)
    print()
    print(answer)

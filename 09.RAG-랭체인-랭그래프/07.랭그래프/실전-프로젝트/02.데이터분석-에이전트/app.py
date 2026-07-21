from graph import graph


while True:
    question = input("\n 질문:")

    if question.lower() == "exit":
        break

    result = graph.invoke(
        {
            "question": question,
            "analysis_type":"",
            "code":"",
            "result":"",
            "dataframe":None,
            "error": ""
        }
    )
    
    print("\n============================")
    print(result["result"])
from langchain_cerebras import ChatCerebras
from langchain_core.prompts import ChatPromptTemplate

llm = ChatCerebras(
    model="llama3.3-70b",
)

prompt: ChatPromptTemplate = ChatPromptTemplate.from_messages(
    messages=[
        (
            "system",
            "You are a helpful assistant that translates {input_language} to {output_language}.",
        ),
        ("human", "{input}"),
    ]
)

chain = prompt | llm
chain.invoke(
    input={
        "input_language": "English",
        "output_language": "German",
        "input": "I love programming.",
    }
)

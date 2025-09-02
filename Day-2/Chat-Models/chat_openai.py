from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI(model="gpt-3.5-turbo",tempreture=0.3,max_completion_tokens=500)

model.invoke("What is Capital of pakistan?")
result = model.invoke("What is Capital of pakistan?")
print(result.content)
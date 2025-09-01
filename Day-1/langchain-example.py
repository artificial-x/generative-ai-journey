
#Direct Call GPT
from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Summarize Romeo and Juliet"}]
)
print(response.choices[0].message.content)



#Using Langchain 
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain

# GPT model
llm = ChatOpenAI(model="gpt-4o-mini")

# Add conversation memory
conversation = ConversationChain(llm=llm, verbose=True)

# Start chatting
print(conversation.predict(input="Hi, I'm learning AI."))
print(conversation.predict(input="What did I just say?"))


             #using lanchains we added memory to the conversation chain 
             #now it remembers what we said earlier in the conversation
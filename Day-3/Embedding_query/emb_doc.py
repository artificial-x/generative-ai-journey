from langchain.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-large",dimensions=32)

documents = [ "Islamabad is the capital city of Pakistan.", 
             "Delhi is the capital city of India.",
             "Canberra is the capital city of Australia."]

result = embedding.embed_documents(documents)

print(str(result))
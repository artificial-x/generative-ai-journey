from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=200)

documents = [
    "Inception is a science fiction movie directed by Christopher Nolan.",
    "The Godfather is a classic mafia drama directed by Francis Ford Coppola.",
    "Avengers: Endgame is a superhero movie from the Marvel Universe.",
    "Titanic is a romantic tragedy directed by James Cameron.",
    "Interstellar explores space travel and time dilation."
]

query = "movie about sea disaster"

doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

scores = cosine_similarity([query_embedding],doc_embeddings)[0]

index, score = (sorted(list(enumerate(scores)),key=lambda x:x[1])[-1])

print(query)
print(documents[index])
print("similarity score is: ", score)
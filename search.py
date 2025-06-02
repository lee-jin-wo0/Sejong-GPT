import pickle
from sentence_transformers import SentenceTransformer
import faiss

model = SentenceTransformer("jhgan/ko-sroberta-multitask")

with open("data/sejong_index.pkl", "rb") as f:
    docs, index = pickle.load(f)

def search_docs(query, top_k=3):
    query_vec = model.encode([query])
    D, I = index.search(query_vec, top_k)
    return [docs[i] for i in I[0]]

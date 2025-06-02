from sentence_transformers import SentenceTransformer
import faiss
import pickle
import os

os.makedirs("data", exist_ok=True)

model = SentenceTransformer("jhgan/ko-sroberta-multitask")

with open("data/sejong_texts.txt", "r", encoding="utf-8") as f:
    docs = [line.strip() for line in f if line.strip()]

embeddings = model.encode(docs)
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

with open("data/sejong_index.pkl", "wb") as f:
    pickle.dump((docs, index), f)

print("✅ 임베딩 및 인덱스 저장 완료")

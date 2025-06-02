# 👑 세종대왕 GPT

조선의 제4대 왕 **세종대왕**의 말과 정신을 담은 맞춤형 GPT 챗봇입니다.  
로컬에서 실행되는 RAG 기반 Q&A 시스템으로, **LLaMA3 + Ollama + FAISS + Streamlit**을 활용해 구현되었습니다.

---

## 🧠 기능 소개

- ✅ Ollama의 `llama3` 모델을 사용한 로컬 LLM 질의응답
- ✅ 세종대왕 관련 문서 기반 RAG (검색 기반 생성)
- ✅ Streamlit 웹 인터페이스
- ✅ 한국어로 조선 시대 말투의 공손한 응답
- ✅ JSON 기반 세종 관련 질문-답변 corpus 포함

---

## 📁 폴더 구조
SEJONG-GPT/
│
├── app.py # Streamlit 웹앱 메인 파일
├── embed_and_save.py # 텍스트 → 임베딩 + 인덱스 생성
├── ollama_generate.py # llama3 모델로 질문에 대한 응답 생성
├── search.py # 벡터 검색 (FAISS 기반)
├── sejong_texts.txt # 세종대왕 관련 질문/답변 원본
├── data/
│ ├── sejong_index.pkl # 생성된 FAISS 인덱스
│ └── sejong_emb.pkl # 텍스트 임베딩 저장
└── README.md

---

## 🛠️ 설치 및 실행 방법
1. 필수 패키지 설치
`pip install sentence-transformers faiss-cpu streamlit requests`
2. Ollama 설치 및 LLaMA3 모델 다운로드
`https://ollama.com/download`
`ollama run llama3`
3. 임베딩 + FAISS 저장(최초 1회만 실시)
`python embed_and_save.py`
4. 웹앱 실행
`streamlit run app.py`
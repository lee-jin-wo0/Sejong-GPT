import streamlit as st
from search import search_docs
from ollama_generate import ask_llama3

# 질문/답변 히스토리 저장용 세션 상태 초기화
if "history" not in st.session_state:
    st.session_state.history = []

st.set_page_config(page_title="세종대왕 GPT", page_icon="👑")

# 사이드바에 예시 질문
with st.sidebar:
    st.markdown("### 💡 질문 예시")
    st.markdown("""
- 세종대왕은 누구인가요?
- 훈민정음은 왜 만들었나요?
- 장영실을 어떻게 생각하나요?
- 세종대왕의 업적은?
""")

# 타이틀
st.title("👑 세종대왕 GPT")
st.write("세종대왕에게 질문해보세요!")

# 질문 입력
query = st.text_input("🗣 질문:")

# 버튼 클릭 시 실행
if st.button("질문하기") and query:
    context = "\n".join(search_docs(query))
    prompt = f"""
너는 조선의 제4대 임금 세종대왕이다. 아래 참고 문서를 바탕으로 조선시대 말투와 철학으로 질문에 답하라. 반드시 한국어로 답하라.

[참고 문서]
{context}

[질문]
{query}

[답변]
"""

    with st.spinner("👑 세종대왕이 답변을 고민 중입니다..."):
        answer = ask_llama3(prompt)

    # 히스토리에 저장
    st.session_state.history.append((query, answer))

# 출력 섹션
st.markdown("---")
for q, a in reversed(st.session_state.history):
    st.markdown(f"<p style='font-size:16px;'>🗣 <b>질문:</b> {q}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size:16px;'>👑 <b>세종대왕의 답변:</b> {a}</p>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)

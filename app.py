import streamlit as st
import uuid  # 🔑 고유 키 생성을 위해 사용
from search import search_docs
from ollama_generate import ask_llama3

# 🌙 다크 테마 설정
st.set_page_config(page_title="세종대왕 GPT", layout="wide")

st.markdown("""
<style>
body, .stApp {
    background-color: #000000 !important;
    color: #eeeeee !important;
}
header, .css-18ni7ap {
    background-color: #000000 !important;
}
h1, h2, h3, h4 {
    color: #FFD700;
}
.stTextInput > div > div > input {
    background-color: #333;
    color: white;
}
.stButton > button {
    background-color: #b22222;
    color: white;
    border-radius: 6px;
    font-weight: bold;
}
.stMarkdown {
    color: #ddd;
}
</style>
""", unsafe_allow_html=True)

# 🧠 세션 초기화
if "history" not in st.session_state:
    st.session_state.history = []
if "submit" not in st.session_state:
    st.session_state.submit = False
if "input_key" not in st.session_state:
    st.session_state.input_key = str(uuid.uuid4())

# 🎯 Enter 누르면 처리
def submit_query():
    st.session_state.submit = True

# 📐 레이아웃 구성
left, right = st.columns([1, 2.5])

# 💡 질문 예시
with left:
    st.markdown("## 💡 질문 예시")
    st.markdown("""
- 세종대왕은 누구인가요?
- 훈민정음은 왜 만들었나요?
- 장영실을 어떻게 생각하나요?
- 세종대왕의 업적은?
- 백성을 위해 무엇을 하셨나요?
- 가장 뿌듯했던 업적은 무엇인가요?
- 조선 시대 과학 발전에 대해 말씀해 주세요.
- 집현전은 왜 만들었나요?
- 학문을 왜 중시하셨나요?
- 음악과 예술에 관심이 있으셨나요?
- 백성의 삶을 위해 어떤 노력을 하셨나요?
    """)
    if st.button("🫐 전체 기록 삭제"):
        st.session_state.history.clear()
        st.rerun()

# 🤖 질문 영역
with right:
    st.markdown("# 👑 세종대왕 GPT")
    st.write("세종대왕에게 질문해보세요!")

    # 🔤 질문 입력창 (랜덤 키를 이용해 재생성 → 초기화 유도)
    query = st.text_input(
        "질문",
        placeholder="예: 훈민정음은 왜 만들었나요?",
        key=st.session_state.input_key,
        on_change=submit_query
    )

    if st.button("질문하기") or st.session_state.submit:
        if query.strip():
            with st.spinner("세종대왕이 답변을 숙고하고 있사옵니다..."):
                context = "\n".join(search_docs(query))
                prompt = f"""
너는 조선의 제4대 임금 세종대왕이다. 아래 참고 문서를 바탕으로 반드시 **조선 시대의 말투**로 질문에 대답하라.
- 반드시 **한글(한국어)** 로만 답하라.
- 말 끝은 항상 '~하노라', '~하였느니라', '~도다', '~느니라'로 마무리하라.
- 현대어, 영어, 외국어, 이모티콘, 친근한 표현은 절대 사용하지 말고, 위엄 있고 격식 있는 어투로 대답하라.
- 임금으로서 품위 있게, 격식 있고 엄숙한 말투로, 질문에 직접적이고 간결하게 응답하라.

[참고 문서]
{context}

[질문]
{query}

[답변]
"""
                answer = ask_llama3(prompt)
                st.session_state.history.append((query, answer))

        # 🔄 입력 필드 초기화용 랜덤 키 생성 → 자동 삭제 효과
        st.session_state.input_key = str(uuid.uuid4())
        st.session_state.submit = False
        st.rerun()

    # 💬 대화 출력
    for q, a in reversed(st.session_state.history):
        st.markdown(f"<h4>🗣 질문: {q}</h4>", unsafe_allow_html=True)
        st.markdown(f"<div style='padding:10px;background-color:#222;border-radius:10px;'>👑 <b>세종대왕의 답변:</b><br>{a}</div>", unsafe_allow_html=True)
        st.markdown("---")

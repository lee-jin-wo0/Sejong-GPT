import streamlit as st
from search import search_docs
from ollama_generate import ask_llama3

st.set_page_config(page_title="세종대왕 GPT", page_icon="👑")
st.title("👑 세종대왕 GPT")
st.write("세종대왕에게 질문해보세요!")

query = st.text_input("🗣 질문:")

if query:
    context = "\n".join(search_docs(query))
    prompt = f"""
너는 조선의 제4대 임금 세종대왕이다. 아래 참고 문서를 바탕으로 반드시 **한국어로** 답하라.
답변은 조선 시대 말투를 반영하되, 현대인이 이해할 수 있도록 공손하고 친절하게 작성하라.

[참고 문서]
{context}

[질문]
{query}

[답변]
"""

    with st.spinner("세종대왕이 답변을 고민 중입니다..."):
        answer = ask_llama3(prompt)
    st.markdown(f"👑 **세종대왕의 답변:**\n\n{answer}")

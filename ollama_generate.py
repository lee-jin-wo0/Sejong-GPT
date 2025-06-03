import requests

def ask_llama3(prompt: str) -> str:
    # 프롬프트 설정: 한글, 품위 있는 말투, 영어 금지, 반복 방지
    full_prompt = f"""\
너는 조선의 성군 세종대왕이다.
사용자의 질문에 대해 예의 바르고 품위 있는 조선시대 말투로,
오직 한글로만 대답해야 한다. 영어는 절대 사용하지 마라.
답변은 간결하고 핵심만 담되 진중하게 말하라.
자기소개는 생략하고 질문에만 답하라.

[질문]
{prompt}

[답변]
"""

    # LLaMA3 API 호출
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": full_prompt,
            "stream": False
        }
    )

    # 응답 받기 및 길이 제한
    answer = response.json().get("response", "").strip()
    if len(answer) > 800:
        answer = answer[:800].rstrip() + "..."

    return answer

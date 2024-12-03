import os
from openai import OpenAI

# 환경 변수에서 API 키 가져오기
openai_api_key = os.getenv("OPENAI_API_KEY")

if not openai_api_key:
    raise ValueError("API 키가 설정되지 않았습니다. 'config/env.py'를 확인하세요.")

def call_openai(system_prompt, user_prompt):
    client = OpenAI(api_key=openai_api_key)

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system",
            "content": system_prompt},                                                    # 시스템 프롬프트
            {"role": "user", 
            "content": user_prompt}                                                         # 질문
        ],
        #max_tokens=4000,                                                                   # 사용가능한 최대 토큰
        temperature=1,                                                                     # 생성할 문장의 다양성
        #n=2,                                                                              # 생성할 문장수
    )

    return response.choices[0].message.content
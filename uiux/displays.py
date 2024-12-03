import streamlit as st
import html

# 캐릭터와 말풍선을 표시하는 함수
def display_interaction(character_type, message, is_reviewer=False):
    """
    캐릭터와 메시지를 화면에 표시합니다.
    - character_type: "researcher", "writer", 또는 "reviewer"
    - message: 캐릭터가 말하는 메시지
    - is_reviewer: Reviewer인 경우 True
    """
    # 텍스트 안전 처리
    message = html.escape(message)

    # 정렬 방향 결정
    char_class = "reviewer" if is_reviewer else character_type
    image_path = f"assets/{character_type}.png"

    with st.container():
        st.markdown(
            f"""
            <div class="character {char_class}">
                <img src="{image_path}" alt="{character_type}">
                <div class="speech-bubble">{message}</div>
            </div>
            """,
            unsafe_allow_html=True
        )
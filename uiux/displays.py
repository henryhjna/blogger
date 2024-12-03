import streamlit as st
import html

def display_interaction(character_type, message, is_reviewer=False):
    """
    캐릭터와 메시지를 화면에 표시합니다.
    - character_type: "researcher", "writer", 또는 "reviewer"
    - message: 캐릭터가 말하는 메시지
    - is_reviewer: Reviewer인 경우 True
    """
    # 텍스트 안전 처리
    message = html.escape(message)

    # 캐릭터 위치에 따라 정렬 설정
    char_class = "reviewer" if is_reviewer else character_type
    image_path = f"assets/{character_type}.png"

    with st.container():
        # 좌우 정렬에 따라 열 구성
        col1, col2 = st.columns([1, 4] if is_reviewer else [4, 1])
        if is_reviewer:
            with col1:
                st.image(image_path, width=100)
            with col2:
                st.markdown(
                    f"""
                    <div class="character {char_class}">
                        <div class="speech-bubble">{message}</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
        else:
            with col1:
                st.markdown(
                    f"""
                    <div class="character {char_class}">
                        <div class="speech-bubble">{message}</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            with col2:
                st.image(image_path, width=100)

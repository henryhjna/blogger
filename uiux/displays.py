import streamlit as st
import html
import html2text

def display_interaction(character_type, message, is_reviewer=False):
    """
    캐릭터와 메시지를 화면에 표시합니다.
    - character_type: "researcher", "writer", 또는 "reviewer"
    - message: 캐릭터가 말하는 메시지
    - is_reviewer: Reviewer인 경우 True
    """
    # HTML을 Markdown 텍스트로 변환
    h = html2text.HTML2Text()
    h.ignore_links = True  # 링크는 제거
    h.body_width = 0       # 줄바꿈 제거
    clean_message = h.handle(message)

    # 캐릭터 이미지 경로
    image_path = f"assets/{character_type}.png"

    with st.container():
        # 열 구성을 통해 캐릭터와 말풍선 배치
        if is_reviewer:
            col1, col2 = st.columns([4, 1])  # 오른쪽 정렬
            with col1:
                st.markdown(f"<div class='speech-bubble'>{clean_message}</div>", unsafe_allow_html=True)
            with col2:
                st.image(image_path, width=100)
        else:
            col1, col2 = st.columns([1, 4])  # 왼쪽 정렬
            with col1:
                st.image(image_path, width=100)
            with col2:
                st.markdown(f"<div class='speech-bubble'>{clean_message}</div>", unsafe_allow_html=True)
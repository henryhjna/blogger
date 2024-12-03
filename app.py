import streamlit as st
import os
import html
from utils import get_openai_api_key
from collaboration.research import researcher_reviewer_collaboration
from collaboration.write import writer_reviewer_collaboration

# OpenAI API 키 로드
try:
    openai_api_key = get_openai_api_key()
except KeyError:
    st.error("API 키를 로드할 수 없습니다. 로컬에서는 'config/env.py'를 확인하세요.")
    raise

# CSS 로드
def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("static/styles.css")

# 캐릭터와 말풍선을 표시하는 함수
def display_interaction(character_type, message, is_reviewer=False):
    """
    캐릭터와 메시지를 화면에 표시합니다.
    - character_type: "researcher", "writer", 또는 "reviewer"
    - message: 캐릭터가 말하는 메시지
    - is_reviewer: Reviewer인 경우 True
    """
    char_class = "reviewer" if is_reviewer else character_type
    # 텍스트를 안전하게 처리
    message = html.escape(message)

    with st.container():
        # Streamlit 이미지를 사용하여 그림 표시
        col1, col2 = st.columns([1, 4] if is_reviewer else [4, 1])
        if is_reviewer:
            with col1:
                st.image(f"assets/{character_type}.png", width=100)
            with col2:
                st.markdown(
                    f"<div class='speech-bubble'>{message}</div>",
                    unsafe_allow_html=True
                )
        else:
            with col1:
                st.markdown(
                    f"<div class='speech-bubble'>{message}</div>",
                    unsafe_allow_html=True
                )
            with col2:
                st.image(f"assets/{character_type}.png", width=100)

# Streamlit 앱
st.title("블로그 작성기")
st.write("주제를 입력하면 LLM-based Multi Agents들이 블로그 글을 작성합니다.")

# 사용자 입력
topic_input = st.text_input("주제를 입력하세요 (예: '바르셀로나'):")

if st.button("블로그 글 생성"):
    if topic_input.strip():
        # 공통 주제를 설정
        st.write(f"선택한 주제: {topic_input}")
        common_topic = topic_input

        # Research 단계
        try:
            st.write("**Research Collaboration Process**")
            with st.spinner("Research Agent와 Reviewer Agent가 협업 중입니다..."):
                research_result = researcher_reviewer_collaboration(
                    common_topic,
                    max_iterations=3,
                    callback=lambda researcher_msg, reviewer_msg, iteration: (
                        display_interaction("researcher", researcher_msg),
                        display_interaction("reviewer", reviewer_msg, is_reviewer=True)
                    )
                )
            st.success("Research Collaboration 완료!")
            st.write(f"**최종 Research 결과:**\n{research_result}")
        except Exception as e:
            st.error(f"Research Collaboration 중 오류 발생: {e}")
            st.stop()

        # Write 단계
        try:
            st.write("**Writing Collaboration Process**")
            with st.spinner("Writer Agent와 Reviewer Agent가 협업 중입니다..."):
                blog_result = writer_reviewer_collaboration(
                    research_result,
                    max_iterations=3,
                    callback=lambda writer_msg, reviewer_msg, iteration: (
                        display_interaction("writer", writer_msg),
                        display_interaction("reviewer", reviewer_msg, is_reviewer=True)
                    )
                )
            st.success("Writing Collaboration 완료!")
            st.markdown(f"**생성된 블로그 글:**\n\n{blog_result}")
        except Exception as e:
            st.error(f"Writing Collaboration 중 오류 발생: {e}")
    else:
        st.warning("올바른 주제를 입력하세요.")

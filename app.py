import streamlit as st
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
        st.write("**Research Collaboration Process**")
        try:
            with st.spinner("Research Agent와 Reviewer Agent가 협업 중입니다..."):
                research_result = researcher_reviewer_collaboration(
                    common_topic,
                    callback=lambda researcher_msg, reviewer_msg, iteration: st.markdown(
                        f"""
                        <div class="character researcher">
                            <img src="assets/researcher.png" alt="Researcher">
                            <div class="speech-bubble">{researcher_msg}</div>
                        </div>
                        <div class="character reviewer">
                            <img src="assets/reviewer.png" alt="Reviewer">
                            <div class="speech-bubble">{reviewer_msg}</div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                )
            st.success("Research Collaboration 완료!")
            st.write(f"**최종 Research 결과:**\n{research_result}")
        except Exception as e:
            st.error(f"Research Collaboration 중 오류 발생: {e}")
            st.stop()

        # Write 단계
        st.write("**Writing Collaboration Process**")
        try:
            with st.spinner("Writer Agent와 Reviewer Agent가 협업 중입니다..."):
                blog_result = writer_reviewer_collaboration(
                    research_result,
                    callback=lambda writer_msg, reviewer_msg, iteration: st.markdown(
                        f"""
                        <div class="character researcher">
                            <img src="assets/writer.png" alt="Writer">
                            <div class="speech-bubble">{writer_msg}</div>
                        </div>
                        <div class="character reviewer">
                            <img src="assets/reviewer.png" alt="Reviewer">
                            <div class="speech-bubble">{reviewer_msg}</div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                )
            st.success("Writing Collaboration 완료!")
            st.markdown(f"**생성된 블로그 글:**\n\n{blog_result}")
        except Exception as e:
            st.error(f"Writing Collaboration 중 오류 발생: {e}")
    else:
        st.warning("올바른 주제를 입력하세요.")

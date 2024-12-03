import config.env
import streamlit as st
from collaboration.research import researcher_reviewer_collaboration
from collaboration.write import writer_reviewer_collaboration

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

        # Research Agent와 Reviewer Agent 협업 시작
        st.write("Research Agent와 Reviewer Agent의 협업을 시작합니다...")
        with st.spinner("주제에 대한 리서치를 진행 중입니다..."):
            try:
                research_result = researcher_reviewer_collaboration(common_topic)
                st.success("리서치 완료!")
                st.write(f"**리서치 결과:**\n{research_result}")
            except Exception as e:
                st.error(f"리서치 중 오류 발생: {e}")
                st.stop()

        # Research 결과를 기반으로 글 작성
        st.write("블로그 글을 작성 중입니다...")
        with st.spinner("Writer Agent와 Reviewer Agent가 협업 중입니다..."):
            try:
                blog_result = writer_reviewer_collaboration(research_result)
                st.success("블로그 글 작성 완료!")
                st.markdown(f"**생성된 블로그 글:**\n\n{blog_result}")
            except Exception as e:
                st.error(f"블로그 글 작성 중 오류 발생: {e}")
    else:
        st.warning("올바른 주제를 입력하세요.")
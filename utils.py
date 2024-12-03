import os
import streamlit as st

def get_openai_api_key():
    """
    OpenAI API 키를 로드합니다.
    로컬 환경에서는 os.environ 또는 config/env.py를 사용하고,
    Streamlit Cloud에서는 st.secrets를 우선 사용합니다.
    """
    # 1. 로컬 환경: os.environ에서 키 확인
    if "OPENAI_API_KEY" in os.environ:
        return os.environ["OPENAI_API_KEY"]

    # 2. 로컬 환경: config/env.py에서 설정
    try:
        import config.env  # config/env.py에서 환경 변수를 설정
        return os.environ["OPENAI_API_KEY"]
    except ImportError:
        pass  # env.py가 없으면 넘어감

    # 3. Streamlit Cloud 환경: st.secrets에서 확인
    try:
        if "OPENAI_API_KEY" in st.secrets:
            return st.secrets["OPENAI_API_KEY"]
    except FileNotFoundError:
        pass  # secrets.toml이 없는 경우 넘어감

    # 4. 키를 찾지 못한 경우 에러 발생
    raise KeyError("API 키를 로드할 수 없습니다. 'config/env.py' 또는 환경 변수를 확인하세요.")

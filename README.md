# Multi-Agent Blog Generator

이 프로젝트는 다중 에이전트를 활용하여 주제를 입력받고 블로그 글을 생성하는 Streamlit 애플리케이션입니다.

## 사용 방법

1. 주제를 입력합니다.
2. `블로그 글 생성` 버튼을 클릭합니다.
3. 다중 에이전트가 협업하여 블로그 글을 생성합니다.

## 설치 방법

1. 저장소 클론: git clone https://github.com/your-username/your-repo-name.git
2. 종속성 설치: pip install -r requirements.txt
3. 환경설정
    3.1. `config/env.py` 파일을 생성하고, OpenAI API 키를 설정합니다:
        ```python
        import os
        os.environ["OPENAI_API_KEY"] = "your_openai_api_key"
4. 앱 실행

## 프로젝트 디렉토리
project/
│
├── app.py                    # Streamlit 애플리케이션 메인 코드
├── agents/                   # 모듈 디렉토리
│   ├── __init__.py           # (필요시 추가)
│   ├── find_topic.py         # find_topic 관련 코드
│   └── ...                   # 기타 에이전트 코드
├── collaboration/            # 협업 관련 모듈 디렉토리
│   ├── __init__.py           # (필요시 추가)
│   ├── research.py           # research 관련 코드
│   └── write.py              # 작성 관련 코드
├── requirements.txt          # Python 종속성 패키지 목록
└── README.md                 # 프로젝트 설명

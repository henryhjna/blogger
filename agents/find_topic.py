from pytrends.request import TrendReq
from common.call_openai import call_openai

def fetch_trending_topics_google():
    """
    Google Trends에서 Pytrends를 사용하여한국의 실시간 트렌드 데이터를 가져오는 함수.  
    Returns:
        list: 트렌드 데이터를 포함하는 딕셔너리 리스트. 각 항목은 title, description, link 정보를 포함합니다.
    """
    try:
        pytrends = TrendReq(hl='ko', tz=540)  # Google Trends 요청 객체 생성 # 한국어와 한국 시간대 설정
        trending_searches_df = pytrends.trending_searches(pn='south_korea') # 실시간 급상승 검색어 데이터 가져오기
        trending_topics = trending_searches_df[0].tolist()  # 결과 데이터 처리 (주제 제목 리스트로 변환) # 첫 번째 열(주제 제목)을 리스트로 변환
        return trending_topics
    
    except Exception as e:
        print(f"오류 발생: {e}")
        return []
    

def find_common_topic(topics):
    """
    call_openai 함수를 사용하여 GPT를 호출하고, 주제 리스트에서 공통된 주제를 도출하는 함수.
    Args:
        topics (list): 트렌드 주제 제목 리스트.
    Returns:
        str: 공통된 주제를 나타내는 키워드.
    """
    if not topics:
        print("트렌드 주제 리스트가 비어 있습니다.")
        return None

    # 시스템 프롬프트
    system_prompt = """
    Role: 당신은 주어진 주제 리스트에서 서로 공통점이 있고, 블로그 포스트로 작성하기 가장 적합한 하나의 항목을 선택하는 전문가입니다.
    Goal: 온라인 검색을 기반으로 아래에 제공된 주제 리스트 중 콘텐츠로 작성하기 가장 적합한 주제 하나를 선택합니다. 
    Backstory: 
    사용자는 인기 있는 주제를 기반으로 블로그 콘텐츠를 작성하려고 합니다. 
    선택 기준은 주제의 대중성, 흥미, 그리고 현재의 트렌드와 관련성이 높아야 합니다.

    Output Requirements:
    1. 리스트 중에서 하나의 항목을 선택하여 반환합니다.
    2. 온라인에 정보가 많은 항목에 선택 가중치를 줍니다.
    3. 결과는 선택된 항목 그대로 작성해야 합니다.
    4. 새롭게 생성된 단어나 리스트 외의 항목은 허용되지 않습니다.
    """

    # 사용자 프롬프트
    user_prompt = f"""
    다음은 현재 인기 있는 주제 리스트입니다:
    {', '.join(topics)}

    위 리스트에서 가장 적합한 항목을 하나 선택하세요.
    """

    try:
        # GPT 호출
        common_topic = call_openai(system_prompt, user_prompt)
        return common_topic

    except Exception as e:
        print(f"오류 발생: {e}")
        return None

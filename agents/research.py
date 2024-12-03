from common.call_openai import call_openai

def research_agent(topic, feedback, feedback_history):
    """
    GPT 모델을 사용하여 주제에 대한 심층적인 리서치를 수행하는 함수.
    Args:
        topic (str): 리서치할 주제.
    Returns:
        str: 리서치 결과 텍스트.
    """
    # 시스템 프롬프트
    system_prompt = """
    [Role]
    당신은 블로그 콘텐츠 작성을 위한 전문 리서치 에이전트입니다.
    주어진 주제에 대해 인터넷 검색을 기반으로 철저하고 심층적인 리서치를 수행합니다.
    당신의 역할은 데이터를 분석하고 체계적으로 정리하여 사용자가 블로그 콘텐츠에 바로 활용할 수 있도록 돕는 것입니다.

    [Goal]
    주제를 바탕으로 글의 제목 선정: 주제와 관련되어서 타겟독자(성별, 연령대, 페르소나)를 설정하고, 가장 독자의 흥미를 끌 수 있는 구체적인 제목을 선정합니다.
    인터넷 검색 수행: 주제와 관련된 최신 정보, 신뢰할 수 있는 통계, 관련 사례 및 독특한 관점을 수집합니다.
    결과 구조화: 독자가 쉽게 이해할 수 있도록 명확하고 체계적인 포맷(예: 개요, 세부 설명, 키 포인트, 데이터 인용)을 사용하여 작성합니다.
    흥미 요소 포함: 독자를 끌어들이기 위한 흥미로운 정보나 스토리를 추가합니다.
    즉시 활용 가능성: 리서치 결과는 블로그 콘텐츠 작성에 바로 사용할 수 있도록 완성된 형태로 제공해야 합니다.

    [Backstory]
    사용자는 다양한 주제에 대해 블로그를 운영하는 콘텐츠 크리에이터입니다.
    그들은 다음과 같은 사항을 요구합니다:

    주제의 배경과 역사적 또는 문화적 맥락 제공.
    신뢰할 수 있는 통계와 데이터 인용.
    독자들이 관심을 가지게 할 흥미로운 사실 또는 트렌드 포함.
    블로그 작성에 필요한 논리적이고 구조화된 프레임워크 제안.
    당신은 사용자가 요구하는 품질과 깊이를 제공하기 위해 최선을 다해야 합니다.

    [Output Requirements]
    1. 만약 Reviewer의 수정 요구사항(지시)이 있다면 따르세요.
    2. 온라인을 검색한 결과를 기반으로 사실만 작성하세요. 
    3. 반드시 다음 포맷을 따르세요:
        1. 타겟독자(성별, 연령대, 페르소나):
        2. 제목:
        3. 제목 선정 배경:
        4. 관련 통계 또는 데이터:
        5. 흥미로운 정보:
        6. 독자를 끌어들이기 위한 흥미로운 포인트:
    4. 각 항목은 구체적이고 간결한 문장으로 작성해야 합니다.
    5. Reviewer의 수정 요구사항(지시)에 동의하지 않거나 궁금한 사항은 글의 마지막에 별도로 표시하고 질문하세요.
    """

    # 사용자 프롬프트
    user_prompt = f"""
    다음 주제에 대해 블로그를 작성할 수 있도록 리서치 결과를 제공해주세요: 
    "{topic}"
    
    Reviewer의 이번 요구사항은 다음과 같습니다.
    "{feedback}

    Reviewer의 이전 요구사항들의 History는 다음과 같습니다.
    "{feedback_history}"
    """
    try:
        # GPT 호출
        research_result = call_openai(system_prompt, user_prompt)
        return research_result
    except Exception as e:
        print(f"오류 발생: {e}")
        return None
    

def reviewer_agent(research_result):
    """
    Research Agent가 생성한 리서치 결과를 검토하고 피드백을 제공하는 Reviewer Agent.
    Args:
        research_result (str): Research Agent의 리서치 결과.
        topic (str): 검토할 주제.
    Returns:
        str: Reviewer Agent가 지시하는 수정사항.
    """
    # 시스템 프롬프트
    system_prompt = """
    [Role]
    당신은 블로그 콘텐츠 품질 관리 전문가입니다. 
    Research Agent가 작성한 리서치 결과를 검토하고, 콘텐츠 품질을 평가해서, 수정사항을 지시합니다.

    [Goal]
    1. 온라인을 검색해서 리서치 결과에 대한 팩트를 체크하고, 수정 사항을 지시합니다.
    2. 리서치 결과가 더 많은 블로그 이용자를 불러올 수 있도록 검토하여, 수정 사항을 지시합니다.
    
    [Backstory]
    사용자는 블로그 콘텐츠를 작성하며, 리서치 결과는 바로 사용할 수 있어야 합니다. 

    Output Requirements:
    1. 팩트가 다른 경우, 지적해주세요.
    2. 리서치 결과에서 포맷이 제대로 지켜지지 않은 경우, 지적해주세요.
    3. 리서치 결과에서 수정해야 할 사항들을 하나씩 지시해주세요.
    4. 각 지시사항은 구체적이고 간결해야 합니다.
    5. Research Agent의 의견이나 질문이 있다면 응답하거나 감안해주세요.
    """

    # 사용자 프롬프트
    user_prompt = f"""
    다음은 검토할 리서치 결과입니다:
    {research_result}
    """
    try:
        # GPT 호출
        improved_result = call_openai(system_prompt, user_prompt)
        return improved_result
    except Exception as e:
        print(f"Reviewer Agent 오류 발생: {e}")
        return research_result  # 개선이 실패하면 기존 결과를 반환
    

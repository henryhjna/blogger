from common.call_openai import call_openai


def blog_writer(research_result, feedback, feedback_history):
    system_prompt = """
    너는 친근하고 체계적인 블로그 작성을 전문으로 하는 작가야. 
    글을 작성할 때 다음의 규칙을 따라야 해:

    1. 만약 Reviewer의 수정 요구사항(지시)이 있다면 따르세요.
    2. 온라인을 검색한 결과를 기반으로 사실만 작성하세요. 
    3. 구어체와 emoji를 사용하여 독자가 친근함을 느낄 수 있게 작성해.
    4. 글은 1000단어 내외로 작성해.
    5. 주제와 타겟 독자를 명확히 하고, 독자가 이해하기 쉬운 구조로 작성해.
    6. 가독성을 높이기 위해:
        - 짧고 명확한 문장을 사용하고,
        - 문단을 3~4문장 단위로 나누며,
        - 서브헤드라인을 활용해 섹션을 구분해.
    7. 필요할 경우 글의 이해를 돕기 위해 이미지, 그래프 등의 시각적 자료를 삽입할 위치와 어떤 시각적 자료인지를 구체적으로 제안해.
    8. Reviewer의 수정 요구사항(지시)에 동의하지 않거나 궁금한 사항은 글의 마지막에 별도로 표시하고 질문하세요.

    작성 결과는 다음의 구조를 따라야 해. 시각자료가 필요한 위치에 [시각자료 번호#]의 형식으로 삽입해 어느 위치에 자료가 들어가는지 알려주세요.:
    [제목]
    [소개]
    [섹션 1: 서브헤드라인]
    [내용]
    [섹션 2: 서브헤드라인]
    [내용]
    [섹션 3: 서브헤드라인]
    [내용]
    [섹션 4: 서브헤드라인]
    [내용]
    [결론]
    [필요한 시각자료 목록]

    필요한 시각자료 목록은 "[시각자료 번호#] 시각자료 내용"의 형식으로 적어서 본문에서 삽입한 것과 동일한 것임을 식별 가능하게 해주세요.
    """
    
    user_prompt = f"""
    [[[아래 리서치 결과를 바탕으로 위의 규칙을 따라 블로그 글을 작성해.]]]
    {research_result}

    [[[Reviewer의 이번 요구사항은 다음과 같습니다.]]] 
    "{feedback}

    [[[Reviewer의 이전 요구사항들의 History는 다음과 같습니다.]]]
    "{feedback_history}"
    """
    
    # call_openai 함수를 사용하여 OpenAI API 호출
    try:
        response = call_openai(system_prompt, user_prompt)
        return response
    except Exception as e:
        return f"블로그 글 생성 중 오류 발생: {e}"
    

def blog_reviewer(blog_post):
    """
    블로그 글을 검토하고 피드백을 제공하는 에이전트.
    Args:
        blog_post (str): blog_writer가 작성한 블로그 글.
        research_result (str): 블로그 작성에 사용된 리서치 결과.
    Returns:
        str: 리뷰와 개선 사항.
    """
    system_prompt = """
    너는 블로그 글을 검토하고 피드백을 제공하는 리뷰어야.
    아래의 규칙을 따라 작성된 블로그 글을 검토하고, 개선 사항을 제안해.

    검토 기준:
    1. 팩트가 다른 경우, 지적해주세요.
    2. 글의 구조가 규칙에 맞게 작성되었는지 확인해.
    3. 블로그 글(대략 1000단어)의 적절한 길이에 맞게 작성되었는지 확인해.
    4. 구어체가 자연스럽고 독자 친화적으로 작성되었는지 평가해.
    5. 가독성을 높이기 위한 요소(문단 길이, 문장 간결성, 서브헤드라인 사용)가 잘 구현되었는지 확인해.
    6. 추가적인 시각적 자료 제안이 적절한지 검토해.
    
    작성 결과:
    1. 전체적인 평가.
    2. 긍정적인 점.
    3. 개선할 점(구체적으로 작성).
    4. 추가적으로 추천하는 시각 자료가 있다면 포함해.
    5. Research Agent의 의견이나 질문이 있다면 응답하거나 감안해.
    """

    user_prompt = f"""  
    블로그 글:
    {blog_post}
    
    기준에 따라 블로그 글을 검토하고 피드백을 작성해줘.
    """
    
    # call_openai 함수를 사용하여 OpenAI API 호출
    try:
        response = call_openai(system_prompt, user_prompt)
        return response
    except Exception as e:
        return f"블로그 글 리뷰 중 오류 발생: {e}"

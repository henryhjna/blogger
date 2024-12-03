from common.call_openai import call_openai

def image_locator(blog_post):
    system_prompt = """
    너는 사진 자료를 찾는 데 전문적인 연구원이야. 주어진 텍스트를 기반으로 필요한 사진들을 검색하여,
    각 사진의 이름, 링크, 설명을 제공해야 해.

    [output format]
    1. 사진 이름
    2. 사진 링크
    3. 사진 설명

    [requirements]
    1. 실제 온라인에 존재하는 사진이어야 합니다.
    2. output format을 정확히 지켜야 합니다.
    3. 사진이 없으면 "없음"이라고 명시하세요.
    """
    
    user_prompt = f"""
    [[[아래 블로그 글 -> 사진목록에 나와있는 이미지 요청 사항을 기반으로, 가장 적합한 사진의 링크를 검색하여 제공하세요.]]]
    {blog_post}
    """
    
    # call_openai 함수를 사용하여 OpenAI API 호출
    try:
        response = call_openai(system_prompt, user_prompt)
        return response
    except Exception as e:
        return f"블로그 글 생성 중 오류 발생: {e}"
    

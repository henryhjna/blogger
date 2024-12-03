from common.call_openai import call_openai

def image_locator(blog_post):
    system_prompt = """
    너는 사진자료에 대해 리서치를 전문적으로 수행하는 연구원이야. 주어진 목록에 대해서 온라인을 검색하고, 가장 적합한 사진의 링크를 찾아서 제시해야해.

    [output format]
    1. 사진 이름
    2. 사진 링크
    3. 사진 설명

    [requirements]
    1. 실제 온라인에 존재해야 해
    2. output format을 충실히 지켜야해
    3. 없으면 없다고 명시해야해.
    """
    
    user_prompt = f"""
    [[[아래 블로그 리포트에 나와있는 사진 목록에 대해 온라인을 검색하고, 가장 적합한 사진의 링크를 제시해주세요.]]]
    {blog_post}
    """
    
    # call_openai 함수를 사용하여 OpenAI API 호출
    try:
        response = call_openai(system_prompt, user_prompt)
        return response
    except Exception as e:
        return f"블로그 글 생성 중 오류 발생: {e}"
    

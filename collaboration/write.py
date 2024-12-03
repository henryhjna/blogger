from agents.writer import blog_writer
from agents.writer import blog_reviewer

def writer_reviewer_collaboration(research_result, max_iterations=3):
    """
    Research Agent와 Reviewer Agent가 협력하여 최종 결과를 도출하는 함수.
    Args:
        topic (str): 리서치할 주제.
        max_iterations (int): 최대 협업 횟수.
    Returns:
        str: 최종 협업 결과.
    """
    # 초기 Writer Agent의 결과 생성
    research_result = blog_writer(research_result, feedback="", feedback_history=[])
    print("Blog Writer의 초안:")
    print(research_result)
    
    feedback_history = []
    
    for iteration in range(max_iterations):
        print(f"\n[Iteration {iteration + 1}] Reviewer Agent 검토 및 피드백 중...")

        # Reviewer Agent의 피드백 생성
        feedback = blog_reviewer(research_result)
        feedback_history.append(feedback)  # 피드백 기록
        
        print("Reviewer Agent의 피드백:")
        print(feedback)
        
        print(f"\n[Iteration {iteration + 1}] Research Agent 피드백 반영 중...")
        
        # Writer Agent가 피드백을 반영하여 결과 개선
        blog_result = blog_writer(research_result, feedback, feedback_history[:-1])
        print("Writer Agent의 개선된 결과:")
        print(blog_result)

    return blog_result

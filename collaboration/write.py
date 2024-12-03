from agents.writer import blog_writer
from agents.writer import blog_reviewer

def writer_reviewer_collaboration(research_result, max_iterations=3, callback=None):
    """
    Writer Agent와 Reviewer Agent가 협력하여 최종 블로그 글을 작성하는 함수.
    Args:
        research_result (str): 리서치 결과.
        max_iterations (int): 최대 협업 횟수.
        callback (function): 각 단계의 메시지를 처리할 콜백 함수.
    Returns:
        str: 최종 블로그 글.
    """
    blog_result = blog_writer(research_result, feedback="", feedback_history=[])
    feedback_history = []

    for iteration in range(max_iterations):
        feedback = blog_reviewer(blog_result)
        feedback_history.append(feedback)

        # 콜백 함수 호출 (진행 상황 표시)
        if callback:
            writer_msg = f"Writer: Iteration {iteration + 1} - {blog_result}"
            reviewer_msg = f"Reviewer Feedback: {feedback}"
            callback(writer_msg, reviewer_msg, iteration)

        blog_result = blog_writer(blog_result, feedback, feedback_history[:-1])

    return blog_result

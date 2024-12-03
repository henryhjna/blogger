from agents.research import research_agent
from agents.research import reviewer_agent

def researcher_reviewer_collaboration(topic, max_iterations=3, callback=None):
    """
    Research Agent와 Reviewer Agent가 협력하여 최종 결과를 도출하는 함수.
    Args:
        topic (str): 리서치할 주제.
        max_iterations (int): 최대 협업 횟수.
        callback (function): 각 단계의 메시지를 처리할 콜백 함수.
    Returns:
        str: 최종 협업 결과.
    """
    research_result = research_agent(topic, feedback="", feedback_history=[])
    feedback_history = []

    for iteration in range(max_iterations):
        feedback = reviewer_agent(research_result)
        feedback_history.append(feedback)

        # 콜백 함수 호출 (진행 상황 표시)
        if callback:
            researcher_msg = f"컨텐츠 연구원 {iteration + 1}회차 조사: \n{research_result}"
            reviewer_msg = f"편집자 피드백: \n{feedback}"
            callback(researcher_msg, reviewer_msg, iteration)

        research_result = research_agent(topic, feedback, feedback_history[:-1])

    return research_result

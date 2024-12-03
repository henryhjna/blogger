from agents.find_topic import fetch_trending_topics_google
from agents.find_topic import find_common_topic
from collaboration.research import researcher_reviewer_collaboration
from collaboration.write import writer_reviewer_collaboration

if __name__ == "__main__":
    common_topic = "바르셀로나"
    print(f"공통 주제: {common_topic}")

    # 3. Research Agent와 Reviewer Agent의 협업 시작
    print("\nResearch Agent와 Reviewer Agent의 협업을 시작합니다...")
    research_result = researcher_reviewer_collaboration(common_topic)

    # 4. Research를 기반으로 블로그 글 작성
    print("\nResearch Agent와 Reviewer Agent의 협업을 시작합니다...")
    blog_result = writer_reviewer_collaboration(research_result)

    print("\n블로그 글을 작성하고 있습니다.")
    print(f"블로그: \n{blog_result}")

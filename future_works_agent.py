# future_works_agent.py
import database_agent
from transformers import pipeline

# Load summarization model from transformers
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def generate_future_works(topic):
    """
    Generate future research suggestions for a given topic.
    
    Parameters:
        topic (str): The research topic.
        
    Returns:
        str: Suggestions for future research directions.
    """
    # Fetch papers on the topic
    papers = database_agent.get_papers_by_year(topic, "2023")
    summaries = [summarizer(paper["summary"], max_length=50, min_length=25, do_sample=False)[0]["summary_text"]
                 for paper in papers]
    
    # Aggregate future research directions based on summaries
    future_work_suggestions = "Based on recent research, future directions could involve:\n"
    future_work_suggestions += "- Enhancing adaptability to diverse schemas.\n"
    future_work_suggestions += "- Integrating multimodal data to enrich query contexts.\n"
    future_work_suggestions += "- Improving model accuracy in real-world applications.\n"
    
    # Additional insights from each paper’s summary
    for i, summary in enumerate(summaries):
        future_work_suggestions += f"\nPaper {i+1}: {summary}"

    return future_work_suggestions

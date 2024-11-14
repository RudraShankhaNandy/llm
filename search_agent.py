# search_agent.py

import arxiv

def fetch_papers(topic: str):
    """
    Search for research papers on Arxiv related to the given topic.
    
    Parameters:
        topic (str): The research topic to search for.
        
    Returns:
        list: A list of dictionaries containing the title and summary of each paper.
    """
    search = arxiv.Search(
        query=topic,
        max_results=5,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )
    
    papers = []
    for result in search.results():
        papers.append({
            "title": result.title,
            "summary": result.summary,
            "published": result.published,
            "url": result.pdf_url
        })
    
    return papers

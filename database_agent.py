# database_a
from neo4j import GraphDatabase
import os

# Load Neo4j credentials from environment variables
uri = os.getenv("NEO4J_URI")
username = os.getenv("NEO4J_USERNAME")
password = os.getenv("NEO4J_PASSWORD")
driver = GraphDatabase.driver(uri, auth=(username, password))

def store_papers(papers, topic):
    """
    Store research papers in the Neo4j database.
    
    Parameters:
        papers (list): A list of dictionaries containing paper data.
        topic (str): The topic associated with the papers.
    """
    with driver.session() as session:
        for paper in papers:
            session.write_transaction(_create_paper_node, paper, topic)

def _create_paper_node(tx, paper, topic):
    query = """
    MERGE (p:Paper {title: $title, summary: $summary, published: $published, url: $url})
    SET p.topic = $topic
    """
    tx.run(query, title=paper["title"], summary=paper["summary"],
           published=paper["published"], url=paper["url"], topic=topic)

def get_papers_by_year(topic, year):
    """
    Retrieve research papers from the database based on topic and year.
    
    Parameters:
        topic (str): The research topic.
        year (str): The year to filter papers by.
        
    Returns:
        list: A list of dictionaries containing paper data for the given year.
    """
    with driver.session() as session:
        result = session.read_transaction(_query_papers_by_year, topic, year)
    return result

def _query_papers_by_year(tx, topic, year):
    query = """
    MATCH (p:Paper) 
    WHERE p.topic = $topic AND p.published CONTAINS $year
    RETURN p.title AS title, p.summary AS summary, p.published AS published, p.url AS url
    """
    results = tx.run(query, topic=topic, year=year)
    return [{"title": record["title"], "summary": record["summary"],
             "published": record["published"], "url": record["url"]} for record in results]

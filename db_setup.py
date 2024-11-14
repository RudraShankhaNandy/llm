from neo4j import GraphDatabase
import os

uri = os.getenv("NEO4J_URI")
username = os.getenv("NEO4J_USERNAME")
password = os.getenv("NEO4J_PASSWORD")
driver = GraphDatabase.driver(uri, auth=(username, password))

def create_fulltext_index(tx):
    query = "CREATE FULLTEXT INDEX paper_index IF NOT EXISTS FOR (n:Paper) ON EACH [n.title, n.content]"
    tx.run(query)

def setup_db():
    with driver.session() as session:
        session.write_transaction(create_fulltext_index)

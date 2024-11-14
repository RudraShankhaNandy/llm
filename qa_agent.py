# qa_agent.py
import database_agent  # Ensure this is imported correctly
from embedder import generate_embeddings
from llama import load_model
from sklearn.metrics.pairwise import cosine_similarity

# Load the model and tokenizer for question answering
model, tokenizer = load_model("llama-3.1")

def answer_question(topic, question):
    """
    Answer questions based on a specific research topic using embeddings.
    
    Parameters:
        topic (str): The research topic.
        question (str): The user's question.
        
    Returns:
        str: The answer generated by the model.
    """
    papers = database_agent.get_papers_by_year(topic, "2023")  # Example: Retrieve recent papers
    embeddings = [generate_embeddings(paper["summary"]) for paper in papers]
    
    # Generate embedding for the question
    question_embedding = generate_embeddings(question)
    
    # Find the most relevant paper based on cosine similarity (basic example)
    similarities = [cosine_similarity(question_embedding, e) for e in embeddings]
    best_paper = papers[similarities.index(max(similarities))]
    
    # Generate answer using the model
    inputs = tokenizer.encode(f"Question: {question}\nContext: {best_paper['summary']}", return_tensors="pt")
    outputs = model.generate(inputs, max_length=200)
    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    return answer

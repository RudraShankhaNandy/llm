from langchain_ollama import OllamaEmbeddings

def generate_embeddings(text):
    embedding_model = OllamaEmbeddings(model="mxbai-embed-large")
    return embedding_model.embed(text)

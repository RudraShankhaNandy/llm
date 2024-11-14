from fastapi import FastAPI, HTTPException
from agent import search_agent, database_agent, qa_agent, future_works_agent

app = FastAPI()

@app.get("/search")
def search_topic(topic: str):
    papers = search_agent.search(topic)
    if not papers:
        raise HTTPException(status_code=404, detail="No papers found")
    return papers

@app.post("/qa")
def question_answer(topic: str, question: str):
    answers = qa_agent.answer_question(topic, question)
    return {"answers": answers}

@app.post("/summarize")
def summarize(topic: str):
    summary = database_agent.summarize_topic(topic)
    return {"summary": summary}

@app.post("/future_works")
def future_research(topic: str):
    suggestions = future_works_agent.generate_future_works(topic)
    return {"suggestions": suggestions}

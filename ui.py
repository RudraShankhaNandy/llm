# ui.py
import streamlit as st
from agent.search_agent import fetch_papers
from database_agent import add_papers, get_papers_by_year
from qa_agent import answer_question
from future_works_agent import generate_future_works

# Streamlit page configuration
st.set_page_config(page_title="Academic Research Assistant", layout="wide")

# Title and Instructions
st.title("Academic Research Paper Assistant")
st.write("This application assists you in finding, summarizing, and analyzing research papers on a given topic.")
st.write("Enter a topic to fetch relevant research papers and interact with them through Q&A.")

# Sidebar Input
topic = st.sidebar.text_input("Enter Research Topic", value="Text-to-SQL")
if st.sidebar.button("Fetch Papers"):
    with st.spinner("Fetching papers..."):
        papers = fetch_papers(topic)
        add_papers(papers)  # Store papers in the database
        st.sidebar.success("Papers added successfully.")

# Display Papers
st.subheader(f"Research Papers for Topic: {topic}")
st.write("The list below shows the papers fetched for the selected topic. Choose a paper to ask questions or view details.")

# Retrieve papers for display
papers = get_papers_by_year(topic, "2023")  # Example: Displaying papers from 2023

# Display papers with selection options
selected_paper = None
if papers:
    paper_titles = [f"{paper['title']} - {paper['authors']}" for paper in papers]
    selected_title = st.selectbox("Select a Paper to Interact With", options=paper_titles)
    
    # Find the paper based on title selection
    selected_paper = next((paper for paper in papers if paper['title'] in selected_title), None)
    
    if selected_paper:
        st.write("### Paper Details")
        st.write(f"**Title:** {selected_paper['title']}")
        st.write(f"**Authors:** {selected_paper['authors']}")
        st.write(f"**Year:** {selected_paper['year']}")
        st.write("#### Abstract")
        st.write(selected_paper['summary'])
else:
    st.write("No papers available for this topic. Try fetching papers using the sidebar.")

# Question Answering Section
st.write("### Ask a Question")
question = st.text_input("Enter your question about the selected paper")

if st.button("Get Answer"):
    if selected_paper and question:
        with st.spinner("Generating answer..."):
            answer = answer_question(topic, question)
            st.write("#### Answer")
            st.write(answer)
    else:
        st.warning("Please select a paper and enter a question.")

# Future Work Suggestions
st.write("### Generate Future Work Ideas")
if st.button("Generate Future Research Directions"):
    with st.spinner("Generating future research ideas..."):
        future_works = generate_future_works(topic)
        st.write("#### Future Research Directions")
        st.write(future_works)

# Timeline Summary
st.write("### Research Timeline")
start_year, end_year = st.slider("Select a timeframe for summarizing research", 2018, 2023, (2018, 2023))

if st.button("Summarize Research"):
    with st.spinner("Summarizing research..."):
        summary = []
        for year in range(start_year, end_year + 1):
            papers_year = get_papers_by_year(topic, str(year))
            if papers_year:
                summary.extend([f"{year} - {paper['title']}" for paper in papers_year])
        
        st.write("#### Timeline Summary")
        st.write("\n".join(summary) if summary else "No papers found for the selected timeframe.")

# Footer
st.markdown("---")
st.write("Academic Research Assistant | Powered by LLMs and Neo4j")


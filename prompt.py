from langchain.prompts import ChatPromptTemplate

qa_prompt = ChatPromptTemplate.from_template("Answer the question based on the document: {document}")

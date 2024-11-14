FROM python:3.9

# Install necessary system dependencies
RUN apt-get update && apt-get install -y libgl1-mesa-glx

# Install Python dependencies
COPY requirements.txt /project-root/
WORKDIR /project-root
RUN pip install -r requirements.txt

# Copy the project files
COPY . /project-root//

# Expose Streamlit and FastAPI ports
EXPOSE 8501 8000

# Start FastAPI and Streamlit using Docker Compose
CMD ["sh", "-c", "uvicorn api:app --host 0.0.0.0 --port 8000 & streamlit run ui.py"]

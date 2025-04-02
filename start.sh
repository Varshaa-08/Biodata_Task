#!/bin/bash

# Start FastAPI backend in the background
nohup uvicorn backend:app --host 0.0.0.0 --port 8000 &

# Wait for the backend to start
sleep 5

# Start Streamlit frontend
nohup streamlit run app.py --server.port 8501 --server.address 0.0.0.0 &

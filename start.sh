#!/bin/bash

# Stop any existing instances of FastAPI and Streamlit
pkill -f "uvicorn backend:app"
pkill -f "streamlit run app.py"

# Start FastAPI backend
uvicorn backend:app --host 0.0.0.0 --port 10000 &

# Start Streamlit frontend
streamlit run app.py --server.port 8501 --server.address 0.0.0.0

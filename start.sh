#!/bin/bash

# Start FastAPI backend
gunicorn -w 4 -k uvicorn.workers.UvicornWorker backend:app --bind 0.0.0.0:8000 &

# Start Streamlit frontend
streamlit run app.py --server.port=8501 --server.address=0.0.0.0

#!/bin/bash

# Make sure the script is executable
chmod +x start.sh

# Start FastAPI backend with Gunicorn (2 workers for efficiency)
gunicorn -w 2 -k uvicorn.workers.UvicornWorker backend:app --bind 0.0.0.0:8000 &

# Wait a bit to ensure backend starts
sleep 5

# Start Streamlit app
streamlit run app.py --server.port 8501 --server.address 0.0.0.0


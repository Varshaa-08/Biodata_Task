#!/bin/bash

echo "Stopping FastAPI and Streamlit..."

# Kill FastAPI process
pkill -f "uvicorn backend:app"

# Kill Streamlit process
pkill -f "streamlit run app.py"

echo "Stopped successfully!"

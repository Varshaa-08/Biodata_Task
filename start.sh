#!/bin/bash

# Make sure the script is executable
chmod +x start.sh

# Start FastAPI backend with Gunicorn (2 workers)
gunicorn -w 2 -k uvicorn.workers.UvicornWorker backend:app --bind 0.0.0.0:8000


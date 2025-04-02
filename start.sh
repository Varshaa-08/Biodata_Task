#!/bin/bash

# Start FastAPI backend
gunicorn -w 4 -k uvicorn.workers.UvicornWorker backend:app --bind 0.0.0.0:8000 &



#!/bin/bash
set -e

echo "Starting AI Coding Assistant..."

# Start backend in background
echo "Starting backend server..."
uvicorn backend.app:app --host 0.0.0.0 --port 8000 &
BACKEND_PID=$!

# Wait for backend to start
sleep 5

# Start frontend
echo "Starting frontend..."
streamlit run frontend/main.py --server.port=8501 --server.address=0.0.0.0

# Cleanup
trap "kill $BACKEND_PID" EXIT

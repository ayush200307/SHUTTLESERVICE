#!/bin/bash
# macOS/Linux shell script to run the Shuttle Management System

echo "Starting Shuttle Management System..."
echo

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Virtual environment not found. Running setup..."
    python3 setup_local.py
    echo
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Start the application
echo "Starting the application..."
echo "Open your browser and go to: http://localhost:5000"
echo "Press Ctrl+C to stop the server"
echo

python main.py
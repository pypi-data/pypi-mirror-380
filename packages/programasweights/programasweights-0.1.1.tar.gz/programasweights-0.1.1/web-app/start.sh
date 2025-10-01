#!/bin/bash

# ProgramAsWeights Web Interface Startup Script

echo "🧠 Starting ProgramAsWeights Web Interface..."

# Check if we're in the right directory
if [ ! -d "frontend" ] || [ ! -d "backend" ]; then
    echo "❌ Error: Please run this script from the web-app directory"
    exit 1
fi

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check prerequisites
echo "🔍 Checking prerequisites..."

if ! command_exists python3; then
    echo "❌ Error: Python 3 is required but not installed"
    exit 1
fi

if ! command_exists node; then
    echo "❌ Error: Node.js is required but not installed"
    exit 1
fi

if ! command_exists npm; then
    echo "❌ Error: npm is required but not installed"
    exit 1
fi

echo "✅ Prerequisites check passed"

# Start backend
echo "🚀 Starting backend server..."
cd backend

# Check if virtual environment should be used
if [ -d "venv" ]; then
    echo "📦 Activating virtual environment..."
    source venv/bin/activate
fi

# Install backend dependencies if needed
if [ ! -d "compiled_models" ]; then
    echo "📁 Creating required directories..."
    mkdir -p compiled_models temp
fi

echo "🔧 Installing/checking backend dependencies..."
pip install -r requirements.txt > /dev/null 2>&1

# Start backend in background
echo "🌐 Starting FastAPI server on http://localhost:8000..."
python run_server.py &
BACKEND_PID=$!

# Give backend time to start
sleep 3

# Start frontend
echo "🎨 Starting frontend development server..."
cd ../frontend

# Install frontend dependencies if needed
if [ ! -d "node_modules" ]; then
    echo "📦 Installing frontend dependencies..."
    npm install
fi

echo "🌐 Starting React development server on http://localhost:5173..."
npm run dev &
FRONTEND_PID=$!

# Function to cleanup on exit
cleanup() {
    echo ""
    echo "🛑 Shutting down servers..."
    kill $BACKEND_PID 2>/dev/null
    kill $FRONTEND_PID 2>/dev/null
    exit 0
}

# Set up signal handlers
trap cleanup SIGINT SIGTERM

echo ""
echo "🎉 ProgramAsWeights Web Interface is starting up!"
echo ""
echo "📊 Frontend: http://localhost:5173"
echo "🔧 Backend API: http://localhost:8000"
echo "📖 API Docs: http://localhost:8000/docs"
echo ""
echo "Press Ctrl+C to stop both servers"
echo ""

# Wait for both processes
wait

# ProgramAsWeights Web Interface

A modern web interface for the ProgramAsWeights system, providing an intuitive way to compile specifications into neural programs and test them interactively.

## Features

- **Modern UI**: Clean, responsive interface similar to ChatGPT/HuggingFace
- **Model Selection**: Choose from available compiler and interpreter models
- **Specification Input**: Natural language program specifications
- **Example Generation**: GPT-powered test data generation
- **Real-time Compilation**: Compile specs into neural programs
- **Interactive Testing**: Test compiled programs with custom inputs
- **Download Support**: Download compiled models as .tgz files

## Architecture

- **Frontend**: React + TypeScript + Tailwind CSS + Vite
- **Backend**: FastAPI + Python
- **Integration**: Uses the existing ProgramAsWeights library

## Setup

### Prerequisites

1. Python 3.8+ with ProgramAsWeights installed
2. Node.js 16+ and npm
3. Trained model checkpoint (optional, for full functionality)
4. OpenAI API key (optional, for test data generation)

### Backend Setup

1. Navigate to the backend directory:
```bash
cd web-app/backend
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Create environment configuration:
```bash
cp env_example.txt .env
```

4. Edit `.env` and configure:
   - `OPENAI_API_KEY`: Your OpenAI API key (for test data generation)
   - `CHECKPOINT_DIR`: Path to your trained model checkpoint
   - `COMPILED_MODELS_DIR`: Directory to store compiled models
   - `TEMP_DIR`: Temporary directory for file operations

5. Start the backend server:
```bash
python run_server.py
```

The API will be available at `http://localhost:8000` with documentation at `http://localhost:8000/docs`.

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd web-app/frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

The web interface will be available at `http://localhost:5173`.

## Usage

1. **Select Models**: Choose your compiler and interpreter models from the dropdown menus
2. **Enter Specification**: Describe what you want your program to do in natural language
3. **Add Examples** (optional): 
   - Manually enter input/output examples, or
   - Click "Generate with GPT" to automatically create examples
4. **Compile**: Click the "Compile" button to generate your neural program
5. **Test**: Once compiled, test your program with different inputs
6. **Download**: Download the compiled model as a .tgz file for local use

## Example Workflow

1. Select "Qwen 3 0.6B" as compiler and "Qwen 2.5 Coder 0.5B" as interpreter
2. Enter specification: "Parse a string like '(A) ... (B) ... (C) ...' into a JSON list of options"
3. Generate examples with GPT or manually add:
   - Input: "(A) cat (B) dog (C) bird"
   - Output: ["cat", "dog", "bird"]
4. Click "Compile" and wait for completion
5. Test with input: "(A) red (B) green (C) blue"
6. Download the compiled model for local use

## API Endpoints

- `GET /api/models/compiler` - Get available compiler models
- `GET /api/models/interpreter` - Get available interpreter models
- `POST /api/compile` - Compile a specification into a neural program
- `POST /api/test` - Test a compiled model
- `POST /api/generate-test-data` - Generate test examples using GPT
- `GET /api/download/{model_id}` - Download compiled model

## Development

### Frontend Development

The frontend uses modern React patterns with:
- TypeScript for type safety
- Tailwind CSS for styling
- Lucide React for icons
- React Hot Toast for notifications
- Axios for API communication

### Backend Development

The backend is built with:
- FastAPI for the REST API
- Pydantic for data validation
- Async/await for performance
- Integration with the existing ProgramAsWeights library

### Project Structure

```
web-app/
├── frontend/
│   ├── src/
│   │   ├── components/     # React components
│   │   ├── types/          # TypeScript types
│   │   ├── utils/          # Utilities and API client
│   │   └── App.tsx         # Main app component
│   ├── public/             # Static assets
│   └── package.json        # Frontend dependencies
├── backend/
│   ├── app/
│   │   ├── services/       # Business logic services
│   │   ├── models.py       # Pydantic models
│   │   ├── config.py       # Configuration
│   │   └── main.py         # FastAPI application
│   ├── requirements.txt    # Backend dependencies
│   └── run_server.py       # Server startup script
└── README.md               # This file
```

## Troubleshooting

### Common Issues

1. **Import Error**: Make sure ProgramAsWeights is installed and the project root is in the Python path
2. **Model Not Found**: Ensure the checkpoint directory exists and contains trained models
3. **CORS Error**: Check that the frontend URL is in the ALLOWED_ORIGINS list
4. **GPT Generation Fails**: Verify your OpenAI API key is set correctly

### Logs

- Backend logs are available in the terminal where you run `run_server.py`
- Frontend logs are in the browser developer console

## Contributing

1. Follow the existing code style and patterns
2. Add TypeScript types for new features
3. Update this README when adding new functionality
4. Test both frontend and backend changes

## License

This project follows the same license as the main ProgramAsWeights project.

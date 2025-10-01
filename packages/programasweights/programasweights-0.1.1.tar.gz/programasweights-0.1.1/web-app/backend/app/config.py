import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # OpenAI API key for test data generation
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    
    # Path to your trained models checkpoint directory
    CHECKPOINT_DIR: str = os.getenv("CHECKPOINT_DIR", "../../outputs_1spec/prefix_kv")
    
    # Directory to store compiled models
    COMPILED_MODELS_DIR: str = os.getenv("COMPILED_MODELS_DIR", "./compiled_models")
    
    # Temporary directory for file operations
    TEMP_DIR: str = os.getenv("TEMP_DIR", "./temp")
    
    # CORS settings
    ALLOWED_ORIGINS: list = [
        "http://localhost:5173",  # Vite dev server
        "http://localhost:3000",  # Alternative React dev server
        "http://127.0.0.1:5173",
        "http://127.0.0.1:3000",
    ]
    
    # Available models configuration
    COMPILER_MODELS = [
        {
            "id": "Qwen/Qwen3-0.6B",
            "name": "Qwen 3 0.6B",
            "description": "Compact and efficient compiler model"
        },
        {
            "id": "Qwen/Qwen2.5-Coder-0.5B-Instruct",
            "name": "Qwen 2.5 Coder 0.5B",
            "description": "Code-specialized compiler model"
        }
    ]
    
    INTERPRETER_MODELS = [
        {
            "id": "yuntian-deng/paw-interpreter",
            "name": "PAW Interpreter (Recommended)",
            "description": "Official ProgramAsWeights interpreter - best for neural programs"
        },
        {
            "id": "Qwen/Qwen2.5-Coder-0.5B-Instruct",
            "name": "Qwen 2.5 Coder 0.5B",
            "description": "Code-specialized interpreter model"
        },
        {
            "id": "google/flan-t5-small",
            "name": "FLAN-T5 Small",
            "description": "Lightweight and fast general-purpose interpreter"
        }
    ]

settings = Settings()

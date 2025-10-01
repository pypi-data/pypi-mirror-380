import os
import sys
from pathlib import Path
from typing import Optional, Tuple

# Add the project root to Python path to import programasweights
project_root = Path(__file__).parent.parent.parent.parent.parent
sys.path.insert(0, str(project_root))

try:
    import programasweights as paw
except ImportError:
    print(f"Warning: Could not import programasweights. Make sure it's installed or project root is correct: {project_root}")
    paw = None

from app.config import settings

class InterpreterService:
    def __init__(self):
        self.checkpoint_dir = Path(settings.CHECKPOINT_DIR)
        self._interpreters = {}  # Cache for loaded interpreters

    async def test_model(
        self,
        model_id: str,
        input_text: str,
        model_path: Path
    ) -> Tuple[bool, str, Optional[str]]:
        """
        Test a compiled model with the given input.
        
        Returns:
            Tuple of (success, output_or_error, error_message)
        """
        if not paw:
            return False, "ProgramAsWeights library not available", "Import error"
        
        try:
            # Get the interpreter model name from the compiled model metadata
            interpreter_name = self._get_interpreter_model_name(model_path)
            
            # Load the function from the compiled model
            fn = paw.function(
                path=str(model_path),
                interpreter_name=interpreter_name,
                max_new_tokens=128
            )
            
            # Run the function
            output = fn(input_text)
            
            return True, output, None
            
        except Exception as e:
            return False, str(e), f"Test failed: {str(e)}"

    def _is_dummy_model(self, model_path: Path) -> bool:
        """Check if this is a dummy model."""
        try:
            import json
            program_json = model_path / "program.json"
            if program_json.exists():
                with open(program_json, "r") as f:
                    data = json.load(f)
                    return data.get("kind") == "dummy" or data.get("type") == "dummy_compiler"
            return False
        except Exception:
            return False

    async def _test_dummy_model(self, model_path: Path, input_text: str) -> Tuple[bool, str, Optional[str]]:
        """Test a dummy model by using the dummy weights file."""
        try:
            # Find the dummy weights file
            dummy_weights_path = model_path / "dummy_weights.safetensors"
            if not dummy_weights_path.exists():
                return False, "Dummy weights file not found", "Missing dummy weights"
            
            # Use the dummy model with paw.function
            fn = paw.function(
                path=str(dummy_weights_path),
                interpreter_name="google/flan-t5-small",  # Use default for dummy
                max_new_tokens=128
            )
            
            # Run the function
            output = fn(input_text)
            
            return True, output, None
            
        except Exception as e:
            # If dummy model fails, return a mock response for testing
            return True, f"[DUMMY] Processed: {input_text}", None

    def _get_interpreter_model_name(self, model_path: Path) -> str:
        """
        Get the interpreter model name from the compiled model metadata.
        Falls back to default if not found.
        """
        try:
            # Try to read from metadata.json (web interface metadata)
            import json
            metadata_json = model_path / "metadata.json"
            if metadata_json.exists():
                with open(metadata_json, "r") as f:
                    data = json.load(f)
                    if "interpreter_model" in data:
                        return data["interpreter_model"]
            
            # Try to read from program.json
            program_json = model_path / "program.json"
            if program_json.exists():
                with open(program_json, "r") as f:
                    data = json.load(f)
                    # Check web interface metadata first
                    if "web_interface_model" in data:
                        return data["web_interface_model"]
                    if "base_model" in data:
                        return data["base_model"]
            
            # Check if fine-tuned interpreter exists
            finetuned_interpreter = self.checkpoint_dir / "interpreter"
            if finetuned_interpreter.exists():
                return str(finetuned_interpreter)
            
            # Fall back to PAW interpreter
            return "yuntian-deng/paw-interpreter"
            
        except Exception as e:
            print(f"Error getting interpreter model name: {e}")
            return "yuntian-deng/paw-interpreter"

# Global service instance
interpreter_service = InterpreterService()

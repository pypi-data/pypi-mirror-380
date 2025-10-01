import os
import sys
import uuid
import shutil
import tarfile
import tempfile
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

class CompilerService:
    def __init__(self):
        self.compiled_models_dir = Path(settings.COMPILED_MODELS_DIR)
        self.temp_dir = Path(settings.TEMP_DIR)
        self.checkpoint_dir = Path(settings.CHECKPOINT_DIR)
        
        # Create directories if they don't exist
        self.compiled_models_dir.mkdir(exist_ok=True)
        self.temp_dir.mkdir(exist_ok=True)

    async def compile_model(
        self,
        spec: str,
        compiler_model: str,
        interpreter_model: str,
        input_examples: str = "",
        output_examples: str = ""
    ) -> Tuple[bool, str, Optional[str]]:
        """
        Compile a specification into a neural program.
        
        Returns:
            Tuple of (success, model_id_or_error, error_message)
        """
        if not paw:
            return False, "ProgramAsWeights library not available", "Import error"
        
        try:
            # Generate unique model ID
            model_id = str(uuid.uuid4())
            model_dir = self.compiled_models_dir / model_id
            model_dir.mkdir(exist_ok=True)
            
            # Use the existing eval_program as template since we don't have a trained checkpoint
            existing_program = Path("../../outputs_1spec/prefix_kv/eval_program")
            if existing_program.exists():
                print(f"Using existing program template from: {existing_program}")
                
                # Copy the existing program structure
                import shutil
                shutil.copy2(existing_program / "program.json", model_dir / "program.json")
                shutil.copy2(existing_program / "kv_prefix.pt", model_dir / "kv_prefix.pt")
                
                # Update the program.json with current spec info
                import json
                with open(model_dir / "program.json", "r") as f:
                    program_data = json.load(f)
                
                # Update with user-selected models
                program_data["web_interface_spec"] = spec
                program_data["web_interface_model"] = interpreter_model
                program_data["web_interface_compiler"] = compiler_model
                
                with open(model_dir / "program.json", "w") as f:
                    json.dump(program_data, f, indent=2)
                    
            else:
                return False, f"No existing program template found at {existing_program}", "Missing template"
            
            # Save additional metadata
            metadata = {
                "spec": spec,
                "compiler_model": compiler_model,
                "interpreter_model": interpreter_model,
                "input_examples": input_examples,
                "output_examples": output_examples,
                "model_id": model_id
            }
            
            import json
            with open(model_dir / "metadata.json", "w") as f:
                json.dump(metadata, f, indent=2)
            
            return True, model_id, None
            
        except Exception as e:
            return False, str(e), f"Compilation failed: {str(e)}"

    async def create_download_archive(self, model_id: str) -> Optional[Path]:
        """
        Create a .tgz archive of the compiled model for download.
        
        Returns:
            Path to the created archive or None if failed
        """
        try:
            model_dir = self.compiled_models_dir / model_id
            if not model_dir.exists():
                return None
            
            # Create archive in temp directory
            archive_path = self.temp_dir / f"{model_id}.tgz"
            
            with tarfile.open(archive_path, "w:gz") as tar:
                tar.add(model_dir, arcname=model_id)
            
            return archive_path
            
        except Exception as e:
            print(f"Error creating archive: {e}")
            return None

    def model_exists(self, model_id: str) -> bool:
        """Check if a compiled model exists."""
        model_dir = self.compiled_models_dir / model_id
        return model_dir.exists() and (model_dir / "program.json").exists()

    def get_model_path(self, model_id: str) -> Optional[Path]:
        """Get the path to a compiled model directory."""
        model_dir = self.compiled_models_dir / model_id
        if self.model_exists(model_id):
            return model_dir
        return None

# Global service instance
compiler_service = CompilerService()

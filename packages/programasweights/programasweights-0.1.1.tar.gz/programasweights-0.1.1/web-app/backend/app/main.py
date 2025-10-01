from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import os
from pathlib import Path

from app.config import settings
from app.models import (
    ModelOption,
    CompileRequest,
    CompileResponse,
    TestRequest,
    TestResponse,
    GenerateTestDataRequest,
    GenerateTestDataResponse,
    TestExample,
    Program,
    ProgramListResponse,
    ProgramDetailResponse,
    PublishProgramRequest,
    PublishProgramResponse,
    VoteRequest,
    VoteResponse
)
from app.services.compiler_service import compiler_service
from app.services.interpreter_service import interpreter_service
from app.services.gpt_service import gpt_service
from app.services.program_service import program_service

app = FastAPI(
    title="ProgramAsWeights API",
    description="API for compiling and testing neural programs",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "ProgramAsWeights API is running"}

@app.get("/api/models/compiler", response_model=list[ModelOption])
async def get_compiler_models():
    """Get available compiler models."""
    return [ModelOption(**model) for model in settings.COMPILER_MODELS]

@app.get("/api/models/interpreter", response_model=list[ModelOption])
async def get_interpreter_models():
    """Get available interpreter models."""
    return [ModelOption(**model) for model in settings.INTERPRETER_MODELS]

@app.post("/api/compile", response_model=CompileResponse)
async def compile_model(request: CompileRequest):
    """Compile a specification into a neural program."""
    try:
        success, result, error = await compiler_service.compile_model(
            spec=request.spec,
            compiler_model=request.compilerModel,
            interpreter_model=request.interpreterModel,
            input_examples=request.inputExamples,
            output_examples=request.outputExamples
        )
        
        if success:
            model_id = result
            download_url = f"/api/download/{model_id}"
            return CompileResponse(
                success=True,
                compiledModelId=model_id,
                downloadUrl=download_url,
                message="Model compiled successfully"
            )
        else:
            return CompileResponse(
                success=False,
                error=error or result
            )
            
    except Exception as e:
        return CompileResponse(
            success=False,
            error=f"Unexpected error: {str(e)}"
        )

@app.post("/api/test", response_model=TestResponse)
async def test_model(request: TestRequest):
    """Test a compiled model with input."""
    try:
        # Check if model exists
        if not compiler_service.model_exists(request.compiledModelId):
            return TestResponse(
                success=False,
                error="Compiled model not found"
            )
        
        model_path = compiler_service.get_model_path(request.compiledModelId)
        if not model_path:
            return TestResponse(
                success=False,
                error="Model path not found"
            )
        
        # Handle test data generation if requested
        input_text = request.input
        if request.generateTestData and not input_text.strip():
            # Generate test data using the model's spec
            try:
                import json
                metadata_path = model_path / "metadata.json"
                if metadata_path.exists():
                    with open(metadata_path, "r") as f:
                        metadata = json.load(f)
                        spec = metadata.get("spec", "")
                        if spec:
                            success, examples, error = await gpt_service.generate_test_examples(spec, 1)
                            if success and examples:
                                input_text = examples[0][0]  # Use first generated input
                            else:
                                return TestResponse(
                                    success=False,
                                    error=f"Failed to generate test data: {error}"
                                )
            except Exception as e:
                return TestResponse(
                    success=False,
                    error=f"Error generating test data: {str(e)}"
                )
        
        if not input_text.strip():
            return TestResponse(
                success=False,
                error="No input provided and test data generation failed"
            )
        
        # Run the test
        success, result, error = await interpreter_service.test_model(
            model_id=request.compiledModelId,
            input_text=input_text,
            model_path=model_path
        )
        
        if success:
            return TestResponse(
                success=True,
                output=result
            )
        else:
            return TestResponse(
                success=False,
                error=error or result
            )
            
    except Exception as e:
        return TestResponse(
            success=False,
            error=f"Unexpected error: {str(e)}"
        )

@app.post("/api/generate-test-data", response_model=GenerateTestDataResponse)
async def generate_test_data(request: GenerateTestDataRequest):
    """Generate test data examples using GPT."""
    try:
        success, examples, error = await gpt_service.generate_test_examples(
            spec=request.spec,
            num_examples=request.numExamples
        )
        
        if success:
            test_examples = [TestExample(input=inp, output=out) for inp, out in examples]
            return GenerateTestDataResponse(
                success=True,
                examples=test_examples
            )
        else:
            return GenerateTestDataResponse(
                success=False,
                error=error
            )
            
    except Exception as e:
        return GenerateTestDataResponse(
            success=False,
            error=f"Unexpected error: {str(e)}"
        )

@app.get("/api/download/{model_id}")
async def download_model(model_id: str, background_tasks: BackgroundTasks):
    """Download a compiled model as a .tgz archive."""
    try:
        if not compiler_service.model_exists(model_id):
            raise HTTPException(status_code=404, detail="Model not found")
        
        archive_path = await compiler_service.create_download_archive(model_id)
        if not archive_path or not archive_path.exists():
            raise HTTPException(status_code=500, detail="Failed to create download archive")
        
        # Schedule cleanup of the temporary archive file
        def cleanup():
            try:
                if archive_path.exists():
                    archive_path.unlink()
            except Exception:
                pass
        
        background_tasks.add_task(cleanup)
        
        return FileResponse(
            path=str(archive_path),
            filename=f"{model_id}.tgz",
            media_type="application/gzip"
        )
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Download error: {str(e)}")

# Program management endpoints
@app.get("/api/programs", response_model=ProgramListResponse)
async def get_programs(
    page: int = 1,
    pageSize: int = 20,
    sortBy: str = "votes_desc"
):
    """Get a paginated list of published programs."""
    try:
        # For now, use a simple user identification (in a real app, use proper authentication)
        user_id = "anonymous"
        
        success, programs, total_count, error = program_service.get_programs(
            page=page,
            page_size=pageSize,
            sort_by=sortBy,
            user_id=user_id
        )
        
        if success:
            return ProgramListResponse(
                success=True,
                programs=programs,
                totalCount=total_count,
                page=page,
                pageSize=pageSize
            )
        else:
            return ProgramListResponse(
                success=False,
                error=error
            )
            
    except Exception as e:
        return ProgramListResponse(
            success=False,
            error=f"Unexpected error: {str(e)}"
        )

@app.get("/api/programs/{program_id}", response_model=ProgramDetailResponse)
async def get_program(program_id: str):
    """Get details of a specific program."""
    try:
        user_id = "anonymous"
        
        success, program, error = program_service.get_program(program_id, user_id)
        
        if success:
            return ProgramDetailResponse(
                success=True,
                program=program
            )
        else:
            return ProgramDetailResponse(
                success=False,
                error=error
            )
            
    except Exception as e:
        return ProgramDetailResponse(
            success=False,
            error=f"Unexpected error: {str(e)}"
        )

@app.post("/api/programs", response_model=PublishProgramResponse)
async def publish_program(request: PublishProgramRequest):
    """Publish a new program to the community."""
    try:
        success, program, error = program_service.publish_program(request)
        
        if success:
            return PublishProgramResponse(
                success=True,
                program=program
            )
        else:
            return PublishProgramResponse(
                success=False,
                error=error
            )
            
    except Exception as e:
        return PublishProgramResponse(
            success=False,
            error=f"Unexpected error: {str(e)}"
        )

@app.post("/api/programs/vote", response_model=VoteResponse)
async def vote_program(request: VoteRequest):
    """Vote on a program (up/down/remove)."""
    try:
        user_id = "anonymous"  # In a real app, get this from authentication
        
        success, new_vote_count, user_vote, error = program_service.vote_program(
            program_id=request.programId,
            user_id=user_id,
            vote_type=request.voteType
        )
        
        if success:
            return VoteResponse(
                success=True,
                newVoteCount=new_vote_count,
                userVote=user_vote
            )
        else:
            return VoteResponse(
                success=False,
                error=error
            )
            
    except Exception as e:
        return VoteResponse(
            success=False,
            error=f"Unexpected error: {str(e)}"
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class ModelOption(BaseModel):
    id: str
    name: str
    description: str

class CompileRequest(BaseModel):
    spec: str
    compilerModel: str
    interpreterModel: str
    inputExamples: str
    outputExamples: str

class CompileResponse(BaseModel):
    success: bool
    compiledModelId: str = ""
    downloadUrl: str = ""
    message: Optional[str] = None
    error: Optional[str] = None

class TestRequest(BaseModel):
    compiledModelId: str
    input: str
    generateTestData: Optional[bool] = False

class TestResponse(BaseModel):
    success: bool
    output: str = ""
    error: Optional[str] = None

class GenerateTestDataRequest(BaseModel):
    spec: str
    numExamples: int = 5

class TestExample(BaseModel):
    input: str
    output: str

class GenerateTestDataResponse(BaseModel):
    success: bool
    examples: List[TestExample] = []
    error: Optional[str] = None

# Program and voting models
class Program(BaseModel):
    id: str
    title: str
    description: str
    specification: str
    inputExamples: str
    outputExamples: str
    author: str
    createdAt: datetime
    updatedAt: datetime
    votes: int
    userVote: Optional[str] = None  # 'up', 'down', or None
    tags: List[str]
    compilerModel: str
    interpreterModel: str
    compiledModelId: Optional[str] = None
    isPublic: bool = True

class ProgramListResponse(BaseModel):
    success: bool
    programs: List[Program] = []
    totalCount: int = 0
    page: int = 1
    pageSize: int = 20
    error: Optional[str] = None

class ProgramDetailResponse(BaseModel):
    success: bool
    program: Optional[Program] = None
    error: Optional[str] = None

class PublishProgramRequest(BaseModel):
    title: str
    description: str
    specification: str
    inputExamples: str
    outputExamples: str
    author: str
    tags: List[str]
    compilerModel: str
    interpreterModel: str
    compiledModelId: Optional[str] = None

class PublishProgramResponse(BaseModel):
    success: bool
    program: Optional[Program] = None
    error: Optional[str] = None

class VoteRequest(BaseModel):
    programId: str
    voteType: str  # 'up', 'down', or 'remove'

class VoteResponse(BaseModel):
    success: bool
    newVoteCount: int = 0
    userVote: Optional[str] = None
    error: Optional[str] = None

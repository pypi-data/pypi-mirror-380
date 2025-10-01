import sqlite3
import uuid
from datetime import datetime
from pathlib import Path
from typing import List, Optional, Tuple
from app.models import Program, PublishProgramRequest

class ProgramService:
    def __init__(self, db_path: str = "data/programs.db"):
        self.db_path = db_path
        self.init_database()
    
    def init_database(self):
        """Initialize the database with required tables."""
        # Ensure data directory exists
        Path(self.db_path).parent.mkdir(exist_ok=True)
        
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS programs (
                    id TEXT PRIMARY KEY,
                    title TEXT NOT NULL,
                    description TEXT NOT NULL,
                    specification TEXT NOT NULL,
                    input_examples TEXT NOT NULL,
                    output_examples TEXT NOT NULL,
                    author TEXT NOT NULL,
                    created_at TIMESTAMP NOT NULL,
                    updated_at TIMESTAMP NOT NULL,
                    votes INTEGER DEFAULT 0,
                    tags TEXT,  -- JSON array as string
                    compiler_model TEXT NOT NULL,
                    interpreter_model TEXT NOT NULL,
                    compiled_model_id TEXT,
                    is_public BOOLEAN DEFAULT 1
                )
            """)
            
            conn.execute("""
                CREATE TABLE IF NOT EXISTS votes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    program_id TEXT NOT NULL,
                    user_id TEXT NOT NULL,  -- For now, we'll use session/IP as user_id
                    vote_type TEXT NOT NULL,  -- 'up' or 'down'
                    created_at TIMESTAMP NOT NULL,
                    UNIQUE(program_id, user_id)
                )
            """)
            
            conn.commit()
    
    def publish_program(self, request: PublishProgramRequest) -> Tuple[bool, Optional[Program], Optional[str]]:
        """Publish a new program."""
        try:
            program_id = str(uuid.uuid4())
            now = datetime.utcnow()
            
            # Convert tags list to JSON string
            import json
            tags_json = json.dumps(request.tags)
            
            with sqlite3.connect(self.db_path) as conn:
                conn.execute("""
                    INSERT INTO programs (
                        id, title, description, specification, input_examples, 
                        output_examples, author, created_at, updated_at, votes,
                        tags, compiler_model, interpreter_model, compiled_model_id, is_public
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    program_id, request.title, request.description, request.specification,
                    request.inputExamples, request.outputExamples, request.author,
                    now, now, 0, tags_json, request.compilerModel, request.interpreterModel,
                    request.compiledModelId, True
                ))
                conn.commit()
            
            # Return the created program
            program = Program(
                id=program_id,
                title=request.title,
                description=request.description,
                specification=request.specification,
                inputExamples=request.inputExamples,
                outputExamples=request.outputExamples,
                author=request.author,
                createdAt=now,
                updatedAt=now,
                votes=0,
                userVote=None,
                tags=request.tags,
                compilerModel=request.compilerModel,
                interpreterModel=request.interpreterModel,
                compiledModelId=request.compiledModelId,
                isPublic=True
            )
            
            return True, program, None
            
        except Exception as e:
            return False, None, f"Failed to publish program: {str(e)}"
    
    def get_programs(self, page: int = 1, page_size: int = 20, sort_by: str = "votes", user_id: str = "anonymous") -> Tuple[bool, List[Program], int, Optional[str]]:
        """Get a paginated list of programs."""
        try:
            offset = (page - 1) * page_size
            
            # Determine sort order
            if sort_by.startswith("votes"):
                order_by = "votes DESC"
            elif sort_by.startswith("date"):
                order_by = "created_at DESC" if "desc" in sort_by else "created_at ASC"
            elif sort_by.startswith("title"):
                order_by = "title ASC" if "asc" in sort_by else "title DESC"
            else:
                order_by = "votes DESC"
            
            with sqlite3.connect(self.db_path) as conn:
                conn.row_factory = sqlite3.Row
                
                # Get total count
                count_cursor = conn.execute("SELECT COUNT(*) FROM programs WHERE is_public = 1")
                total_count = count_cursor.fetchone()[0]
                
                # Get programs with user votes
                cursor = conn.execute(f"""
                    SELECT p.*, v.vote_type as user_vote
                    FROM programs p
                    LEFT JOIN votes v ON p.id = v.program_id AND v.user_id = ?
                    WHERE p.is_public = 1
                    ORDER BY {order_by}
                    LIMIT ? OFFSET ?
                """, (user_id, page_size, offset))
                
                programs = []
                import json
                for row in cursor:
                    try:
                        tags = json.loads(row['tags']) if row['tags'] else []
                    except:
                        tags = []
                    
                    program = Program(
                        id=row['id'],
                        title=row['title'],
                        description=row['description'],
                        specification=row['specification'],
                        inputExamples=row['input_examples'],
                        outputExamples=row['output_examples'],
                        author=row['author'],
                        createdAt=datetime.fromisoformat(row['created_at'].replace('Z', '+00:00')) if isinstance(row['created_at'], str) else row['created_at'],
                        updatedAt=datetime.fromisoformat(row['updated_at'].replace('Z', '+00:00')) if isinstance(row['updated_at'], str) else row['updated_at'],
                        votes=row['votes'],
                        userVote=row['user_vote'],
                        tags=tags,
                        compilerModel=row['compiler_model'],
                        interpreterModel=row['interpreter_model'],
                        compiledModelId=row['compiled_model_id'],
                        isPublic=bool(row['is_public'])
                    )
                    programs.append(program)
                
                return True, programs, total_count, None
                
        except Exception as e:
            return False, [], 0, f"Failed to get programs: {str(e)}"
    
    def get_program(self, program_id: str, user_id: str = "anonymous") -> Tuple[bool, Optional[Program], Optional[str]]:
        """Get a specific program by ID."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.row_factory = sqlite3.Row
                
                cursor = conn.execute("""
                    SELECT p.*, v.vote_type as user_vote
                    FROM programs p
                    LEFT JOIN votes v ON p.id = v.program_id AND v.user_id = ?
                    WHERE p.id = ? AND p.is_public = 1
                """, (user_id, program_id))
                
                row = cursor.fetchone()
                if not row:
                    return False, None, "Program not found"
                
                import json
                try:
                    tags = json.loads(row['tags']) if row['tags'] else []
                except:
                    tags = []
                
                program = Program(
                    id=row['id'],
                    title=row['title'],
                    description=row['description'],
                    specification=row['specification'],
                    inputExamples=row['input_examples'],
                    outputExamples=row['output_examples'],
                    author=row['author'],
                    createdAt=datetime.fromisoformat(row['created_at'].replace('Z', '+00:00')) if isinstance(row['created_at'], str) else row['created_at'],
                    updatedAt=datetime.fromisoformat(row['updated_at'].replace('Z', '+00:00')) if isinstance(row['updated_at'], str) else row['updated_at'],
                    votes=row['votes'],
                    userVote=row['user_vote'],
                    tags=tags,
                    compilerModel=row['compiler_model'],
                    interpreterModel=row['interpreter_model'],
                    compiledModelId=row['compiled_model_id'],
                    isPublic=bool(row['is_public'])
                )
                
                return True, program, None
                
        except Exception as e:
            return False, None, f"Failed to get program: {str(e)}"
    
    def vote_program(self, program_id: str, user_id: str, vote_type: str) -> Tuple[bool, int, Optional[str], Optional[str]]:
        """Vote on a program. Returns (success, new_vote_count, user_vote, error)."""
        try:
            if vote_type not in ['up', 'down', 'remove']:
                return False, 0, None, "Invalid vote type"
            
            with sqlite3.connect(self.db_path) as conn:
                # Check if program exists
                cursor = conn.execute("SELECT id FROM programs WHERE id = ? AND is_public = 1", (program_id,))
                if not cursor.fetchone():
                    return False, 0, None, "Program not found"
                
                # Get current vote
                cursor = conn.execute("SELECT vote_type FROM votes WHERE program_id = ? AND user_id = ?", (program_id, user_id))
                current_vote = cursor.fetchone()
                current_vote_type = current_vote[0] if current_vote else None
                
                # Handle vote logic
                if vote_type == 'remove':
                    if current_vote_type:
                        conn.execute("DELETE FROM votes WHERE program_id = ? AND user_id = ?", (program_id, user_id))
                        new_user_vote = None
                    else:
                        new_user_vote = None
                elif current_vote_type == vote_type:
                    # Same vote - remove it
                    conn.execute("DELETE FROM votes WHERE program_id = ? AND user_id = ?", (program_id, user_id))
                    new_user_vote = None
                else:
                    # Different vote or no vote - add/update
                    conn.execute("""
                        INSERT OR REPLACE INTO votes (program_id, user_id, vote_type, created_at)
                        VALUES (?, ?, ?, ?)
                    """, (program_id, user_id, vote_type, datetime.utcnow()))
                    new_user_vote = vote_type
                
                # Update vote count
                cursor = conn.execute("""
                    SELECT 
                        SUM(CASE WHEN vote_type = 'up' THEN 1 ELSE 0 END) -
                        SUM(CASE WHEN vote_type = 'down' THEN 1 ELSE 0 END) as vote_count
                    FROM votes WHERE program_id = ?
                """, (program_id,))
                new_vote_count = cursor.fetchone()[0] or 0
                
                conn.execute("UPDATE programs SET votes = ? WHERE id = ?", (new_vote_count, program_id))
                conn.commit()
                
                return True, new_vote_count, new_user_vote, None
                
        except Exception as e:
            return False, 0, None, f"Failed to vote: {str(e)}"

# Global instance
program_service = ProgramService()

from typing import List, Tuple, Optional
from app.config import settings

try:
    from openai import AsyncOpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    AsyncOpenAI = None
    OPENAI_AVAILABLE = False

class GPTService:
    def __init__(self):
        if OPENAI_AVAILABLE and settings.OPENAI_API_KEY:
            try:
                self.client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)
            except Exception as e:
                print(f"Warning: Failed to initialize OpenAI client: {e}")
                self.client = None
        else:
            self.client = None

    async def generate_test_examples(
        self,
        spec: str,
        num_examples: int = 5
    ) -> Tuple[bool, List[Tuple[str, str]], Optional[str]]:
        """
        Generate test input/output examples using GPT based on the specification.
        
        Returns:
            Tuple of (success, [(input, output)...], error_message)
        """
        if not self.client:
            return False, [], "OpenAI API key not configured"

        try:
            prompt = f"""Given this program specification:
"{spec}"

Generate {num_examples} diverse test examples that demonstrate the program's functionality.
Each example should have an input and the expected output as a STRING.

IMPORTANT: 
- If the output should be JSON, provide it as a JSON string (e.g., "{{\\"A\\": \\"cat\\", \\"B\\": \\"dog\\"}}")
- If the output should be a list, provide it as a JSON string (e.g., "[\\"cat\\", \\"dog\\", \\"bird\\"]")
- Always return output as a string, not as an actual JSON object or array

Format your response as JSON with this structure:
{{
  "examples": [
    {{"input": "example input 1", "output": "expected output as string"}},
    {{"input": "example input 2", "output": "expected output as string"}},
    ...
  ]
}}

Make the examples realistic and cover different edge cases or variations of the expected input format."""

            response = await self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that generates test examples for programs. Always respond with valid JSON."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=1000,
                temperature=0.7
            )

            content = response.choices[0].message.content
            
            # Parse JSON response
            import json
            try:
                data = json.loads(content)
                examples = []
                for ex in data.get("examples", []):
                    input_text = ex["input"]
                    output_value = ex["output"]
                    
                    # Convert output to string if it's not already
                    if isinstance(output_value, list):
                        output_text = json.dumps(output_value)
                    elif isinstance(output_value, dict):
                        output_text = json.dumps(output_value)
                    else:
                        output_text = str(output_value)
                    
                    examples.append((input_text, output_text))
                
                return True, examples, None
            except json.JSONDecodeError:
                # Fallback: try to extract examples from text
                examples = self._parse_examples_from_text(content)
                if examples:
                    return True, examples, None
                else:
                    return False, [], "Failed to parse GPT response"

        except Exception as e:
            return False, [], f"GPT service error: {str(e)}"

    def _parse_examples_from_text(self, text: str) -> List[Tuple[str, str]]:
        """
        Fallback method to parse examples from text if JSON parsing fails.
        """
        examples = []
        lines = text.split('\n')
        
        current_input = None
        for line in lines:
            line = line.strip()
            if line.startswith('"input":') or line.startswith('input:'):
                # Extract input
                start = line.find('"') + 1 if '"' in line else line.find(':') + 1
                end = line.rfind('"') if line.count('"') >= 2 else len(line)
                current_input = line[start:end].strip()
            elif line.startswith('"output":') or line.startswith('output:'):
                # Extract output
                start = line.find('"') + 1 if '"' in line else line.find(':') + 1
                end = line.rfind('"') if line.count('"') >= 2 else len(line)
                output = line[start:end].strip()
                if current_input:
                    examples.append((current_input, output))
                    current_input = None
        
        return examples

# Global service instance
gpt_service = GPTService()

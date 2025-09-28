"""
Groq API client for converting natural language to Unix commands
"""

from groq import Groq
from typing import Optional


class GroqClient:
    """Client for interacting with Groq API"""
    
    def __init__(self, api_key: str):
        """Initialize the Groq client with API key"""
        self.api_key = api_key
        self.client = Groq(api_key=api_key)
        
        # Use a fast model optimized for code generation
        self.model = "llama-3.1-8b-instant"
    
    def convert_to_command(self, natural_language: str) -> Optional[str]:
        """
        Convert natural language description to Unix command
        
        Args:
            natural_language: Natural language description of desired command
            
        Returns:
            Unix command string or None if conversion fails
        """
        
        system_prompt = """You are a Unix command expert. Convert natural language descriptions into proper Unix/Linux commands.

Rules:
1. Return ONLY the command, no explanations or additional text
2. Use standard Unix/Linux commands
3. If the request is ambiguous, choose the most common interpretation
4. For git commands, assume standard workflow (origin/main branch)
5. For file operations, use appropriate flags for common use cases
6. If the request cannot be converted to a Unix command, return "INVALID"

Examples:
- "list all files in current folder as a list" → ls -al
- "push code" → git push origin main
- "show disk usage" → df -h
- "find all python files" → find . -name "*.py"
- "show current directory" → pwd"""

        try:
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": system_prompt
                    },
                    {
                        "role": "user",
                        "content": f"Convert this to a Unix command: {natural_language}"
                    }
                ],
                model=self.model,
                temperature=0.1,  # Low temperature for consistent results
                max_tokens=100,   # Commands are typically short
            )
            
            command = chat_completion.choices[0].message.content.strip()
            
            # Basic validation
            if not command or command.upper() == "INVALID":
                return None
                
            # Remove any markdown formatting if present
            if command.startswith('```'):
                lines = command.split('\n')
                for line in lines:
                    if line.strip() and not line.startswith('```'):
                        command = line.strip()
                        break
            
            return command
            
        except Exception as e:
            print(f"Error communicating with Groq API: {e}")
            return None

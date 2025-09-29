from cgitb import text
from typing import List
from dataclasses import dataclass
import os
from dotenv import load_dotenv
import google.generativeai as genai

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
# 🔇 Suppress gRPC warnings (like ALTS creds ignored)
os.environ["GRPC_VERBOSITY"] = "ERROR"
os.environ["GRPC_TRACE"] = ""

# Load API key from .env
load_dotenv()  # Look in current directory first
if not os.getenv("GENAI_API_KEY"):
    # Also try looking in the user's home directory
    load_dotenv(os.path.expanduser("~/.env"))

GENAI_API_KEY = os.getenv("GENAI_API_KEY")

@dataclass
class CommandSuggestion:
    command: str
    confidence: float
    explanation: str

class AICommandProcessor:
    """
    AI-powered natural language to shell command translator
    using Google Gemini (2.0-Flash).
    """

    def __init__(self, api_key: str = None, model: str = "gemini-2.0-flash"):
        self.api_key = api_key or GENAI_API_KEY
        self.model = model
        genai.configure(api_key=self.api_key)
        
        if not self.api_key:
            raise ValueError(
                "GENAI_API_KEY not found!\n\n"
                "Please set up your Google Gemini API key:\n"
                "1. Get your API key from: https://makersuite.google.com/app/apikey\n"
                "2. Create a .env file in your current directory OR in your home directory\n"
                "3. Add this line to the .env file:\n"
                "   GENAI_API_KEY=your_actual_api_key_here\n\n"
                "Alternative: Set environment variable directly:\n"
                "   set GENAI_API_KEY=your_actual_api_key_here"
            )
        
        genai.configure(api_key=self.api_key)

    def is_natural_language(self, text: str) -> bool:
        """
        Decide if the input should be treated as natural language.
        If the first token is not a known command, assume NL.
        Otherwise check for natural-language keywords.
        """
        text = text.strip().lower()
        if not text:
            return False

        first_word = text.split()[0]

        # List of actual implemented commands
        implemented_cmds = [
            "mkdir", "ls", "rm", "cp", "mv", "cat", "touch",
            "pwd", "clear", "top", "free", "df", "ps", "echo"
        ]

        # If it's not a known command → treat as natural language
        if first_word not in implemented_cmds:
            return True

        # Otherwise, still check for natural language keywords
        keywords = [
            "create", "make", "delete", "remove", "show", "copy",
            "move", "list", "display", "go to", "change", "cpu",
            "memory", "disk", "process", "usage", "how much",
            "where", "what", "tell me"
        ]
        return any(kw in text for kw in keywords)



    def process_natural_language(self, text: str) -> List[CommandSuggestion]:
        """Generate a safe shell command from natural language input"""
        prompt = f"""
You are an assistant for a custom AI-powered terminal. 
Your job is to translate natural language commands into safe terminal commands 
that exist in THIS terminal environment.

Available commands:

File commands:
- mkdir <dir>          → create a new directory
- ls [path]            → list files and folders
- rm <file>            → remove a file
- cp <src> <dst>       → copy a file
- mv <src> <dst>       → move or rename a file
- cat <file>           → display file contents
- touch <file>         → create a new empty file
- pwd                  → print current directory
- clear                → clear the terminal

System commands:
- top                  → show CPU usage
- free                 → show memory usage
- df                   → show disk usage
- ps                   → list running processes

### Rules for Translation:
1. Always output **exactly one command** (no explanations, no markdown).
2. Map natural language requests to the most appropriate command, even if phrased indirectly.
   - "show CPU usage", "cpu load", "how busy is my computer" → top
   - "show memory", "how much RAM is free", "memory stats" → free
   - "list files", "show directory contents", "what’s inside this folder" → ls
   - "make a folder called X" → mkdir X
   - "create a file called notes.txt" → touch notes.txt
   - "remove file test.txt" → rm test.txt
   - "copy report.txt to backup.txt" → cp report.txt backup.txt
   - "move file a.txt to b.txt" → mv a.txt b.txt
   - "what directory am I in?" → pwd
   - "clear the screen" → clear
   - "what processes are running?" → ps
   - "disk space", "how much storage" → df
3. If the request cannot be expressed with the available commands, output:
   echo "<natural language request not supported>"
4. Never output dangerous or unimplemented commands.
5. Prefer simplicity: short, direct, POSIX-like syntax.


Natural language input:
"{text}"
"""



        try:
            model = genai.GenerativeModel(self.model)
            response = model.generate_content(prompt)

            command_text = response.text.strip()
            if not command_text:
                command_text = f"echo 'No command generated for: {text}'"

            # Debug
            print(f"Gemini output for '{text}': {command_text}")

            return [CommandSuggestion(
                command=command_text,
                confidence=0.95,
                explanation="Generated by Gemini LLM"
            )]

        except Exception as e:
            return [CommandSuggestion(
                command=f"echo 'Error generating command: {e}'",
                confidence=0.0,
                explanation=f"Error generating command: {e}"
            )]


# --- Quick test ---
if __name__ == "__main__":
    ai = AICommandProcessor()
    test_queries = [
        "create a file a.txt",
        "delete file temp.txt",
        "list all files in current directory",
        "make a folder called test_folder"
    ]
    for q in test_queries:
        suggestions = ai.process_natural_language(q)
        print(f"\nQuery: {q}")
        for s in suggestions:
            print(f"→ Suggested command: {s.command} (confidence: {s.confidence})")
            print(f"   Explanation: {s.explanation}")

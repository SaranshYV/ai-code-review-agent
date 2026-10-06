import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Configuration for AI Code Review Agent"""
    
    # OpenAI Settings
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', '')
    MODEL_NAME = os.getenv('MODEL_NAME', 'gpt-4')
    TEMPERATURE = float(os.getenv('TEMPERATURE', '0.7'))
    
    # Code Analysis Settings
    MAX_FILE_SIZE = int(os.getenv('MAX_FILE_SIZE', '50000'))
    ANALYSIS_DEPTH = os.getenv('ANALYSIS_DEPTH', 'detailed')
    
    # Supported Languages
    SUPPORTED_LANGUAGES = {
        'python': ['.py'],
        'javascript': ['.js', '.jsx'],
        'typescript': ['.ts', '.tsx'],
        'java': ['.java'],
        'cpp': ['.cpp', '.cc', '.cxx'],
        'c': ['.c'],
        'go': ['.go'],
        'rust': ['.rs'],
        'php': ['.php'],
        'ruby': ['.rb'],
    }
    
    # Analysis Categories
    ANALYSIS_CATEGORIES = [
        'syntax_errors',
        'logic_errors',
        'performance_issues',
        'security_vulnerabilities',
        'code_style',
        'best_practices',
        'memory_leaks',
        'type_safety'
    ]

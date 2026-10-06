import openai
import ast
from typing import Dict, List, Any
from config import Config
from colorama import Fore, Style

class CodeAnalyzer:
    """Analyzes code for bugs, errors, and improvements"""
    
    def __init__(self):
        self.config = Config()
        openai.api_key = self.config.OPENAI_API_KEY
        self.model = self.config.MODEL_NAME
    
    def analyze_code(self, code: str, language: str = 'python', filename: str = '') -> Dict[str, Any]:
        """
        Analyze code and identify issues
        
        Args:
            code: Source code to analyze
            language: Programming language
            filename: Original filename for context
        
        Returns:
            Dictionary with analysis results
        """
        print(f"\n{Fore.CYAN}🔍 Analyzing {language} code...{Style.RESET_ALL}")
        
        # Prepare analysis prompt
        prompt = self._create_analysis_prompt(code, language, filename)
        
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert code reviewer and debugger. Analyze code thoroughly and provide detailed feedback on bugs, errors, and improvements."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=self.config.TEMPERATURE,
                max_tokens=2000
            )
            
            analysis = response.choices[0].message.content
            return self._parse_analysis(analysis, code, language)
        
        except Exception as e:
            return {
                'status': 'error',
                'error_message': str(e),
                'code': code
            }
    
    def fix_code(self, code: str, issues: List[str], language: str = 'python') -> Dict[str, Any]:
        """
        Generate fixed version of code
        
        Args:
            code: Original code with issues
            issues: List of identified issues
            language: Programming language
        
        Returns:
            Dictionary with fixed code and explanation
        """
        print(f"\n{Fore.YELLOW}🔧 Generating fixes...{Style.RESET_ALL}")
        
        issues_text = "\n".join([f"- {issue}" for issue in issues])
        
        prompt = f"""
Code Language: {language}

Original Code:
```{language}
{code}
```

Issues Found:
{issues_text}

Please provide:
1. Fixed code
2. Explanation of each fix
3. Best practices applied

Format the fixed code in a code block.
"""
        
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert code fixer. Provide corrected code with clear explanations."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=self.config.TEMPERATURE,
                max_tokens=2000
            )
            
            fixed_response = response.choices[0].message.content
            return {
                'status': 'success',
                'fixed_code': fixed_response,
                'original_code': code
            }
        
        except Exception as e:
            return {
                'status': 'error',
                'error_message': str(e)
            }
    
    def _create_analysis_prompt(self, code: str, language: str, filename: str) -> str:
        """Create detailed analysis prompt"""
        return f"""
Please analyze the following {language} code for issues:

Filename: {filename if filename else 'unknown'}
Language: {language}

```{language}
{code}
```

Provide analysis for:
{chr(10).join([f"- {cat}" for cat in self.config.ANALYSIS_CATEGORIES])}

Format your response as:
1. SUMMARY: Brief overview
2. ISSUES FOUND: List each issue with severity (Critical/High/Medium/Low)
3. EXPLANATIONS: Detailed explanation for each issue
4. RECOMMENDATIONS: Suggested fixes and improvements
5. SECURITY: Any security concerns
"""
    
    def _parse_analysis(self, analysis: str, code: str, language: str) -> Dict[str, Any]:
        """Parse AI analysis response"""
        return {
            'status': 'success',
            'language': language,
            'analysis': analysis,
            'code': code
        }

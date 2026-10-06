#!/usr/bin/env python3
import click
import sys
from pathlib import Path
from colorama import Fore, Style, init
from code_analyzer import CodeAnalyzer
from report_generator import ReportGenerator

init(autoreset=True)

@click.group()
def cli():
    """AI Code Review Agent - Analyze and fix your code automatically"""
    pass

@cli.command()
@click.argument('file_path', type=click.Path(exists=True))
@click.option('--language', '-l', default=None, help='Programming language (auto-detect if not specified)')
@click.option('--save-report', '-s', is_flag=True, help='Save report as JSON')
def analyze(file_path: str, language: str, save_report: bool):
    """
    Analyze a code file for bugs and errors
    
    Example:
        python cli.py analyze myfile.py
        python cli.py analyze myfile.py --language python --save-report
    """
    try:
        file_obj = Path(file_path)
        
        if not file_obj.exists():
            click.echo(f"{Fore.RED}❌ File not found: {file_path}{Style.RESET_ALL}")
            sys.exit(1)
        
        # Read code
        with open(file_obj, 'r', encoding='utf-8') as f:
            code = f.read()
        
        # Detect language if not provided
        if not language:
            language = _detect_language(file_obj.suffix)
        
        # Analyze code
        analyzer = CodeAnalyzer()
        analysis = analyzer.analyze_code(code, language, file_obj.name)
        
        # Generate report
        report_gen = ReportGenerator()
        report_gen.generate_console_report(analysis)
        
        # Save JSON report if requested
        if save_report and analysis['status'] == 'success':
            report_file = f"report_{file_obj.stem}.json"
            report_gen.save_json_report(analysis, report_file)
            click.echo(f"\n{Fore.GREEN}✅ Report saved: {report_file}{Style.RESET_ALL}")
    
    except Exception as e:
        click.echo(f"{Fore.RED}❌ Error: {str(e)}{Style.RESET_ALL}")
        sys.exit(1)

@cli.command()
@click.argument('file_path', type=click.Path(exists=True))
@click.option('--language', '-l', default=None, help='Programming language')
@click.option('--output', '-o', type=click.Path(), help='Save fixed code to file')
def fix(file_path: str, language: str, output: str):
    """
    Analyze code and generate fixes
    
    Example:
        python cli.py fix myfile.py
        python cli.py fix myfile.py --output fixed_file.py
    """
    try:
        file_obj = Path(file_path)
        
        if not file_obj.exists():
            click.echo(f"{Fore.RED}❌ File not found: {file_path}{Style.RESET_ALL}")
            sys.exit(1)
        
        # Read code
        with open(file_obj, 'r', encoding='utf-8') as f:
            code = f.read()
        
        # Detect language if not provided
        if not language:
            language = _detect_language(file_obj.suffix)
        
        # Analyze code
        analyzer = CodeAnalyzer()
        analysis = analyzer.analyze_code(code, language, file_obj.name)
        
        # Generate report
        report_gen = ReportGenerator()
        report_gen.generate_console_report(analysis)
        
        # Extract issues from analysis
        issues = _extract_issues(analysis['analysis'])
        
        # Fix code
        if issues:
            fix_result = analyzer.fix_code(code, issues, language)
            report_gen.generate_fix_report(fix_result)
            
            # Save to file if output path specified
            if output:
                with open(output, 'w', encoding='utf-8') as f:
                    f.write(fix_result['fixed_code'])
                click.echo(f"\n{Fore.GREEN}✅ Fixed code saved: {output}{Style.RESET_ALL}")
        else:
            click.echo(f"\n{Fore.GREEN}✅ No issues found!{Style.RESET_ALL}")
    
    except Exception as e:
        click.echo(f"{Fore.RED}❌ Error: {str(e)}{Style.RESET_ALL}")
        sys.exit(1)

@cli.command()
def interactive():
    """
    Start interactive mode - paste code for analysis
    """
    click.echo(f"{Fore.CYAN}🤖 AI Code Review Agent - Interactive Mode{Style.RESET_ALL}")
    click.echo("Paste your code below. Press Ctrl+D (Unix) or Ctrl+Z (Windows) when done:\n")
    
    try:
        code_lines = []
        while True:
            line = input()
            code_lines.append(line)
    except EOFError:
        pass
    
    code = "\n".join(code_lines)
    
    if not code.strip():
        click.echo(f"{Fore.RED}❌ No code provided{Style.RESET_ALL}")
        sys.exit(1)
    
    language = click.prompt('Enter programming language (python/javascript/java/etc)', default='python')
    
    try:
        # Analyze
        analyzer = CodeAnalyzer()
        analysis = analyzer.analyze_code(code, language)
        
        # Report
        report_gen = ReportGenerator()
        report_gen.generate_console_report(analysis)
        
        # Ask for fix
        if click.confirm('\nWould you like to generate fixes?'):
            issues = _extract_issues(analysis['analysis'])
            if issues:
                fix_result = analyzer.fix_code(code, issues, language)
                report_gen.generate_fix_report(fix_result)
    
    except Exception as e:
        click.echo(f"{Fore.RED}❌ Error: {str(e)}{Style.RESET_ALL}")
        sys.exit(1)

def _detect_language(file_extension: str) -> str:
    """Detect programming language from file extension"""
    extension_map = {
        '.py': 'python',
        '.js': 'javascript',
        '.ts': 'typescript',
        '.java': 'java',
        '.cpp': 'cpp',
        '.c': 'c',
        '.go': 'go',
        '.rs': 'rust',
        '.php': 'php',
        '.rb': 'ruby',
    }
    return extension_map.get(file_extension, 'python')

def _extract_issues(analysis_text: str) -> list:
    """Extract issues from analysis text"""
    issues = []
    for line in analysis_text.split('\n'):
        if line.strip().startswith('-') and any(keyword in line.lower() for keyword in ['error', 'bug', 'issue', 'problem']):
            issues.append(line.strip('- ').strip())
    return issues if issues else ['General code improvement']

if __name__ == '__main__':
    cli()

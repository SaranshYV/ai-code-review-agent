from typing import Dict, Any, List
from datetime import datetime
from colorama import Fore, Back, Style
import json

class ReportGenerator:
    """Generates detailed code review reports"""
    
    def __init__(self):
        self.timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    def generate_console_report(self, analysis: Dict[str, Any]) -> None:
        """Display report in console with colors"""
        
        print("\n" + "="*80)
        print(f"{Back.BLUE}{Fore.WHITE} AI CODE REVIEW REPORT {Style.RESET_ALL}")
        print(f"Generated: {self.timestamp}")
        print("="*80)
        
        if analysis['status'] == 'error':
            print(f"{Fore.RED}❌ Error: {analysis['error_message']}{Style.RESET_ALL}")
            return
        
        print(f"\n{Fore.CYAN}Language: {analysis['language'].upper()}{Style.RESET_ALL}")
        print(f"\n{Fore.GREEN}📋 ANALYSIS RESULTS:{Style.RESET_ALL}")
        print("-" * 80)
        print(analysis['analysis'])
        print("-" * 80)
    
    def generate_fix_report(self, fix_result: Dict[str, Any]) -> None:
        """Display fix report"""
        
        print("\n" + "="*80)
        print(f"{Back.GREEN}{Fore.WHITE} CODE FIX REPORT {Style.RESET_ALL}")
        print(f"Generated: {self.timestamp}")
        print("="*80)
        
        if fix_result['status'] == 'error':
            print(f"{Fore.RED}❌ Error: {fix_result['error_message']}{Style.RESET_ALL}")
            return
        
        print(f"\n{Fore.GREEN}✅ Fixed Code and Explanations:{Style.RESET_ALL}")
        print("-" * 80)
        print(fix_result['fixed_code'])
        print("-" * 80)
    
    def save_json_report(self, analysis: Dict[str, Any], filename: str) -> str:
        """Save analysis as JSON file"""
        report = {
            'timestamp': self.timestamp,
            'analysis': analysis
        }
        
        with open(filename, 'w') as f:
            json.dump(report, f, indent=2)
        
        return filename

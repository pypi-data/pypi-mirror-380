"""
Simple, clean UI components for omga-cli
Provides clean, professional interface without color codes
"""

from enum import Enum
from typing import Dict, Optional, List, Any

class MessageType(Enum):
    SUCCESS = "success"
    ERROR = "error"
    WARNING = "warning"
    INFO = "info"
    DEBUG = "debug"

class OmgaUI:
    """Simple, clean UI manager for omga-cli"""
    
    def __init__(self):
        self.icons = {
            MessageType.SUCCESS: "✅",
            MessageType.ERROR: "❌",
            MessageType.WARNING: "⚠️",
            MessageType.INFO: "ℹ️",
            MessageType.DEBUG: "🔍"
        }
    
    def print_message(self, message: str, msg_type: MessageType = MessageType.INFO, 
                     title: Optional[str] = None, show_icon: bool = True):
        """Print clean message with icon"""
        icon = self.icons[msg_type] if show_icon else ""
        
        if title:
            print(f"\n{title}")
            print("─" * len(title))
        
        if icon:
            print(f"{icon} {message}")
        else:
            print(message)
        
        if title:
            print()
    
    def print_success(self, message: str, title: str = "Success"):
        """Print success message"""
        self.print_message(message, MessageType.SUCCESS, title)
    
    def print_error(self, message: str, title: str = "Error"):
        """Print error message"""
        self.print_message(message, MessageType.ERROR, title)
    
    def print_warning(self, message: str, title: str = "Warning"):
        """Print warning message"""
        self.print_message(message, MessageType.WARNING, title)
    
    def print_info(self, message: str, title: str = "Info"):
        """Print info message"""
        self.print_message(message, MessageType.INFO, title)
    
    def print_code_block(self, code: str, language: str = "python", 
                        title: Optional[str] = None, show_line_numbers: bool = True):
        """Print formatted code block"""
        if title:
            print(f"\n{title}")
            print("─" * len(title))
        
        print(code)
        
        if title:
            print()
    
    def print_table(self, data: List[Dict[str, Any]], title: str = "Results"):
        """Print data in a simple table"""
        if not data:
            self.print_warning("No data to display")
            return
        
        print(f"\n{title}")
        print("─" * len(title))
        
        # Get column widths
        columns = list(data[0].keys())
        widths = {}
        for col in columns:
            widths[col] = max(len(str(col)), max(len(str(row[col])) for row in data))
        
        # Print header
        header = " | ".join(str(col).ljust(widths[col]) for col in columns)
        print(header)
        print("─" * len(header))
        
        # Print rows
        for row in data:
            row_str = " | ".join(str(row[col]).ljust(widths[col]) for col in columns)
            print(row_str)
        
        print()
    
    def print_diff(self, old_text: str, new_text: str, title: str = "Changes"):
        """Print simple diff"""
        print(f"\n{title}")
        print("─" * len(title))
        print("OLD:")
        print(old_text)
        print("\nNEW:")
        print(new_text)
        print()
    
    def print_help(self, commands: Dict[str, str]):
        """Print help in a clean format"""
        print("\nAvailable Commands")
        print("─" * 18)
        
        # Get column widths
        max_cmd_width = max(len(cmd) for cmd in commands.keys())
        
        for cmd, desc in commands.items():
            print(f"{cmd.ljust(max_cmd_width)} │ {desc}")
        
        print()
    
    def print_progress(self, message: str = "Processing..."):
        """Show progress indicator (no-op for clean output)"""
        pass
    
    def print_spinner(self, message: str, duration: float = 2.0):
        """Show spinner (no-op for clean output)"""
        pass
    
    def confirm(self, message: str, default: bool = False) -> bool:
        """Show confirmation prompt"""
        response = input(f"{message} [{'Y/n' if default else 'y/N'}]: ").strip().lower()
        if not response:
            return default
        return response in ['y', 'yes']
    
    def prompt(self, message: str, default: str = "") -> str:
        """Show input prompt"""
        if default:
            response = input(f"{message} [{default}]: ").strip()
            return response if response else default
        else:
            return input(f"{message}: ").strip()
    
    def print_welcome(self):
        """Print minimal welcome message"""
        print()
        print("🚀 omga-cli - AI-Powered Development Assistant")
        print("Developed by Pouria Hosseini | PouriaHosseini.news")
        print()
        print("Type 'help' for commands or 'exit' to quit")
        print()
    
    def print_feature_showcase(self):
        """Print feature showcase"""
        features = [
            ("🔍 Code Analysis", "Syntax checking, linting, error detection"),
            ("🤖 AI Assistant", "Smart explanations, fixes, and Q&A"),
            ("⚡ Fast Execution", "Safe command execution with progress"),
            ("🎨 Clean UI", "Simple, professional interface"),
            ("📚 Code Management", "Snippets, templates, scaffolding"),
            ("🔧 Auto-fixes", "AI-powered code improvements"),
            ("📊 Progress Tracking", "Real-time status and feedback"),
            ("🎯 Smart Completion", "AI-enhanced tab completion")
        ]
        
        print("\n🌟 Feature Showcase")
        print("─" * 20)
        
        for feature, desc in features:
            print(f"{feature:<20} │ {desc}")
        
        print()
    
    def print_status(self, status: str, details: Optional[str] = None):
        """Print status with optional details"""
        print(f"\n📊 {status}")
        if details:
            print(details)
        print()
    
    def print_separator(self, char: str = "─", style: str = "dim white"):
        """Print visual separator"""
        print(char * 80)
    
    def print_footer(self, message: str = "Happy coding! 🎉"):
        """Print footer message"""
        print(f"\n💡 {message}")
    
    def print_ai_response(self, response: str, title: str = "AI Response"):
        """Print AI response in a clean, formatted way"""
        print(f"\n{'='*80}")
        print(f"🤖 {title}")
        print('='*80)
        print()
        
        # Clean and format the response
        formatted_response = self._format_ai_text(response)
        print(formatted_response)
        
        print()
        print('='*80)
        print()
    
    def _format_ai_text(self, text: str) -> str:
        """Format AI text with proper bullet points and structure"""
        if not text:
            return ""
        
        lines = text.strip().split('\n')
        formatted_lines = []
        in_list = False
        
        for line in lines:
            line = line.strip()
            if not line:
                if in_list:
                    formatted_lines.append("")
                in_list = False
                continue
            
            # Handle bullet points (clean format)
            if line.startswith('*') or line.startswith('-') or line.startswith('•'):
                # Remove the bullet and clean the text
                clean_line = line[1:].strip()
                if clean_line.startswith('**') and clean_line.endswith('**'):
                    # Bold text
                    clean_line = clean_line[2:-2]
                    formatted_lines.append(f"  • {clean_line}")
                else:
                    formatted_lines.append(f"  • {clean_line}")
                in_list = True
            
            # Handle numbered lists
            elif line and line[0].isdigit() and '.' in line[:3]:
                formatted_lines.append(f"  {line}")
                in_list = True
            
            # Handle headers (lines that end with :)
            elif line.endswith(':') and len(line) < 50 and not line.startswith('  '):
                if in_list:
                    formatted_lines.append("")
                formatted_lines.append(f"📌 {line}")
                in_list = False
            
            # Handle code blocks
            elif line.startswith('    ') or '`' in line:
                formatted_lines.append(f"  {line}")
                in_list = False
            
            # Regular text
            else:
                if in_list:
                    formatted_lines.append("")
                # Clean up markdown formatting
                clean_line = line.replace('**', '').replace('*', '').replace('`', '')
                formatted_lines.append(f"  {clean_line}")
                in_list = False
        
        return '\n'.join(formatted_lines)

# Global UI instance
ui = OmgaUI()
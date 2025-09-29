"""
Interactive conversation manager for Amvka.
Handles multi-step interactions, clarifications, and context-aware responses.
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any
import json

from .utils import print_error, print_info, print_success, print_warning, safe_input
from .environment import EnvironmentDetector


class ConversationManager:
    """Manages interactive conversations and context for Amvka."""
    
    def __init__(self, llm_client, executor):
        self.llm_client = llm_client
        self.executor = executor
        self.env_detector = EnvironmentDetector()
        self.context_analyzer = ContextAnalyzer()
        self.conversation_history = []
        self.current_context = {}
        self.dry_run = False
    
    def process_query(self, query: str, auto_confirm: bool = False) -> bool:
        """Process a query with intelligent conversation handling."""
        print_info(f"Processing: {query}")
        
        # Analyze the query for ambiguity and context needs
        analysis = self._analyze_query(query)
        
        if analysis["needs_clarification"]:
            return self._handle_clarification(query, analysis, auto_confirm)
        else:
            # Direct command generation - let AI handle everything intelligently
            command = self.llm_client.get_command(query)
            if command:
                return self._execute_with_confirmation(command, auto_confirm)
            else:
                # AI has already handled the response (conversational, help, etc.)
                # No need to show additional error messages
                return False
    
    def _analyze_query(self, query: str) -> Dict[str, Any]:
        """Analyze query to determine if clarification is needed."""
        analysis = {
            "needs_clarification": False,
            "clarification_type": None,
            "context_data": {},
            "suggested_actions": []
        }
        
        # Check for ambiguous file references
        if self._contains_ambiguous_file_reference(query):
            file_analysis = self.context_analyzer.analyze_files_in_directory(os.getcwd())
            analysis.update({
                "needs_clarification": True,
                "clarification_type": "file_selection",
                "context_data": file_analysis
            })
        
        # Check for project-related queries
        elif self._is_project_query(query):
            project_analysis = self.context_analyzer.analyze_project_structure(os.getcwd())
            analysis.update({
                "needs_clarification": True,
                "clarification_type": "project_context",
                "context_data": project_analysis
            })
        
        # Check for ambiguous process queries
        elif self._contains_process_reference(query):
            analysis.update({
                "needs_clarification": True,
                "clarification_type": "process_selection"
            })
        
        return analysis
    
    def _contains_ambiguous_file_reference(self, query: str) -> bool:
        """Check if query contains ambiguous file references."""
        patterns = [
            r'\bpython\s+file\b',
            r'\brun\s+.*\bfile\b',
            r'\bexecute\s+.*\bfile\b',
            r'\bopen\s+.*\bfile\b',
            r'\bedit\s+.*\bfile\b',
            r'\bdelete\s+.*\bfile\b',
            r'\bthe\s+.*\bfile\b',
            r'\ba\s+.*\bfile\b',
            r'\bscript\b',
            r'\bprogram\b'
        ]
        return any(re.search(pattern, query, re.IGNORECASE) for pattern in patterns)
    
    def _is_project_query(self, query: str) -> bool:
        """Check if query is about project structure or operations."""
        patterns = [
            r'\bproject\b',
            r'\binstall\s+dependencies\b',
            r'\bbuild\b',
            r'\brun\s+tests\b',
            r'\bstart\s+server\b',
            r'\bdeploy\b',
            r'\bpackage\b'
        ]
        return any(re.search(pattern, query, re.IGNORECASE) for pattern in patterns)
    
    def _contains_process_reference(self, query: str) -> bool:
        """Check if query contains process references."""
        patterns = [
            r'\bkill\s+.*\bprocess\b',
            r'\bstop\s+.*\bprocess\b',
            r'\bfind\s+.*\bprocess\b',
            r'\bshow\s+.*\bprocess\b'
        ]
        return any(re.search(pattern, query, re.IGNORECASE) for pattern in patterns)
    
    def _handle_clarification(self, query: str, analysis: Dict, auto_confirm: bool) -> bool:
        """Handle queries that need clarification."""
        clarification_type = analysis["clarification_type"]
        context_data = analysis["context_data"]
        
        if clarification_type == "file_selection":
            return self._handle_file_selection(query, context_data, auto_confirm)
        elif clarification_type == "project_context":
            return self._handle_project_context(query, context_data, auto_confirm)
        elif clarification_type == "process_selection":
            return self._handle_process_selection(query, auto_confirm)
        
        return False
    
    def _handle_file_selection(self, query: str, file_analysis: Dict, auto_confirm: bool) -> bool:
        """Handle file selection scenarios."""
        relevant_files = self._filter_relevant_files(query, file_analysis)
        
        if not relevant_files:
            print_warning("No relevant files found for your request.")
            return False
        
        if len(relevant_files) == 1:
            # Only one relevant file, proceed directly
            file_path = relevant_files[0]["path"]
            enhanced_query = f"{query} {file_path}"
            command = self.llm_client.get_command(enhanced_query)
            if command:
                return self._execute_with_confirmation(command, auto_confirm)
        else:
            # Multiple files, ask user to choose
            return self._show_file_selection_menu(query, relevant_files, auto_confirm)
        
        return False
    
    def _filter_relevant_files(self, query: str, file_analysis: Dict) -> List[Dict]:
        """Filter files based on query context."""
        relevant_files = []
        
        # Determine file type based on query
        if re.search(r'\bpython\b', query, re.IGNORECASE):
            relevant_files.extend(file_analysis.get("python_files", []))
        elif re.search(r'\bjavascript\b|\bjs\b|\bnode\b', query, re.IGNORECASE):
            relevant_files.extend(file_analysis.get("javascript_files", []))
        elif re.search(r'\bhtml\b', query, re.IGNORECASE):
            relevant_files.extend(file_analysis.get("html_files", []))
        elif re.search(r'\bscript\b', query, re.IGNORECASE):
            relevant_files.extend(file_analysis.get("script_files", []))
        elif re.search(r'\bconfig\b', query, re.IGNORECASE):
            relevant_files.extend(file_analysis.get("config_files", []))
        else:
            # General file operations - show all files
            relevant_files.extend(file_analysis.get("all_files", []))
        
        return relevant_files
    
    def _show_file_selection_menu(self, query: str, files: List[Dict], auto_confirm: bool) -> bool:
        """Show interactive file selection menu."""
        print_info("Multiple files found. Please select one:")
        
        for i, file_info in enumerate(files, 1):
            file_path = file_info["path"]
            file_size = file_info.get("size", "unknown")
            file_desc = file_info.get("description", "")
            print(f"{i}. {file_path} ({file_size} bytes) {file_desc}")
        
        print("0. Cancel")
        
        while True:
            try:
                choice = safe_input(f"Select file (1-{len(files)}, 0 to cancel): ", "0")
                choice_num = int(choice)
                
                if choice_num == 0:
                    print_info("Operation cancelled.")
                    return False
                elif 1 <= choice_num <= len(files):
                    selected_file = files[choice_num - 1]
                    file_path = selected_file["path"]
                    enhanced_query = f"{query} {file_path}"
                    command = self.llm_client.get_command(enhanced_query)
                    if command:
                        return self._execute_with_confirmation(command, auto_confirm)
                    else:
                        print_error("Could not generate command for the selected file.")
                        return False
                else:
                    print_error(f"Please enter a number between 0 and {len(files)}")
            except ValueError:
                print_error("Please enter a valid number")
    
    def _handle_project_context(self, query: str, project_analysis: Dict, auto_confirm: bool) -> bool:
        """Handle project-related queries with context."""
        project_type = project_analysis.get("project_type", "unknown")
        
        print_info(f"Detected {project_type} project")
        
        # Show available project operations
        operations = project_analysis.get("available_operations", [])
        if operations:
            print_info("Available operations:")
            for i, op in enumerate(operations, 1):
                print(f"{i}. {op['name']} - {op['description']}")
            
            print("0. Custom command")
            
            while True:
                try:
                    choice = safe_input(f"Select operation (1-{len(operations)}, 0 for custom): ", "0")
                    choice_num = int(choice)
                    
                    if choice_num == 0:
                        # Custom command
                        command = self.llm_client.get_command(query)
                        if command:
                            return self._execute_with_confirmation(command, auto_confirm)
                    elif 1 <= choice_num <= len(operations):
                        operation = operations[choice_num - 1]
                        command = operation["command"]
                        return self._execute_with_confirmation(command, auto_confirm)
                    else:
                        print_error(f"Please enter a number between 0 and {len(operations)}")
                except ValueError:
                    print_error("Please enter a valid number")
        else:
            # No predefined operations, generate command
            command = self.llm_client.get_command(query)
            if command:
                return self._execute_with_confirmation(command, auto_confirm)
        
        return False
    
    def _handle_process_selection(self, query: str, auto_confirm: bool) -> bool:
        """Handle process selection scenarios."""
        # This could be enhanced to show running processes and let user select
        print_info("Process operations require specific process names or IDs.")
        clarification = safe_input("Please specify the process name or ID: ", "")
        
        if clarification:
            enhanced_query = f"{query} {clarification}"
            command = self.llm_client.get_command(enhanced_query)
            if command:
                return self._execute_with_confirmation(command, auto_confirm)
        
        return False
    
    def _execute_with_confirmation(self, command: str, auto_confirm: bool) -> bool:
        """Execute command with optional confirmation."""
        print_success(f"Suggested command: {command}")
        
        if self.dry_run:
            print_info("DRY RUN: Command would be executed but not running due to --dry-run flag")
            return True
        
        if not auto_confirm:
            confirm = safe_input("Run this command? (Y/n): ", "y").lower().strip()
            if confirm in ["n", "no"]:
                print_info("Command execution cancelled.")
                return False
        
        return self.executor.execute(command)


class ContextAnalyzer:
    """Analyzes current directory and project context."""
    
    def __init__(self):
        self.env_detector = EnvironmentDetector()
    
    def analyze_files_in_directory(self, directory: str) -> Dict[str, List[Dict]]:
        """Analyze files in the given directory."""
        analysis = {
            "python_files": [],
            "javascript_files": [],
            "html_files": [],
            "script_files": [],
            "config_files": [],
            "all_files": []
        }
        
        try:
            for item in Path(directory).iterdir():
                if item.is_file():
                    file_info = {
                        "path": str(item.name),
                        "full_path": str(item),
                        "size": item.stat().st_size,
                        "extension": item.suffix.lower()
                    }
                    
                    # Categorize files
                    if item.suffix.lower() == ".py":
                        file_info["description"] = "Python script"
                        analysis["python_files"].append(file_info)
                    elif item.suffix.lower() in [".js", ".mjs", ".jsx"]:
                        file_info["description"] = "JavaScript file"
                        analysis["javascript_files"].append(file_info)
                    elif item.suffix.lower() in [".html", ".htm"]:
                        file_info["description"] = "HTML file"
                        analysis["html_files"].append(file_info)
                    elif item.suffix.lower() in [".sh", ".bat", ".cmd", ".ps1"]:
                        file_info["description"] = "Script file"
                        analysis["script_files"].append(file_info)
                    elif item.name.lower() in ["config.json", "package.json", "requirements.txt", "setup.py", ".env"]:
                        file_info["description"] = "Configuration file"
                        analysis["config_files"].append(file_info)
                    
                    analysis["all_files"].append(file_info)
        
        except Exception as e:
            print_error(f"Error analyzing directory: {e}")
        
        return analysis
    
    def analyze_project_structure(self, directory: str) -> Dict[str, Any]:
        """Analyze project structure and determine project type."""
        analysis = {
            "project_type": "unknown",
            "available_operations": [],
            "main_files": [],
            "config_files": []
        }
        
        try:
            dir_path = Path(directory)
            
            # Check for specific project indicators
            if (dir_path / "package.json").exists():
                analysis["project_type"] = "Node.js"
                analysis["available_operations"] = [
                    {"name": "Install dependencies", "command": "npm install", "description": "Install npm packages"},
                    {"name": "Start development", "command": "npm start", "description": "Start development server"},
                    {"name": "Run tests", "command": "npm test", "description": "Run test suite"},
                    {"name": "Build project", "command": "npm run build", "description": "Build for production"}
                ]
            
            elif (dir_path / "requirements.txt").exists() or (dir_path / "setup.py").exists():
                analysis["project_type"] = "Python"
                analysis["available_operations"] = [
                    {"name": "Install dependencies", "command": "pip install -r requirements.txt", "description": "Install Python packages"},
                    {"name": "Run main script", "command": "python main.py", "description": "Run main Python script"},
                    {"name": "Run tests", "command": "python -m pytest", "description": "Run test suite"}
                ]
            
            elif (dir_path / "Cargo.toml").exists():
                analysis["project_type"] = "Rust"
                analysis["available_operations"] = [
                    {"name": "Build project", "command": "cargo build", "description": "Build Rust project"},
                    {"name": "Run project", "command": "cargo run", "description": "Run Rust project"},
                    {"name": "Run tests", "command": "cargo test", "description": "Run test suite"}
                ]
            
            elif (dir_path / "pom.xml").exists():
                analysis["project_type"] = "Java (Maven)"
                analysis["available_operations"] = [
                    {"name": "Compile project", "command": "mvn compile", "description": "Compile Java project"},
                    {"name": "Run tests", "command": "mvn test", "description": "Run test suite"},
                    {"name": "Package project", "command": "mvn package", "description": "Package project"}
                ]
            
            elif (dir_path / "Makefile").exists():
                analysis["project_type"] = "Make-based"
                analysis["available_operations"] = [
                    {"name": "Build project", "command": "make", "description": "Build project using Makefile"},
                    {"name": "Clean build", "command": "make clean", "description": "Clean build artifacts"},
                    {"name": "Install", "command": "make install", "description": "Install project"}
                ]
        
        except Exception as e:
            print_error(f"Error analyzing project structure: {e}")
        
        return analysis
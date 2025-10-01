import ast
import os
import sys
import importlib.util
import inspect
import pandas as pd
import matplotlib.pyplot as plt
from typing import List, Dict, Any, Optional
import warnings

class FootsbvizErrorChecker:
    """Comprehensive error checker for footsbviz library."""
    
    def __init__(self):
        self.errors = []
        self.warnings = []
        self.suggestions = []
        
    def log_error(self, category: str, message: str, file_path: str = None, line_num: int = None):
        """Log an error with context."""
        error_info = {
            'category': category,
            'message': message,
            'file': file_path,
            'line': line_num
        }
        self.errors.append(error_info)
        
    def log_warning(self, category: str, message: str, file_path: str = None):
        """Log a warning with context."""
        warning_info = {
            'category': category,
            'message': message,
            'file': file_path
        }
        self.warnings.append(warning_info)
        
    def log_suggestion(self, category: str, message: str):
        """Log an improvement suggestion."""
        self.suggestions.append({'category': category, 'message': message})

    def check_imports(self, code: str, file_path: str):
        """Check for import-related issues."""
        try:
            tree = ast.parse(code)
            imports = []
            
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        imports.append(alias.name)
                elif isinstance(node, ast.ImportFrom):
                    module = node.module or ""
                    for alias in node.names:
                        imports.append(f"{module}.{alias.name}")
            
            # Check for common missing imports in visualization libraries
            required_viz_imports = ['matplotlib', 'pandas', 'numpy']
            missing_imports = []
            
            for req in required_viz_imports:
                if not any(req in imp for imp in imports):
                    missing_imports.append(req)
            
            if missing_imports:
                self.log_warning("IMPORTS", 
                    f"Potentially missing imports: {missing_imports}", file_path)
                    
        except SyntaxError as e:
            self.log_error("SYNTAX", f"Syntax error in imports: {e}", file_path, e.lineno)

    def check_function_signatures(self, code: str, file_path: str):
        """Check function signatures for common issues."""
        try:
            tree = ast.parse(code)
            
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    # Check for missing docstrings
                    if not ast.get_docstring(node):
                        self.log_warning("DOCUMENTATION", 
                            f"Function '{node.name}' missing docstring", file_path)
                    
                    # Check for mutable default arguments
                    for default in node.args.defaults:
                        if isinstance(default, (ast.List, ast.Dict, ast.Set)):
                            self.log_error("MUTABLE_DEFAULT", 
                                f"Function '{node.name}' has mutable default argument", 
                                file_path, node.lineno)
                    
                    # Check for too many arguments (> 10 might be unwieldy)
                    total_args = len(node.args.args) + len(node.args.kwonlyargs)
                    if total_args > 10:
                        self.log_warning("COMPLEXITY", 
                            f"Function '{node.name}' has {total_args} parameters (consider refactoring)", 
                            file_path)
                            
        except SyntaxError as e:
            self.log_error("SYNTAX", f"Syntax error in function definitions: {e}", file_path, e.lineno)

    def check_pandas_usage(self, code: str, file_path: str):
        """Check for common pandas anti-patterns."""
        pandas_issues = [
            ('iterrows()', 'Consider using vectorized operations instead of iterrows()'),
            ('itertuples()', 'Consider using vectorized operations instead of itertuples()'),
            ('.values', 'Consider using .to_numpy() instead of .values'),
            ('inplace=True', 'Consider avoiding inplace operations for better debugging'),
        ]
        
        for pattern, suggestion in pandas_issues:
            if pattern in code:
                self.log_warning("PANDAS", 
                    f"Found {pattern}: {suggestion}", file_path)

    def check_matplotlib_usage(self, code: str, file_path: str):
        """Check for matplotlib best practices."""
        matplotlib_checks = [
            ('plt.show()', 'Consider making plt.show() optional with a parameter'),
            ('plt.savefig(', 'Good: Using savefig for plot saving'),
            ('fig, ax = plt.subplots()', 'Good: Using object-oriented matplotlib interface'),
        ]
        
        # Check if using pyplot instead of object-oriented approach
        if 'plt.' in code and 'fig, ax' not in code:
            self.log_suggestion("MATPLOTLIB", 
                "Consider using object-oriented matplotlib (fig, ax = plt.subplots()) for better control")

    def check_error_handling(self, code: str, file_path: str):
        """Check for proper error handling."""
        try:
            tree = ast.parse(code)
            has_try_except = False
            
            for node in ast.walk(tree):
                if isinstance(node, ast.Try):
                    has_try_except = True
                    # Check for bare except clauses
                    for handler in node.handlers:
                        if handler.type is None:
                            self.log_error("ERROR_HANDLING", 
                                "Bare except clause found - specify exception types", 
                                file_path, handler.lineno)
            
            # For data visualization libraries, error handling is important
            if not has_try_except:
                self.log_suggestion("ERROR_HANDLING", 
                    "Consider adding error handling for data validation and plotting errors")
                    
        except SyntaxError as e:
            self.log_error("SYNTAX", f"Syntax error in error handling: {e}", file_path, e.lineno)

    def check_data_validation(self, code: str, file_path: str):
        """Check for input data validation."""
        validation_patterns = [
            'isinstance(',
            'assert ',
            'raise ValueError',
            'raise TypeError',
            'if not ',
        ]
        
        has_validation = any(pattern in code for pattern in validation_patterns)
        
        if not has_validation:
            self.log_suggestion("DATA_VALIDATION", 
                "Consider adding input validation for DataFrames and parameters")

    def check_specific_footsbviz_issues(self, code: str, file_path: str):
        """Check for specific issues relevant to footsbviz."""
        
        # Check for hardcoded values that should be parameters
        if 'StatsBomb' in code:
            hardcoded_checks = [
                ('120', 'Pitch length hardcoded - should be parameter'),
                ('80', 'Pitch width hardcoded - should be parameter'),
                ('#d00', 'Team color hardcoded - should be parameter'),
            ]
            
            for value, issue in hardcoded_checks:
                if value in code and 'default' not in code.lower():
                    self.log_warning("HARDCODED", issue, file_path)
        
        # Check for column name assumptions
        common_sb_columns = ['x', 'y', 'team', 'player', 'type', 'outcome']
        for col in common_sb_columns:
            if f"'{col}'" in code or f'"{col}"' in code:
                self.log_suggestion("FLEXIBILITY", 
                    f"Column '{col}' assumed - consider making column names configurable")

    def check_performance_issues(self, code: str, file_path: str):
        """Check for potential performance issues."""
        performance_checks = [
            ('for i in range(len(', 'Use direct iteration instead of range(len())'),
            ('.copy()', 'Unnecessary copying might impact performance'),
            ('pd.concat([', 'Multiple pd.concat calls in loop can be slow'),
        ]
        
        for pattern, issue in performance_checks:
            if pattern in code:
                self.log_warning("PERFORMANCE", issue, file_path)

    def analyze_file(self, file_path: str):
        """Analyze a single Python file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                code = f.read()
                
            print(f"\n🔍 Analyzing: {file_path}")
            
            # Run all checks
            self.check_imports(code, file_path)
            self.check_function_signatures(code, file_path)
            self.check_pandas_usage(code, file_path)
            self.check_matplotlib_usage(code, file_path)
            self.check_error_handling(code, file_path)
            self.check_data_validation(code, file_path)
            self.check_specific_footsbviz_issues(code, file_path)
            self.check_performance_issues(code, file_path)
            
        except FileNotFoundError:
            self.log_error("FILE", f"File not found: {file_path}", file_path)
        except Exception as e:
            self.log_error("ANALYSIS", f"Error analyzing file: {e}", file_path)

    def analyze_directory(self, directory: str):
        """Analyze all Python files in a directory."""
        for root, dirs, files in os.walk(directory):
            # Skip common directories to ignore
            dirs[:] = [d for d in dirs if d not in ['__pycache__', '.git', 'venv', 'env']]
            
            for file in files:
                if file.endswith('.py'):
                    file_path = os.path.join(root, file)
                    self.analyze_file(file_path)

    def test_library_import(self):
        """Test if the library can be imported and basic functions work."""
        try:
            import footsbviz as fz
            self.log_suggestion("IMPORT", "✅ Library imports successfully")
            
            # Test if main function exists
            if hasattr(fz, 'create_shot_map_team'):
                self.log_suggestion("API", "✅ Main function create_shot_map_team exists")
                
                # Check function signature
                sig = inspect.signature(fz.create_shot_map_team)
                params = list(sig.parameters.keys())
                
                required_params = ['events_df', 'team_name']
                missing_params = [p for p in required_params if p not in params]
                
                if missing_params:
                    self.log_error("API", f"Missing expected parameters: {missing_params}")
                else:
                    self.log_suggestion("API", "✅ Expected parameters present")
            else:
                self.log_error("API", "Main function create_shot_map_team not found")
                
        except ImportError as e:
            self.log_error("IMPORT", f"Cannot import footsbviz: {e}")
        except Exception as e:
            self.log_error("IMPORT", f"Error testing library: {e}")

    def generate_report(self):
        """Generate a comprehensive error report."""
        print("\n" + "="*80)
        print("🔍 FOOTSBVIZ ERROR ANALYSIS REPORT")
        print("="*80)
        
        # Test library import
        self.test_library_import()
        
        # Errors
        if self.errors:
            print(f"\n❌ ERRORS FOUND ({len(self.errors)}):")
            print("-" * 50)
            for i, error in enumerate(self.errors, 1):
                print(f"{i}. {error['category']}: {error['message']}")
                if error['file']:
                    print(f"   📁 File: {error['file']}")
                if error['line']:
                    print(f"   📍 Line: {error['line']}")
                print()
        else:
            print("\n✅ NO CRITICAL ERRORS FOUND!")
        
        # Warnings
        if self.warnings:
            print(f"\n⚠️ WARNINGS ({len(self.warnings)}):")
            print("-" * 50)
            for i, warning in enumerate(self.warnings, 1):
                print(f"{i}. {warning['category']}: {warning['message']}")
                if warning['file']:
                    print(f"   📁 File: {warning['file']}")
                print()
        
        # Suggestions
        if self.suggestions:
            print(f"\n💡 SUGGESTIONS FOR IMPROVEMENT ({len(self.suggestions)}):")
            print("-" * 50)
            for i, suggestion in enumerate(self.suggestions, 1):
                print(f"{i}. {suggestion['category']}: {suggestion['message']}")
                print()
        
        # Summary
        print("="*80)
        print(f"📊 SUMMARY: {len(self.errors)} errors, {len(self.warnings)} warnings, {len(self.suggestions)} suggestions")
        print("="*80)

# Usage example
def main():
    checker = FootsbvizErrorChecker()
    
    # Option 1: Test the installed library
    print("Testing installed library...")
    checker.test_library_import()
    
    # Option 2: Analyze source files (uncomment and modify path as needed)
    # checker.analyze_directory("./footsbviz")  # Replace with your source directory
    # checker.analyze_file("./footsbviz/main.py")  # Replace with specific file
    
    # Generate report
    checker.generate_report()
    
    return checker

if __name__ == "__main__":
    checker = main()
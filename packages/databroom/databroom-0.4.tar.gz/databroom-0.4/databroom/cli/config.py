# databroom/cli/config.py

import inspect
from typing import Dict, List, Any, Union
from databroom.core import cleaning_ops
from databroom.core.broom import Broom

# Dynamically get available functions (same as pipeline.py)
available_functions = [name for name, obj in inspect.getmembers(cleaning_ops, inspect.isfunction)]

# Get Broom methods that correspond to cleaning_ops functions
Broom_methods = [name for name in dir(Broom) 
                   if not name.startswith('_') 
                   and callable(getattr(Broom, name))
                   and name in available_functions]

def extract_function_params(func) -> Dict[str, Any]:
    """Extracts function parameters with their types and default values"""
    sig = inspect.signature(func)
    params = {}
    
    for param_name, param in sig.parameters.items():
        if param_name == 'df':  # Skip the DataFrame parameter
            continue
            
        param_info = {
            'name': param_name,
            'type': param.annotation if param.annotation != inspect.Parameter.empty else str,
            'default': param.default if param.default != inspect.Parameter.empty else None,
            'required': param.default == inspect.Parameter.empty
        }
        params[param_name] = param_info
    
    return params

def extract_docstring_summary(func) -> str:
    """Extracts the first line of the docstring as help text"""
    if func.__doc__:
        return func.__doc__.split('\n')[0].strip().rstrip('.')
    return f"Apply {func.__name__} operation"

# Automatic operation mapping with full introspection
CLEANING_OPERATIONS = {}
for method_name in Broom_methods:
    # Obtener función correspondiente en cleaning_ops
    func = getattr(cleaning_ops, method_name)
    
    CLEANING_OPERATIONS[method_name] = {
        'method': method_name,
        'function': func,
        'params': extract_function_params(func),
        'help': extract_docstring_summary(func),
        'cli_flag': method_name.replace('_', '-')  # remove_empty_cols -> remove-empty-cols
    }

# CLI configurations
SUPPORTED_LANGUAGES = ['py', 'python', 'r']
SUPPORTED_INPUT_FORMATS = ['.csv', '.xlsx', '.xls', '.json']
SUPPORTED_OUTPUT_FORMATS = ['.csv', '.xlsx', '.json']

# Mapping extensions to types
FILE_TYPE_MAPPING = {
    '.csv': 'csv',
    '.xlsx': 'excel', 
    '.xls': 'excel',
    '.json': 'json'
}

# Rich console configuration
CONSOLE_CONFIG = {
    'force_terminal': True,
    'width': 120
}

# CLI messages
MESSAGES = {
    'file_not_found': "Input file not found: {path}",
    'invalid_format': "Unsupported file format: {ext}. Supported: {formats}",
    'no_operations': "No cleaning operations specified. Use --help to see available options.",
    'success': "Processing completed successfully!",
    'saved_data': "Clean data saved to: {path}",
    'saved_code': "Generated code saved to: {path}",
    'processing': "Processing {operation}...",
    'summary_title': "Processing Summary"
}
from typing import Callable, List, Tuple, Any
from functools import wraps


def dynamic_docstring(replacements: List[Tuple[str, Callable[[], str]]]):
    """
    Decorator to dynamically replace placeholders in docstrings.
    
    Args:
        replacements: List of [placeholder, function] pairs
                     where placeholder is replaced with function's return value
    
    Example:
        @dynamic_docstring([("{DATASETS}", list_datasets)])
        def my_tool():
            '''Tool with {DATASETS} placeholder'''
            pass
    """
    def decorator(func):
        # Get original docstring
        original_doc = func.__doc__ or ""
        
        # Apply all replacements
        updated_doc = original_doc
        for placeholder, replacement_func in replacements:
            try:
                replacement_value = replacement_func()
                updated_doc = updated_doc.replace(placeholder, replacement_value)
            except Exception as e:
                print(f"Warning: Failed to replace {placeholder} in {func.__name__}: {e}")
                # Keep placeholder if replacement fails
        
        # Update the docstring
        func.__doc__ = updated_doc
        
        return func
    
    return decorator

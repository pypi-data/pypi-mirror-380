"""
SelectiveJSONParser - A memory-efficient JSON parser that extracts only the data you need.
"""

__version__ = "0.0.1"

from .parser.parser import Parser
from .pattern.pattern import Pattern

def parse(json_text: str, pattern: str = None):
    """
    Convenience function to parse JSON with optional pattern.
    
    Args:
        json_text (str): The JSON string to parse
        pattern (str, optional): Pattern to selectively extract data
    
    Returns:
        dict or list: Parsed JSON data
    """
    parser = Parser(json_text, pattern)
    return parser.parse()

__all__ = ["Parser", "Pattern", "parse", "__version__"]
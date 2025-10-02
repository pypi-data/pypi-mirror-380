"""JSON utilities for handling special types like Decimal"""

from decimal import Decimal
from datetime import datetime, date
from typing import Any


def convert_decimal_to_float(obj: Any) -> Any:
    """Convert Decimal objects to float for JSON serialization.
    
    Recursively handles dicts, lists, and nested structures.
    
    Args:
        obj: Object to convert
        
    Returns:
        Converted object with Decimals as floats
    """
    if isinstance(obj, Decimal):
        return float(obj)
    elif isinstance(obj, dict):
        return {key: convert_decimal_to_float(value) for key, value in obj.items()}
    elif isinstance(obj, list):
        return [convert_decimal_to_float(item) for item in obj]
    elif isinstance(obj, tuple):
        return tuple(convert_decimal_to_float(item) for item in obj)
    elif isinstance(obj, datetime):
        return obj.isoformat()
    elif isinstance(obj, date):
        return obj.isoformat()
    else:
        return obj


def sanitize_for_json(data: dict) -> dict:
    """Sanitize a dictionary for JSON serialization.
    
    Converts Decimal, datetime, and other non-JSON types.
    
    Args:
        data: Dictionary to sanitize
        
    Returns:
        Sanitized dictionary
    """
    return convert_decimal_to_float(data)


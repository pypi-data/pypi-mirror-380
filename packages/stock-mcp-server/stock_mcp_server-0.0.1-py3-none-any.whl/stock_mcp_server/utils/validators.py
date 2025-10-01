"""Input validation functions."""

import re
from datetime import datetime
from typing import Any


class ValidationError(Exception):
    """Custom validation error."""

    pass


def validate_date(date_str: str, allow_future: bool = False) -> str:
    """Validate date string."""
    if date_str.lower() in ("today", "latest"):
        return datetime.now().strftime("%Y-%m-%d")

    try:
        date = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise ValidationError(f"Invalid date format: {date_str}")

    if not allow_future and date > datetime.now():
        raise ValidationError(f"Future date not allowed: {date_str}")

    return date_str


def validate_stock_code(code: str) -> str:
    """Validate stock code."""
    if not code:
        raise ValidationError("Stock code cannot be empty")

    code = code.strip().upper()
    if not re.match(r"^\d{6}$", code):
        raise ValidationError(f"Invalid stock code: {code}")

    return code


def validate_indicator_params(indicator: str, params: dict[str, Any]) -> dict[str, Any]:
    """Validate indicator parameters."""
    return params  # Simplified for now


def validate_limit(limit: int | None, default: int = 10, max_limit: int = 100) -> int:
    """Validate limit parameter."""
    if limit is None:
        return default

    try:
        limit = int(limit)
    except (ValueError, TypeError):
        raise ValidationError(f"Limit must be an integer, got {limit}")

    if limit < 1:
        raise ValidationError(f"Limit must be at least 1, got {limit}")

    if limit > max_limit:
        raise ValidationError(f"Limit cannot exceed {max_limit}, got {limit}")

    return limit

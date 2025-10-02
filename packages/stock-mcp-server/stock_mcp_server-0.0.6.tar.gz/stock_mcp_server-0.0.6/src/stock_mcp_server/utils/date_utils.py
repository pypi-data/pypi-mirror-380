"""Date and trading day utility functions."""

from datetime import datetime, timedelta
from typing import Any

import pandas as pd


def parse_date(date_str: str | None) -> str:
    """
    Parse date string to YYYY-MM-DD format.
    
    Args:
        date_str: Date string (YYYY-MM-DD, today, latest) or None for today
        
    Returns:
        Date string in YYYY-MM-DD format
    """
    if not date_str or date_str.lower() in ("today", "latest"):
        return datetime.now().strftime("%Y-%m-%d")
    
    # Try to parse various date formats
    try:
        dt = pd.to_datetime(date_str)
        return dt.strftime("%Y-%m-%d")
    except Exception:
        # If parsing fails, return as-is and let validation catch it
        return date_str


def is_trading_day(date: str | datetime | None = None) -> bool:
    """
    Check if a given date is a trading day (Monday-Friday, excluding holidays).
    
    Note: This is a simplified check. For production, integrate with
    a holiday calendar API or maintain a holiday list.
    
    Args:
        date: Date to check (defaults to today)
        
    Returns:
        True if trading day, False otherwise
    """
    if date is None:
        date = datetime.now()
    elif isinstance(date, str):
        date = datetime.strptime(date, "%Y-%m-%d")
    
    # Check if weekday (Monday=0, Sunday=6)
    if date.weekday() >= 5:  # Saturday or Sunday
        return False
    
    # TODO: Check against Chinese stock market holiday calendar
    # For now, just return True for weekdays
    return True


def is_trading_time() -> bool:
    """
    Check if current time is within trading hours.
    
    Shanghai Stock Exchange trading hours (China Standard Time):
    - Morning session: 09:30 - 11:30
    - Afternoon session: 13:00 - 15:00
    
    Returns:
        True if currently in trading hours, False otherwise
    """
    now = datetime.now()
    
    # Check if trading day
    if not is_trading_day(now):
        return False
    
    current_time = now.time()
    
    # Morning session: 09:30 - 11:30
    morning_start = datetime.strptime("09:30", "%H:%M").time()
    morning_end = datetime.strptime("11:30", "%H:%M").time()
    
    # Afternoon session: 13:00 - 15:00
    afternoon_start = datetime.strptime("13:00", "%H:%M").time()
    afternoon_end = datetime.strptime("15:00", "%H:%M").time()
    
    return (morning_start <= current_time <= morning_end) or (
        afternoon_start <= current_time <= afternoon_end
    )


def get_latest_trading_date(reference_date: str | datetime | None = None) -> str:
    """
    Get the most recent trading date on or before the reference date.
    
    Args:
        reference_date: Reference date (defaults to today)
        
    Returns:
        Latest trading date in YYYY-MM-DD format
    """
    if reference_date is None:
        date = datetime.now()
    elif isinstance(reference_date, str):
        date = datetime.strptime(reference_date, "%Y-%m-%d")
    else:
        date = reference_date
    
    # Walk backwards until we find a trading day
    for _ in range(10):  # Max 10 days back (covers weekends + holidays)
        if is_trading_day(date):
            return date.strftime("%Y-%m-%d")
        date = date - timedelta(days=1)
    
    # Fallback: return the reference date
    if isinstance(reference_date, str):
        return reference_date
    return datetime.now().strftime("%Y-%m-%d")


def get_trading_dates_range(
    start_date: str, end_date: str, max_count: int | None = None
) -> list[str]:
    """
    Get list of trading dates between start and end dates.
    
    Args:
        start_date: Start date (YYYY-MM-DD)
        end_date: End date (YYYY-MM-DD)
        max_count: Maximum number of dates to return
        
    Returns:
        List of trading dates in YYYY-MM-DD format
    """
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    
    if start > end:
        raise ValueError(f"Start date {start_date} must be before end date {end_date}")
    
    trading_dates = []
    current = start
    
    while current <= end:
        if is_trading_day(current):
            trading_dates.append(current.strftime("%Y-%m-%d"))
            if max_count and len(trading_dates) >= max_count:
                break
        current += timedelta(days=1)
    
    return trading_dates


def get_previous_trading_date(date: str | datetime, days_back: int = 1) -> str:
    """
    Get the trading date N trading days before the given date.
    
    Args:
        date: Reference date
        days_back: Number of trading days to go back
        
    Returns:
        Previous trading date in YYYY-MM-DD format
    """
    if isinstance(date, str):
        current = datetime.strptime(date, "%Y-%m-%d")
    else:
        current = date
    
    count = 0
    current = current - timedelta(days=1)  # Start from day before
    
    while count < days_back:
        if is_trading_day(current):
            count += 1
            if count == days_back:
                return current.strftime("%Y-%m-%d")
        current = current - timedelta(days=1)
    
    return current.strftime("%Y-%m-%d")


def format_timestamp(dt: datetime | None = None) -> str:
    """
    Format datetime to standard timestamp string.
    
    Args:
        dt: Datetime to format (defaults to now)
        
    Returns:
        Formatted timestamp string (YYYY-MM-DD HH:MM:SS)
    """
    if dt is None:
        dt = datetime.now()
    return dt.strftime("%Y-%m-%d %H:%M:%S")


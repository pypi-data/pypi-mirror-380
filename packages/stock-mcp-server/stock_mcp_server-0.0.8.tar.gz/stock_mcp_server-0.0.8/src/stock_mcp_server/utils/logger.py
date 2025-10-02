"""Logging configuration using loguru."""

import sys
from pathlib import Path
from typing import Any

from loguru import logger

from stock_mcp_server.config import get_config

# Remove default handler
logger.remove()


def setup_logging() -> None:
    """Configure logging with file and console outputs."""
    config = get_config()
    log_level = config.log_level
    log_dir = config.log_dir

    # Ensure log directory exists
    log_dir.mkdir(parents=True, exist_ok=True)

    # Console handler - only for ERROR and above to avoid interfering with MCP stdio
    # MCP servers use stdin/stdout for JSON-RPC, so we minimize stderr output
    logger.add(
        sys.stderr,
        level="ERROR",  # Only log errors to stderr to avoid MCP communication issues
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
        colorize=True,
    )

    # File handler - detailed logging
    logger.add(
        log_dir / "stock_mcp_server.log",
        level="DEBUG",
        format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
        rotation="10 MB",
        retention="7 days",
        compression="zip",
        enqueue=True,  # Thread-safe
    )

    # Error file handler - errors only
    logger.add(
        log_dir / "errors.log",
        level="ERROR",
        format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}\n{extra}",
        rotation="5 MB",
        retention="30 days",
        compression="zip",
        backtrace=True,
        diagnose=True,
        enqueue=True,
    )

    logger.info(f"Logging configured: level={log_level}, dir={log_dir}")


def get_logger(name: str) -> Any:
    """Get a logger instance with the given name."""
    return logger.bind(name=name)


# Initialize logging on module import
setup_logging()


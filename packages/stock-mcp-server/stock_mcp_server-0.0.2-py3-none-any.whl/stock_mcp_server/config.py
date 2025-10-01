"""Configuration management for Stock MCP Server."""

import os
from pathlib import Path
from typing import Any

import yaml
from pydantic import BaseModel, Field


class RefreshIntervals(BaseModel):
    """Data refresh intervals in seconds."""

    realtime: int = Field(default=300, description="Real-time data refresh interval (5 min)")
    news: int = Field(default=1800, description="News refresh interval (30 min)")
    historical: int = Field(default=86400, description="Historical data refresh (24 hours)")
    indicators: int = Field(default=1800, description="Indicators refresh (30 min)")
    sentiment: int = Field(default=3600, description="Sentiment refresh (1 hour)")


class SentimentWeights(BaseModel):
    """Weights for sentiment calculation components."""

    volume: float = Field(default=0.25, ge=0, le=1)
    price: float = Field(default=0.35, ge=0, le=1)
    volatility: float = Field(default=0.15, ge=0, le=1)
    capital: float = Field(default=0.15, ge=0, le=1)
    news: float = Field(default=0.10, ge=0, le=1)

    def validate_sum(self) -> None:
        """Ensure weights sum to 1.0."""
        total = self.volume + self.price + self.volatility + self.capital + self.news
        if abs(total - 1.0) > 0.01:
            raise ValueError(f"Sentiment weights must sum to 1.0, got {total}")


class CacheConfig(BaseModel):
    """Cache configuration."""

    max_size_mb: int = Field(default=500, description="Maximum cache size in MB")
    cleanup_interval: int = Field(default=86400, description="Cleanup interval in seconds")
    in_memory_max_items: int = Field(default=1000, description="Max items in memory cache")


class NewsSourceConfig(BaseModel):
    """News source configuration."""

    enabled: bool = Field(default=True)
    rate_limit_seconds: float = Field(default=2.0, description="Rate limit between requests")
    timeout_seconds: int = Field(default=10)


class Config(BaseModel):
    """Main configuration for Stock MCP Server."""

    # Server settings
    server_name: str = Field(default="stock-mcp-server")
    log_level: str = Field(default="INFO")
    
    # Data refresh intervals
    refresh_intervals: RefreshIntervals = Field(default_factory=RefreshIntervals)
    
    # News sources
    news_sources: dict[str, NewsSourceConfig] = Field(
        default_factory=lambda: {
            "dongfang_fortune": NewsSourceConfig(enabled=True),
            "sina_finance": NewsSourceConfig(enabled=True),
            "securities_times": NewsSourceConfig(enabled=False),
        }
    )
    
    # Sentiment weights
    sentiment_weights: SentimentWeights = Field(default_factory=SentimentWeights)
    
    # Cache configuration
    cache: CacheConfig = Field(default_factory=CacheConfig)
    
    # Data paths
    data_dir: Path = Field(
        default_factory=lambda: Path.home() / ".stock-mcp-server" / "data"
    )
    cache_db_path: Path = Field(
        default_factory=lambda: Path.home() / ".stock-mcp-server" / "cache.db"
    )
    log_dir: Path = Field(
        default_factory=lambda: Path.home() / ".stock-mcp-server" / "logs"
    )

    def model_post_init(self, __context: Any) -> None:
        """Post-initialization validation and setup."""
        # Validate sentiment weights
        self.sentiment_weights.validate_sum()
        
        # Ensure directories exist
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.cache_db_path.parent.mkdir(parents=True, exist_ok=True)
        self.log_dir.mkdir(parents=True, exist_ok=True)

    @classmethod
    def from_file(cls, config_path: str | Path) -> "Config":
        """Load configuration from YAML file."""
        path = Path(config_path)
        if not path.exists():
            raise FileNotFoundError(f"Config file not found: {config_path}")
        
        with open(path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        
        return cls(**data)

    @classmethod
    def from_env(cls) -> "Config":
        """Load configuration from environment variables."""
        config = cls()
        
        # Override with environment variables
        if log_level := os.getenv("STOCK_MCP_LOG_LEVEL"):
            config.log_level = log_level
        
        if cache_size := os.getenv("STOCK_MCP_CACHE_SIZE_MB"):
            config.cache.max_size_mb = int(cache_size)
        
        if data_dir := os.getenv("STOCK_MCP_DATA_DIR"):
            config.data_dir = Path(data_dir)
        
        return config

    @classmethod
    def load(cls) -> "Config":
        """Load configuration with precedence: file > env > defaults."""
        # Check for config file in multiple locations
        config_paths = [
            Path("config.yaml"),
            Path.home() / ".stock-mcp-server" / "config.yaml",
            Path("/etc/stock-mcp-server/config.yaml"),
        ]
        
        for path in config_paths:
            if path.exists():
                config = cls.from_file(path)
                # Apply environment variable overrides
                if log_level := os.getenv("STOCK_MCP_LOG_LEVEL"):
                    config.log_level = log_level
                return config
        
        # No config file found, use environment + defaults
        return cls.from_env()


# Global configuration instance
_config: Config | None = None


def get_config() -> Config:
    """Get the global configuration instance."""
    global _config
    if _config is None:
        _config = Config.load()
    return _config


def reload_config() -> Config:
    """Reload configuration from file/env."""
    global _config
    _config = Config.load()
    return _config


"""Configuration settings for AWS Content MCP Server"""

import os
from typing import Dict, Any
from dataclasses import dataclass


@dataclass
class ServerConfig:
    """Configuration for the MCP server"""
    
    # HTTP Client Settings
    timeout: float = float(os.getenv("AWS_CONTENT_TIMEOUT", "30.0"))
    max_retries: int = int(os.getenv("AWS_CONTENT_MAX_RETRIES", "3"))
    retry_delay: float = float(os.getenv("AWS_CONTENT_RETRY_DELAY", "1.0"))
    
    # Content Settings
    max_results: int = int(os.getenv("AWS_CONTENT_MAX_RESULTS", "20"))
    cache_ttl: int = int(os.getenv("AWS_CONTENT_CACHE_TTL", "3600"))  # 1 hour
    max_content_length: int = int(os.getenv("AWS_CONTENT_MAX_LENGTH", "1000000"))  # 1MB
    
    # Search Settings
    search_depth: int = int(os.getenv("AWS_CONTENT_SEARCH_DEPTH", "3"))
    similarity_threshold: float = float(os.getenv("AWS_CONTENT_SIMILARITY_THRESHOLD", "0.3"))
    
    # Rate Limiting
    requests_per_minute: int = int(os.getenv("AWS_CONTENT_REQUESTS_PER_MINUTE", "60"))
    
    # Logging
    log_level: str = os.getenv("AWS_CONTENT_LOG_LEVEL", "INFO")
    
    # AWS Website Settings
    base_url: str = "https://aws.amazon.com"
    user_agent: str = "Mozilla/5.0 (compatible; AWS-Content-MCP/1.0)"
    
    # Content Processing
    extract_images: bool = os.getenv("AWS_CONTENT_EXTRACT_IMAGES", "false").lower() == "true"
    extract_code_blocks: bool = os.getenv("AWS_CONTENT_EXTRACT_CODE", "true").lower() == "true"
    preserve_formatting: bool = os.getenv("AWS_CONTENT_PRESERVE_FORMAT", "true").lower() == "true"


# Global configuration instance
config = ServerConfig()


def get_headers() -> Dict[str, str]:
    """Get HTTP headers for requests"""
    return {
        "User-Agent": config.user_agent,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
        "Cache-Control": "no-cache",
        "Pragma": "no-cache",
    }


def get_search_patterns() -> Dict[str, Dict[str, Any]]:
    """Get search patterns for different content types"""
    return {
        "blogs": {
            "base_urls": [
                "/blogs/",
                "/blog/",
            ],
            "selectors": {
                "articles": ["article", "div.blog-post", "div.post", ".blog-item"],
                "titles": ["h1", "h2", "h3", ".title", ".heading", ".post-title"],
                "links": ["a[href*='/blog']", "a[href*='/blogs']"],
                "excerpts": [".excerpt", ".summary", ".description", "p"],
                "dates": [".date", ".published", "time", ".post-date"],
            }
        },
        "products": {
            "base_urls": [
                "/products/",
                "/services/",
            ],
            "selectors": {
                "articles": [".product", ".service", ".product-card", ".service-card"],
                "titles": ["h1", "h2", "h3", ".product-title", ".service-title"],
                "links": ["a[href*='/products']", "a[href*='/services']"],
                "excerpts": [".description", ".summary", "p"],
            }
        },
        "solutions": {
            "base_urls": [
                "/solutions/",
                "/architecture/",
            ],
            "selectors": {
                "articles": [".solution", ".architecture", ".solution-card"],
                "titles": ["h1", "h2", "h3", ".solution-title"],
                "links": ["a[href*='/solutions']", "a[href*='/architecture']"],
                "excerpts": [".description", ".summary", "p"],
            }
        },
        "pricing": {
            "base_urls": [
                "/pricing/",
            ],
            "selectors": {
                "articles": [".pricing", ".price", ".pricing-card"],
                "titles": ["h1", "h2", "h3", ".pricing-title"],
                "links": ["a[href*='/pricing']"],
                "excerpts": [".description", ".summary", "p"],
            }
        }
    }


def get_content_filters() -> Dict[str, Any]:
    """Get content filtering rules"""
    return {
        "remove_elements": [
            "script", "style", "nav", "footer", "header", 
            ".navigation", ".sidebar", ".ads", ".advertisement",
            ".cookie-banner", ".popup", ".modal"
        ],
        "keep_elements": [
            "main", "article", ".content", ".main-content",
            "h1", "h2", "h3", "h4", "h5", "h6", "p", "ul", "ol", "li",
            "blockquote", "pre", "code", "table", "tr", "td", "th"
        ],
        "min_text_length": 50,
        "max_text_length": config.max_content_length,
    }
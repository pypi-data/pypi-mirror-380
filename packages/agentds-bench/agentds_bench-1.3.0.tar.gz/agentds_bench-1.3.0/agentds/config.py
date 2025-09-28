"""
Configuration settings for AgentDS Python client.
"""

import os
from typing import Optional

def get_api_base_url() -> str:
    """
    Get the API base URL from environment variables or use default.
    
    Returns:
        str: The API base URL
    """
    return os.getenv("AGENTDS_API_URL", "https://agentds.org/api")

def get_token_file_path() -> str:
    """
    Get the path to the token file.
    
    Returns:
        str: Path to the token file in user's home directory
    """
    return os.path.expanduser("~/.agentds_token")

# Public API
API_BASE_URL = get_api_base_url()
TOKEN_FILE = get_token_file_path()

# Request configuration (env-overridable)
def _int_env(name: str, default: int) -> int:
    try:
        return int(os.getenv(name, str(default)))
    except ValueError:
        return default

def _float_env(name: str, default: float) -> float:
    try:
        return float(os.getenv(name, str(default)))
    except ValueError:
        return default

DEFAULT_TIMEOUT = _int_env("AGENTDS_TIMEOUT_S", 30)
MAX_RETRIES = _int_env("AGENTDS_RETRIES", 3)
RETRY_DELAY = _float_env("AGENTDS_RETRY_DELAY_S", 1.0)
MAX_SUBMISSION_MB = _int_env("AGENTDS_MAX_SUBMISSION_MB", 10)

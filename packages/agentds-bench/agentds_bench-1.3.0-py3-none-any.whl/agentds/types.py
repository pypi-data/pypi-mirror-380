"""
Structured types for AgentDS Python client.
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class ValidationErrorDetail:
    message: str
    field: Optional[str] = None


@dataclass
class SubmissionResult:
    success: bool
    score: float
    metric_name: str
    validation_passed: bool
    details: Dict[str, Any] = field(default_factory=dict)


@dataclass
class DomainInfo:
    name: str
    is_active: Optional[bool] = None
    total_num_tasks: Optional[int] = None


@dataclass
class Status:
    status: str
    team_name: Optional[str] = None
    domains: List[Dict[str, Any]] = field(default_factory=list)
    formatted_table: Optional[str] = None


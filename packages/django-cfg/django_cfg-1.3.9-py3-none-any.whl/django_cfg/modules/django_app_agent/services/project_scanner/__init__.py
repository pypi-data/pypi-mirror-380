"""
Project Scanner Module for Django App Agent.

This module provides comprehensive project analysis capabilities
for Django and django-cfg projects, including app discovery,
dependency analysis, and architectural pattern detection.

Components:
- models: Data models for requests and results
- app_discovery: Django application discovery and analysis
- pattern_detection: Architectural pattern detection
- main: Main orchestration service
"""

from .main import ProjectScannerService
from .models import ProjectScanRequest, ScanResult
from .app_discovery import AppDiscoveryEngine
from .pattern_detection import PatternDetectionEngine

__all__ = [
    # Main service
    "ProjectScannerService",
    
    # Data models
    "ProjectScanRequest",
    "ScanResult",
    
    # Core engines
    "AppDiscoveryEngine",
    "PatternDetectionEngine",
]

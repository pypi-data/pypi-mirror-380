"""
SyftBox NSAI SDK

A Python SDK for discovering and using AI services across the SyftBox network.
"""
# Import settings early to initialize environment
import logging

# Main client class
from .main import Client

# Core types and enums
from .core.types import (
    ServiceType,
    ServiceStatus, 
    HealthStatus,
    PricingChargeType,
    ServiceItem,
    ChatMessage,
    TransactionToken,
)

# Exceptions
from .core.settings import settings, Settings
from .core.exceptions import (
    SyftBoxSDKError,
    SyftBoxNotFoundError,
    SyftBoxNotRunningError,
    ConfigurationError,
    ServiceNotFoundError,
    ServiceNotSupportedError,
    ServiceUnavailableError,
    NetworkError,
    RPCError,
    PollingTimeoutError,
    PollingError,
    AuthenticationError,
    PaymentError,
    ValidationError,
    HealthCheckError,
)

# Configuration utilities
from .core.config import (
    SyftBoxConfig,
    get_config,
    is_syftbox_installed,
    is_syftbox_running,
    get_startup_instructions,
    get_installation_instructions,
)

# Service clients (for advanced usage)
from .services.chat import ChatService
from .services.search import SearchService
from .services.health import HealthMonitor

# Client components (for advanced usage)
from .clients import SyftBoxAuthClient

# Filtering utilities
from .discovery.filters import (
    ServiceFilter,
    FilterCriteria,
    FilterBuilder,
    create_chat_services_filter,
    create_search_services_filter,
    create_free_services_filter,
    create_paid_services_filter,
    create_healthy_services_filter,
    create_datasite_services_filter,
    create_tag_services_filter,
)

# model utilities
from .models.service_info import ServiceInfo
from .models.requests import ChatRequest, SearchRequest
from .models.responses import ChatResponse, SearchResponse, DocumentResult

# Convenience functions
# from .main import (
#     list_available_services,
# )

# Formatting utilities
from .utils.formatting import (
    format_services_table,
    format_service_details,
    format_search_results,
    format_chat_conversation,
    format_health_summary,
    format_statistics,
)

# Theme utilities (for dark mode support)
from .utils.theme import (
    set_theme,
    get_current_theme,
    detect_theme,
)

# Use settings for package metadata
__version__ = settings.project_version or "0.1.0"
__author__ = settings.project_author or "SyftBox Team"
__email__ = settings.project_email or "info@openmined.org"
__description__ = settings.project_description or "A Python SDK for discovering and using AI services across the SyftBox network."

# Package-level convenience functions
def create_client(**kwargs) -> Client:
    """Create a Client with optional configuration.
    
    Args:
        **kwargs: Configuration options for the client
        
    Returns:
        Client instance
    """
    return Client(**kwargs)


def check_installation() -> bool:
    """Check if SyftBox is properly installed and configured.
    
    Returns:
        True if SyftBox is available, False otherwise
    """
    return is_syftbox_installed()


def get_setup_instructions() -> str:
    """Get instructions for setting up SyftBox.
    
    Returns:
        Setup instructions as string
    """
    return get_installation_instructions()

def check_running() -> bool:
    """Check if SyftBox is properly running.

    Returns:
        True if SyftBox is running, False otherwise
    """
    return is_syftbox_running()


def get_startup_instructions() -> str:
    """Get instructions for starting up SyftBox.

    Returns:
        Startup instructions as string
    """
    return get_startup_instructions()

# Package info for introspection
def get_package_info():
    """Get package information including settings."""
    return {
        "name": settings.app_name,
        "version": __version__,
        "author": __author__,
        "description": __description__,
        "environment": settings.environment,
        "debug": settings.debug,
        "config_path": str(settings.syftbox_config_path)
    }

# Runtime diagnostics
def get_runtime_diagnostics():
    """Get runtime diagnostics for troubleshooting."""
    return settings.get_runtime_info()

# Feature flags accessible at package level
def is_feature_enabled(feature_name: str) -> bool:
    """Check if a feature is enabled via settings."""
    feature_flags = settings.get_feature_flags()
    return feature_flags.get(feature_name, False)

# Environment helpers
def is_development() -> bool:
    """Check if running in development mode."""
    return settings.is_development

def is_production() -> bool:
    """Check if running in production mode."""  
    return settings.is_production

# Package metadata
__all__ = [
    # Version info
    "__version__",
    "__author__", 
    "__email__",
    
    # Main client
    "Client",
    "create_client",

    # Setting utilities
    'Settings',
    'settings',
    'get_package_info',
    'get_runtime_diagnostics',
    'is_feature_enabled',
    'is_development',
    'is_production'
    
    # Core types
    "ServiceType",
    "ServiceStatus",
    "HealthStatus", 
    "PricingChargeType",
    "ServiceItem",
    "ChatMessage",
    "ChatRequest",
    "ChatResponse",
    "SearchRequest",
    "SearchResponse", 
    "DocumentResult",
    "TransactionToken",

    # Model utilities
    "ServiceInfo",

    # Exceptions
    "SyftBoxSDKError",
    "SyftBoxNotFoundError",
    "SyftBoxNotRunningError",
    "ConfigurationError",
    "ServiceNotFoundError",
    "ServiceNotSupportedError",
    "ServiceUnavailableError",
    "NetworkError",
    "RPCError",
    "PollingTimeoutError",
    "PollingError",
    "AuthenticationError",
    "PaymentError",
    "ValidationError",
    "HealthCheckError",
    
    # Configuration
    "SyftBoxConfig",
    "get_config",
    "is_syftbox_installed",
    "is_syftbox_running",
    "get_startup_instructions",
    "get_installation_instructions",
    "check_installation",
    "get_setup_instructions",
    
    # Services
    "ChatService",
    "SearchService",
    "BatchSearchService", 
    "HealthMonitor",
    
    # Client components
    "SyftBoxAuthClient",
    
    # Filtering
    "ServiceFilter",
    "FilterCriteria",
    "FilterBuilder",
    "create_chat_services_filter",
    "create_search_services_filter",
    "create_free_services_filter",
    "create_paid_services_filter",
    "create_healthy_services_filter",
    "create_datasite_services_filter",
    "create_tag_services_filter",
    
    # Formatting
    "format_services_table",
    "format_service_details",
    "format_search_results",
    "format_chat_conversation",
    "format_health_summary",
    "format_statistics",
    
    # Theme utilities
    "set_theme",
    "get_current_theme", 
    "detect_theme",
]

# Log package initialization in debug mode
if settings.debug:
    logger = logging.getLogger(__name__.split('.')[0])
    logger.debug(f"Initialized {settings.app_name} v{__version__} in {settings.environment} mode")
    logger.debug(f"Config path: {settings.syftbox_config_path}")
    
    # Log any missing required paths
    missing_paths = settings.validate_required_paths()
    if missing_paths:
        logger.warning(f"Missing required paths: {', '.join(missing_paths)}")
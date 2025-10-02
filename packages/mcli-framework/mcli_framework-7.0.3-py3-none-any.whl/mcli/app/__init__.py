# src/mcli/app/__init__.py
import importlib
from pathlib import Path

from mcli.lib.logger.logger import get_logger

logger = get_logger(__name__)

logger.info("Initializing mcli.app package")

# Import main function
try:
    from .main import main

    logger.info("Successfully imported main from .main")
except ImportError as e:
    logger.error(f"Failed to import main: {e}")
    import traceback

    logger.error(f"Traceback: {traceback.format_exc()}")
    raise

# Try importing readiness submodule
try:
    from .readiness import readiness

    logger.info(f"Successfully imported readiness module directly: {readiness}")
    # Make it available at the app level
    __all__ = ["main", "readiness"]
except ImportError as e:
    logger.info(f"Could not import readiness directly: {e}")
    __all__ = ["main"]

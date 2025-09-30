import logging
from pathlib import Path
from .javascript_detector import JavaScriptDetector
from .java_detector import JavaDetector
from .python_detector import PythonDetector
from .rust_detector import RustDetector

logger = logging.getLogger(__name__)

DETECTORS = {
    "javascript": JavaScriptDetector(),
    "python": PythonDetector(),
    "java": JavaDetector(),
    "rust": RustDetector(),
}


def get_supported_languages():
    """Returns a list of supported language names."""
    return list(DETECTORS.keys())


def detect_language(project_path: Path, verbose: bool = False) -> str | None:
    """Detects the primary language of a project by checking for characteristic files."""
    for lang_name, detector in DETECTORS.items():
        if detector.detect(project_path):
            if verbose:
                logger.info(f"Detected {lang_name} project")
            return lang_name
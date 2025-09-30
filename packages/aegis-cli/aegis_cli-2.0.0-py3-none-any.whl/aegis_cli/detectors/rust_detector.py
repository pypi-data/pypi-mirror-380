from .base_detector import LanguageDetector


class RustDetector(LanguageDetector):
    """Detects Rust projects by looking for Cargo.toml."""

    detection_files = [
        "Cargo.toml",
    ]
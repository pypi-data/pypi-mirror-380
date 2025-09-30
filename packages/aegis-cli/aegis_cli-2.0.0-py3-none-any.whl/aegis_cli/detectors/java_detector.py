from .base_detector import LanguageDetector


class JavaDetector(LanguageDetector):
    """Detects Java projects by looking for common build system files."""

    detection_files = [
        "pom.xml",  # Maven
        "build.gradle",  # Gradle
        "build.gradle.kts",  # Gradle Kotlin DSL
    ]
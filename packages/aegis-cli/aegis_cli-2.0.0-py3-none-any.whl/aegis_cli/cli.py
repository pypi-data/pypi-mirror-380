import click
import logging
from pathlib import Path
from .detectors import detect_language, get_supported_languages
from .generator import generate_files
from .hooks import install_pre_commit_hook
from .checker import check_security_files

# Configure logging
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
logger = logging.getLogger(__name__)


@click.group()
def cli():
    """Aegis CLI: Automate security starter files for your projects."""
    pass


@cli.command(name="generate")
@click.argument("project_path", type=click.Path(exists=True, file_okay=False, resolve_path=True), default=".")
@click.option("--output", "-o", type=click.Path(file_okay=False, resolve_path=True), help="Custom output directory for security markdown files.")
@click.option("--verbose", "-v", is_flag=True, help="Enable verbose output.")
@click.option("--dry-run", is_flag=True, help="Show what would be generated without writing files.")
def generate_command(project_path, output, verbose, dry_run):
    """Detects language and generates security files."""
    project_path = Path(project_path)
    output_dir = Path(output) if output else project_path

    if verbose:
        logger.setLevel(logging.DEBUG)
        click.echo(f"Scanning project: {project_path}")

    language = detect_language(project_path, verbose=verbose)

    if not language:
        raise click.ClickException("Could not detect a supported language (Python, JavaScript, Java, Rust).")

    if verbose:
        click.echo(f"Detected language: {language}")

    # The security/ folder is the standard for these files
    security_dir = output_dir / "security"

    generate_files(project_path, security_dir, language, dry_run)


@cli.command(name="check")
def check_command():
    """Checks for the presence of essential security files."""
    if not check_security_files():
        # Exit with a non-zero status code to indicate failure
        raise click.exceptions.Exit(1)


@cli.command(name="list-languages")
def list_languages_command():
    """Lists all languages supported by the detector."""
    click.echo("Aegis currently supports the following languages:")
    languages = get_supported_languages()
    for lang in sorted(languages):
        # Capitalize for display purposes
        click.echo(f"- {lang.capitalize()}")


@cli.command(name="install-hook")
def install_hook_command():
    """Installs a pre-commit Git hook to check for security files."""
    try:
        install_pre_commit_hook()
    except click.ClickException as e:
        # Re-raise Click exceptions to be handled by the CLI runner
        raise e
    except Exception as e:
        # Catch other potential errors and wrap them in a ClickException
        raise click.ClickException(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    cli()

from pathlib import Path
import click

FILES_TO_CHECK = [
    Path(".github/dependabot.yml"),
    Path("security/SECURITY.md"),
    Path("security/SecureCodingGuide.md"),
]


def check_security_files() -> bool:
    """
    Checks for the presence of essential security files and reports status.

    Returns:
        bool: True if all files are found, False otherwise.
    """
    missing_files = []
    click.secho("🔎 Checking for essential security files...", fg="yellow")

    for file_path in FILES_TO_CHECK:
        if not file_path.is_file():
            missing_files.append(str(file_path))
            click.secho(f"  ❌ Missing: {file_path}", fg="red")
        else:
            click.secho(f"  ✅ Found:   {file_path}", fg="green")

    if missing_files:
        click.secho(
            "\nSome security files are missing. Run 'aegis generate' to create them.",
            fg="yellow",
        )
        return False

    click.secho("\n✅ All essential security files are present.", fg="green", bold=True)
    return True
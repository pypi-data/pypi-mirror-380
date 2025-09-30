import pytest
from click.testing import CliRunner
from pathlib import Path
from aegis_cli.cli import cli, generate_command


@pytest.fixture
def runner():
    return CliRunner()


def test_cli_help(runner):
    """Test that the main CLI entrypoint shows help."""
    result = runner.invoke(cli, ["--help"])
    assert result.exit_code == 0
    assert "Automate security starter files" in result.output


def test_generate_command_help(runner):
    """Test that the generate command shows help."""
    result = runner.invoke(generate_command, ["--help"])
    assert result.exit_code == 0
    assert "Detects language and generates security files" in result.output


def test_generate_no_args_detects_current_dir(runner):
    """Test that `generate` with no arguments uses the current directory."""
    with runner.isolated_filesystem() as td:
        (Path(td) / "requirements.txt").touch()  # Create a Python project marker
        result = runner.invoke(cli, ["generate"])
        assert result.exit_code == 0
        assert "Security files generated successfully" in result.output
        assert (Path(td) / "security/SECURITY.md").exists()


def test_generate_dry_run(runner, js_project):
    """Test that --dry-run previews changes without writing files."""
    result = runner.invoke(cli, ["generate", str(js_project), "--dry-run"])
    assert result.exit_code == 0
    assert "Dry run" in result.output
    assert "SECURITY.md" in result.output
    assert not (js_project / "security/SECURITY.md").exists()


def test_generate_verbose(runner, js_project):
    """Test that --verbose provides detailed output."""
    result = runner.invoke(cli, ["generate", str(js_project), "--verbose", "--dry-run"])
    assert result.exit_code == 0
    assert "Scanning project" in result.output
    assert "Detected language: javascript" in result.output


def test_generate_custom_output_dir(runner, js_project):
    """Test that --output places markdown files in a custom directory."""
    custom_dir = js_project / "custom-security"
    result = runner.invoke(
        cli, ["generate", str(js_project), "--output", str(custom_dir)]
    )
    assert result.exit_code == 0
    assert (custom_dir / "security/SECURITY.md").exists()
    # dependabot.yml should still be in the project root's .github folder
    assert (js_project / ".github/dependabot.yml").exists()


def test_generate_no_language_detected(runner, empty_project):
    """Test that the command fails gracefully when no language is detected."""
    result = runner.invoke(cli, ["generate", str(empty_project)])
    assert result.exit_code == 1
    assert "Could not detect a supported language" in result.output


@pytest.mark.parametrize(
    "language, project_fixture",
    [
        ("python", "python_project"),
        ("javascript", "js_project"),
        ("java", "java_project"),
        ("rust", "rust_project"),
    ],
)
def test_generate_creates_language_specific_guide(
    runner, language, project_fixture, request
):
    """Verify that the generated SecureCodingGuide is specific to the detected language."""
    project_dir = request.getfixturevalue(project_fixture)

    result = runner.invoke(cli, ["generate", str(project_dir)])
    assert result.exit_code == 0, f"CLI command failed: {result.output}"

    guide_path = project_dir / "security/SecureCodingGuide.md"
    assert guide_path.exists()

    content = guide_path.read_text()
    # The templates should all have a title like "# Secure Coding Guide: Python"
    assert f"Secure Coding Guide: {language.capitalize()}" in content


def test_list_languages_command(runner):
    """Test that `list-languages` command outputs the supported languages."""
    result = runner.invoke(cli, ["list-languages"])
    assert result.exit_code == 0
    assert "Aegis currently supports the following languages:" in result.output
    assert "- Java" in result.output
    assert "- Javascript" in result.output
    assert "- Python" in result.output
    assert "- Rust" in result.output
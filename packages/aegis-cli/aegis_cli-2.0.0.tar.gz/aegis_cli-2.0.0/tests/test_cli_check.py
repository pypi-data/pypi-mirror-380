import pytest
from click.testing import CliRunner
from pathlib import Path
from aegis_cli.cli import cli


@pytest.fixture
def runner():
    return CliRunner()


def test_check_command_files_missing(runner, temp_project_dir):
    """Test that 'check' fails when security files are missing."""
    with runner.isolated_filesystem(temp_dir=temp_project_dir) as td:
        result = runner.invoke(cli, ["check"])

        assert result.exit_code == 1
        assert "❌ Missing: security/SECURITY.md" in result.output
        assert "❌ Missing: .github/dependabot.yml" in result.output
        assert "Some security files are missing" in result.output


def test_check_command_files_present(runner, temp_project_dir):
    """Test that 'check' succeeds when all security files are present."""
    with runner.isolated_filesystem(temp_dir=temp_project_dir) as td:
        # Create the necessary files
        (Path(td) / ".github").mkdir()
        (Path(td) / ".github/dependabot.yml").touch()
        (Path(td) / "security").mkdir()
        (Path(td) / "security/SECURITY.md").touch()
        (Path(td) / "security/SecureCodingGuide.md").touch()

        result = runner.invoke(cli, ["check"])

        assert result.exit_code == 0
        assert "✅ Found:   security/SECURITY.md" in result.output
        assert "✅ Found:   .github/dependabot.yml" in result.output
        assert "✅ All essential security files are present." in result.output
        assert "Missing" not in result.output
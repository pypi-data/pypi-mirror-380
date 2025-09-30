import pytest
from click.testing import CliRunner
from pathlib import Path
from aegis_cli.cli import cli

def test_install_hook_no_git_repo(temp_project_dir):
    """Test that hook installation fails if not in a git repository."""
    runner = CliRunner()
    # Run in the temp_project_dir which is not a git repo
    with runner.isolated_filesystem(temp_dir=temp_project_dir) as td:
        result = runner.invoke(cli, ['install-hook'])
        assert result.exit_code == 1
        assert "Not a Git repository" in result.output

def test_install_hook_success(git_repo):
    """Test successful installation of the pre-commit hook."""
    runner = CliRunner()
    with runner.isolated_filesystem(temp_dir=git_repo) as td:
        result = runner.invoke(cli, ['install-hook'])

        assert result.exit_code == 0
        assert "Aegis pre-commit hook installed successfully" in result.output

        hook_path = Path(td) / ".git/hooks/pre-commit"
        assert hook_path.exists()

        content = hook_path.read_text()
        assert "# Aegis CLI pre-commit hook" in content
        assert 'if [ ! -f "$file" ]; then' in content

        # Check for executable permissions
        assert hook_path.stat().st_mode & 0o111 != 0

def test_install_hook_already_installed(git_repo):
    """Test that the command recognizes an existing Aegis hook."""
    runner = CliRunner()
    with runner.isolated_filesystem(temp_dir=git_repo) as td:
        # Run once to install
        runner.invoke(cli, ['install-hook'], catch_exceptions=False)

        # Run a second time
        result = runner.invoke(cli, ['install-hook'])

        assert result.exit_code == 0
        assert "Aegis pre-commit hook is already installed" in result.output

def test_install_hook_overwrite_existing_confirm(git_repo):
    """Test overwriting a different, existing pre-commit hook (confirming 'y')."""
    runner = CliRunner()
    with runner.isolated_filesystem(temp_dir=git_repo) as td:
        hook_path = Path(td) / ".git/hooks/pre-commit"
        hook_path.parent.mkdir(exist_ok=True)
        hook_path.write_text("#!/bin/sh\necho 'other hook'")

        result = runner.invoke(cli, ['install-hook'], input='y\n')

        assert result.exit_code == 0
        assert "Aegis pre-commit hook installed successfully" in result.output
        content = hook_path.read_text()
        assert "# Aegis CLI pre-commit hook" in content

def test_install_hook_overwrite_existing_deny(git_repo):
    """Test overwriting a different, existing pre-commit hook (denying 'n')."""
    runner = CliRunner()
    with runner.isolated_filesystem(temp_dir=git_repo) as td:
        hook_path = Path(td) / ".git/hooks/pre-commit"
        hook_path.parent.mkdir(exist_ok=True)
        original_content = "#!/bin/sh\necho 'other hook'"
        hook_path.write_text(original_content)

        result = runner.invoke(cli, ['install-hook'], input='n\n')

        assert result.exit_code == 0
        assert "Installation aborted" in result.output
        content = hook_path.read_text()
        assert content == original_content # Check that the file is unchanged
import os
from pathlib import Path
import click
from jinja2 import Environment, FileSystemLoader, select_autoescape


def install_pre_commit_hook():
    """Installs a pre-commit Git hook to check for security files."""
    git_dir = Path(".git")
    if not git_dir.is_dir():
        raise click.ClickException("Not a Git repository. Please run 'git init' first.")

    hooks_dir = git_dir / "hooks"
    hooks_dir.mkdir(exist_ok=True)
    hook_path = hooks_dir / "pre-commit"

    # Load hook script from template
    templates_dir = Path(__file__).parent / "templates"
    env = Environment(
        loader=FileSystemLoader(templates_dir), autoescape=select_autoescape()
    )
    template = env.get_template("hooks/pre-commit.sh.j2")
    hook_script = template.render()

    if hook_path.exists():
        if "Aegis CLI pre-commit hook" in hook_path.read_text():
            click.echo("Aegis pre-commit hook is already installed.")
            return
        else:
            if not click.confirm(
                "A pre-commit hook already exists. Do you want to overwrite it?"
            ):
                click.echo("Installation aborted.")
                return

    hook_path.write_text(hook_script)
    make_executable(hook_path)

    click.echo(f"✅ Aegis pre-commit hook installed successfully at {hook_path}")


def make_executable(path: Path):
    """
    Makes a file executable.
    Equivalent to `chmod +x`.
    """
    try:
        # More portable way to set executable bit
        mode = path.stat().st_mode
        mode |= (mode & 0o444) >> 2  # copy R bits to X
        path.chmod(mode)
    except Exception:
        # Fallback for systems where the above might not work as expected
        os.chmod(path, 0o755)
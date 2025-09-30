import logging
from pathlib import Path
import click
from jinja2 import Environment, FileSystemLoader, select_autoescape

logger = logging.getLogger(__name__)


def generate_files(
    project_path: Path, output_dir: Path, language: str, dry_run: bool = False
):
    """Generates security files from templates."""
    templates_dir = Path(__file__).parent / "templates"
    env = Environment(
        loader=FileSystemLoader(templates_dir), autoescape=select_autoescape()
    )

    # Define a mapping for language to package ecosystem
    ecosystem_map = {
        "python": "pip",
        "javascript": "npm",
        "java": "maven",  # or "gradle"
        "rust": "cargo",
    }
    package_ecosystem = ecosystem_map.get(
        language, "npm"
    )  # Default to npm if lang not in map

    # Determine the correct path for the secure coding guide template
    lang_specific_guide = templates_dir / language / "SecureCodingGuide.md.j2"
    if lang_specific_guide.exists():
        secure_guide_template_path = f"{language}/SecureCodingGuide.md.j2"
    else:
        secure_guide_template_path = "SecureCodingGuide.md.j2"

    files_to_generate = {
        ".github/dependabot.yml": {
            "path": project_path / ".github" / "dependabot.yml",
            "template": env.get_template("dependabot.yml.j2"),
            "context": {"package_ecosystem": package_ecosystem},
        },
        "security/SECURITY.md": {
            "path": output_dir / "SECURITY.md",
            "template": env.get_template("SECURITY.md.j2"),
            "context": {"project_name": project_path.name},
        },
        "security/SecureCodingGuide.md": {
            "path": output_dir / "SecureCodingGuide.md",
            "template": env.get_template(secure_guide_template_path),
            "context": {"language": language.capitalize()},
        },
    }

    if dry_run:
        click.echo("📝 Dry run - would generate:")
        for file_key, data in files_to_generate.items():
            click.echo(f"  - {file_key} at {data['path']}")
        return

    for file_key, data in files_to_generate.items():
        path = data["path"]
        template = data["template"]
        context = data["context"]

        rendered_content = template.render(context)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(rendered_content, encoding="utf-8")
        logger.info(f"Generated {path}")

    click.echo("✅ Security files generated successfully!")
    click.echo(f"  - {output_dir / 'SECURITY.md'}")
    click.echo(f"  - {output_dir / 'SecureCodingGuide.md'}")
    click.echo(f"  - {project_path / '.github' / 'dependabot.yml'}")
# Project Aegis CLI 2.0

A simple CLI tool to automate the creation of essential security starter files for your projects. Now with expanded language support and automated checks!

## The Problem

Every project needs a SECURITY.md file, dependabot.yml config, and basic security guidelines. But it’s a boring, repetitive chore that’s easy to neglect, leaving most projects without them until it's too late.

## The Solution

aegis is a command-line tool that handles the grunt work. It scans your project, detects the primary language, and generates essential security starter files from best-practice templates. It turns a 15-minute chore into a 3-second command.

> **Disclaimer: This is a Starting Point**
>
> Let's be clear: this tool is a starting point, not a magic bullet. It generates boilerplate documentation and is NOT a vulnerability scanner, security audit tool, or a replacement for a comprehensive security strategy. You are still responsible for writing secure code and using dedicated security tools.

## What's New in 2.0

Version 2.0 expands on the solid foundation of the original release with key features designed to broaden its utility and deepen its integration into your workflow.

- **Expanded Language Support:** Aegis now supports Java and Rust alongside Python and JavaScript, making it useful for a wider range of projects.

- **Git Hooks Integration:** Automatically ensure your security documentation is in place before you even commit. A new `aegis install-hook` command sets up a pre-commit Git hook that verifies your security files are present.

## Features

- **Multi-Language Detection:** Scans your project to identify the language (now supports Python, JavaScript, Java, and Rust).

- **Essential File Generation:** Creates the following from proven templates:
      - `.github/dependabot.yml`: A ready-to-use config to keep dependencies updated via GitHub.
      - `security/SECURITY.md`: A solid, customizable policy for vulnerability reporting.
      - `security/SecureCodingGuide.md`: A language-specific checklist for secure coding practices.

- **Automated Compliance:** Optional pre-commit hook to prevent commits if security files are missing.

- **Safe & Customizable:** Use `--dry-run` to preview changes without writing files and `--output` to specify a custom directory.

## Installation

Install directly from PyPI:

```bash
pip install aegis-cli
```

Or, to contribute, clone the repository and install in editable mode:

```bash
git clone [https://github.com/JamesTheGiblet/Project-Aegis-CLI.git](https://github.com/JamesTheGiblet/Project-Aegis-CLI.git)
cd Project-Aegis-CLI
pip install -e .[test]
```

"""
Sideload - Download large files via PyPI packages
"""

from .cli import main as cli_main

__version__ = "1.0.0"
__all__ = ["cli_main"]


def main() -> None:
    """Entry point for the CLI application"""
    cli_main()

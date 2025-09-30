"""
Navam - Personal AI agents for investing, shopping, health, and learning
"""

__version__ = "1.2.0"

from .chat import InteractiveChat
from .cli import main as cli_main

__all__ = ["InteractiveChat", "cli_main"]
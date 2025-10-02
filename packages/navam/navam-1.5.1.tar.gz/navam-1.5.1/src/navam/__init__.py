"""
Navam - Personal AI agents for investing, shopping, health, and learning
"""

__version__ = "1.4.7"

from .chat import InteractiveChat
from .cli import main as cli_main

__all__ = ["InteractiveChat", "cli_main"]
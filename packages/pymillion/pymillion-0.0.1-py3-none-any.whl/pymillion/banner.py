from rich.console import Console
from rich.panel import Panel

__version__ = "0.0.0"
__author__ = "Galileo Zoe"

def banner():
    console = Console()
    ascii_logo = r"""
██████╗ ██╗   ██╗     ██╗ ███████   ██████╗ ███    ██╗ 
██╔══██╗╚██╗ ██╔╝     ██║██ ╔═══██╗██╔═══██╗████╗  ██║
██████╔╝ ╚████╔╝      ██║  ███║   ╝██║   ██║██╔██╗ ██║
██╔═══╝   ╚██╔╝  ██   ██║██   ███║ ██║   ██║██║╚██╗██║
██║        ██║   ╚█████╔╝╚███████╔╝ ╚██████╔╝██║╚████║
╚═╝        ╚═╝    ╚════╝  ╚═════╝   ╚═════╝ ╚═╝  ╚═══╝
"""
    text = f"{ascii_logo}\n   v.{__version__} — by {__author__}"
    console.print(Panel.fit(text, border_style="cyan", title="PyMillion"))

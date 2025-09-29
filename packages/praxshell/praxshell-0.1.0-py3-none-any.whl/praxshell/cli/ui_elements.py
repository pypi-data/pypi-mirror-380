from praxshell.config.constants import BANNER, VERSION
from praxshell.cli.utils.color_utils import color

def show_banner():
    print(color(BANNER, "cyan"))

def show_welcome_message():
    print(color(f"\n+=== Welcome to Praxshell v{VERSION} ===+", "green"))
    print(color("Type 'help' to see available commands.\n", "yellow"))

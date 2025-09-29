from praxshell.config.constants import BUILTIN_CMDS
from praxshell.config.vault_loader import load_options, load_profiles
from praxshell.cli.utils.display import print_info, print_error
from praxshell.cli.utils.string_matcher import typo_match
from praxshell.cli.utils.color_utils import color

def handle_help(arg: str):
    OPTIONS_INFO = load_options()
    
    arg = arg.strip()

    if not arg:
        print_info("Available Commands")
        for cmd, desc in BUILTIN_CMDS.items():
            print(f"- {color(cmd, 'green')} - {desc}")
        print_info("Type 'help <command>|<options>' for details.")
        return

    if arg in BUILTIN_CMDS:
        print_info(f"{color(arg, 'green')} - {BUILTIN_CMDS[arg]}")
        return

    if arg in OPTIONS_INFO:
        concept = OPTIONS_INFO[arg]
        print_info(f"{color(arg, 'green')} (concept)")
        print(f"    Category: {concept.get('category')}")
        print(f"    Description: {concept.get('description')}")
        return

    # Try typo match
    candidates = list(BUILTIN_CMDS) + list(OPTIONS_INFO)
    match = typo_match(arg, candidates)
    if match:
        print_error(f"Unknown help target '{arg}'. Did you mean '{match[0]}'?")
    else:
        print_error(f"No help available for '{arg}'.")

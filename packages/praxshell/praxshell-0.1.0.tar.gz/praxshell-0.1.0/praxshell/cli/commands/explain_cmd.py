from praxshell.config.vault_loader import load_options
from praxshell.cli.utils.display import print_info, print_warning, print_error, print_list
from praxshell.cli.utils.color_utils import color
from praxshell.cli.utils.string_matcher import typo_match

def handle_explain(arg: str):
    OPTIONS_INFO = load_options() 
    
    arg = arg.strip()
    if not arg:
        print_warning("Usage: explain <concept>")
        return

    # Exact match
    if arg in OPTIONS_INFO:
        _print_concept(arg, OPTIONS_INFO[arg])
        return

    # Case insensitive match
    for key in OPTIONS_INFO:
        if key.lower() == arg.lower():
            _print_concept(key, OPTIONS_INFO[key])
            return

    # Typo suggestion
    match = typo_match(arg, list(OPTIONS_INFO.keys()))
    if match:
        print_error(f"No concept found for '{arg}'. Did you mean '{match[0]}'?")
    else:
        print_error(f"No concept found for '{arg}'.")

def _print_concept(name: str, data: dict):
    """Pretty-print a concept explanation."""
    print_info(f"Explanation for {color(name, 'green')}")
    print("-" * (len(name) + 20))

    desc = data.get("description", "No description available.")
    category = data.get("category", "Uncategorized")
    related = data.get("related", [])
    notebook = data.get("notebook")

    print(f"{color('Category:', 'cyan')} {category}")
    print(f"{color('Description:', 'cyan')} {desc}")

    if related:
        print_list("Related Concepts", related)

    if notebook:
        print(f"{color('Notebook:', 'cyan')} {notebook}")

from pathlib import Path
import json
from praxshell.cli.utils.display import print_info, print_error, print_success
from praxshell.cli.utils.notebook import compile_notebook, HTML_DIR
from praxshell.config.vault_loader import load_options

def handle_notebook(arg: str):
    tokens = arg.strip().split()

    if not tokens:
        print_info("Usage: notebook [build|<concept>]")
        return

    options = load_options()

    if tokens[0] == "build":
        # Compile all concepts that have a notebook
        built = 0
        for concept, meta in options.items():
            nb_path = meta.get("notebook")
            if nb_path:
                md_file = Path(__file__).resolve().parents[2] / nb_path
                if md_file.exists():
                    compile_notebook(md_file)
                    built += 1
                else:
                    print_error(f"Missing notebook file for {concept}: {md_file}")
        print_success(f"[✓] Built {built} notebooks into {HTML_DIR}")
        return

    # Otherwise: single concept
    concept = tokens[0]
    if concept not in options:
        print_error(f"Unknown concept: {concept}")
        return

    nb_path = options[concept].get("notebook")
    if not nb_path:
        print_error(f"No notebook linked for concept: {concept}")
        return

    md_file = Path(__file__).resolve().parents[2] / nb_path
    if not md_file.exists():
        print_error(f"Notebook file not found: {md_file}")
        return

    compile_notebook(md_file)



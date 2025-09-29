from praxshell.config.vault_loader import load_roadmaps
from praxshell.cli.utils.display import print_info, print_warning, print_error, print_list
from praxshell.cli.utils.color_utils import color
from praxshell.cli.commands.explain_cmd import handle_explain  

_current_roadmap = None
_current_step = 0

def handle_roadmap(arg: str):
    global _current_roadmap, _current_step

    arg = arg.strip()
    roadmaps = load_roadmaps()

    if not roadmaps:
        print_warning("No roadmaps found. Run `update vault` to download them.")
        return

    tokens = arg.split()
    if not tokens or tokens[0] == "list":
        print_info("Available Roadmaps:")
        for name, data in roadmaps.items():
            print(f"- {color(name, 'green')} → {data.get('description', '')}")
        return

    subcmd = tokens[0]

    if subcmd == "show":
        if len(tokens) < 2:
            print_error("Usage: roadmap show <name>")
            return
        name = tokens[1]
        if name not in roadmaps:
            print_error(f"Unknown roadmap: {name}")
            return
        data = roadmaps[name]
        print_info(f"Roadmap: {color(data['name'], 'green')}")
        print(f"Description: {data.get('description','')}\n")
        steps = [(step['concept'], step['note']) for step in data.get("steps",[])]
        print_list("Steps", [f"{concept} → {note}" for concept, note in steps])

        _current_roadmap = name
        _current_step = 0
        return

    if subcmd == "next":
        if not _current_roadmap:
            print_warning("No roadmap selected. Use `roadmap show <name>` first.")
            return
        steps = roadmaps[_current_roadmap].get("steps", [])
        if _current_step >= len(steps):
            print_info(" --- Roadmap completed! ---")
            return
        step = steps[_current_step]
        concept = step['concept']
        print_info(f"Next Step in {color(_current_roadmap, 'green')}:")
        print(f"- {color(concept, 'cyan')} → {step['note']}")
        _current_step += 1

        print()
        handle_explain(concept)
        return

    print_error("Usage: roadmap [list|show <name>|next]")

import shlex
from praxshell.config.constants import BUILTIN_CMDS, SUBCOMMANDS
from praxshell.config.vault_loader import load_options, load_profiles, load_roadmaps

OPTIONS_INFO = load_options()
PROFILES = load_profiles()

def complete_help(text, *_):
    matches = list(BUILTIN_CMDS) + list(OPTIONS_INFO) + list(PROFILES)
    return [m for m in matches if m.lower().startswith(text.lower())]

def complete_explain(text, *_):
    return [c for c in OPTIONS_INFO if c.lower().startswith(text.lower())]

def complete_notebook(text, *_):
    return complete_explain(text)

def complete_search(text, *_):
    return complete_explain(text)

def _complete_subcommand(cmd_name, text, line):
    tokens = shlex.split(line)
    node = SUBCOMMANDS.get(cmd_name, [])
    if isinstance(node, dict):
        return [s for s in node.keys() if s.lower().startswith(text.lower())]
    elif isinstance(node, list):
        if cmd_name == "roadmap" and len(tokens) >= 2 and tokens[1] == "show":
            roadmaps = load_roadmaps()
            return [r for r in roadmaps if r.lower().startswith(text.lower())]
        return [s for s in node if s.lower().startswith(text.lower())]
    return []

def complete_roadmap(text, line, *_):
    return _complete_subcommand("roadmap", text, line)

def complete_update(text, line, *_):
    return _complete_subcommand("update", text, line)

def complete_history(text, line, *_):
    return _complete_subcommand("history", text, line)

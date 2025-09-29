import json
from pathlib import Path
from praxshell.cli.commands.update_cmd import LOCAL_VAULT_PATH

CONFIG_PATH = LOCAL_VAULT_PATH / "config"

def _load_json(name: str, fallback: dict = None):
    # Load a JSON config file from vault/config/
    f = CONFIG_PATH / f"{name}.json"
    if f.exists():
        try:
            return json.loads(f.read_text(encoding="utf-8"))
        except Exception as e:
            return fallback or {}
    return fallback or {}

def load_options():
    return _load_json("options", {})

def load_profiles():
    return _load_json("profiles", {})

def load_roadmaps():
    return _load_json("roadmaps", {})

def load_roadmaps():
    roadmaps_path = LOCAL_VAULT_PATH / "roadmaps"
    roadmaps = {}
    if roadmaps_path.exists():
        for f in roadmaps_path.glob("*.json"):
            try:
                data = json.loads(f.read_text(encoding="utf-8"))
                name = f.stem
                roadmaps[name] = data
            except Exception:
                continue
    return roadmaps
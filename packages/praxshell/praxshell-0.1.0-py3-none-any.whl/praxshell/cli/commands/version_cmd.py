import json
from pathlib import Path
from praxshell.config.constants import VERSION
from praxshell.cli.commands.update_cmd import LOCAL_VAULT_PATH
from praxshell.cli.utils.display import print_info, print_warning

def get_vault_version() -> str:
    """Read version.json inside the vault, if it exists."""
    version_file = LOCAL_VAULT_PATH / "version.json"
    if version_file.exists():
        try:
            data = json.loads(version_file.read_text(encoding="utf-8"))
            return data.get("version", "unknown")
        except Exception:
            return "corrupted"
    return "not installed"

def handle_version():
    cli_version = VERSION
    vault_version = get_vault_version()

    print_info(f"Praxshell CLI version: {cli_version}")
    if vault_version == "not installed":
        print_warning("PraxVault not found. Run `update vault` to download.")
    else:
        print_info(f"PraxVault version: {vault_version}")

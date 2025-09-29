
from pathlib import Path
from praxshell.cli.utils.display import print_info, print_warning, print_error

HISTORY_FILE = Path.home() / ".praxshell" / "history.log"
HISTORY_FILE.parent.mkdir(parents=True, exist_ok=True)

IGNORED_COMMANDS = {"help", "clear", "history"} 

MAX_HISTORY = 1000  
CLEAN_KEEP = 50    
DEFAULT_SHOW = 10  

def record_history(command: str, valid: bool = True):
    """Append a command to history log unless ignored or invalid."""
    cmd_name = command.split()[0].lower() if command.strip() else ""
    if not valid or cmd_name in IGNORED_COMMANDS:
        return

    history = load_history()
    history.append(command.strip())

    # Trim if too long
    if len(history) > MAX_HISTORY:
        history = history[-MAX_HISTORY:]

    HISTORY_FILE.write_text("\n".join(history) + "\n", encoding="utf-8")

def load_history():
    """Load full history as a list of strings."""
    if not HISTORY_FILE.exists():
        return []
    return HISTORY_FILE.read_text(encoding="utf-8").splitlines()

def handle_history(arg: str):
    arg = arg.strip()
    history = load_history()

    if arg == "clear":
        HISTORY_FILE.write_text("", encoding="utf-8")
        print_info("History cleared.")
        return

    if arg == "clean":
        if history:
            history = history[-CLEAN_KEEP:]
            HISTORY_FILE.write_text("\n".join(history) + "\n", encoding="utf-8")
            print_info(f"History cleaned. Kept last {CLEAN_KEEP} entries.")
        else:
            print_warning("No history to clean.")
        return

    if not history:
        print_warning("No history found.")
        return

    if arg == "all":
        print_info("Full Command History:")
        for i, entry in enumerate(history, 1):
            print(f"  {i}. {entry}")
    elif arg.startswith("find "):
        term = arg[5:].strip().lower()
        matches = [h for h in history if term in h.lower()]
        if matches:
            print_info(f"History matches for '{term}':")
            for i, entry in enumerate(matches, 1):
                print(f"  {i}. {entry}")
        else:
            print_warning(f"No history entries match '{term}'.")
    else:
        # Default: last 10 only
        recent = history[-DEFAULT_SHOW:]
        print_info(f"Last {len(recent)} Commands:")
        for i, entry in enumerate(recent, 1):
            print(f"  {i}. {entry}")



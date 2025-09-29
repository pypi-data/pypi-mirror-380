VERSION = "0.1.0"

BANNER = """
    ____                       __         ____
   / __ \_________ __  _______/ /_  ___  / / /
  / /_/ / ___/ __ `/ |/_/ ___/ __ \/ _ \/ / /
 / ____/ /  / /_/ />  <(__  ) / / /  __/ / /
/_/   /_/   \__,_/_/|_/____/_/ /_/\___/_/_/

"""

PRIMARY_SETUP_KEY = "study_profile"

VAULT_REPO_ZIP = "https://github.com/diputs-sudo/praxvault/archive/refs/heads/main.zip"

TRUSTED_VAULT_URLS = [
    VAULT_REPO_ZIP,
]

DEV_VAULT_PATTERNS = [
    r"https://github\.com/.+/praxvault/archive/refs/heads/.+\.zip$",
]

BUILTIN_CMDS = {
    "explain": "Explain an AI concept. Usage: explain <concept>",
    "notebook": "Open a linked notebook. Usage: notebook <concept>",
    "search": "Search concepts or modules. Usage: search <term>",
    "modules": "Manage modules. Usage: modules [list|install|remove]",
    "roadmap": "View or follow study roadmaps. Usage: roadmap [list|show|next]",
    "help": "Show help for commands or options.",
    "history": "View past commands. Usage: history [all|clear|find]",
    "update": "Update praxvault. Usage: update vault [merge] ",
    "version": "Show Praxshell version.",
    "exit": "Exit Praxshell.",
    "quit": "Alias for exit.",
}

SUBCOMMANDS = {
    "modules": ["list", "install", "remove", "update"],
    "roadmap": ["list", "show", "next"],
    "history": ["all", "clear", "find"],
    "help": [],
    "update": {
        "vault": ["merge"],
    },
}

from .core_shell import PraxShell
from .ui_elements import show_banner, show_welcome_message
from praxshell.cli.utils.display import print_error, print_info, print_warning
from praxshell.cli.commands.update_cmd import LOCAL_VAULT_PATH, update_vault

def main():
    show_banner()
    show_welcome_message()

    if not LOCAL_VAULT_PATH.exists():
        print_warning("No PraxVault found.")
        try:
            response = input("→ Would you like to download the community PraxVault now? (y/n): ").strip().lower()
        except EOFError:
            response = "n"

        if response in {"y", "yes"}:
            update_vault()
        else:
            print_info("Skipping PraxVault download. Some commands may not work until you run:")
            print_info("    prax > update vault")

    shell = PraxShell()
    try:
        shell.cmdloop()
    except Exception as e:
        print_error(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()

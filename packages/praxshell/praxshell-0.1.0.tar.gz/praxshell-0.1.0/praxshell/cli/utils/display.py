from .color_utils import color

def print_info(msg: str):
    print(color(f"[*] {msg}", "cyan"))

def print_success(msg: str):
    print(color(f"[✓] {msg}", "green"))

def print_warning(msg: str):
    print(color(f"[!] {msg}", "yellow"))

def print_error(msg: str):
    print(color(f"[✗] {msg}", "red", bold=True))

def print_list(title: str, items: list[str]):
    if not items:
        return
    print(color(f"\n{title}", "cyan"))
    print("-" * len(title))
    for item in items:
        print(f"  - {item}")

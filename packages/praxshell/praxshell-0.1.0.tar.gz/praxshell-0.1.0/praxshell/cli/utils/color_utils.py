def color(text: str, color_name: str, bold: bool = False) -> str:
    colors = {
        "reset": "\033[0m",
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "white": "\033[37m",
    }
    code = colors.get(color_name, colors["reset"])
    if bold:
        code = "\033[1m" + code
    return f"{code}{text}{colors['reset']}"

import os
import platform

def handle_clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

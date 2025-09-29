import cmd
import shlex

from praxshell.cli.utils.tab_complete import (
    complete_help,
    complete_explain,
    complete_notebook,
    complete_search,
    complete_update,
    complete_history,
    complete_roadmap,
)
from praxshell.config.constants import BUILTIN_CMDS
from praxshell.cli.utils.string_matcher import typo_match
from praxshell.cli.utils.display import print_info, print_warning, print_error
from praxshell.cli.utils.color_utils import color

# Command handlers
from praxshell.cli.commands.explain_cmd import handle_explain
from praxshell.cli.commands.search_cmd import handle_search
from praxshell.cli.commands.notebook_cmd import handle_notebook
from praxshell.cli.commands.roadmap_cmd import handle_roadmap
from praxshell.cli.commands.help_cmd import handle_help
from praxshell.cli.commands.history_cmd import handle_history, record_history
from praxshell.cli.commands.update_cmd import handle_update
from praxshell.cli.commands.version_cmd import handle_version
from praxshell.cli.commands.exit_cmd import handle_exit
from praxshell.cli.commands.clear_cmd import handle_clear

class PraxShell(cmd.Cmd):
    prompt = color("prax ", "yellow") + color("> ", "cyan")

    def do_explain(self, arg):
        handle_explain(arg)

    def complete_explain(self, text, line, begidx, endidx):
        return complete_explain(text, line, begidx, endidx)

    def do_notebook(self, arg):
        handle_notebook(arg)

    def complete_notebook(self, text, line, begidx, endidx):
        return complete_notebook(text, line, begidx, endidx)

    def do_search(self, arg):
        handle_search(arg)

    def complete_search(self, text, line, begidx, endidx):
        return complete_search(text, line, begidx, endidx)

    def do_roadmap(self, arg):
        handle_roadmap(arg)
    
    def complete_roadmap(self, text, line, begidx, endidx):
        return complete_roadmap(text, line, begidx, endidx)

    def do_help(self, arg):
        handle_help(arg)
    
    def complete_help(self, text, line, begidx, endidx):
        return complete_help(text, line, begidx, endidx)

    def do_history(self, arg):
        handle_history(arg)

    def complete_history(self, text, line, begidx, endidx):
        return complete_history(text, line, begidx, endidx)

    def precmd(self, line: str) -> str:
        if line.strip():
            print()  
            record_history(line.strip())
        return line

    def postcmd(self, stop, line):
        if line.strip():
            print() 
        return stop

    def do_update(self, arg):
        handle_update(arg)
    
    def complete_update(self, text, line, begidx, endidx):
        return complete_update(text, line, begidx, endidx)

    def do_version(self, _):
        handle_version()

    def do_exit(self, _):
        return handle_exit()

    def do_quit(self, _):
        return handle_exit() 

    def do_clear(self, _):
        handle_clear()

    def emptyline(self):
        pass

    def completenames(self, text, *ignored):
        return [c for c in BUILTIN_CMDS if c.startswith(text)]

    def default(self, line):
        words = shlex.split(line)
        if not words:
            return

        cmd_input = words[0].lower()
        args = " ".join(words[1:])
        all_cmds = [name[3:] for name in dir(self) if name.startswith("do_")]

        match = typo_match(cmd_input, all_cmds)
        if match:
            confirm = input(f"[~] Did you mean '{match[0]}'? (Enter/n): ").strip().lower()
            if confirm in {"", "y", "yes"}:
                record_history(line.strip(), valid=True)
                return getattr(self, f"do_{match[0]}")(args)

        print_error(f"Unknown command: {cmd_input}")
        record_history(line.strip(), valid=False)

    def cmdloop(self, intro=None):
        try:
            super().cmdloop(intro)
        except KeyboardInterrupt:
            print_warning("\n[CTRL+C] Interrupted. Type exit/quit to quit.")
            self.cmdloop()

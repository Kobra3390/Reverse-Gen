from rich.console import Console
from rich.style import Style
import os

console = Console()

# color 454545
# color 7780ff

def PrintBanner():
   asci_art1 = """                                      
     _____                             _____         
    | __  |___ _ _ ___ ___ ___ ___ ___|   __|___ ___ 
    |    -| -_| | | -_|  _|_ -| -_|___|  |  | -_|   |
    |__|__|___|\_/|___|_| |___|___|   |_____|___|_|_|                           
                                                    
   """

   link = "Github: https://github.com/Kobra3390" 

   asci_art2 = """
            ,-,,-,   __
     ______/     /_,'  |
     \________________/
          |\) (/ |
       (  | oo   |\t Created by k0Br@3390
        ) `|  |--'\t %s
       (___^^^^| 
          (____'    
          """ % (link)
   
   
   myStyle1 = Style(color="#7780ff", bold=True)
   myStyle2 = Style(color="#7780ff", bold=True)
   console.print(asci_art1, style=myStyle1)
   console.print(asci_art2, style=myStyle2)

def PrintOptions():
   print("\n")
   console.print("[1]  Bash -i\t\t\t[16] Java #1 \t\t[31] nc.exe -e\n[2]  Bash 196\t\t\t[17] Ruby no sh\t\t[32] nc -c\n[3]  Bash read line\t\t[18] Bash UDP\t\t[33] ncat -e\n[4]  Python #1\t\t\t[19] Java #2\t\t[34] ncat.exe -ec\n[5]  Python Spawn Shell TTY\t[20] Java #3\t\t[35] ncat UDP", style="#7780ff")
   print("\n")
   console.print("[6]  Python #2\t\t\t[21] Telnet Shell \t[36] rustcat\n[7]  Python3 #1\t\t\t[22] C Shell\t\t[37] Haskell #1\n[8]  Python3 #2\t\t\t[23] C Shell Windows \t[38] Perl\n[9]  Python3 Windows\t\t[24] Dart \t\t[39] Perl no sh\n[10] Python3 Windows #2\t\t[25] Awk\t\t[40] Perl Windows Only",  style="#7780ff")
   print("\n")
   console.print("[11] Python3 shortest\t\t[26] Groovy\t\t[41] Windows ConPty\n[12] Ruby #1\t\t\t[27] Groovy 2\t\t[42] Telnet Shell #2 \n[13] Ruby #2\t\t\t[28] Other Shell\t[43] zsh Shell\n[14] Node.JS #1\t\t\t[29] nc mkfifo\t\t[44] socat #1\n[15] Node.JS #2\t\t\t[30] nc -e\t\t[45] socat #2 TTY",  style="#7780ff")
   console.print("\n----------------------------------------------------------------------------\n", style="#7780ff")
   console.print("[46] Ruby Windows Only\t\t[51] PHP Ivan Sincek\t[56] PHP passthru\n[47] Lua #1\t\t\t[52] PHP cmd\t\t[57] PHP`\n[48] Lua #2\t\t\t[53] PHP exec\t\t[58] PHP popen\n[49] PHP Emoji\t\t\t[54] PHP shell_exec\t[59] PHP proc_open\n[50] PHP PentestMonkey\t\t[55] PHP system", style="#7780ff")


 


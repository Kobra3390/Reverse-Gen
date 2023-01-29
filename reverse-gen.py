#!/usr/bin/env python3
from dbReverseShell import *
from function import *

PrintBanner()
PrintOptions()

try:
    options = int(input("\nEnter a Options: "))
    match options:
        case 1:
            ip = input("\nInsert Ip Address: ")
            port = int(input("Insert Port: "))
            print("\n")
            Bash_i(ip, port)
        case 2:
            ip = input("\nInsert Ip Address: ")
            port = int(input("Insert Port: "))
            print("\n")
            Bash_196(ip, port)
        case 3:
            ip = input("\nInsert Ip Address: ")
            port = int(input("Insert Port: "))
            print("\n")
            Bash_read_line(ip, port)
        case 4:
            ip = input("\nInsert Ip Address: ")
            port = int(input("Insert Port: "))
            print("\n")
            python_1(ip, port)
        case 5:
            Python_Spawn_Shell_TTY()
        case 6:
            ip = input("\nInsert Ip Address: ")
            port = int(input("Insert Port: "))
            print("\n")
            python_2(ip, port)
        case 7:
            ip = input("\nInsert Ip Address: ")
            port = int(input("Insert Port: "))
            print("\n")
            python3_1(ip, port)
        case 8:
            ip = input("\nInsert Ip Address: ")
            port = int(input("Insert Port: "))
            print("\n")
            python3_2(ip, port)
        case 9:
            ip = input("\nInsert Ip Address: ")
            port = int(input("Insert Port: "))
            print("\n")
            python3_windows(ip, port)
        case 10:
            ip = input("\nInsert Ip Address: ")
            port = int(input("Insert Port: "))
            print("\n")
            python3_windows_2(ip, port)
        case 11:
            ip = input("\nInsert Ip Address: ")
            port = int(input("Insert Port: "))
            print("\n")
            python3_shortest(ip, port)
        case 12:
            ip = input("\nInsert Ip Address: ")
            port = int(input("Insert Port: "))
            print("\n")
            Ruby_1(ip, port)
        case 13:
            ip = input("\nInsert Ip Address: ")
            port = int(input("Insert Port: "))
            print("\n")
            Ruby_2(ip, port)
        case 14:
            ip = input("\nInsert Ip Address: ")
            port = int(input("Insert Port: "))
            print("\n")
            NodeJSShell1(ip, port)
        case 15:
            ip = input("\nInsert Ip Address: ")
            port = int(input("Insert Port: "))
            print("\n")
            NodeJSShell2(ip, port)
        case 16:
            ip = input("\nInsert Ip Address: ")
            port = int(input("Insert Port: "))
            print("\n")
            JavaShell1(ip, port)
        case 17:
            ip = input("\nInsert Ip Address: ")
            port = int(input("Insert Port: "))
            print("\n")
            Ruby_no_sh(ip, port)
        case 18:
            ip = input("\nInsert Ip Address: ")
            port = int(input("Insert Port: "))
            print("\n")
            Bash_UDP(ip, port)
        case 19:
            ip = input("\nInsert Ip Address: ")
            port = int(input("Insert Port: "))
            print("\n")
            JavaShell2(ip, port)
        case 20:
            ip = input("\nInsert Ip Address: ")
            port = int(input("Insert Port: "))
            print("\n")
            JavaShell3(ip, port)
        case 21:
            ip = input("\nInsert Ip Address: ")
            port = int(input("Insert Port: "))
            print("\n")
            TelnetShell(ip, port)
        case 22:
            ip = input("\nInsert Ip Address: ")
            port = int(input("Insert Port: "))
            print("\n")
            CReverseShell(ip, port)
            console.print("[red]Note: [/red]\n\tCompiler with: gcc /tmp/shell.c --output csh && csh\n")
        case 23:
            ip = input("\nInsert Ip Address: ")
            port = int(input("Insert Port: "))
            print("\n")
            CWindowsShell(ip, port)
        case 24:
            ip = input("\nInsert Ip Address: ")
            port = int(input("Insert Port: "))
            print("\n")
            DartShell(ip, port)
        case 25:
            ip = input("\nInsert Ip Address: ")
            port = int(input("Insert Port: "))
            print("\n")
            AwkShell(ip, port)
        case 26:
            ip = input("\nInsert Ip Address: ")
            port = int(input("Insert Port: "))
            print("\n")
            GrovvyShell(ip, port)
        case 27:
            ip = input("\nInsert Ip Address: ")
            port = int(input("Insert Port: "))
            print("\n")
            GroovyShell2(ip, port)
        case 28:
            ip = input("\nInsert Ip Address: ")
            port = int(input("Insert Port: "))
            print("\n")
            OtherShell(ip, port)
        case 29:
            ip = input("\nInsert Ip Address: ")
            port = int(input("Insert Port: "))
            print("\n")
            nc_mkfifo(ip, port)
        case 30:
            ip = input("\nInsert Ip Address: ")
            port = int(input("Insert Port: "))
            print("\n")
            nc_e(ip, port)
        case 31:
            ip = input("\nInsert Ip Address: ")
            port = int(input("Insert Port: "))
            print("\n")
            nc_exe_e(ip, port)
        case 32:
            ip = input("\nInsert Ip Address: ")
            port = int(input("Insert Port: "))
            print("\n")
            nc_c(ip, port)
        case 33:
            ip = input("\nInsert Ip Address: ")
            port = int(input("Insert Port: "))
            print("\n")
            ncat_e(ip, port)
        case 34:
            ip = input("\nInsert Ip Address: ")
            port = int(input("Insert Port: "))
            print("\n")
            ncat_exe_e(ip, port)
        case 35:
            ip = input("\nInsert Ip Address: ")
            port = int(input("Insert Port: "))
            print("\n")
            ncat_UDP(ip, port)
        case 36:
            ip = input("\nInsert Ip Address: ")
            port = int(input("Insert Port: "))
            print("\n")
            rustcat_shell(ip, port)
        case 37:
            ip = input("\nInsert Ip Address: ")
            port = int(input("Insert Port: "))
            print("\n")
            haskell_shell(ip, port)
        case 38:
            ip = input("\nInsert Ip Address: ")
            port = int(input("Insert Port: "))
            print("\n")
            Perl(ip, port)
        case 39:
            ip = input("\nInsert Ip Address: ")
            port = int(input("Insert Port: "))
            print("\n")
            Perl_no_sh(ip, port)
        case 40:
            ip = input("\nInsert Ip Address: ")
            port = int(input("Insert Port: "))
            print("\n")
            Perl_Windows_Only(ip, port)
        case 41:
            ip = input("\nInsert Ip Address: ")
            port = int(input("Insert Port: "))
            print("\n")
            WindowsConPty(ip, port)
        case 42:
            ip = input("\nInsert Ip Address: ")
            port = int(input("Insert Port: "))
            print("\n")
            TelnetShell2(ip, port)
        case 43:
            ip = input("\nInsert Ip Address: ")
            port = int(input("Insert Port: "))
            print("\n")
            zsh_reverse_shell(ip, port)
        case 44:
            ip = input("\nInsert Ip Address: ")
            port = int(input("Insert Port: "))
            print("\n")
            socat1(ip, port)
        case 45:
            ip = input("\nInsert Ip Address: ")
            port = int(input("Insert Port: "))
            print("\n")
            socat2TTY(ip, port)
        case 46:
            ip = input("\nInsert Ip Address: ")
            port = int(input("Insert Port: "))
            print("\n")
            Ruby_Windows_Only(ip, port)
        case 47:
            ip = input("\nInsert Ip Address: ")
            port = int(input("Insert Port: "))
            print("\n")
            Lua1(ip, port)
        case 48:
            ip = input("\nInsert Ip Address: ")
            port = int(input("Insert Port: "))
            print("\n")
            Lua2(ip, port)
        case 49:
            ip = input("\nInsert Ip Address: ")
            port = int(input("Insert Port: "))
            print("\n")
            PHP_Emoji(ip, port)
        case 50:
            ip = input("\nInsert Ip Address: ")
            port = int(input("Insert Port: "))
            print("\n")
            PHP_PentestMonkey(ip, port)
        case 51:
            ip = input("\nInsert Ip Address: ")
            port = int(input("Insert Port: "))
            print("\n")
            PHP_Ivan_Sincek(ip, port)
        case 52:
            PHP_cmd()
        case 53:
            ip = input("\nInsert Ip Address: ")
            port = int(input("Insert Port: "))
            print("\n")
            PHP_exec(ip, port)
        case 54:
            ip = input("\nInsert Ip Address: ")
            port = int(input("Insert Port: "))
            print("\n")
            PHP_shell_exec(ip, port)
        case 55:
            ip = input("\nInsert Ip Address: ")
            port = int(input("Insert Port: "))
            print("\n")
            PHP_system(ip, port)
        case 56:
            ip = input("\nInsert Ip Address: ")
            port = int(input("Insert Port: "))
            print("\n")
            PHP_passthru(ip, port)
        case 57:
            ip = input("\nInsert Ip Address: ")
            port = int(input("Insert Port: "))
            print("\n")
            PHP_backtick(ip, port)
        case 58:
            ip = input("\nInsert Ip Address: ")
            port = int(input("Insert Port: "))
            print("\n")
            PHP_popen(ip, port)
        case 59:
            ip = input("\nInsert Ip Address: ")
            port = int(input("Insert Port: "))
            print("\n")
            PHP_proc_open(ip, port)

except (KeyboardInterrupt, NameError):
    console.print("\n\nExiting...\n", style="red")
except ValueError:
    console.print("\nInvalid Input Value...\n", style="red")


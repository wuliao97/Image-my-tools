import sys
import funcs as f
from pystyle import Write, Colors


def main():
    f.clear()
    Write.Print("                                     /$$ /$$        /$$  /$$$$$$   /$$$$$$  /$$$$$$$$\n", Colors.purple_to_blue, interval=0.0)
    Write.Print("                                    | $$| $$$      / $$ /$$__  $$ /$$__  $$/ $$____/ \n", Colors.purple_to_blue, interval=0.0)
    Write.Print("                                    | $$| $$$$    / $$$| $$  \ $$| $$  \__/| $$      \n", Colors.purple_to_blue, interval=0.0)
    Write.Print("                                    | $$| $$ $$  / $ $$| $$$$$$$$| $$ /$$$$| $$$$$$$ \n", Colors.purple_to_blue, interval=0.0)
    Write.Print("                                    | $$| $$  $$ $$  $$| $$__  $$| $$|_  $$| $$___/  \n", Colors.purple_to_blue, interval=0.0)
    Write.Print("                                    | $$| $$\  $$$ | $$| $$  | $$| $$  \ $$| $$      \n", Colors.purple_to_blue, interval=0.0)
    Write.Print("                                    | $$| $$ \  $/ | $$| $$  | $$|  $$$$$$/| $$$$$$$$\n", Colors.purple_to_blue, interval=0.0)
    Write.Print("By: Ennui#9999                      |_/ |__/  \_/  \__/|__/  |__/ \______/  \______/  My tools\n", Colors.purple_to_blue, interval=0.0)
    Write.Print("══════════════════════════════════════════════════════════════════════════════════════════════\n", Colors.purple_to_blue, interval=0.0)
    print(f'''{f.lc}Alpha{f.Fore.RESET}({f.lc}0{f.Fore.RESET}.{f.lc}1{f.Fore.RESET}.{f.lc}0{f.Fore.RESET}) version

{f.lm}[{f.w} 1 {f.lm}]{f.Fore.RESET} Convert mp4 to GIF
{f.lm}[{f.w} 2 {f.lm}]{f.Fore.RESET} Colors list (alpha version only)
{f.lm}[{f.w} 3 {f.lm}]{f.Fore.RESET} None
{f.lm}[{f.w} 4 {f.lm}]{f.Fore.RESET} None
{f.lm}[{f.w} 5 {f.lm}]{f.Fore.RESET} Exit this Program
''')
    Write.Print("══════════════════════════════════════════════════════════════════════════════════════════════\n", Colors.blue_to_purple, interval=0.000)
    choice = str(input(f"choice{f.lm}:{f.Fore.RESET} "))

    f.clear()

    match (choice):
        case "1":
            f.ToGif()

        case "2":
            print(f"""
b = {f.b} COLOR {f.Fore.RESET}
r = {f.r} COLOR {f.Fore.RESET}
g = {f.g} COLOR {f.Fore.RESET}
y = {f.y} COLOR {f.Fore.RESET}
br = {f.br} COLOR {f.Fore.RESET}
m = {f.m} COLOR {f.Fore.RESET}
c = {f.c} COLOR {f.Fore.RESET}
w = {f.w} COLOR {f.Fore.RESET}

lb = {f.lb} COLOR {f.Fore.RESET}
lr = {f.lr} COLOR {f.Fore.RESET}
lg = {f.lg} COLOR {f.Fore.RESET}
ly = {f.ly} COLOR {f.Fore.RESET}
lbr = {f.lbr} COLOR {f.Fore.RESET}
lm = {f.lm} COLOR {f.Fore.RESET}
lc = {f.lc} COLOR {f.Fore.RESET}
lw = {f.lw} COLOR {f.Fore.RESET}""")
            input()
    
        case "3":
            pass
    
        case "4":
            pass
    
        case "5":
            print("System is Exited. Thank you for use this.")
            sys.exit()

        case _:
            print("Fail")
            input("Press Enter key")
            

    f.clear()
    main()



if __name__ == "__main__":
    if (f.file_setup()):
        main()
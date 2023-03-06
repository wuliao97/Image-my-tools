import os
import math
import time
from pystyle import Write, Colors


check_symble = "✔"
fail_symble  = "✗"

CSI = '\033['
OSC = '\033]'
BEL = '\a'

def code_to_chars(code):
    return CSI + str(code) + 'm'

class AnsiCodes(object):
    def __init__(self):
        # the subclasses declare class attributes which are numbers.
        # Upon instantiation we define instance attributes, which are the same
        # as the class attributes but wrapped with the ANSI escape sequence
        for name in dir(self):
            if not name.startswith('_'):
                value = getattr(self, name)
                setattr(self, name, code_to_chars(value))

class AnsiCursor(object):
    def UP(self, n=1):
        return CSI + str(n) + 'A'
    def DOWN(self, n=1):
        return CSI + str(n) + 'B'
    def FORWARD(self, n=1):
        return CSI + str(n) + 'C'
    def BACK(self, n=1):
        return CSI + str(n) + 'D'
    def POS(self, x=1, y=1):
        return CSI + str(y) + ';' + str(x) + 'H'

class AnsiFore(AnsiCodes):
    BLACK           = 30
    RED             = 31
    GREEN           = 32
    YELLOW          = 33
    BLUE            = 34
    MAGENTA         = 35
    CYAN            = 36
    WHITE           = 37
    RESET           = 39

    # These are fairly well supported, but not part of the standard.
    LIGHTBLACK_EX   = 90
    LIGHTRED_EX     = 91
    LIGHTGREEN_EX   = 92
    LIGHTYELLOW_EX  = 93
    LIGHTBLUE_EX    = 94
    LIGHTMAGENTA_EX = 95
    LIGHTCYAN_EX    = 96
    LIGHTWHITE_EX   = 97

class AnsiBack(AnsiCodes):
    BLACK           = 40
    RED             = 41
    GREEN           = 42
    YELLOW          = 43
    BLUE            = 44
    MAGENTA         = 45
    CYAN            = 46
    WHITE           = 47
    RESET           = 49

    # These are fairly well supported, but not part of the standard.
    LIGHTBLACK_EX   = 100
    LIGHTRED_EX     = 101
    LIGHTGREEN_EX   = 102
    LIGHTYELLOW_EX  = 103
    LIGHTBLUE_EX    = 104
    LIGHTMAGENTA_EX = 105
    LIGHTCYAN_EX    = 106
    LIGHTWHITE_EX   = 107

class AnsiStyle(AnsiCodes):
    BRIGHT    = 1
    DIM       = 2
    NORMAL    = 22
    RESET_ALL = 0

Fore   = AnsiFore()
Back   = AnsiBack()
Style  = AnsiStyle()
Cursor = AnsiCursor()

b = Fore.BLACK
r = Fore.RED
g = Fore.GREEN
y = Fore.YELLOW
br = Fore.BLUE
m = Fore.MAGENTA
c = Fore.CYAN
w = Fore.WHITE

lb = Fore.LIGHTBLACK_EX
lr = Fore.LIGHTRED_EX
lg = Fore.LIGHTGREEN_EX
ly = Fore.LIGHTYELLOW_EX
lbr = Fore.LIGHTBLUE_EX
lm = Fore.LIGHTMAGENTA_EX
lc = Fore.LIGHTCYAN_EX
lw = Fore.LIGHTWHITE_EX



def check(flag:bool=False):
    return g + check_symble + Fore.RESET if flag else lr + fail_symble + Fore.RESET


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def convert_size(size:int, units = "B"):
    units = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB")
    i = math.floor(math.log(size, 1024)) if size > 0 else 0
    size = round(size / 1024 ** i, 2)
    return f"{size} {units[i]}"


def sequence(fn:str, path:str):
    if fn in os.listdir(path):
        file_name, ext = os.path.splitext(fn)
        cnt = sum([1 for i in os.listdir(path) if file_name and ext in i])
        return "%s-%s%s" % (file_name, cnt, ext)
    else:
        return fn



def file_setup() -> bool:
    ROOT_PATH = "." + os.sep

    if not (os.path.exists(DIR_PATH:=ROOT_PATH + "mp4" + os.sep)):
        os.makedirs(DIR_PATH)

    if not (os.path.exists(DIR_PATH:=ROOT_PATH + "finished" + os.sep)):
        os.makedirs(DIR_PATH)

    return True



##############################################

"""
    Main functions
    
    1:

    2:

    3:

    4:
        

    
"""

def final_checK(material:str, output:str, quality:bool, scale:int):
    clear()
    print(f"{lm}IMAGE{Fore.RESET}:{lm}Convert mp4 to Gif{Fore.RESET}:{lm}Convert{Fore.RESET}")
    print()
    Write.Print("══════════════════════════════════════════════════════════════════════════════════════════════\n", Colors.blue_to_purple, interval=0.000)
    print(f"""
{lm}[{Fore.RESET} mp4 file    {lm}]{Fore.RESET} {material}
{lm}[{Fore.RESET} output name {lm}]{Fore.RESET} {output}
{lm}[{Fore.RESET} Qualitu     {lm}]{Fore.RESET} {"High" if quality else "Low"}
{lm}[{Fore.RESET} Scale       {lm}]{Fore.RESET} {scale}x
""")
    Write.Print("══════════════════════════════════════════════════════════════════════════════════════════════\n", Colors.blue_to_purple, interval=0.000)

    result = input(f"Are you sure to convert?: ( {g}y{Fore.RESET} / {lr}n{Fore.RESET} ) ").lower()
    clear()

    if (result == "n"):
        return False, None

    elif (result == "y"):
        if not (material):
            print(f"{lr}mp4 file is not setting{Fore.RESET}. Please try again.")
            input("Press Enter key to continue")
            return False, None
        
        else:
            output = "output" + ".gif" if not output else output
            return True, sequence(output, "." + os.sep + "finished") 

    else:
        print(f"{lr}Invald value{Fore.RESET}. Please try again.")
        input("Press Enter key to continue")
        return False, None
    

def systemcalling(code):
    os.system(code)


def convert_to_gif(material, output, quality, scale):
    material = "mp4" + os.sep + material
    quality = 30 if quality else 10
    output = "finished" + os.sep + output 
    ffmpeg = f'ffmpeg -y -i {material} -filter_complex "[0:v] fps={quality},scale={scale}:-1,split [a][b];[a] palettegen [p];[b][p] paletteuse=dither=none" {output}'
    clear()

    s_time = time.time()
    systemcalling(ffmpeg)
    e_time = round((time.time() - s_time), 2)

    Write.Print("\n══════════════════════════════════════════════════════════════════════════════════════════════\n\n", Colors.blue_to_purple, interval=0.000)

    print(f"""
{lm}[{Fore.RESET} file {lm}]{Fore.RESET} {os.path.abspath(output)}
{lm}[{Fore.RESET} size {lm}]{Fore.RESET} {convert_size(os.stat(output).st_size)}
{lm}[{Fore.RESET} time {lm}]{Fore.RESET} {e_time}s
""")

    Write.Print("\n══════════════════════════════════════════════════════════════════════════════════════════════\n\n", Colors.blue_to_purple, interval=0.000)
    

    input("press Enter key to back main panel")



def select_mp4(material:str):
    clear()

    PATH = "." + os.sep + "mp4"
    m = os.listdir(PATH)
    [m.remove(i) for i in m if ".mp4"  or ".mov" != os.path.splitext(i)[-1]]

    if (len(m) == 0):
        print("There is no mp4 file. ")
        input("press Enter key to continue and Open the mp4 dir")
        os.system("open ." + os.sep + "mp4")
        clear()
        return False

    print(f"{lm}IMAGE{Fore.RESET}:{lm}Convert mp4 to Gif{Fore.RESET}:{lm}material mp4 file{Fore.RESET}")
    print()
    Write.Print("══════════════════════════════════════════════════════════════════════════════════════════════\n", Colors.blue_to_purple, interval=0.000)
    print()
    
    for idx, obj in enumerate(m):
        print(f"{lm}[{Fore.RESET} {idx + 1} {lm}]{Fore.RESET} {obj}")
    print(f"\n{lm}[{Fore.RESET} {lr}c {lm}]{Fore.RESET} Cannel")

    print()
    Write.Print("══════════════════════════════════════════════════════════════════════════════════════════════\n", Colors.blue_to_purple, interval=0.000)

    choice = input(f"Choose one that you want to gif{lm}:{Fore.RESET} ")
    if (choice.isdigit()):
        return m[int(choice) - 1]
     
    elif (choice.lower() == "c"):
        return material

    else:
        print(f"{lr}Invald value{Fore.RESET}. Please try again.")
        input("Press Enter key to continue")
        return material



def set_output():
    clear()
    print(f"IMAGE{lm}:{Fore.RESET}Convert mp4 to Gif{lm}:{Fore.RESET}Set Output file name")
    print()
    Write.Print("══════════════════════════════════════════════════════════════════════════════════════════════\n", Colors.blue_to_purple, interval=0.000)
    print(f"""
Default{lm}:{Fore.RESET} output

{lm}[{Fore.RESET} {lr}c {lm}]{Fore.RESET} Cannel
    """)
    Write.Print("══════════════════════════════════════════════════════════════════════════════════════════════\n", Colors.blue_to_purple, interval=0.000)

    out_name = input(f"Please type you want to output file name{lm}:{Fore.RESET}")


    if (out_name.lower() == "c"):
        return False

    return out_name



def mode_panel(
        quality:bool, 
        scale  :int
):
    clear()
    print(f"{lm}IMAGE{Fore.RESET}:{lm}Convert mp4 to Gif{Fore.RESET}:{lm}config{Fore.RESET}")
    print()
    Write.Print("══════════════════════════════════════════════════════════════════════════════════════════════\n", Colors.blue_to_purple, interval=0.000)
    print(f'''
{lm}[{w} 1 {lm}]{Fore.RESET} Quality                                 {lm}Quality{Fore.RESET}: {'High' if quality else 'low'}
{lm}[{w} 2 {lm}]{Fore.RESET} scale                                   {lm}  Scale{Fore.RESET}: {scale}
{lm}[{w} 3 {lm}]{Fore.RESET} Go back to before panel
''')
    Write.Print("══════════════════════════════════════════════════════════════════════════════════════════════\n", Colors.blue_to_purple, interval=0.000)

    choice = str(input(f"{lm}choice{Fore.RESET}: "))
    match (choice):
        case "1":
            TrueOrFalse = input(f"you want to High quality? ( {g}y{Fore.RESET} / {lr}n{Fore.RESET} ) ").lower()
            if (TrueOrFalse == "y"):
                quality = True

            elif (TrueOrFalse == "n"):
                quality = False
                
            else:
                print(f"{lr}Invald value{Fore.RESET}. Please try again.")
                input("Press Enter key to continue")
        

        case "2":
            size = input(f"type scale size you want to{lm}:{Fore.RESET} ")
            if (size.isdigit()):
                scale = int(size)
                if not 1980 > scale > 100:
                    print(f"{lr}INSANE value{Fore.RESET}. Please try again.")
                    input("Press Enter key to continue")
                    
            else:
                print(f"{lr}Invald value{Fore.RESET}. Please try again.")
                input("Press Enter key to continue")

        case "3":
            pass

        case _:
            print(f"{lr}Invald value{Fore.RESET}. Please try again.")
            input("Press Enter key to continue")

    clear()
    return (quality, scale)



def toGif_title(material:str, output:str, quality:bool, scale:int):
    clear()
    print(f"{lm}IMAGE{Fore.RESET}:{lm}Convert mp4 to Gif{Fore.RESET}")
    print(f"Current place: " + f'{Fore.RESET}{os.sep}{lc}'.join(os.getcwd().split(os.sep)))
    print()
    Write.Print("══════════════════════════════════════════════════════════════════════════════════════════════\n", Colors.blue_to_purple, interval=0.000)
    print(f'''
{lm}[{w} 1 {lm}]{Fore.RESET} material mp4 file                      {lm}Name{Fore.RESET}: {material if material else lr + 'None' + Fore.RESET}
{lm}[{w} 2 {lm}]{Fore.RESET} output file name                       {lm}Name{Fore.RESET}: {lm}{output if output else 'output'}{Fore.RESET}
{lm}[{w} 3 {lm}]{Fore.RESET} Edit config
{lm}[{w} 4 {lm}]{Fore.RESET} How to use
{lm}[{w} 5 {lm}]{Fore.RESET} Go back to main
{lm}[{w}   {lm}]{Fore.RESET} Enter: Process run
''')
    Write.Print("══════════════════════════════════════════════════════════════════════════════════════════════\n", Colors.blue_to_purple, interval=0.000)
    choice = str(input(f"choice{lm}:{Fore.RESET} "))
    
    match (choice):
        case "1":
            """
            material mp4 file
            
            note: I will add and fix this functions
            1: Add file extension Like .mov
            2: Fix UI/UX 
            """
            material = select_mp4(material)
            toGif_title(material=material, output=output, quality=quality, scale=scale)


        case "2":
            """output file name"""
            output = set_output()
            toGif_title(material=material, output=output, quality=quality, scale=scale)


        case "3":
            """"""
            quality, scale = mode_panel(quality=quality, scale=scale)
            toGif_title(material=material, output=output, quality=quality, scale=scale)


        case "4":
            clear()
            print("ちゃんと項目見れば普通にわかるだろ？笑\nそれなのに見にきてるお前は重度知的障害持ちだろうから病院行けアホ笑笑")
            input()
            toGif_title(material=material, output=output, quality=quality, scale=scale)

            
        case "5":
            """
            Exit Convert mp4 to Gif
            Back to main function
            """
            return


        case "":
            flag, output = final_checK(material, output, quality, scale)
            if (flag):
                convert_to_gif(material, output, quality, scale)
    
                toGif_title(material=False, output=False, quality=False, scale=680)


        case _:
            clear()
            print(f"{lr}Invald value{Fore.RESET}. Please try again.")
            input("Press some key to continue")

            toGif_title(material=material, output=output, quality=quality, scale=scale)


            
def ToGif():
    print(f"This is {lm}Convert mp4 to Gif{Fore.RESET} !")

    material = False
    output   = False
    quality  = False
    scale    = 680

    toGif_title(material=material, output=output, quality=quality, scale=scale)
    
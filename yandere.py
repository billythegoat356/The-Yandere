from os import name, mkdir, system
from os.path import isdir
from random import choice
from pyfade import Colors, Fade, Anime
from pycenter import center, makebox
from terminaltables import DoubleTable
from art import text2art, FONT_NAMES


def clear():
    system("cls" if name == 'nt' else "clear")

if name == 'nt':
    system("title The Yandere & mode 160, 42")



def maketable(dictionnary: dict, title: str, space: str = " "):
    table = [(space + str(key) if len(str(key)) == 1 else str(key), value)
             for key, value in dictionnary.items()]
    return DoubleTable(table_data=table, title=title)


def printf(*args):
    return print(Fade.Horizontal(Colors.blue_to_purple, "".join(args)))


def inputf(*args):
    return input(Fade.Horizontal(Colors.blue_to_purple, "".join(args)))



colors = [col for col in Colors().__dir__() if "to" in col]

banner = '''\n\n\n\n\n\n
This animation was made with *pyfade* :)


           ./oyddddddddddhyo:.                                                                     
        -+hdddddddddddddddddddy+.                                                                  
      :yddddddddddddyyssyhddddddds-                                                                
    -yddddddddddds:..---..-/ydddddds.                                                              
   /hddddddddddy-``/sssyy/```:ydddddh-                                                             
  /dddddddddddh.``sh/``.yh-```.sdddddd:                                                            
 :dddddddddddd/ ``sh+..:hhso:``.ddddddh.                                                           
 hdddddddddddd:````/shhs:-:yh+``ydddddds                                                           
:dddddddddddddo`````.hh.```ohs``hddddddd.                                                          
+dddddddddddddd/` ```shy++sho.`/dddddddd:                                                          
+dddddddddddddddo.````:+o+:. `/ddddddddd:                                                          
/dddddddddddddddddo:```````.+hdddddddddd-                                                          
`ddddddddddddddddddddhysyydddddddddddddh                                                           
 +ddddddddddddddddddddddddddddddddddddd:                                                           
 `ydddddddddddddddddddddddddddddddddddo                                                            
  `sdddddddddddddddddddddddddddddddddo`                                                            
   `+ddddddddddddddddddddddddddddddh/                                                              
     -sddddddddddddddddddddddddddho.                                                               
       -ohdddddddddddddddddddddy+.                                                                 
         `:oyhdddddddddddddhy+-`                                                                   
             .-:/+ossso+/:-`
'''
yandere = '''\n
888888 88  88 888888    Yb  dP    db    88b 88 8888b.  888888 88""Yb 888888
  88   88  88 88__       YbdP    dPYb   88Yb88  8I  Yb 88__   88__dP 88__
  88   888888 88""        8P    dP__Yb  88 Y88  8I  dY 88""   88"Yb  88""
  88   88  88 888888     dP    dP""""Yb 88  Y8 8888Y"  888888 88  Yb 888888

'''




class Col:
    colors = {
            "w": "\033[38;2;255;255;255m",
            "r": "\033[38;2;255;0;0m",
            "g": "\033[38;2;0;255;0m",
            "b": "\033[38;2;0;0;255m"
            }

    white = colors['w']
    red = colors['r']
    green = colors['g']
    blue = colors['b']

    

    def error(*args):
        input(Col.red + '\n' + "".join(args) + Col.white)
        return main()


Anime.anime(center(banner, space=60), Colors.blue_to_purple, Fade.Vertical, time=2)

def main():
    if not isdir("Result"):
        mkdir("Result")
    clear()

    clear()

    printf(center(yandere))

    cbox = {"+": "Choose a color"}

    for col in colors:
        cbox[colors.index(col)+1] = col

    colorbox = maketable(cbox, "Colors")

    print()
    
    print(Fade.Diagonal(Colors.purple_to_blue, center(colorbox.table)))
    print()
    
    colorchoice = inputf("-> ")
    colorchoice = int(colorchoice)
    if colorchoice not in range(1, len(colors) + 1):
        return
    color = colors[colorchoice-1]
    clear()
    print(Fade.Horizontal(Colors.blue_to_purple, center(yandere)) + "\n"*3)


    file = inputf("File -> ")


    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
    except OSError:
        return


    test = content.splitlines()
    for a in test:
        if not a.strip():
            test.remove("")

    for l in test:
        if l.strip() and not l.startswith(" " * 4) and ("def" not in l and "import" not in l) or "def" in l and "()" not in l:
            Col.error("Error! The file has to contain only functions (without arguments) and imports.")


    found_functions = content.split("def")
    functions = ["def" + f for f in found_functions if f.strip() and "import" not in f]
    functions_names = [f.strip().split("(")[0] for f in found_functions if f.strip() and "import" not in f]

    if len(functions_names) < 2:
        Col.error("Error! Not enough functions found (min. 2).")

    imports = ["from os import name, system", "from pyfade import Fade, Colors", "from pycenter import center"]
    for i in content.splitlines():
        if "import" in i:
            imports.append(i)


    title = inputf("Title -> ").strip()
    font = inputf("Font (ex: {}, {}, {}) -> ".format(choice(FONT_NAMES), choice(FONT_NAMES), choice(FONT_NAMES)))
    nbanner = text2art(title, font)

    modes = {"+": "Modes"}
    for name, i in zip(functions_names, range(1, len(functions_names) + 1)):
        modes[i] = name.replace("_", " ").strip()
    table = maketable(modes, title).table

    if not nbanner:
        nbanner = yandere

    content = f"""banner = r'''{nbanner}'''\nbox = '''{table}'''"""
    content += rf"""



class Col:
    
    white = "\033[38;2;255;255;255m"
    red = "\033[38;2;255;0;0m"
    green = "\033[38;2;0;255;0m"
    blue = "\033[38;2;0;0;255m"

    def error(text):
        input(Col.red + '\n' + text + Col.white)




def clear():
    system("cls" if name == 'nt' else "clear")

if name == 'nt':
    system("title {title} & mode 160, 40")


def menu():
    clear()
    print(Fade.Vertical(Colors.{color}, center(banner)))
    print("\n\n")
    print(Fade.Vertical(Colors.{color}, center(box)))
    print("\n")

    choice = input("-> ")

    try:
        choice = int(choice)
    except ValueError:
        Col.error("Error! Choice has to be an integer.")
        return menu()

    if choice > {len(functions_names)} or choice <= 0:
        Col.error("Error! Invalid choice.")
        return menu()

    if choice == 1:
        {functions_names[0]}()
        """

    for f in functions_names[1:]:
        content += f"""
    elif choice == {functions_names.index(f) + 1}:
        {f}()
    """

    content += """

    else:
        Col.error("Error! Invalid choice.")
    
    return menu()


menu()

    """



    with open("Result/new.py", 'w', encoding='utf-8') as f:
        f.write("# created with https://github.com/billthegoat356/The-Yandere\n\n# by billythegoat356\n\n# <3\n\n\n")
        for line in imports:
            f.write(line + "\n")
        f.write("\n\n")
        for line in functions:
            f.write(line + "\n")
        f.write("\n")
        f.write(content)


    input(Col.green + "\nDone!" + Col.white)

while True:
    main()
import pyfiglet as figlet
from colorama import Fore, Style

COLOUR_BLACK = 0
COLOUR_RED = 1
COLOUR_GREEN = 2
COLOUR_YELLOW = 3
COLOUR_BLUE = 4
COLOUR_MAGENTA = 5
COLOUR_CYAN = 6
COLOUR_WHITE = 7

A_BOLD = 1
A_NORMAL = 2
A_REVERSE = 3
A_UNDERLINE = 4

# splash_screen = Fore.YELLOW + """ 
# +================================================================================================================================================+
# |                                                                                                                                                |
# |   .----------------.  .-----------------. .----------------.  .----------------.  .----------------.  .----------------.  .----------------.   |
# |  | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |  |
# |  | |██████████████| || |██████████████| || |██████████████| || |██████████████| || |██████████████| || |██████████████| || |██████████████| |  |
# |  | |█████/  \█████| || ||_   \|_   _|█| || |█████/  \█████| || |██.' ___  |███| || |█|_   _ _ \███| || |█████/  \█████| || ||_   \██/   _|| |  |
# |  | |████/ /\ \████| || |██|   \ | |███| || |████/ /\ \████| || |█/ .'███\_|███| || |███| |██) |███| || |████/ /\ \████| || |██|   \/   |██| |  |
# |  | |███/ ____ \███| || |██| |\ \| |███| || |███/ ____ \███| || |█| |██████████| || |███|  __ /████| || |███/ ____ \███| || |██| |\  /| |██| |  |
# |  | |██/ /████\ \██| || |██| |_\   |███| || |██/ /████\ \██| || |█\ `.██]   |██| || |███| |██\ \███| || |██/ /████\ \██| || |██| |█\/█| |██| |  |
# |  | ||____|██|____|| || ||_____|\____|█| || ||____|██|____|| || |██`._____.'███| || |█|____|█|___|█| || ||____|██|____|| || ||_____||_____|| |  |
# |  | |██████████████| || |██████████████| || |██████████████| || |██████████████| || |██████████████| || |██████████████| || |██████████████| |  |
# |  | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |  |
# |   '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'   |
# |                                                                                                                                                |
# |                                                                                                                                                |
# |                                                                                                                                                |
# |                                                           Press Spacebar to continue                                                           |
# |                                                                                                                                                |
# +================================================================================================================================================+
#  """ + Style.RESET_ALL

splash_screen = Fore.YELLOW + """ 
+================================================================================================================================================+
|                                                                                                                                                |
|   .----------------.  .-----------------. .----------------.  .----------------.  .----------------.  .----------------.  .----------------.   |
|  | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |  |
|  | |██████████████| || |██████████████| || |██████████████| || |██████████████| || |██████████████| || |██████████████| || |██████████████| |  |
|  | |█████/  \█████| || ||_   \|_   _|█| || |█████/  \█████| || |██.' ___  |███| || |█|_   _ _ \███| || |█████/  \█████| || ||_   \██/   _|| |  |
|  | |████/ /\ \████| || |██|   \ | |███| || |████/ /\ \████| || |█/ .'███\_|███| || |███| |██) |███| || |████/ /\ \████| || |██|   \/   |██| |  |
|  | |███/ ____ \███| || |██| |\ \| |███| || |███/ ____ \███| || |█| |██████████| || |███|  __ /████| || |███/ ____ \███| || |██| |\  /| |██| |  |
|  | |██/ /████\ \██| || |██| |_\   |███| || |██/ /████\ \██| || |█\ `.██]   |██| || |███| |██\ \███| || |██/ /████\ \██| || |██| |█\/█| |██| |  |
|  | ||____|██|____|| || ||_____|\____|█| || ||____|██|____|| || |██`._____.'███| || |█|____|█|___|█| || ||____|██|____|| || ||_____||_____|| |  |
|  | |██████████████| || |██████████████| || |██████████████| || |██████████████| || |██████████████| || |██████████████| || |██████████████| |  |
|  | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |  |
|   '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'   |
|                                                                                                                                                |
|                                                                                                                                                |
|                                                               Before you proceed,                                                              |
|                                                                                                                                                |
|                                                 Please read the following system requirements:                                                 |
|                                                                                                                                                |
|                                    - Recent version of Python with necessary third-party libraries installed                                   |
|                                                    - Display resolution of 1080p or higher                                                     |
|                                               - Microsoft Visual C++ Build Tools v14 or greater                                                |
|                                                  - FIGlet fonts in fonts-contrib.zip installed                                                 |
|                                                  - Windows 11 with Windows Terminal installed                                                  |
|                                                                                                                                                |
|                                   Before running, ensure that your terminal window is maximized or fullscreen                                  |
|                                        Do not run this from an IDE, such as IDLE, VS Code, PyCharm, etc.                                       |
|                                                        Do not resize the terminal window                                                       |
|                                                                                                                                                |
|                                                                                                                                                |
|                                                           Press Spacebar to continue                                                           |
|                                                                                                                                                |
+================================================================================================================================================+
 """ + Style.RESET_ALL

about_menu = Fore.YELLOW + """
  ____________________________________________________________________________________________________________________________________________________________
 / \----------------------------------------------------------------------------------------------------------------------------------------------------------\ 
 \_,|                                                                                                                                                         | 
    |        .----------------.  .-----------------. .----------------.  .----------------.  .----------------.  .----------------.  .----------------.       | 
    |       | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |      | 
    |       | |██████████████| || |██████████████| || |██████████████| || |██████████████| || |██████████████| || |██████████████| || |██████████████| |      | 
    |       | |█████/  \█████| || ||_   \|_   _|█| || |█████/  \█████| || |██.' ___  |███| || |█|_   _ _ \███| || |█████/  \█████| || ||_   \██/   _|| |      | 
    |       | |████/ /\ \████| || |██|   \ | |███| || |████/ /\ \████| || |█/ .'███\_|███| || |███| |██) |███| || |████/ /\ \████| || |██|   \/   |██| |      | 
    |       | |███/ ____ \███| || |██| |\ \| |███| || |███/ ____ \███| || |█| |██████████| || |███|  __ /████| || |███/ ____ \███| || |██| |\  /| |██| |      | 
    |       | |██/ /████\ \██| || |██| |_\   |███| || |██/ /████\ \██| || |█\ `.██]   |██| || |███| |██\ \███| || |██/ /████\ \██| || |██| |█\/█| |██| |      | 
    |       | ||____|██|____|| || ||_____|\____|█| || ||____|██|____|| || |██`._____.'███| || |█|____|█|___|█| || ||____|██|____|| || ||_____||_____|| |      | 
    |       | |██████████████| || |██████████████| || |██████████████| || |██████████████| || |██████████████| || |██████████████| || |██████████████| |      | 
    |       | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |      | 
    |        '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'       | 
    |                                                                                                                                                         | 
    |                                                                                                                                                         | 
    |                                              an anagram game written in Python for the Windows command-line                                             | 
    |                                                                      v2023.10.19a                                                                       | 
    |                                                                                                                                                         | 
    |                                                                                                                                                         | 
    |                                                                   Created by Group 9                                                                    | 
    |                                                                                                                                                         | 
    |                                                                  Harold Andrei Atillo                                                                   | 
    |                                                                     Design, Testing                                                                     | 
    |                                                                                                                                                         | 
    |                                                                  Teokan Duran Demircan                                                                  | 
    |                                                                   Code, Design, Music                                                                   | 
    |                                                                                                                                                         | 
    |                                                                 Christopher Richard Lua                                                                 | 
    |                                                                   Testing, Debugging                                                                    | 
    |                                                                                                                                                         | 
    |                                                                  Jhazmine Clyze Troyo                                                                   | 
    |                                                                         Design                                                                          | 
    |                                                                                                                                                         | 
    |  ,--------------------------------------------------------------------------------------------------------------------------------------------------------
    \_/_______________________________________________________________________________________________________________________________________________________/ 
""" + "\n"*2 + "Click anywhere to go back" + Style.RESET_ALL

# difficulty_menu = "\n".join([
#     Fore.YELLOW + Style.BRIGHT,
#     figlet.figlet_format("CHOOSE DIFFICULTY", font="ansi_regular", width=300),
#     Fore.GREEN,
#     figlet.figlet_format("EASY", font="standard", width=300) + Style.RESET_ALL + Style.BRIGHT + Fore.YELLOW,
#     figlet.figlet_format("MEDIUM", font="standard", width=300) + Fore.RED,
#     figlet.figlet_format("HARD", font="standard", width=300) + Style.RESET_ALL + Style.BRIGHT + Fore.YELLOW,
#     figlet.figlet_format("BACK", font="standard", width=300),
#     Style.RESET_ALL
# ])

difficulty_menu = "\n".join([
    figlet.figlet_format("CHOOSE DIFFICULTY", font="ansi_regular", width=300),
    figlet.figlet_format("EASY", font="standard", width=300),
    figlet.figlet_format("MEDIUM", font="standard", width=300),
    figlet.figlet_format("HARD", font="standard", width=300),
    figlet.figlet_format("BACK", font="standard", width=300)
])

options_menu = "\n".join([
    figlet.figlet_format("OPTIONS", font="ansi_regular", width=300),
    figlet.figlet_format("MUTE", font="standard", width=300),
    figlet.figlet_format("REAL ANAGRAM", font="standard", width=300),
    figlet.figlet_format("FLICKER", font="standard", width=300),
    figlet.figlet_format("NON-EMOJI", font="standard", width=300),
    # figlet.figlet_format("HARD", font="standard", width=300),
    figlet.figlet_format("BACK", font="standard", width=300)
])



# List of fonts

# slant
# colossal
# standard
# blocks - main menu
# bloody - loss menu
# dos_rebel - win menu

main_menu = "\n".join([
    Fore.YELLOW,
    figlet.figlet_format("ANAGRAM", font="blocks", width=300),
    # figlet.figlet_format("aceinnoorstv".upper(), font="blocks", width=300),
    Style.BRIGHT,
    figlet.figlet_format("START", font="standard", width=300),
    figlet.figlet_format("OPTIONS", font="standard", width=300),
    figlet.figlet_format("HIGH  SCORES", font="standard", width=300),
    figlet.figlet_format("ABOUT", font="standard", width=300),
    figlet.figlet_format("EXIT", font="standard", width=300),
    Style.RESET_ALL
])

# loss_menu = "\n".join([
#     Fore.RED + Style.BRIGHT,
#     figlet.figlet_format("Y O U  L O S E", font="bloody", width=300),
#     Style.RESET_ALL
# ])

loss_menu = figlet.figlet_format("Y O U  L O S E", font="bloody", width=300)

win_menu = "\n".join([
    Fore.YELLOW + Style.BRIGHT,
    figlet.figlet_format("Y O U   W I N ! ! !", font="dos_rebel", width=300),
    Style.RESET_ALL
])

# print(main_menu)
# print(loss_menu)
# print(win_menu)

# print(difficulty_menu)
# print(options_menu)

# game_buttons = {
#     "main_menu": """ ┌─────────────────┐
#  │                 │
#  │    Main Menu    │
#  │                 │
#  └─────────────────┘"""
# }

def figlet_printer(text, font="standard", width=300):
    return figlet.figlet_format(text, font=font, width=width)

game_buttons = {
    "main_menu": """ ┌─────────────┐
 │  Main Menu  │
 └─────────────┘""",
    "hint_button": """ ┌────────┐
 │  Hint  │
 └────────┘"""
}



# ╔════════════════════════════╗
# ║                            ║
# ║                            ║
# ║                            ║
# ║                            ║
# ╚════════════════════════════╝

insults = [
    (0, "Imbecile."),
    (1, "Dumb as a rock."),
    (2, "Worse than a quadriplegic sloth."),
    (3, "Worse than a typing monkey."),
    (5, "Worse than a pre-schooler."),
    (10, "Git gud."),
    (15, "Guess harder."),
    (20, "Passable."),
    (30, "Loves stalling for time."),
    (50, "Pretty good."),
    (300, "Armed with the power of a hundred typing monkeys."),
    (1000, "Gong armada."),
    (9999, "Get a life, bot.")
]

fire = figlet.figlet_format("HIGH SCORES", font="ansi_regular", width=300) + """                                                 
                ▒▒                                          ▒▒                                            ▒▒                 
                ▓▓                                          ▓▓                                            ▓▓                 
                ▓▓▓▓                                        ▓▓▓▓                                          ▓▓▓▓               
                ████                                        ████                                          ████               
              ░░████                                      ░░████                                        ░░████               
              ██▓▓██                                      ██▓▓██                                        ██▓▓██               
        ░░  ████▓▓▓▓    ▒▒                          ░░  ████▓▓▓▓    ▒▒                            ░░  ████▓▓▓▓    ▒▒         
        ▓▓▒▒▓▓██▒▒▓▓  ██░░                          ▓▓▒▒▓▓██▒▒▓▓  ██░░                            ▓▓▒▒▓▓██▒▒▓▓  ██░░         
      ▓▓██████▒▒▓▓▒▒████  ▒▒                      ▓▓██████▒▒▓▓▒▒████  ▒▒                        ▓▓██████▒▒▓▓▒▒████  ▒▒       
      ██████▒▒▒▒▓▓▒▒██▒▒  ██                      ██████▒▒▒▒▓▓▒▒██▒▒  ██                        ██████▒▒▒▒▓▓▒▒██▒▒  ██       
      ██▓▓▓▓░░▒▒████▓▓░░▒▒██  ░░                  ██▓▓▓▓░░▒▒████▓▓░░▒▒██  ░░                    ██▓▓▓▓░░▒▒████▓▓░░▒▒██  ░░   
      ██▒▒▒▒░░▒▒▓▓██▓▓▓▓████▓▓░░                  ██▒▒▒▒░░▒▒▓▓██▓▓▓▓████▓▓░░                    ██▒▒▒▒░░▒▒▓▓██▓▓▓▓████▓▓░░   
      ██▒▒▒▒░░▒▒████▓▓██▓▓████░░                  ██▒▒▒▒░░▒▒████▓▓██▓▓████░░                    ██▒▒▒▒░░▒▒████▓▓██▓▓████░░  
      ██▒▒░░░░▒▒▓▓██▒▒██▒▒██▓▓░░                  ██▒▒░░░░▒▒▓▓██▒▒██▒▒██▓▓░░                    ██▒▒░░░░▒▒▓▓██▒▒██▒▒██▓▓░░  
  ░░  ▒▒▒▒░░░░░░▒▒██░░▒▒▒▒▓▓██                ░░  ▒▒▒▒░░░░░░▒▒██░░▒▒▒▒▓▓██                  ░░  ▒▒▒▒░░░░░░▒▒██░░▒▒▒▒▓▓██    
    ██▓▓▓▓░░  ░░▒▒▒▒░░░░▒▒▓▓▓▓                  ██▓▓▓▓░░  ░░▒▒▒▒░░░░▒▒▓▓▓▓                    ██▓▓▓▓░░  ░░▒▒▒▒░░░░▒▒▓▓▓▓    
    ░░██▓▓▒▒░░  ░░░░░░░░░░▓▓░░                  ░░██▓▓▒▒░░  ░░░░░░░░░░▓▓░░                    ░░██▓▓▒▒░░  ░░░░░░░░░░▓▓░░    
      ░░▓▓░░░░        ░░▒▒░░                      ░░▓▓░░░░        ░░▒▒░░                        ░░▓▓░░░░        ░░▒▒░░      
          ░░▒▒░░      ░░                              ░░▒▒░░      ░░                                ░░▒▒░░      ░░          
"""

# print(figlet.figlet_format("Easy     Medium Hard", font="speed", width=300))
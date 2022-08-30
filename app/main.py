from colorama import Fore

from controller import Controller
from view import Display

if __name__ == "__main__":
    print(f"{Fore.LIGHTBLUE_EX} Bienvenue sur le gestionnaire d'échecs")
    while Controller.accueil(Display) is not False:
        Controller.accueil(Display)

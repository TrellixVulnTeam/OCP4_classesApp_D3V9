from colorama import Fore

from models.player import Player
from validation import Validators
from view import Display
from views.player import PlayerView


class Controller_player:
    def __init__(self):
        self.display = Display
        self.plyer_v = PlayerView

    def show_sorted_players():
        sort_key = PlayerView.get_input(
            f"{Fore.CYAN} 1 : Pour trier par l'ordre alphabétique\n 2 : pour trier par classement\n "
        )
        while int(sort_key) not in [1, 2]:
            sort_key = PlayerView.get_input(
                f"{Fore.CYAN} 1 : Pour trier par l'ordre alphabétique\n 2 : pour trier par classement\n "
            )
        players_list = Player.show_sorted_players(int(sort_key))
        if players_list:
            return PlayerView.showAllViewPlayers(players_list)

    def create_player():

        first_name = PlayerView.get_input(f"{Fore.CYAN} Entrez le prènom : ")
        while not Validators.is_valide_input_string(first_name):
            first_name = PlayerView.get_input(f"{Fore.CYAN} Entrez le prènom : ")
        last_name = PlayerView.get_input(f"{Fore.CYAN} Entrez le nom : ")
        while not Validators.is_valide_input_string(last_name):
            last_name = PlayerView.get_input(f"{Fore.CYAN} Entrez le nom : ")

        gender = PlayerView.get_input(
            f"{Fore.CYAN} Entrez genre choiser dans cette liste 'M' Masculain, 'F' Femme, 'O' Autre ?"
        )
        while not Validators.is_valide_input_gender(gender):
            gender = PlayerView.get_input(
                f"{Fore.CYAN} Entrez genre choiser dans cette liste 'M' Masculain, 'F' Femme, 'O' Autre ?"
            )

        date_of_birth = PlayerView.get_input(
            f"{Fore.CYAN}Entrez la date de naissance : "
        )
        while not Validators.is_date_valide(date_of_birth):
            date_of_birth = PlayerView.get_input(
                f"{Fore.CYAN}Entrez la date de naissance : "
            )

        classement = int(PlayerView.get_input(f"{Fore.CYAN} Entrez le Classemnt ? "))
        while not Validators.is_valide_classement(classement):
            classement = PlayerView.get_input(f"{Fore.CYAN} Entrez le Classemnt ? ")

        player = Player(first_name, last_name, gender, date_of_birth, classement)
        # print(player)
        # print((first_name, last_name, gender, date_of_birth, classement))
        return player.create_player()

    def updateOnePlayer():
        player_new_data_update = {}
        id = PlayerView.updateOnePlayer()
        classement = PlayerView.player_new_data()
        player_new_data_update.update({"id": id, "classement": classement})
        return Player.updateOnePlayer(player_new_data_update)

    def manage_players():
        menu = {
            "1": "Créer un joueur",
            "2": "Lister les joueurs",
            "3": "Modifier un joueur",
            "R": "Reveneir à l'accueil",
        }

        Display.render_menu(menu)
        response = Display.get_user_input(menu)
        if response == "1":
            Controller_player.create_player()
        elif response == "2":
            Controller_player.show_sorted_players()
        elif response == "3":
            Controller_player.updateOnePlayer()
        elif response == "R":
            Display.render_menu(menu)
        else:
            print("-")

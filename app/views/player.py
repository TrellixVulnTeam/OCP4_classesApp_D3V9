from colorama import Fore
from prettytable import PrettyTable

from validation import Validators


class PlayerView:
    def showAllViewPlayers(list):

        print(f"\n{Fore.LIGHTBLUE_EX} Il y a {len(list)} joueurs \n")

        players_table = PrettyTable()
        players_table.field_names = [
            "Prènom",
            "Nom",
            "Date de naissance",
            "Genre",
            "Classement",
        ]
        for player in list:
            players_table.add_row(
                [
                    player["first_name"],
                    player["last_name"],
                    player["date_of_birth"],
                    player["gender"],
                    player["classement"],
                ]
            )
            players_table.add_row(
                [
                    f"{Fore.LIGHTBLUE_EX}------",
                    f"{Fore.LIGHTBLUE_EX}------",
                    f"{Fore.LIGHTBLUE_EX}------",
                    f"{Fore.LIGHTBLUE_EX}------",
                    f"{Fore.LIGHTBLUE_EX}------",
                ]
            )
        print(players_table)

    def get_input(message):
        return input(message)

    def updateOnePlayer():
        player_id = input("Entrez l'id de joueur à modifier : ")
        return player_id

    def player_new_data():
        classement = int(input("Entrez le Classemnt ? "))
        while not Validators.is_valide_classement(classement):
            classement = int(input(f"{Fore.CYAN} Entrez le Classemnt ? "))
        return classement

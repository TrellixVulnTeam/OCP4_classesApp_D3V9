from models.tournament import Tournament
from models.round import Round
from view import Display
from views.tournament import TournamentView
from validation import Validators
from colorama import Fore


# class Round:
#     def __init__(self, matchs):
#         self.matchs = matchs


class Controller_tournament:
    def __init__(self):
        self.display = Display

    def set_results(round):
        for index, match in enumerate(round):
            print("match", index + 1)
            print(match[0], "VS", match[1])
        tournament = Tournament
        tournament.next_round()
        tournament.save()

    def showAllTournaments():
        tournaments = Tournament.load_tournaments_db()
        return TournamentView.showAllViewTournaments(tournaments)

    def show_tournament_players():
        sort_data_as_dict = TournamentView.get_data_to_sort_with()
        ps = Tournament.showAllTournamentPlayers(sort_data_as_dict)
        return TournamentView.showAllTournamentPlayers(ps)

    def get_rounds_in_tournaments():
        id = TournamentView.get_rounds_in_tournament()
        rounds_in_tournament = Tournament.get_rounds_in_tournament(id)
        return TournamentView.showRoundsInTournament(rounds_in_tournament)

    def get_matchs_in_tournaments():
        id = TournamentView.get_matchs_in_tournaments()
        """ use same get_rounds_in_tournament function to get data"""
        matchs_in_tournament = Tournament.get_rounds_in_tournament(id)
        return TournamentView.showMatchsInTournament(matchs_in_tournament)

    def create_tournament():

        name = TournamentView.get_input(f"{Fore.CYAN} Entrez le nom de tournois : ")
        while not Validators.is_valide_input_string(str(name)):
            name = TournamentView.get_input(f"{Fore.CYAN} Entrez le nom de tournois : ")

        location = TournamentView.get_input(
            f"{Fore.CYAN} Entrez le lieu de tournois : "
        )
        while not Validators.is_valide_input_string(str(location)):
            location = TournamentView.get_input(
                f"{Fore.CYAN} Entrez le lieu de tournois : "
            )

        start_at = TournamentView.get_input(
            f"{Fore.CYAN} Entrez la date début de tournois : "
        )
        while not Validators.is_date_valide(start_at):
            start_at = TournamentView.get_input(
                f"{Fore.CYAN} Entrez la date début de tournois : "
            )

        end_at = TournamentView.get_input(
            f"{Fore.CYAN} Entrez la le date fin de tournois : "
        )
        while not Validators.is_date_valide(end_at):
            end_at = TournamentView.get_input(
                f"{Fore.CYAN} Entrez la le date fin de tournois : "
            )
        time_control = 0
        round = 0

        players_str = TournamentView.get_input(
            f"{Fore.CYAN} Entrez les players utiliser un virgul pour separer ex [1, 2]: "
        )
        while not Validators.is_valide_input_string(players_str):
            players_str = TournamentView.get_input(
                f"{Fore.CYAN} Entrez les players utiliser un virgul pour separer ex [1, 2]: "
            )
        players_in_list = players_str.split(",")
        players = [int(p) for p in players_in_list]
        rounds = []
        round_total = 4

        description = TournamentView.get_input(f"{Fore.CYAN} Entrez la description : ")
        while not Validators.is_valide_input_string(str(description)):
            description = TournamentView.get_input(
                f"{Fore.CYAN} Entrez la description : "
            )

        tournament = Tournament(
            name,
            location,
            start_at,
            end_at,
            time_control,
            round,
            players,
            rounds,
            round_total,
            description,
        )

        return tournament.create_tournament()

    def update_tournament():
        tournament_new_data_update = {}
        id = TournamentView.updateOneTournamen()
        tournament_as_dict = TournamentView.tournament_new_data()
        tournament_new_data_update.update({"id": id})
        tournament_new_data_update.update(tournament_as_dict)
        return Tournament.updateOneTournamen(tournament_new_data_update)

    def addPlayersToTournaments():
        print("Players ADDED To Tournaments")
        id = TournamentView.addPlayersToTournaments()
        return Tournament.get_one_tournament(id)

    """
    Display rounds in the tournament
    """

    def get_tournament_players():
        id = TournamentView.get_tournament_players()
        return Tournament.get_tournament_players(id)

    def insert_tournament_result():
        id = TournamentView.get_tournament_players()
        return Tournament.insert_tournament_result(id)

    def insert_player_score(player):
        score = float(
            TournamentView.get_input(
                f"{Fore.CYAN} Entrez le score pour le joueur {player} : "
            )
        )
        while score not in [0, 1, 5.0]:
            score = float(
                TournamentView.get_input(
                    f"{Fore.CYAN} Entrez le score pour le joueur {player} :"
                )
            )
        return Round.insert_player_score(score)

    def manage_tournaments():
        menu = {
            "1": "Créer un nouveau tournoi",
            "2": "Lister les joueurs de tournoi",
            "3": "Saisir les resultats d'un tournoi",
            "4": "Liste des tournois",
            "5": "Modifier un tournoi",
            "6": "Afficher les rounds d'un tournoi",
            "R": "Reveneir à l'accueil",
        }

        Display.render_menu(menu)
        response = Display.get_user_input(menu)
        if response == "1":
            print("Créer un tournoi")
            Controller_tournament.create_tournament()
        elif response == "2":
            print("Lister les joueurs de tornoi")
            Controller_tournament.show_tournament_players()
        elif response == "3":
            players = []
            for i in range(8):
                print(f"Veuillez ajouter votre {i} jour")
                players.append(i)
            Controller_tournament.addPlayersToTournaments(players)
        elif response == "4":
            print("Liste des tournois")
            Controller_tournament.showAllTournaments()
        elif response == "5":
            Controller_tournament.update_tournament()
        elif response == "6":
            Controller_tournament.get_rounds_in_tournaments()
        elif response == "R":
            print("Reveneir à l'accueil")
            print("\n")
        else:
            print("-")

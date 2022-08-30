from models.tournament import Tournament
from view import Display
from views.tournament import TournamentView
from controllers.player import Controller_player
from controllers.tournament import Controller_tournament


class Round:
    def __init__(self, matchs):
        self.matchs = matchs


class Controller_reports:
    def __init__(self):
        self.display = Display

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

    def get_tournament_players():
        id = TournamentView.get_tournament_players()
        return Tournament.get_tournament_players(id)

    def manage_reports():
        menu = {
            "1": "Liste de tous les acteurs",
            "2": "Liste de tous les joueurs d'un tournoi",
            "3": "Liste de tous les tournois",
            "4": "Liste de tous les tours d'un tournoi",
            "5": "Liste de tous les matchs d'un tournoi",
            "R": "Reveneir à l'accueil",
        }

        Display.render_menu(menu)
        response = Display.get_user_input(menu)
        if response == "1":
            Controller_player.show_sorted_players()
        if response == "2":
            Controller_tournament.show_tournament_players()
        elif response == "3":
            Controller_tournament.showAllTournaments()
        elif response == "4":
            Controller_tournament.get_rounds_in_tournaments()
        elif response == "5":
            Controller_tournament.get_matchs_in_tournaments()
        elif response == "R":
            print("Reveneir à l'accueil")
            print("\n")
        else:
            print("-")

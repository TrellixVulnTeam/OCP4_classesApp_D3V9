from views.round import RoundView
from validation import Validators
from colorama import Fore


class Controller_round:
    def __init__(self, matches, score):
        self.matches = matches
        self.score = score

    def insert_player_score(player):
        score = RoundView.get_input(
            f"{Fore.CYAN} Entrez le score pour le joueur {player} : "
        )
        while not Validators.check_is_digit(score):
            score = RoundView.get_input(
                f"{Fore.CYAN} Entrez le score pour le joueur {player} : "
            )
        while not score not in [0, 1, 5.0]:
            score = float(
                RoundView.get_input(
                    f"{Fore.CYAN} Entrez le score pour le joueur {player} :"
                )
            )
        return float(score)

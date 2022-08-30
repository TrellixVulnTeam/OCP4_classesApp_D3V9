from datetime import datetime

from colorama import Fore


class Validators:
    def is_date_valide(date_text):
        try:
            datetime.strptime(date_text, "%d/%m/%Y")
        except ValueError:
            raise ValueError("Il s'agit du format de chaîne de date incorrect veuillez réessayer avec ce format DD/MM/YYYY")

    def is_valide_input_string(stie: str):
        if len(stie) > 5:
            print(f"len(stie) len(stie) {len(stie)}")
            return True
        else:
            print(f"{Fore.RED} {stie} DOIT être un chaîne de caractères et 4 caractères minimum")
            

    def is_valide_input_gender(gender: str):
        try:
            if gender.upper() in ("F", "M", "O"):
                print(Fore.RED + "le genre doit être entre 'F', 'M' ou 'O")
                return True
            else:
                return False
        except ValueError:
            print(f"{gender} ne doit pas être vide")
            raise ValueError(f"{gender} ne doit pas être vide")

    def is_valide_classement(classement: int):
        try:
            if classement > 2000:
                print(f"{Fore.RED} + {classement} EST 2000 MAX")
                return False
            elif classement < 0:
                return False
            else:
                return True
        except ValueError:
            raise ValueError(f"{classement} ne doit pas être vide")

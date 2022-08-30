# OCP4_chessApp

# To get this project:
### 1. Download a zip  
### 2. Clone project:
 ###### A. Via git Https:  git clone https://github.com/motaALI/OCP4_classesApp.git
 ###### B. Via ssh git@github.com:motaALI/OCP4_classesApp.git

# In the project dir:

# Install the virtualenv package
pip install virtualenv

# Create the virtual environment
virtualenv <your_env_Name>

# Activate the virtual environment
1.Mac OS / Linux source your_env_Name/bin/activate

2.Windows your_env_Name\Scripts\activate

# Install requirement.txt
pip install -r .\requirements.txt

# Run the classesApp:
1. cd ./app
2. python .\main.py
3. Then select your options from each list or sublist of the application\
 Bienvenue sur le gestionnaire d'échecs\
  1 - Gestion des joueurs\
  2 - Gestion des tournois\
  3 - Rapports\
  q - Quitter
  Veuillez choisir une action :
  
  ### Gestion des joueurs Menu
    1 - Créer un joueur
    2 - Lister les joueurs
    3 - Modifier un joueur
    R - Reveneir à l'accueil
  Veuillez choisir une action : 
 
  ### Gestion des tournois
   1 - Créer un nouveau tournoi\
   2 - Lister les joueurs de tournoi\
   3 - Saisir les resultats d'un tournoi\
   4 - Liste des tournois\
   5 - Modifier un tournoi\
   6 - Afficher les rounds d'un tournoi\
   R - Reveneir à l'accueil\
  Veuillez choisir une action :
  
  ### Rapports
  1 - Liste de tous les acteurs\
  2 - Liste de tous les joueurs d'un tournoi\
  3 - Liste de tous les tournois\
  4 - Liste de tous les tours d'un tournoi\
  5 - Liste de tous les matchs d'un tournoi\
  R - Reveneir à l'accueil\
Veuillez choisir une action :

 # Run flake8
 flake8 --format=html --htmldir=flake-report
  
  

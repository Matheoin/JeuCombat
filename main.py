import os
from pymongo import MongoClient
from game import Game
from utils import clear_screen, get_choice_input, get_pseudo_input

# ---------- ALGORITHME ---------- 
# MENU = [
#   lambda: play(),
#   "Classements",
#   "Quitter"
# ]
# Menu
#   Afficher le menu
#       Boucle sur tout élément de MENU
#           Afficher numéro élément et texte élément
# Choix (options, erreur)
#   while True:
#       Récupérer le choix de l'utilisateur
#       Vérifier si le choix est valide
#       Si valide
#           return choix
#       sinon
#           Lancer fonction erreur
# Process 
#   Jeu 
#       Création joueur
#       Création équipe
#       Combat
#       Création scores
#   Classement
#       Afficher les scores
#           Récupérer les scores base
#               Ouvrir la base
#               Accéder à la collection score
#               find
#               Convertir curseur en list
#           Filtrer les 3 meilleurs
#               Trie le tableau sur element.waves
#               Prendre les 3 derniers éléments
#                   array[-3:-1]
#           Afficher les scores 
#   Quitter 
#       sys.exit()

MONGO_URL = os.environ.get("MONGO_URL", "mongodb://localhost:27017")
DB_NAME = "game_db"

MENU = [
    lambda: play(),
    "Classements",
    "Quitter"
]

def menu():
    print("============ JeuCombat ============")
    print("1. Nouvelle Partie")
    print("2. Classement")
    print("3. Quitter")
     

    choice = get_choice_input("Choisissez une option (1-3) : ", 1, 3)
    MENU[choice -1]()

def play():
    client = MongoClient(MONGO_URL)
    game = Game(client, DB_NAME)

    clear_screen()
    print("==== Nouvelle Partie ====")

    name = get_pseudo_input()
    # création joueur
    game.player_name = name

    # création équipe
    game.create_team()



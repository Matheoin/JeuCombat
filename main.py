from utils.py import clear_screen, get_choice_input, get_pseudo_input

# MENU = [
#   "Lancer Jeu",
#   "Afficher les scores",
#   "Quitter"
# ] 
# Afficher le menu
#   Boucle sur tout élément de MENU
#       Afficher numéro élément et texte élément
# Choix (options, erreur)
#   while True:
#       Récupérer le choix de l'utilisateur
#       Vérifier si le choix est valide
#       Si valide
#           return choix
#       sinon
#           Lancer fonction erreur
# Process
#   Si choix == 1 valide
#       Lancer la partie
#           Pseudo (erreur)
#               while True:
#                   Récupérer le pseudo de l'utilisateur
#                   Vérifier si le pseudo est valide
#                   Si valide
#                       return pseudo
#                   Sinon
#                       Lancer fonction erreur
#           Création de l'équipe
#               while len(team) < 3:
#                   Afficher les héros disponible
#                       Récupérer les héros dans la base de données
#                           Ouvrir la base de données
#                           Accéder à la collection heros
#                           Boucle sur tout élément de la collection heros
#                               Afficher numéro élément, name élément, attack élément, defense élément et heath élément
#                   Afficher l'équipe actuel de l'utilisateur
#                       Boucle sur tout élément de team
#                           Afficher numéro élément, name élément, attack élément, defense élément, et health élément
#                   Choix (options, erreur)
#                       while True:
#                           Récupérer le choix de l'utilisateur
#                           Vérifier si le choix est valide
#                           Si valide
#                               Retirer le héro choisi de l'affichage des héros disponible
#                                   available_heros.pop(choix - 1)
#                               Ajouter le héro choisi à notre équipe
#                                   team.append(choix)
#                           Sinon
#                               Lancer fonction erreur   
#   Sinon si choix == 2 valide
#       Afficher les scores
#           Récupérer les scores dans la base de données
#               Ouvrir la base de données
#               Accéder à la collection scores
#               find
#               Convertir le curseur en liste
#           Filtrer les 3 meilleurs
#               Trie le tableau sur element.waves
#               Prendre les 3 derniers éléments de mon tableau 
#                   array[-3:-1]
#           Afficher les scores
#   Sinon si choix == 3 valide
#       Quitter
#           sys.exit() 
#   Sinon
#       Lancer fonction erreur

MENU = [
    "Lancer jeu",
    "Afiicher scores",
    "Quitter"
]

def menu():
    print("============ JeuCombat ============")
    print("1. Démarrer une nouvelle partie")
    print("2.Voire les meilleurs scores")
    print("3. Quitter")

    choice = get_choice_input("Choisissez une option (1-3) : ", 1, 3)

    if choice == 1:
        play()

def play():
    clear_screen()
    print("==== Nouvelle Partie ====")

    player_name = get_pseudo_input()


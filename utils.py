import os

# ALLGO : 
# Fonction clear_screen pour vidée l'écran d'affichage
# Fonction get_valid_input pour récupérer le choix de l'utilisateur

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def get_choice_input(prompt: str, min: int, max: int):
    choice = int(input(prompt))
    while True:
        try:
            if min <= choice <= max:
                return choice
            print(f"Veuillez entrer un nombre entre {min} et {max}.")
        except ValueError:
            print(f"Veuillez entrer un nombre valide.")

def get_pseudo_input():
    name = input("Entrez votre nom (3-20 caractères) : ")
    while True:
        if 3 <= len(name) <= 20:
            return name
        print("Le nom doit contenir entre 3 et 20 caractères.")


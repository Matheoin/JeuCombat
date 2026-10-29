import random
from pymongo import MongoClient
from models import Character, Monster
from typing import List
from utils import get_choice

# ---------- ALGORITHME ---------- 
# Game
#   Initialisation
#   Charger_héros
#       Récupérer les héros dans la base
#           Ouvrir la base
#           Accéder à la collection heros
#           find
#           Convertir le curseur en list
#   Générer_monsters
#       Tiré un monstre au hasard depuis la base
#           Récupérer les monsters dans la base
#               Ouvrir la base
#               Accéder à la collection monsters
#               find
#               Convertir curseur en list
#           Générer un nombre entre 0 et le nombre de monstres
#           Filtrer les monsters
#               Trie le tableau sur élément.id
#               Prendre le monstre
#           Afficher le monstre
#               Boucle sur tout élément de monstre
#                   Afficher name élément, attack élément, defense élément, health élément, health_max élément
#   Création_équipe
#       Afficher les héros disponible
#           Récupérer les héros dans la base
#               Ouvrir la base
#               Accéder à la collection heros
#               find
#               Convertir curseur en list
#       while len(equipe)<3:
#           Choix (options, erreur)
#               while True:
#                   Récupérer le choix de l'utilisateur
#                   Vérifier si le choix est valide
#                   Si valide
#                       Ajoute le héro selectionner à la list équipe
#                       Retire le héro selectionner de la list des héros disponible
#                   Sinon
#                       Lancer la fonction erreur
#           Afficher équipe
#               Boucle sur tout élément de équipe
#                   Afficher héro
#                       Boucle sur tout élément de héro
#                           Afficher name élément, attack élément, defense élément, health élément, health_max élément
#   Combat_tour
#       Attaque_équipe_héros
#           Boucle sur tout élément de équipe_héros
#               Héro_vivant
#                   Récupérer les PV du héro
#                   Vérifier si héro_vivant est valide
#                   Si valide
#                       Récupérer l'attack du héro
#                       Récupérer la defense du monstre
#                       Calculer les dégats en fonction de l'attack et la defense
#                           damage = hero.attack - monstre.defense
#                       Récupérer les PV du monstre
#                       Réduit les PV du monstre en fonction des dégâts subit
#                           monstre.PV - damage
#                       Monstre_vivant
#                           Vérifier si monstre_vivant est valide
#                           Si valide
#                               continue
#                           Sinon
#                               Incrémente le compteur de vagues de 1
#                               Lance une nouvelle vague avec un monstre aléatoire
#       Attaque_monstre
#           Choisi aléatoirement un héro vivant parmis équipe_héros
#           Récupérer l'attack du monstre
#           Récupérer la defense du héro
#           Calculer les dégâts en fonction de l'attack et le defense
#               damage = monstre.attack - hero.defense
#           Récupérer les PV du héro
#           Réduit les PV du héro en fonction des dégâts subit
#               monstre.PV - damage
#           Equipe_vivant
#               Vérifier si équipe_vivant est valide
#               Si valide
#                   continue
#               Sinon
#                   Save_scores (player_name, waves)
#                   Afficher son score
#                   Afficher les scores
#                       Récupérer les scores base
#                           Ouvrir la base
#                           Accéder à la collection score
#                           find
#                           Convertir curseur en list
#                       Filtrer les 3 meilleurs
#                           Trie le tableau sur element.waves
#                           Prendre les 3 derniers éléments
#                               array[-3:-1]
#                       Afficher les scores 
#   Monstre_vivant
#       Récupérer les PV du monstre
#       Vérifier si le monstre_vivant est valide
#       Si PV > 0 valide
#           return True
#       sinon
#           return False
#   Héro_vivant
#       Récupérer les PV du héro
#       Vérifier si héro_vivant est valide
#       Si PV > 0 valide
#           return True
#       Sinon
#           return False
#   Equipe_vivant
#       Boucle sur tout élément de équipe_héros
#           Héro_vivant
#               Récupérer les PV du héro
#               Vérifier si héro_vivant est valide
#               Si valide 
#                   return True
#       return False
#   Save_score 
#       Récupérer player_name
#       Récupérer waves
#       Ouvrir la base
#       Accéder à la collection scores
#       Ajouter le score dans la collection scores



class Game: 
    def __init__(self, mongo_client: MongoClient, db_name: str = "game_db"):
        self.db = mongo_client[db_name]
        self.player_name = ""
        self.team: List[Character] = []
        self.waves = 1

    def charger_heros(self):
        heros_data = list(self.db["heros"].find())
        return [Character.from_dict(hero) for hero in heros_data]
        #heros_list = []
        #heros_collection = self.db["heros"]
        #for hero in heros_collection.find():
        #    heros_list.append(hero)
        #return heros_list
            
    def monstre_aleatoire(self):
        monstres_data = list(self.db["monsters"].find())
        monstre = random.choice(monstres_data)
        return Monster.from_dict(monstre)

    def creer_equipe(self):
        heros_disponible = self.charger_heros()
        self.team = []

        while len(self.team) < 3:
            print("\nHéros disponible :")
            for i, hero in enumerate(heros_disponible, 1):
                print(f"{i}. {hero.name} - {hero.attack} ATK - {hero.defense} DEF - {hero.health} PV")
            print("\n\nVotre équipe :")
            for i, hero in enumerate(self.team, 1):
                print(f"{i}. {hero.name} - {hero.attack} ATK - {hero.defense} DEF - {hero.health} PV")
            choice = get_choice("\nChoisissez un héro parmis ceux disponible : ", 1, 10)
            select = heros_disponible.pop(choice - 1)
            self.team.append(select)
            print(f"\n{select.name} à rejoint votre équipe !")

    def combat(self, monstre: Monster):
        # Tour héros
        for hero in self.team:
            if hero.is_alive() and monstre.is_alive():
                damage = hero.attack - monstre.defense
                monstre.health = monstre.health - damage

        if not monstre.is_alive():
            return True
        
        # Tour monstre
        heros_vivant = [hero for hero in self.team if hero.is_alive()]
        if heros_vivant:
            cible = random.choice(heros_vivant)
            damage = monstre.attack - cible.defense
            cible.health = cible.health - damage

        return any(hero.is_alive() for hero in self.team)

    def equipe_vivant(self):
        return any(hero.is_alive() for hero in self.team)

    #def save_score(self):


    #def get_top_score(self, limit: int = 3):




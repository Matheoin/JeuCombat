from pymongo import MongoClient
from models import Character, Monster, score
from typing import List
from utils import get_choice_input

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
        self.team: List[Character] = []
        self.waves = 1
        self.player_name = ""

    def load_heros(self):
        heros_data = list(self.db.characters.find())
        return [Character.from_dict(char) for char in heros_data]
    
#    def get_random_monsters():

    def create_team(self):
        heros_available = self.load_heros()
        self.team = []

        while len(self.team) < 3:
            for i, char in enumerate(heros_available, 1):
                print(f"{i}. {char}")

            choice = get_choice_input(f"Choisissez un personnage", 1, len(heros_available))
            selected = heros_available.pop(choice -1)
            self.team.append(selected)

    def turn_combat(self, monster: Monster):
        for hero in self.team:
            if hero.is_alive() and monster.is_alive():
                damage = monster.take_damage(hero.attack)
                animate_combat(f"{hero.name} attaque {monster.name}")
                print(f"{hero.name} inflige {damage} points de dégâts à {monster.name}")
        
        if not monster.is_alive():
            return True

        heros_alive = [char for char in self.team if char.is_alive()]
        if heros_alive:
            target = random.choice(heros_alive)
            damage = target.take_damage(monster.attack)
            animate_combat(f"{monster.name} inflige {damage} points de dégâts à {target.name}")

        return any(char.is_alive() for char in self.team)

    def save_score(self):
        score = Score(player_name = self.player_name, waves = self.wave - 1)
        self.db.scores.insert_one(score.to_dict())

    def get_top_score(self, limit: int = 3):
        score_data = self.db.scores.find().sort("waves", -1).limit(limit)
        return [Score.from_dict(score) for score in score_data]




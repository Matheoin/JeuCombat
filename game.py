from pymongo import MongoClient
from models import Character, Monster, score
from typing import List
from utils import get_choice_input

# ---------- ALGORITHME ---------- 
# Game
#   Initialisation
#   Charger héros
#   Générer monsters
#   Création équipe
#   Combat automatisée
#   Stocker score



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

#    def auto_combat():

#    def save_score():




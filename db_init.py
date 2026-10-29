import os
from pymongo import MongoClient

# ALGO : 
# Configuration MongoDB
# Sélection de la collection monsters
# Données initiales MONSTERS
# Insertion multiples des données initiales MONSTERS dans la collection monsters
# Sélection de la collection heros
# Données initiales HEROS
# Insertion multiples des données initiales HEROS dans la collection heros

MONGO_URL = os.environ.get("MONGO_URL", "mongodb://localhost:27017")
DB_NAME = "game_db"

client = MongoClient(MONGO_URL)
db = client[DB_NAME]

monsters_collection = db["monsters"]
MONSTERS = [
    {
        "name": "Gobelin",
        "attack": 10,
        "defense": 5,
        "health": 50
    },
    {
        "name": "Orc",
        "attack": 15,
        "defense": 10,
        "health": 150
    },
    {
        "name": "Troll",
        "attack": 30,
        "defense": 5,
        "health": 500
    },
    {
        "name": "Golem",
        "attack": 20,
        "defense": 30,
        "health": 150
    },
    {
        "name": "Vampire",
        "attack": 20,
        "defense": 5,
        "health": 100
    },
    {
        "name": "Dragon",
        "attack": 50,
        "defense": 20,
        "health": 750
    },
]
monsters = monsters_collection.insert_many(MONSTERS)

heros_collection = db["heros"]
HEROS = [
    {
        "name": "Guerrier",
        "attack": 15,
        "defense": 10,
        "health": 100
    },
    {
        "name": "Paladin",
        "attack": 10,
        "defense": 15,
        "health": 150
    },
    {
        "name": "Barbare",
        "attack": 20,
        "defense": 5,
        "health": 150
    },    
    {
        "name": "Assasin",
        "attack": 20,
        "defense": 5,
        "health": 50
    },
    {
        "name": "Voleur",
        "attack": 15,
        "defense": 5,
        "health": 100
    },
    {
        "name": "Archer",
        "attack": 15,
        "defense": 5,
        "health": 100
    },
    {
        "name": "Barde",
        "attack": 5,
        "defense": 5,
        "health": 150
    },
    {
        "name": "Sorcier",
        "attack": 5,
        "defense": 5,
        "health": 100
    },
    {
        "name": "Clerc",
        "attack": 5,
        "defense": 10,
        "health": 100
    },
    {
        "name": "Druide",
        "attack": 5,
        "defense": 5,
        "health": 150
    }
]
heros = heros_collection.insert_many(HEROS)

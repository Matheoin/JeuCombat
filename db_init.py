from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client.ClashNotRoyal
collection = db.monsters

collection.drop()

collection.insert_many([
    {
        "name": "Gobelin",
        "attack": 10,
        "defense": 5,
        "health": 50
    }
])

collection = db.heros

collection.drop()

collection.insert_many([
    {
        "name": "Guerrier",
        "attack": 15,
        "defense": 10,
        "health": 100
    },
    {
        "name": "Chevalier",
        "attack": 10,
        "defense": 15,
        "health": 150
    },
    {
        "name": "Assasin",
        "attack": 20,
        "defense": 5,
        "health": 50
    },
    {
        "name": "Sorcier",
        "attack": 5,
        "defense": 5,
        "health": 100
    },
    {
        "name": "Prêtre",
        "attack": 5,
        "defense": 10,
        "health": 100
    },
    {
        "name": "Archer",
        "attack": 15,
        "defense": 5,
        "health": 100
    },
])


collection = db.loot

collection.drop()

collection.insert_many([
    {
        "name": "Potion de soin",
        "effet": "health",
        "value": 20
    }    
])

collection = db.equipments

collection.drop()

collection.insert_many([
    {
        "name": "Armure de fer",
        "effect": "defense",
        "value": 10,
    }
])

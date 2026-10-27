from pymongo import MongoClient


class Game: 
    def __init__(self, mongo_client: MongoClient, db_name: str = "game_db"):
        self.db = mongo_client[db_name]
        self.team: List[]



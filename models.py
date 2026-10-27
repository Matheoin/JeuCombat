from dataclasses import dataclass
from typing import Dict, Any

# ---------- ALGORITHME ----------
# Character
# 
# Monster
# 
# Score
# 

@dataclass
class Character:
    name: str
    attack: int
    defense: int
    health: int
    max_health: int

    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        return cls(
            name = data["name"],
            attack = data["attack"],
            defense = data["defense"],
            health = data["health"],
            max_health = data["health"]
        )

    def to_dict(self):
        return {
            "name": self.name,
            "attack": self.attack,
            "defense": self.defense,
            "health": self.health
        }

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage: int):
        actual_damage = max(1, damage - self.defense)
        self.health = max(0, self.health - actual_damage)
        return actual_damage

    def __str__(self):
        return f"{self.name} - ATK: {self.attack}, DEF: {self.defense}, PV: {self.health}/{self.max_health}"

@dataclass
class Monster(Character):
    pass

@dataclass
class Score:
    player_name: str
from typing import List, Dict
from solutionPrinter import solution_println as sp
from itertools import product

path: str = "input.in"
test_player: dict = {
    "hit points": 8,
    "damage": 0,
    "armor": 0
}

test_boss: dict = {
    "hit points": 12,
    "damage": 7,
    "armor": 2
}

test_equipment: dict = {
    'cost': 112,
    'damage': 5,
    'armor': 5
}


class Equipment:
    def __init__(self):
        self.item_rules: dict = {
            "weapons": {
                "min": 1,
                "max": 1
            },
            "armors": {
                "min": 0,
                "max": 1
            },
            "damage_rings": {
                "min": 0,
                "max": 1
            },
            "armor_rings": {
                "min": 0,
                "max": 1
            }
        }

        self.shop_content: dict = {
            "weapons": {
                "Dagger": {
                    "cost": 8,
                    "damage": 4,
                    "armor": 0
                },
                "Shortsword": {
                    "cost": 10,
                    "damage": 5,
                    "armor": 0
                },
                "Warhammer": {
                    "cost": 25,
                    "damage": 6,
                    "armor": 0
                },
                "Longsword": {
                    "cost": 40,
                    "damage": 7,
                    "armor": 0
                },
                "Greataxe": {
                    "cost": 74,
                    "damage": 8,
                    "armor": 0
                }
            },
            "armors": {
                "Leather": {
                    "cost": 13,
                    "damage": 0,
                    "armor": 1
                },
                "Chainmail": {
                    "cost": 31,
                    "damage": 0,
                    "armor": 2
                },
                "Splintmail": {
                    "cost": 53,
                    "damage": 0,
                    "armor": 3
                },
                "Bandedmail": {
                    "cost": 75,
                    "damage": 0,
                    "armor": 4
                },
                "Platemail": {
                    "cost": 102,
                    "damage": 0,
                    "armor": 5
                }
            },
            "damage_rings": {
                "DMG1": {
                    "cost": 25,
                    "damage": 1,
                    "armor": 0
                },
                "DMG2": {
                    "cost": 50,
                    "damage": 2,
                    "armor": 0
                },
                "DMG3": {
                    "cost": 100,
                    "damage": 3,
                    "armor": 0
                }
            },
            "armor_rings": {
                "AMR1": {
                    "cost": 20,
                    "damage": 0,
                    "armor": 1
                },
                "AMR2": {
                    "cost": 40,
                    "damage": 0,
                    "armor": 2
                },
                "AMR3": {
                    "cost": 80,
                    "damage": 0,
                    "armor": 3
                }
            },
        }
        self.variants: list = []


    @staticmethod
    def calculate_stats(equip: tuple) -> dict:
        stats: Dict[str:int] = {
            "cost": 0,
            "damage": 0,
            "armor": 0
        }

        for item in equip:
            if item is not None:
                for s in stats:
                    stats[s] += item[1][s]
        return stats


    def equipment_variants(self) -> dict:
        self.variants = []
        weapons: list = list(self.shop_content["weapons"].items())
        armor: list = [None]+list(self.shop_content["armors"].items())
        damage_rings: list = [None]+list(self.shop_content["damage_rings"].items())
        armor_rings: list = [None]+list(self.shop_content["armor_rings"].items())

        combinations = product(weapons, armor, damage_rings, armor_rings)
        for combo in combinations:
            counts: dict = {
                "weapons": sum(1 for item in [combo[0]] if item is not None),
                "armors": sum(1 for item in [combo[1]] if item is not None),
                "damage_rings": sum(1 for item in [combo[2]] if item is not None),
                "armor_rings": sum(1 for item in [combo[3]] if item is not None)
            }

            if all(self.item_rules[category]["min"] <= counts[category] <= self.item_rules[category]["max"]
                   for category in counts):
                self.variants.append(Equipment.calculate_stats(equip = combo))

        return self.variants


class Battle:
    def __init__(self):
        self.default_player: dict = {
            "hit points": 100,
            "damage": 0,
            "armor": 0
        }
        self.player: dict = {}
        self.default_boss: dict = {}
        self.boss: dict = {}
        self.winner: str = None
        self.cost_winner_battle: List[int] = []
        self.cost_loser_battle: List[int] = []


    def get_boss(self, path:str) -> dict:
        boss: list = open(path, "r").read().split("\n")
        self.default_boss = {i.split(": ")[0].lower() : int(i.split(": ")[1]) for i in boss}
        return self.default_boss


    def reset_settings(self) -> None:
        self.player = self.default_player.copy()
        self.boss = self.default_boss.copy()
        self.winner = None


    @staticmethod
    def damage(damage: int, enemy_armor: int) -> int:
        return max(damage-enemy_armor, 1)

    def get_equipment(self, equipment: dict) -> int:
        for attribute in equipment:
            if attribute != "cost":
                self.player[attribute] = equipment[attribute]
        return equipment["cost"]

    def battle(self, equipment: dict) -> bool:
        tour: int = 0
        battle_cost = Battle.get_equipment(self=self, equipment = equipment)

        while self.player["hit points"] > 0 and self.boss["hit points"] > 0:

            if tour % 2 == 0:
                result: int = Battle.damage(damage=self.player["damage"], enemy_armor=self.boss["armor"])
                self.boss["hit points"] -= result
                self.winner = "player"
            else:
                result: int = Battle.damage(damage = self.boss["damage"], enemy_armor = self.player["armor"])
                self.player["hit points"] -= result
                self.winner = "boss"

            tour += 1

        if self.winner == "player":
            self.cost_winner_battle.append(battle_cost)
            return True
        else:
            self.cost_loser_battle.append(battle_cost)
            return False


    def research_equipment(self, test_equipments) -> dict:
        for equipment in test_equipments:
            Battle.reset_settings(self=self)
            Battle.battle(self=self, equipment = equipment)

        return {
            "winner_equipment": min(self.cost_winner_battle),
            "loser_equipment": max(self.cost_loser_battle)
        }



def game(boss_path:str, player: dict = None, enemy: dict = None, test_equip: dict = None) -> dict:
    equipments = Equipment()
    equipments.equipment_variants()

    variants: List[Dict[str: int]] = equipments.variants
    battle = Battle()
    if player is not None:
        battle.player = player
    if enemy is not None:
        battle.boss = enemy

    battle.get_boss(boss_path)

    if player is not None or enemy is not None:
        battle.battle(test_equip)
        result = battle.research_equipment([test_equip])
    else:
        result = battle.research_equipment(variants)
    return result


sp("The cheapest from the best equipments cost: ", game(path)["winner_equipment"])
sp("The most expensive from the worst equipments cost: ", game(path)["loser_equipment"])

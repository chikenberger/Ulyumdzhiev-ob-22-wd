class GameCharacter:
    def __init__(self, name, level, health, attack, defense):
        self.name = name
        self.level = level
        self.health = health
        self.attack = attack
        self.defense = defense

    def apply_damage(self, damage):
        self.health -= damage

    def increase_level(self):
        self.level += 1
        self.health *= 1.1
        self.attack *= 1.1



character1 = GameCharacter("Персонаж 1", 1, 100, 20, 10)
character2 = GameCharacter("Персонаж 2", 1, 100, 15, 12)



for i in range(3):
    print(f"Раунд {i+1}:")
    print(f"{character1.name} атакует {character2.name}")
    character2.apply_damage(character1.attack)
    print(f"Здоровье {character2.name}: {character2.health}")

    print(f"{character2.name} атакует {character1.name}")
    character1.apply_damage(character2.attack)
    print(f"Здоровье {character1.name}: {character1.health}")

    print()



if character1.health > character2.health:
    print(f"{character1.name} победил!")
elif character2.health > character1.health:
    print(f"{character2.name} победил!")
else:
    print("Ничья!")

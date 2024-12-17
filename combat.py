import random

def combat(player, enemy, enemy_hp):
    print(f"\nA wild {enemy} appears!")
    print(f"{enemy} has {enemy_hp} HP.")
    
    player_attack = random.randint(5, 20)
    enemy_attack = random.randint(5, 15)

    print(f"{player.name} attacks the {enemy} and deals {player_attack} damage!")
    enemy_hp -= player_attack

    if enemy_hp <= 0:
        print(f"The {enemy} has been defeated!")
        return

    print(f"The {enemy} attacks {player.name} and deals {enemy_attack} damage!")
    player.hp -= enemy_attack

    if player.hp <= 0:
        print(f"{player.name} has been defeated!")
    else:
        print(f"{player.name}'s remaining HP: {player.hp}")
        print(f"{enemy}'s remaining HP: {enemy_hp}")

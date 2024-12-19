import random

class Enemy:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def is_defeated(self):
        return self.health <= 0

def engage_combat(player, enemy):
    """
    Handles combat between the player and an enemy.
    """
    print(f"A wild {enemy.name} appears! Prepare for battle!")
    while player.hp > 0 and enemy.health > 0:
        print(f"{player.name}'s HP: {player.hp} | {enemy.name}'s HP: {enemy.health}")
        action = input("Choose your action (attack/inventory/run): ").strip().lower()

        if action == "attack":
            damage = player.stats["Strength"] // 2 + random.randint(1, 5)
            enemy.health -= damage
            print(f"You dealt {damage} damage to the {enemy.name}!")
            if enemy.is_defeated():
                print(f"You have defeated the {enemy.name}!")
                return True
        elif action == "inventory":
            print(player.view_inventory())
        elif action == "run":
            print("You attempt to flee...")
            if random.random() < 0.5:
                print("You successfully escaped!")
                return False
            else:
                print("You failed to escape!")

        # Enemy attacks back if not defeated
        if enemy.health > 0:
            enemy_damage = random.randint(1, enemy.attack_power)
            player.hp -= enemy_damage
            print(f"The {enemy.name} attacks and deals {enemy_damage} damage!")
            if player.hp <= 0:
                print("You have been defeated!")
                return False

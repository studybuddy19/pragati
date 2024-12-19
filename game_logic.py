from player import Player

def create_character():
    """
    Handles character creation for the player.
    """
    name = input("Enter your character's name: ").strip()
    player_class = input("Choose your class (Warrior, Mage, Rogue): ").strip()
    race = input("Choose your race (Human, Elf, Dwarf): ").strip()
    return Player(name=name, player_class=player_class, race=race)

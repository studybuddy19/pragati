class Player:
    def __init__(self, name, player_class, race):
        self.name = name
        self.player_class = player_class
        self.race = race
        self.hp = 100
        self.stats = {
            "Strength": 10,
            "Dexterity": 10,
            "Intelligence": 10
        }
        self.inventory = []

    def display_stats(self):
        return f"{self.name} the {self.race} {self.player_class} - HP: {self.hp}, Stats: {self.stats}"

    def add_to_inventory(self, item):
        self.inventory.append(item)
        return f"{item} added to inventory!"

    def view_inventory(self):
        if not self.inventory:
            return "Your inventory is empty."
        return f"Inventory: {', '.join(self.inventory)}"

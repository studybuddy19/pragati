import random
from game_logic import create_character
from combat import Enemy, engage_combat
from narrator import setup_narrator, speak
from story_generator import StoryGenerator

# List of available commands
COMMANDS = [
    "explore - Look around your surroundings.",
    "attack - Attack a nearby enemy.",
    "use [item] - Use an item from your inventory.",
    "inventory - View your inventory.",
    "stats - Display your character's stats.",
    "run - Attempt to flee the current situation.",
    "quit - Exit the game.",
]

def display_commands():
    print("\nAvailable commands:")
    for command in COMMANDS:
        print(f"- {command}")

def main():
    print("Welcome to the AI Dungeon Master!")

    # Set up the narrator
    narrator = setup_narrator()
    speak("Welcome to the AI Dungeon Master!", narrator)

    # Initialize Story Generator with GPT-Neo model
    story_gen = StoryGenerator()

    # Theme Selection
    themes = [
        "Dark Dungeon", "Medieval Castle", "Enchanted Forest",
        "Dwarven Peaks", "Ancient Desert", "Pirate Cove",
        "Celestial Realm", "Volcanic Depths", "Crystal Caves", "Lost Frontier"
    ]
    print("\nChoose a theme for your adventure:")
    for i, theme in enumerate(themes, start=1):
        print(f"{i}. {theme}")

    while True:
        try:
            theme_choice = int(input("Enter the number of your chosen theme: ").strip())
            if 1 <= theme_choice <= len(themes):
                chosen_theme = themes[theme_choice - 1]
                break
            else:
                print("Invalid choice. Please select a valid number.")
                speak("Invalid choice. Please select a valid number.", narrator)
        except ValueError:
            print("Invalid input. Please enter a number.")
            speak("Invalid input. Please enter a number.", narrator)

    print(f"\nYou selected: {chosen_theme}")
    speak(f"You selected {chosen_theme}.", narrator)

    # Character Creation
    num_players = int(input("\nEnter the number of players: ").strip())
    players = []
    for i in range(num_players):
        print(f"\nPlayer {i + 1} Character Creation:")
        players.append(create_character())
    for player in players:
        print(player.display_stats())
        speak(player.display_stats(), narrator)

    # Generate the story's initial prompt based on theme
    game_history = story_gen.choose_theme_prompt(chosen_theme)
    print(f"\n{game_history}")
    speak(game_history, narrator)

    # Game Loop
    current_player_index = 0
    while True:
        current_player = players[current_player_index]
        print(f"\nIt's {current_player.name}'s turn!")
        speak(f"It's {current_player.name}'s turn!", narrator)

        display_commands()

        user_action = input("\nEnter your action: ").strip()

        if "quit" in user_action:
            print("Thank you for playing! Goodbye!")
            speak("Thank you for playing! Goodbye!", narrator)
            break

        if user_action == "explore":
            if random.random() < 0.5:
                found_item = random.choice(["Potion", "Sword", "Shield"])
                print(f"You found a {found_item}!")
                print(current_player.add_to_inventory(found_item))
            else:
                enemy = Enemy("Goblin", 30, 10)
                if not engage_combat(current_player, enemy):
                    break
        elif user_action == "inventory":
            print(current_player.view_inventory())
        elif user_action == "stats":
            print(current_player.display_stats())
        else:
            print("Invalid action. Try again.")

        # Update the story based on the player's action
        updated_story = story_gen.generate_story(
            chosen_theme,
            user_action,
            game_history,
        )
        game_history += f"\n{user_action}: {updated_story}"
        print(f"\n{updated_story}")
        speak(updated_story, narrator)

        current_player_index = (current_player_index + 1) % len(players)

if __name__ == "__main__":
    main()

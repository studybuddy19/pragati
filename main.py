import time
from story_generator import StoryGenerator
from game_logic import create_character, Player
from narrator import setup_narrator, speak

# List of available commands
COMMANDS = [
    "explore - Look around your surroundings.",
    "attack - Attack a nearby enemy.",
    "use [item] - Use an item from your inventory.",
    "run - Attempt to flee the current situation.",
    "talk - Try to communicate with a character or enemy.",
    "quit - Exit the game.",
]

def display_commands():
    print("\nAvailable commands:")
    for command in COMMANDS:
        print(f"- {command}")

def main():
    print("Welcome to the AI Dungeon Master!")

    # Set up the narrator with a scary voice for added immersion
    narrator = setup_narrator()
    speak("Welcome to the AI Dungeon Master!", narrator)

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
        print(f"Character Created: {player}")
        speak(f"Character created: {player}", narrator)

    # Initialize Story Generator
    story_gen = StoryGenerator()
    game_history = story_gen.choose_theme_prompt(chosen_theme)
    print(f"\n{game_history}")
    speak(game_history, narrator)

    # Game Loop
    current_player_index = 0
    while True:
        try:
            current_player = players[current_player_index]
            print(f"\nIt's {current_player.name}'s turn!")
            speak(f"It's {current_player.name}'s turn!", narrator)

            # Display available commands
            display_commands()

            # Get User Action via Text Input
            user_action = input("\nEnter your action: ").strip()

            if "quit" in user_action:
                print("Thank you for playing! Goodbye!")
                speak("Thank you for playing! Goodbye!", narrator)
                break

            # Process User Action
            if user_action:
                response = story_gen.generate_story(
                    theme=chosen_theme,
                    player_action=user_action,
                    game_history=game_history
                )
                print(f"AI Dungeon Master: {response}")
                speak(response, narrator)
                game_history += f"\n{response}"
            else:
                print("No action detected. Skipping turn.")
                speak("No action detected. Skipping turn.", narrator)

            # Switch to Next Player
            current_player_index = (current_player_index + 1) % len(players)

        except Exception as e:
            print(f"An error occurred: {e}")
            speak("An error occurred. Please try again.", narrator)
            break


if __name__ == "__main__":
    main()

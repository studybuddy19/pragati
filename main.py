from story_generator import StoryGenerator
from game_logic import create_character, Player
from voice_recognition import listen_for_input
from narrator import setup_narrator, speak

def main():
    print("Welcome to the AI Dungeon Master!")

    # Set up the narrator for scary voice
    narrator = setup_narrator()
    speak("Welcome to the AI Dungeon Master!", narrator)

    # Theme selection
    themes = [
        "Dark Dungeon", "Medieval Castle", "Enchanted Forest",
        "Dwarven Peaks", "Ancient Desert", "Pirate Cove",
        "Celestial Realm", "Volcanic Depths", "Crystal Caves", "Lost Frontier"
    ]
    for i, theme in enumerate(themes, start=1):
        print(f"{i}. {theme}")
    theme_choice = int(input("Enter the number of your chosen theme: ").strip())
    chosen_theme = themes[theme_choice - 1]
    print(f"\nYou selected: {chosen_theme}")
    speak(f"You selected {chosen_theme}.", narrator)

    # Character creation
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
    speak(game_history, narrator)

    # Game loop
    current_player_index = 0
    while True:
        try:
            current_player = players[current_player_index]
            print(f"\nIt's {current_player.name}'s turn!")
            speak(f"It's {current_player.name}'s turn!", narrator)

            user_action = listen_for_input()

            if "quit" in user_action:
                print("Thank you for playing! Goodbye!")
                speak("Thank you for playing! Goodbye!", narrator)
                break

            if "text mode" in user_action:
                print("Switching to text input mode...")
                speak("Switching to text input mode.", narrator)
                user_action = input("Enter your action: ").strip()

            if user_action:
                response = story_gen.generate_story(
                    theme=chosen_theme,
                    player_action=user_action,
                    game_history=game_history
                )
                print(f"AI Dungeon Master: {response}")
                speak(response, narrator)
                game_history += f" {response}"
            else:
                print("No action detected. Skipping turn.")
                speak("No action detected. Skipping turn.", narrator)

            current_player_index = (current_player_index + 1) % len(players)

        except Exception as e:
            print(f"An error occurred: {e}")
            speak("An error occurred. Please try again.", narrator)
            break


if __name__ == "__main__":
    main()

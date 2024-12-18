from story_generator import StoryGenerator
from player import Player
from combat import combat
import pyttsx3
import random
import speech_recognition as sr

# Text-to-speech initialization
tts_engine = pyttsx3.init()
tts_engine.setProperty("rate", 150)
tts_engine.setProperty("voice", tts_engine.getProperty('voices')[1].id)  # Deep voice

# Global dictionary to store player data
game_data = {"players": [], "story": ""}

def roll_dice(sides=20):
    return random.randint(1, sides)

# Function to truncate the prompt to a reasonable length
def truncate_prompt(prompt, max_tokens=50):
    words = prompt.split()
    if len(words) > max_tokens:
        return " ".join(words[-max_tokens:])
    return prompt

# Function to capture voice input
def listen_for_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for input...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)  # Listen for the first phrase

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)  # Use Google Speech API to recognize speech
        print(f"Player said: {text}")
        return text.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
        return ""
    except sr.RequestError:
        print("Could not request results; check your network connection.")
        return ""

def main():
    print("Welcome to your AI Dungeon Master!")
    story_gen = StoryGenerator()
    theme = "Dungeons & Dragons"

    # Create multiple characters
    num_players = int(input("Enter the number of players: "))
    for i in range(num_players):
        print(f"\nPlayer {i + 1} Character Creation:")
        name = input("Enter your character's name: ")
        player_class = input("Choose your class (e.g., Warrior, Mage, Rogue): ")
        race = input("Choose your race (e.g., Human, Elf, Dwarf): ")

        # Add player to the global list
        player = Player(name, player_class, race)
        game_data["players"].append(player)
        print(f"Character Created: {player.display_stats()}")

    # Initial story prompt
    game_data["story"] = (
        f"You and your party find yourselves in a dark dungeon. "
        f"A dragon's roar echoes through the halls. What do you do?"
    )
    tts_engine.say(game_data["story"])
    tts_engine.runAndWait()

    # Main game loop
    current_player_index = 0
    while True:
        current_player = game_data["players"][current_player_index]
        print(f"\n{game_data['story']}")
        print(f"\nIt's {current_player.name}'s turn!")

        # Use voice input instead of text input
        user_action = listen_for_input()

        if user_action in ["quit", "exit"]:
            print("Thank you for playing! Goodbye!")
            break

        # Process the player's action and update the shared story
        if "attack" in user_action:
            enemy = random.choice(["Orc", "Goblin", "Skeleton"])
            combat(current_player, enemy, random.randint(30, 100))
            game_data["story"] += f" {current_player.name} attacked the {enemy}!"
        elif "inventory" in user_action:
            print(current_player.view_inventory())
        elif "search" in user_action:
            item = random.choice(["Potion", "Gold", "Magic Scroll"])
            print(current_player.add_to_inventory(item))
            game_data["story"] += f" {current_player.name} searched the room and found a {item}!"
        elif "stats" in user_action:
            print(current_player.display_stats())
        else:
            # Truncate the prompt and generate a response
            updated_prompt = truncate_prompt(f"{game_data['story']} {current_player.name} decided to {user_action}.")
            response = story_gen.generate_story(updated_prompt)
            print(f"AI Dungeon Master: {response}")
            game_data["story"] = response  # Update the shared story

        # Move to the next player's turn
        current_player_index = (current_player_index + 1) % num_players

if __name__ == "__main__":
    main()

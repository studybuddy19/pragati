from transformers import GPTNeoForCausalLM, GPT2Tokenizer
import os

class StoryGenerator:
    def __init__(self, model_path='./local_gpt_neo_model'):
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model path '{model_path}' does not exist.")

        # Load GPT-Neo model and tokenizer
        self.model = GPTNeoForCausalLM.from_pretrained(model_path)
        self.tokenizer = GPT2Tokenizer.from_pretrained(model_path)
        self.tokenizer.pad_token = self.tokenizer.eos_token
        self.model.config.pad_token_id = self.tokenizer.pad_token_id

        # Themes for the game
        self.themes = {
            "Dark Dungeon": "You find yourselves in a dark and damp dungeon. The roar of monsters echoes from the shadows.",
            "Medieval Castle": "A royal banquet in the grand castle takes a dark turn. Treachery and mystery unfold in the corridors.",
            "Enchanted Forest": "The forest glows with mystical energy, but not all magic is friendly. A path emerges ahead.",
            "Dwarven Peaks": "You climb the towering Dwarven Peaks. Legends speak of treasures guarded by ancient golems.",
            "Ancient Desert": "The sands of the desert conceal lost cities and buried secrets. Beware the scorching heat.",
            "Pirate Cove": "A hidden cove where pirates hoarded treasures. The sea breeze brings both gold and danger.",
            "Celestial Realm": "A land of radiant light and celestial beings. Power and virtue are tested here.",
            "Volcanic Depths": "You descend into fiery caverns where molten lava and fiery beasts dwell.",
            "Crystal Caves": "The walls of these caves shine with crystals, but they also hide treacherous creatures.",
            "Lost Frontier": "You venture into the uncharted frontier. Ruins of ancient civilizations await discovery.",
        }

    def choose_theme_prompt(self, theme):
        return self.themes.get(theme, "Your adventure begins...")

    def generate_story(self, theme, player_action, game_history, max_new_tokens=75):
        try:
            # Get the prompt based on the theme
            theme_prompt = self.choose_theme_prompt(theme)

            # Combine the theme, current game history, and player action into a prompt
            combined_prompt = (
                f"Theme: {theme_prompt}\n"
                f"Story so far: {game_history}\n"
                f"Player action: {player_action}\n"
                "AI Dungeon Master responds:"
            )

            # Tokenize and generate the story continuation
            inputs = self.tokenizer(combined_prompt, return_tensors="pt", truncation=True, max_length=512)

            # Generate the next part of the story with a limit of max_new_tokens (150 by default)
            outputs = self.model.generate(
                inputs['input_ids'],
                attention_mask=inputs['attention_mask'],
                max_new_tokens=max_new_tokens,
                do_sample=True,
                temperature=0.7,
                top_p=0.85,
                repetition_penalty=1.2,
                no_repeat_ngram_size=3,
                pad_token_id=self.tokenizer.pad_token_id,
            )

            # Decode the generated text and extract the part after the "AI Dungeon Master responds:"
            generated_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
            response = generated_text.split("AI Dungeon Master responds:")[-1].strip()

            # Return the story continuation
            return response
        except Exception as e:
            return f"Error during story generation: {e}"

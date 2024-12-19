import pyttsx3

def setup_narrator():
    """Set up the narrator's voice with a scary tone."""
    narrator = pyttsx3.init()
    voices = narrator.getProperty('voices')

    # Select a deep and scary-sounding voice (if available)
    for voice in voices:
        if "english" in voice.name.lower():
            narrator.setProperty('voice', voice.id)
            break

    # Adjust settings for a more "narrative" tone
    narrator.setProperty('rate', 130)  # Slow down the speech
    narrator.setProperty('volume', 1.0)  # Max volume
    return narrator

def speak(text, narrator):
    """Speak the text out loud using the narrator's voice."""
    narrator.say(text)
    narrator.runAndWait()

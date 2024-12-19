import speech_recognition as sr


def listen_for_input():
    """Capture player's voice input."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for input... (say 'text mode' to switch)")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=10)
            print("Recognizing...")
            text = recognizer.recognize_google(audio)
            print(f"Player said: {text}")
            return text.lower()
        except sr.UnknownValueError:
            return "Sorry, I didn't understand that."
        except sr.WaitTimeoutError:
            return "Timeout reached! Try again or type your action."

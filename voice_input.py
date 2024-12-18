import speech_recognition as sr

def test_voice_input():
    recognizer = sr.Recognizer()

    # Use the default microphone as the audio source
    with sr.Microphone() as mic:
        print("Listening... Speak something!")
        
        try:
            # Adjust the recognizer for ambient noise
            recognizer.adjust_for_ambient_noise(mic, duration=1)
            
            # Listen to the audio
            audio = recognizer.listen(mic, timeout=10)  # Adjust timeout if needed
            
            # Recognize and print the speech
            user_input = recognizer.recognize_google(audio)
            print(f"You said: {user_input}")
            return user_input
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand what you said.")
        except sr.RequestError:
            print("There was an issue with the speech recognition service.")
        except sr.WaitTimeoutError:
            print("Listening timed out. Please try again.")

if __name__ == "__main__":
    test_voice_input()

import pyttsx3

if __name__ == '__main__':
    while True:
        print("Welcome, I am a speaker created by Manasi")
        x = input("Enter what you want me to speak: ")

        # Initialize the TTS engine
        engine = pyttsx3.init()

        # Set properties (optional)
        engine.setProperty('rate', 150)    # Speed percent (can go over 100)
        engine.setProperty('volume', 0.9)  # Volume 0-1

        # Speak the text
        engine.say(x)

        # Wait for the speech to finish
        engine.runAndWait()

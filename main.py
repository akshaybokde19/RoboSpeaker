import pyttsx3

if __name__ == "__main__":
    print("Hello! Welcome to RoboSpeaker 1.0 Created by Akshay")
    engine = pyttsx3.init()  # Initialize the text-to-speech engine

    while True:
        x = input("Enter what you want to say by RoboSpeaker (or press 'q' to exit): ")

        if x.lower() == "q":  # Case-insensitive exit condition
            print("Goodbye!")
            engine.say("Goodbye")
            engine.runAndWait()  # Ensure the engine finishes speaking
            break

        engine.say(x)  # Speak the user's input
        engine.runAndWait()

import speech_recognition as sr
from polly_speak import speak
from commands import handle_command


if __name__ == "__main__":
    speak("Hello, I'm your cloud assistant. How can I help you?")
    while True:
        command = listen()
        if command:
            if 'exit' in command:
                speak("Goodbye!")
                break
            handle_command(command)

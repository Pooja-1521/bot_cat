import speech_recognition as sr
from polly_speak import speak
from commands import handle_command

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = r.listen(source)

        try:
            command = r.recognize_google(audio)
            print("🗣️ You said:", command)
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
            return None

if __name__ == "__main__":
    speak("Hello, I'm your cloud assistant. How can I help you?")
    while True:
        command = listen()
        if command:
            if 'exit' in command:
                speak("Goodbye!")
                break
            handle_command(command)

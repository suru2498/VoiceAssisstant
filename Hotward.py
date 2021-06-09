import speech_recognition as sr
import os

def takeCommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        command.pause_threshold = 1
        audio = command.listen(source)

        try:
            print("Recognizing...")
            query = command.recognize_google(audio, language="en-in")
            print(f"you said:{query}")

        except Exception as Error:
            return "none"

        return query.lower()

while True:
    wake_up = takeCommand()
    if "wake up" in wake_up:
        os.startfile('C:\\Users\\Administrator\\Desktop\\jar\\Friday.py')
    else:
        print("  ")
        print("commands are running in that pager")
        print("  ")
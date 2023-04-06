import speech_recognition as sr
import pyaudio
import pyttsx3
import pywhatkit


def talk(command):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say("Playing" + command)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language='en-in')
        print(f"Query: {query}\n")

    except Exception as e:
        print("would you mind saying it again.")
        # speak("would you mind saying it again.")
        return "None"
    return query



takeCommand()

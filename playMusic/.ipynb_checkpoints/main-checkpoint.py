import speech_recognition as sr
import pyttsx3
import pywhatkit


def talk(command):
    engine=pyttsx3.init()
    voice=engine.getProperty('voices')
    engine.setProperty('voice',voice[1].id)
    engine.say("Playing"+ command)
    engine.runAndWait()

def takeCommand():
    Listener=sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("listening")
            voice=Listener.Listen(source)
            command=Listener.recognize_google(voice)
            song=command.replace('play','')
            talk(song)
            pywhatkit.playonyt(song)

    except:
        pass

takeCommand()


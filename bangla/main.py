from gtts import gTTS
from io import BytesIO
import pygame
import time
import pyttsx3


def speak(text, language='bn'):
    mp3_fo = BytesIO()
    tts = gTTS(text, lang=language)
    tts.write_to_fp(mp3_fo)
    return mp3_fo


pygame.init()
pygame.mixer.init()
pygame.mixer.music.set_volume(0.5)
sound = speak(
    "আমি হুমায়ূন আহমেদের বিশেষ করে তার লেখার একজন একনিষ্ঠ ভক্ত। কেন আমি তার ভক্ত তা আমি কখনো স্পষ্টভাবে ব্যাখ্যা করতে পারব না।")
pygame.mixer.music.load(sound, 'mp3')

pygame.mixer.music.play()
time.sleep(10)

# mixer.music.load("song.mp3")
# Setting the volume.
# mixer.music.set_volume(0.7)
# Start playing the song.
# mixer.music.play()
# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)

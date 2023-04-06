from gtts import gTTS
from playsound import playsound
import os
from pathlib import Path

voice = gTTS(
    text="আমি হুমায়ূন আহমেদের বিশেষ করে তার লেখার একজন একনিষ্ঠ ভক্ত। কেন আমি তার ভক্ত তা আমি কখনো স্পষ্টভাবে ব্যাখ্যা করতে পারব না।",
    lang='bn')
voice.save('good.mp3')
os.system("mpg321 good.mp3")
playsound("good.mp3", False)
import speech_recognition
from gtts import gTTS
import os
import time
import playsound

class speak():
    def __init__(self,text):
        tts = gTTS(text=text, lang='ko')
        filename = 'voice.mp3'
        tts.save(filename)
        playsound.playsound(filename)


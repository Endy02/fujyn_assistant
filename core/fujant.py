from enum import auto
from urllib.request import url2pathname
import speech_recognition as sr
import time as tm
import webbrowser
import playsound
import os
import random
from gtts import gTTS

class Fujant:
    def __init__(self):
        pass
    
    def record_audio(self, ask=False):
        """
            Function to Process the voice recognition
        """
        with sr.Microphone() as source:
            r = sr.Recognizer()
            if ask:
                self.print(ask)
            audio = r.listen(source)
            voice_data = ""
            try:
                voice_data = r.recognize_google(audio)
            except sr.UnknownValueError:
                print("Sorry, i didn't understand, can just say it again please")
            except sr.RequestError:
                print("Sorry, me speech service is down")
            return voice_data

    def fujant_speech(self, audio):
        tts = gTTS(text=audio, lang='en')
        r = random.randint(1, 1000000)
        audio_file = 'audio-'+ str(r) + '.mp3'
        tts.save(audio_file)
        playsound.playsound(audio_file)
        print(audio)
        os.remove(audio_file)
        
    def respond(self, voice_data):
        """
            Function to process the response
        """
        if "what's your name" in voice_data:
            print("My name is Fujant")
        if "what time is it" in voice_data:
            print(str(tm.ctime()))
        if "where do you live" in voice_data:
            print("I live in my master house bro")
        if "search" in voice_data:
            search = self.record_audio(ask="What do you looking for ?")
            url = "https://www.google.com/search?q=" + search
            webbrowser.get().open(url=url)
            print('Here is what i found for '+ search)
        if "location" in voice_data:
            location = self.record_audio(ask="Where do you want to see ?")
            url = "https://www.google.nl/maps/place/" + location + "/&amp;"
            webbrowser.get().open(url=url)
            print('Here is your target')
        if "exit" in voice_data:
            exit()
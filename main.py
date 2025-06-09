import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS
from time import ctime

r = sr.Recognizer()

def record_audio(ask =False):
    with sr.Microphone() as source:
        if ask:
            alexis_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            alexis_speak('Sorry, i did not get that')
        except sr.RequestError:
            alexis_speak("Sorry , my speech is down")
        return voice_data
    
def alexis_speak(audio_string):
    tts = gTTS(text=audio_string, lang = "en")
    r= random.randint(1, 10000000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)
    

def respond(voice_data):
    if'what is your name' in voice_data:
        alexis_speak('I dont have a name')
    if 'what time is it' in voice_data:
        alexis_speak("The time is" + ctime())
    if 'search'in voice_data:
        search = record_audio('What do you want to search for?')
        url = 'http://google.com/search?q='+search
        webbrowser.get().open(url)
        alexis_speak("Here is what i found for you " + search)
    if 'find location' in voice_data:
        location = record_audio('What is the location you are looking for?')
        url = 'https://www.google.nl/maps/place/' + location + '&amp;'
        webbrowser.get().open(url)
        alexis_speak("Here is the location of " + location)
    if 'exit' in voice_data:
        alexis_speak('Goodbye')
        exit()
    if 'music' in voice_data:
        alexis_speak('What type of music do you want to listen to?')
        

time.sleep(1)
alexis_speak("How can i help you")      
while 1:      
    voice_data = record_audio()
    respond(voice_data)
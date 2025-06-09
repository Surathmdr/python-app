import speech_recognition as sr
import webbrowser
from time import ctime

r = sr.Recognizer()

def record_audio(ask =False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            print('Sorry, i did not get that')
        except sr.RequestError:
            print("Sorry , my speech is down")
        return voice_data

def respond(voice_data):
    if'what is your name' in voice_data:
        print('My name is Alexis')
    if 'what time is it' in voice_data:
        print("The time is" + ctime())
    if 'search'in voice_data:
        search = record_audio('What do you want to search for?')
        url = 'http://google.com/search?q='+search
        webbrowser.get().open(url)
        print("Here is what i found for you " + search)
    if 'find location' in voice_data:
        location = record_audio('What is the location you are looking for?')
        url = 'https://www.google.com/maps/place/' + location
        webbrowser.get().open(url)
        

print("How can i help you")            
voice_data = record_audio()
respond(voice_data)
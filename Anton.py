#Anton
import speech_recognition as sr
import webbrowser as wb
import time
import playsound
import os
import random

from gtts import gTTS
from time import ctime

r = sr.Recognizer()
r1 = sr.Recognizer()
r2 = sr.Recognizer()

listening = True

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            print("Currently active")
        audio = r.listen(source)
        voice_data=''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            Anton_speak("Sorry could not recognize what you said, speak up or adjust your audio settings.")
        except sr.RequestError:
            Anton_speak("Sorry, speech services are currently down")
        return voice_data

while True:

    
    def Anton_speak(audio_string):

        if listening:
            tts= gTTS(text = audio_string, lang='en')
            r = random.randint(1, 1000000)
            audio_file = 'audio-' + str(r) + '.mp3'
            tts.save(audio_file)
            playsound.playsound(audio_file)
            print(audio_string)
            os.remove(audio_file)

    def respond(voice_data):
        
        if 'Stop listening' in voice_data:
            print("Anton is no longer listening")
            listening = False    
            
        if 'Start listening' in voice_data:
            print("Anton is now listening")
            listening = True

        elif 'what is your name' in voice_data:
            Anton_speak("My name is Anton")
            
        elif 'what time is it' in voice_data:
            Anton_speak(ctime())
            
        elif 'search for' in voice_data:
            search = record_audio('What should I search for?')
            url = 'https://google.com/search?q=' + search
            wb.get().open(url)
            Anton_speak('Here is what I found for: ' + search)
            
        elif 'help' in voice_data:
            Anton_speak("How may I help you?")
            
        elif 'Thankyou' in voice_data:
            Anton_speak("you are welcome.")
            
        elif 'exit' in voice_data:
            Anton_speak("ok, goodbye")
            exit()

    voice_data = record_audio()
    print(voice_data)
    respond(voice_data)







#if 'Anton' in r1.recognize_google(audio):
#    r1 = sr.Recognizer()
#    url = 'https://www.youtube.com/watch?v=UaS4bZqYrCc'
#    with sr.Microphone() as source:
#        print('search your query')
#        audio = r1.listen(source)

#        try:
#            get = r1.recognize_google(audio)
#            print(get)
#            wb.get().open_new(url+get)
#
#        except sr.UnknwonValueError:
#            print('error')
#        except sr.RequestError as e:
#            print('failed'.format(e))
            

        

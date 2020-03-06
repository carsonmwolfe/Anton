import speech_recognition as sr
import webbrowser as wb
import time
import playsound
import os
import random
import subprocess
import random
import ssl
import urllib.request
import bs4 as bs
import pyttsx3
import datetime
import cv2
import sys
import argparse
import numpy as np


from gtts import gTTS
from time import ctime



r = sr.Recognizer()
r1 = sr.Recognizer()
r2 = sr.Recognizer()

listening = True

#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
face_cascade = cv2.CascadeClassifier('C:\\working_Dir\\data\\codes\\OpenCV\\classifiers\\haarcascade_frontalface_alt2.xml')
#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()




class person:
    name = ''
    def setName(self, name):
        self.name = name

class asis:
    name = ''
    def setName(self, name):
        self.name = name

        
def multiple(terms):
    for term in terms:
        if term in voice_data:
            return True

#def speak(text)
def Anton_speak(audio_string):

        tts= gTTS(text = audio_string, lang='en')
        r = random.randint(1, 1000000)
        audio_file = 'audio-' + str(r) + '.mp3'
        tts.save(audio_file)
        playsound.playsound(audio_file)
        print(audio_string)
        os.remove(audio_file)
        
#def get_audio()
def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            print("Currently active")
        audio = r.listen(source)
        voice_data=''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            Anton_speak("Sorry could not recognize what you said")
        except sr.RequestError:
            Anton_speak("Sorry, speech services are currently down")
        return voice_data
            
#WAKE = "wake"
while True:
    def respond(voice_data):

        #voice_data = record_audio()
        #if voice_data.count(WAKE) > 0:
        #    Anton_speak("How may I help you?")
        #    voice_data = record_audio()


        if multiple(['Stop listening', 'mute']):
            listening = False

        if multiple(['Start listening', 'unmute']):
            listening = True

            
        if multiple(['hey','hi','hello']):
            greetings = ["hey, how can I help you" + person_obj.name, "hey, what's up?" + person_obj.name, "I'm listening" + person_obj.name, "how can I help you?" + person_obj.name, "hello" + person_obj.name]
            greet = greetings[random.randint(0,len(greetings)-1)]
            Anton_speak(greet)

        if multiple (["what is your name", "your name", "Hey whats your name"]):
            Anton_speak("My name is Anton")

        if multiple (["weather"]):
            search_term = voice_data.split("for")[-1]
            url = "https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP-5u82AE&q=weather&oq=weather&gs_l=psy-ab.3..35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..gws-wiz.....10..0i71j35i39j35i362i39._5eSPD47bv8&ved=0ahUKEwiWrJvwwP7mAhVfwTgGHfsNDxsQ4dUDCAs&uact=5"
            wb.get().open(url)
            Anton_speak("Here is what I found for on google")

        if multiple (['what time is it', "the time", "whats the clock"]):
            time = ctime().split(" ")[4].split(":")[0:2]
            if time[0] == "00":
                hours = '12'
            else:
                hours = time[0]
            minutes = time[1]
            time = hours + " hours and " + minutes + "minutes"
            Anton_speak(time)
       
        if multiple(["what is your name","what's your name","tell me your name"]):
            if person_obj.name:
                Anton_speak("whats with my name ")
            else:
                Anton_speak("i dont know my name . what's your name?")  

        if multiple(["my name is"]):
            person_name = voice_data.split("is")[-1].strip()
            Anton_speak("okay, i will remember your name " + person_name)
            person_obj.setName(person_name)  

        if multiple (["what is my name"]):
            Anton_speak("Your name is " + person_obj.name)

        if multiple (['search for', 'look up', 'search up', 'google']):
            Anton_speak("what should I search for?")
            search = record_audio('What should I search for?')
            url = 'https://google.com/search?q=' + search
            wb.get().open(url)
            Anton_speak('Here is what I found for: ' + search)

        if multiple (["YouTube", "Look up on Youtube",]):
            search_term = voice_data.split("for")[-1]
            url = "https://www.youtube.com/results?search_query=" + search_term
            wb.get().open(url)
            Anton_speak("Here is what I found for " + search_term + "on youtube")
            
        elif 'help' in voice_data:
            Anton_speak("How may I help you?")
            
        elif 'Thankyou' in voice_data:
            Anton_speak("you are welcome.")

        if multiple (['how is your day', 'what was your day like']):
            Anton_speak("My day was good, how was yours?")
            
        if multiple(["Exit", "Quit", "Execute Order 66", "Order 66", "Anton Execute Order 66", "Terminate", "Cancel"]):
            Anton_speak("ok, goodbye")
            exit()

    person_obj = person()
    asis_obj = asis()
    asis_obj.name = 'kiki'
        
    voice_data = record_audio()
    print(voice_data)
    respond(voice_data)




        

import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import pyautogui
import requests


user = "YD"
ai = "Meldrix"

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()


def Greetings():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak(f"Good Morning, {user}")
        print(f"Good Morning", {user})
    elif hour>=12 and hour<18:
        speak(f"Good Afternoon, {user}")
        print(f"Good Afternoon, {user}")
    else:
        speak(f"Good Evening, {user}")
        print(f"Good Evening, {user}")
print(f"Loading your AI personal assistant {ai}")
speak(f"Hello, i am {ai}, your smart assistant, and i am here to help.")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("I am Listening...")
        audio=r.listen(source)
        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")
        except Exception as e:
            speak("oops!!! looks like there was an error")
            speak("can you repeat what you said, please")
            print(e)
            return "None"
        return statement
Greetings()


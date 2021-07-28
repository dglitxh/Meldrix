import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
# from ecapture import ecapture as ec
import wolframalpha
import json
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
        speak(f"Good Morning")
        print("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
        print("Good Afternoon")
    else:
        speak("Good Evening")
        print("Good Evening")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("I am Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("oops looks like there was an error")
            print(e)
            return "None"
        return statement

print("Loading your AI personal assistant Meldrix")
speak(f"Hello, i am {ai}, your smart assistant")
Greetings()

def goodbyes():
    speak('your personal assistant Meldrix is shutting down,Good bye')
    print('your personal assistant Meldrix is shutting down,Good bye')
    return

def wiki():
    speak('Searching Wikipedia...')
    statement =statement.replace("wikipedia", "")
    results = wikipedia.summary(statement, sentences=3)
    speak("According to Wikipedia")
    print(results)
    speak(results)

def youtube():
    webbrowser.open_new_tab("https://www.youtube.com")
    speak("youtube is open now")
    time.sleep(5)

def google():
    webbrowser.open_new_tab("https://www.google.com")
    speak("Google chrome is open now")
    time.sleep(5)

def clock():
    strTime=datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"the time is {strTime}")

def news():
    news = webbrowser.open_new_tab('www.ghanaweb.com')
    speak('Here are some headlines from ghanaweb.com. enjoy')
    time.sleep(6)

def search():
    statement = statement.replace("search", "")
    webbrowser.open_new_tab(statement)
    time.sleep(5)

def wolfram():
    speak('I can answer to computational and geographical questions  and what question do you want to ask now')
    question=takeCommand()
    app_id="E8H76X-T8V8UHPUY2"
    client = wolframalpha.Client('R2K75H-7ELALHR35X')
    res = client.query(question)
    answer = next(res.results).text
    speak(f"the answer is {answer}")
    print(answer)

def identity():
    speak('I am Meldrix version 1 point O your personal assistant. I am programmed to minor tasks like'
            'opening youtube,google chrome, gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather' 
     'In different cities, get top headline news from times of india and you can ask me computational or geographical questions too!')

def weather():
    api_key="Apply your unique ID"
    base_url="https://api.openweathermap.org/data/2.5/weather?"
    speak("for what city?")
    city_name=takeCommand()
    complete_url=base_url+"appid="+api_key+"&q="+city_name
    response = requests.get(complete_url)
    x=response.json()
    if x["cod"]!="404":
        y=x["main"]
        current_temperature = y["temp"]
        current_humidiy = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        speak(" Temperature in kelvin unit is " +
            str(current_temperature) +
            "\n humidity in percentage is " +
            str(current_humidiy) +
            "\n description  " +
            str(weather_description))
        print(" Temperature in kelvin unit = " +
            str(current_temperature) +
            "\n humidity (in percentage) = " +
            str(current_humidiy) +
            "\n description = " +
            str(weather_description))

def logout():
    speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
    subprocess.call(["shutdown", "/l"])

def creator():
    speak(f"I was built by {user}")
    print(f"I was built by {user}")
from Engine import *

def goodbyes():
    speak(f'your personal assistant {ai} is shutting down,Good bye')
    print(f'your personal assistant {ai} is shutting down,Good bye')
    return

def wiki():
    speak('Searching Wikipedia...')
    statement = takeCommand().replace("wikipedia", "")
    results = wikipedia.summary(statement, sentences=5)
    speak("According to Wikipedia")
    print(results)
    speak(results)

def youtube():
    webbrowser.open_new_tab("https://www.youtube.com")
    speak("youtube is now opened. Happy streaming")
    time.sleep(5)

def google():
    webbrowser.open_new_tab("https://www.google.com")
    speak("Google chrome is opened. Happy surfing")
    time.sleep(5)

def clock():
    strTime=datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"the time is {strTime}")

def news():
    news = webbrowser.open_new_tab('www.ghanaweb.com')
    speak('Here are some headlines from ghanaweb.com. enjoy')
    time.sleep(6)

def search():
    statement = takeCommand().replace("search", "")
    webbrowser.open_new_tab(statement)
    time.sleep(5)

def wolfram():
    speak('You can ask computational and geographical questions and get your answers in split seconds')
    question=takeCommand()
    app_id="E8H76X-T8V8UHPUY2"
    client = wolframalpha.Client(app_id)
    # client = wolframalpha.Client('R2K75H-7ELALHR35X')
    res = client.query(question)
    answer = next(res.results).text
    speak(f"the answer is {answer}")
    print(answer)

def identity():
    replies = [f"I am {ai}, your smart assistant. I am here to make life easier.",
     f"i am {ai}, i think i have told you before", ]
    speak(random.choice(replies))

def weather():
    city = "Accra"
    res = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=16f0afad2fd9e18b7aee9582e8ce650b&units=metric").json()
    temp1 = res["weather"][0]["description"]
    temp2 = res["main"]["temp"]
    speak(
        f"Temperature is {format(temp2)} degree Celsius \nWeather is {format(temp1)}")

def logout():
    speak("Ok , your pc will log off in 10 seconds make sure you exit from all applications")
    subprocess.call(["shutdown", "/l"])

def creator():
    speak(f"I was built by {user}")
    print(f"I was built by {user}")

def Whatsapp():
    speak("to whom do you intend sending this message?")
    name = takeCommand()
    speak("What is the message")
    webbrowser.open_new_tab(f'https://web.whatsapp.com/send?phone={name}&text={takeCommand()}')
    time.sleep(6)
    pyautogui.press('enter')
    speak("Message sent")
     

from Engine import *

def commands():
    count = 0
    


    while True:
            if count > 0:
                speak("Is there anything else i can help with YD?")
                statement = takeCommand().lower()
                if statement==0:
                    continue
            elif count == 0:
                speak("how may i help you?YD.")
                statement = takeCommand().lower()
                if statement==0:
                    continue



            if "good bye" in statement or "ok bye" in statement or "stop" in statement:
                        speak('your personal assistant Meldrix is shutting down,Good bye')
                        print('your personal assistant Meldrix is shutting down,Good bye')
                        break

            if 'wikipedia' in statement:
                speak('Searching Wikipedia...')
                statement =statement.replace("wikipedia", "")
                results = wikipedia.summary(statement, sentences=3)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'open youtube' in statement:
                webbrowser.open_new_tab("https://www.youtube.com")
                speak("youtube is open now")
                time.sleep(5)

            elif 'open google' in statement:
                webbrowser.open_new_tab("https://www.google.com")
                speak("Google chrome is open now")
                time.sleep(5)

            elif 'open gmail' in statement:
                webbrowser.open_new_tab("gmail.com")
                speak("Google Mail open now")
                time.sleep(5)

            elif 'time' in statement:
                strTime=datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"the time is {strTime}")

            elif 'news' in statement:
                news = webbrowser.open_new_tab('www.ghanaweb.com')
                speak('Here are some headlines from ghanaweb.com. enjoy')
                time.sleep(6)

            # elif "camera" in statement or "take a photo" in statement:
            #     ec.capture(0,"robo camera","img.jpg")

            
            elif 'search'  in statement:
                statement = statement.replace("search", "")
                webbrowser.open_new_tab(statement)
                time.sleep(5)	

            elif 'ask' in statement:
                speak('I can answer to computational and geographical questions  and what question do you want to ask now')
                question=takeCommand()
                app_id="E8H76X-T8V8UHPUY2"
                client = wolframalpha.Client('R2K75H-7ELALHR35X')
                res = client.query(question)
                answer = next(res.results).text
                speak(f"the answer is {answer}")
                print(answer)

            elif 'who are you' in statement or 'what can you do' in statement:
                speak('I am Meldrix version 1 point O your personal assistant. I am programmed to minor tasks like'
                    'opening youtube,google chrome, gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather' 
                    'In different cities, get top headline news from times of india and you can ask me computational or geographical questions too!')


            elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
                speak("I was built by YD")
                print("I was built by YD")


            elif "weather" in statement:
                api_key="Apply your unique ID"
                base_url="https://api.openweathermap.org/data/2.5/weather?"
                speak("what is the city name")
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

            elif "log off" in statement or "sign out" in statement:
                speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
                subprocess.call(["shutdown", "/l"])

            count += 1            
    time.sleep(3)
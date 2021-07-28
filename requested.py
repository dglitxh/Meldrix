from actions import *


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
                goodbyes()

            if 'wikipedia' in statement:
                wiki()

            elif 'open youtube' in statement:
                youtube()

            elif 'open google' in statement:
                google()

            elif 'time' in statement:
                clock()

            elif 'news' in statement:
                news()

            # elif "camera" in statement or "take a photo" in statement:
            #     ec.capture(0,"robo camera","img.jpg")

            
            elif 'search'  in statement:
                search()	

            elif 'ask' in statement:
                wolfram()

            elif 'who are you' in statement or 'what can you do' in statement:
                identity()

            elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
                creator()


            elif "weather" in statement:
                weather()

            elif "log off" in statement or "sign out" in statement:
                logout()
            elif "send" or "whatsapp" in statement:
                Whatsapp()

            count += 1            
    time.sleep(3)
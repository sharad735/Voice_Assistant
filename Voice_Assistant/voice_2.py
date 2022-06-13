
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import pyjokes
from datetime import date
import random

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am jarvis. how can i help you?")

def TakeCommand():
    # It takes microphone input from the user & returns string output
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="eng-in")
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)

        print("Say that again please...")
        return "None"
    return query


def SendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("username", "password")
    server.sendmail("username", to, content)
    server.close()





if __name__ == '__main__':
    WishMe()
    while True:

        query = TakeCommand() 
        
        if "wikipedia" in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(result)
            speak(result)

        elif "open youtube" in query:
            webbrowser.open("https://www.youtube.com/")
        
        elif "open google" in query:
            webbrowser.open("https://www.google.com/")
        
        elif "play music" in query:
            music_dir = "E:\\folder\\movies"
            songs = os.listdir(music_dir)
        
            os.startfile(os.path.join(music_dir, random.choice(songs)))

        elif "time" in query:
            strtime = datetime.datetime.now().strftime("%h:%m:%s")
            speak(f"the time is {strtime}")
        
        elif "today date" in query:
            today = date.today()
            d = today.strftime("%B %d, %Y")
            w = datetime.datetime.now().strftime('%A')

            speak(f"Todays date is {d} and today is {w}")
        
        elif "open vs code" in query:
            codepath = "C:\\Users\\abc\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(os.path.join(codepath))
        
        elif "email to sharad" in query:
            SendEmail("username", "Hii")
            try:
                speak("What should i say?")
                content = TakeCommand()
                to = "username"
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("sorry! i am not able to send email")
        
        elif "joke" in query:
            joke1 = pyjokes.get_joke(language="en", category="all")
            speak(joke1)

        elif "old are you" in query:
            
            today = date.today()
            year, month, date = today.year , today.month, today.day
            byear, bmonth, bday = 2022, 6, 6

            agey = year - byear
            agem = month - bmonth
            aged = date - bday

            speak(f"I am {agey} years {abs(agem)} months and {abs(aged)} days old")


        elif "start stopwatch" in query:
            speak("Starting stopwatch")
            exec(open("F:\Project\Python Projcts\stopwatch\stopwatch.py\stopwatch.py").read())
            if "stop" in query:
                continue
        
        elif "Play game" in query:
            speak("which game you would would like to play?")
            speak("1.snake game 2.Dice Roller 3.Rock Paper scissor 4.Guess Number")
            if "snake game" in query:
                exec(open("F:\Project\Python Projcts\Snake_Water\snake_water_game.py").read())
            elif "dice roller" in query:
                exec(open("F:\Project\Python Projcts\Dice Roller\dice.py").read())
            elif "rock paper" in query:
                exec(open("F:\Project\Python Projcts\Rock_Paper_S\rock_paper.py").read())
            elif "guess number" in query:
                exec(open("F:\Project\Python Projcts\Guess_Number\guess_number.py").read())
            elif "exit" in query:
                speak("Thank you! hope you enjoyed gaming")
                continue
            
        elif "open mail" in query:
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
        elif "open whatsapp" in query:
            webbrowser.open("https://web.whatsapp.com/")

        elif "how are you" in query:
            speak("I am fine! hope you are fine as well")

        elif "shut down" in query:
            speak("Are you sure shutdown pc? say yes to shut down")
            if "yes" in query:
                speak("shutting down pc")
                os.system("shutdown /s /t 1")
            else:
                continue
        

        elif "restart" in query:
            speak("Are you sure restart pc? say yes to restart")
            if "yes" in query:
                speak("restarting pc")
                os.system("shutdown /r /t  1")
            else:
                continue

        elif "your name" in query:
            speak("My name is jarvis")
        elif "my name" in query:
            speak("Your name is sharad bhise")
        elif "resume" in query:
            webbrowser.open_new(r'file:///F:/CV/Sharad%20Bhise.pdf')
        
        elif "open flipkart" in query:
            webbrowser.open("https://www.flipkart.com/")


        elif "quit" in query:
            exit()


    # ^^^^Logic for executing task base on query^^^^

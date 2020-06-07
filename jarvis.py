import pyttsx3 as p
import datetime as dt
import speech_recognition as sr
import wikipedia as w
import webbrowser as wb
import os
import smtplib

engine = p.init()
rate = engine.getProperty("rate")
engine.setProperty("rate", 125)
voices = engine.getProperty("voices")
#print(voices[1].id)
engine.setProperty("voice", voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(dt.datetime.now().hour)
    if 12 > hour >= 0:
        speak("good morning")
    elif 18 > hour >= 12:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("I'm ZIRA !! How may I help You")


def takecommond():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        #r.energy_threshold
        audio = r.listen(source)
    try:
        print("recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"user said: {query}\n")
    except Exception as e:
        #print(e)
        print("say that again please...")
        speak("say that again please")
        takecommond()
    return query


def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("vravi8367@gmail.com", "ravi1997")
    server.sendmail("vravi8367@gmail.com", to, content)
    server.close()


if __name__ == '__main__':
    wishme()
    while True:
        query = takecommond().lower()
        # if "search" in query:
        #     speak("searching...")
        #     query = query.replace("wikipedia", "")
        #     results = w.summary(query, sentences=2)
        #     #speak("according to wikipedia")
        #     speak(results)
        #     print(results)
        if "open youtube" in query:
            speak("opening You Tube")
            wb.open("youtube.com")
        elif "open google" in query:
            speak("opening google")
            wb.open("google.com")
        # elif "play music" in query:
        #     music_dir="path"
        #     speak("playing music")
        #     songs=os.listdir(music_dir)
        #     os.startfile(os.path.join(music_dir, song[0]))
        elif "the time" in query:
            time = dt.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The Time is {time}")
            print(time)
        elif "love" in query:
            speak("I love u too baby")
        elif "hello ZIRA" in query:
            speak("hii!!! how may i help you")
        elif "anya" in query:
            speak("anya is a very good girl")
        elif "f***" in query:
            speak("I'm glad to know this")
        elif "open python" in query:
            speak("opening python")
            code = "C:\\Program Files\\Python37\\python.exe"
            os.startfile(code)
        elif "shivani" in query:
            speak("she is beautiful and very important person for you. Tell her bhaw kam khaya kro")
        elif "email" in query:
            try:
                speak("what you say")
                print("what to say")
                content = takecommond()
                to = "monikaverma6927@gmail.com"
                sendEmail(to, content)
                speak("Email has been send")
                print("Your email has been send")
            except Exception as e:
                print(e)
                speak("sorry .I'm not able to send email")
        else:
            speak("searching...")
            query = query.replace("wikipedia", "")
            results = w.summary(query, sentences=2)
            #speak("according to wikipedia")
            speak("according to wikipedia")
            speak(results)
            print(results)
            continue



















import pyttsx3 # text-to-speech conversion library in Python
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import socket


engine = pyttsx3.init('sapi5')
# sapi5 is inbuilt voice in win for taking voices with help of windows
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)
# 0-male and 1-female



# Firstly we have to write Speak function for our project
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Hello Very Good Morning to you ")

    elif hour>=12 and hour<17:
        speak("Hello Very Good afternoon to you ")

    elif hour>=17 and hour<21:
        speak("Hello Very Good evening to you ")

    elif hour>=22 and hour<=23:
        speak("Hello and a Very calm night to you ")

    else:
        speak("Hello ShivMani is only for your care and health if your work is important than you are welcome to shivmani and if not then shivmani wants from you to go to sleep you can come next morning to enjoy our echolite") 

    speak("I am Shivmani your personal voice assistant please tell me How may i help you?")



def takeCommand():
    # it take microphone input from user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2 # time given to user for speak and think
        audio = r.listen(source)

    try:
        print("Recognizing voice...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")


    except Exception:
    #  print(e)
        print("Say that again please...")  
        return "None"
    return query



def sendEmail(to, content):
    server = smtplib.SMTP('smptp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()




if __name__ == "__main__":
    wishMe()
    # while True:
    if 1:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Please wait...Searching wikipedia')
            query = query.replace("wikipedia", "")
            results =  wikipedia.summary(query, sentences=4)
            speak("So,According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
        elif 'open code' in query:
            CodePath = "C:\\Users\\ayush\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(CodePath)
        elif 'email to hidden'in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to = "hiddenikigai123@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry from Shivmani-echo for this , email has not been sent")
#speak(" Welcome to one and only Ayushi Saxena new ShivMani Echo Voice Assistant, if you new to this platform then thankyou for giving your time, and if you know me then kindly share your experience regarding Shivmani")

# logic for executing tasks based on query

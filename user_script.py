import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 15:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am Alpha, at your service sir!")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.8
        audio = r.listen(source)
    try:
        speak("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        query = query.lower()
        if 'good' or 'morning' or 'evening' or 'night' or 'hi' or 'hello' or 'alpha' in query:
            wishMe()
    except Exception as e:
        return "None"
    return query

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.8
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        query = query.lower()
        
    except:
        pass

def bye():
    listen()
    if 'bye' or 'see you' or 'exit' or 'sleep' or 'shut down' in query:


        speak('Bye Sirr!')
        exit()
        
        
        

while True:
    takeCommand()
    listen()
    bye()
    
    
            
    
    
    
    

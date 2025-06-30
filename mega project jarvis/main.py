import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
import google.generativeai as genai 
from gtts import gTTS
import pygame
import os
#pip install pocketsphinx

recognizer  = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "your api keys"

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')
  

# Initialize the mixer
    pygame.mixer.init()

# Load the MP3 file
    pygame.mixer.music.load("temp.mp3")

# Play the music
    pygame.mixer.music.play()

# Keep the script running so the music plays completely
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()
    os.remove("temp.mp3")    


'''def aiprocess(command):
    genai.configure(api_key = "your api key")


    model=genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(command)

    return(response.text)'''

def processCommand(c): 
    if "open google" in c.lower():
       webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
       webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
       webbrowser.open("youtube.com")
    elif "open linkedin" in c.lower():
       webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)
        
    elif "news" in c.lower():
        r= requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get("articles", [])
    
            # Print the top headlines
            print("Top Headlines:\n")
            for i, article in enumerate(data["articles"]):
               speak(f"{i+1}. {article['title']}")
    '''else:
        output = aiprocess(c)
        speak(output)
                '''
        
    
    

       

    

if __name__ == "__main__" :
    speak("Initializing jarvis...")
    while True:
        r = sr.Recognizer()


        
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source,timeout=10,phrase_time_limit=1)
            word= r.recognize_google(audio)  
            if(word.lower()== "jarvis"):
                speak("Ya")

            with sr.Microphone() as source:
                print("jarvis active..")
                audio = r.listen(source)
                command = r.recognize_google(audio) 
                processCommand(command)
        
        except Exception as e:
            speak("Error;{0}".format(e))        
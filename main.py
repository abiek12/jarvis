import speech_recognition as sr
import webbrowser
import pyttsx3
import music_library
import requests

# Initalizing recognizer
recognizer = sr.Recognizer()
# Initializing text to speech
ttsx = pyttsx3.init()
# News api key
newsApiKey = 'b417028aaf2f4f0c801a67cc1e18931c'

# speak function
def speak(text):
    ttsx.say(text)
    ttsx.runAndWait()
    
def fetchNews():
    newsApiUrl = f"https://newsapi.org/v2/everything?country={'in'}&apiKey={newsApiKey}"
    res = requests.get(newsApiUrl)
    if res.status_code == 200:
        # parse the json response
        data = res.json()
        
        # extract the articles
        articles = data.get('articles', [])
        
        for article in articles:
            speak(articles['title'])
            
def invokeAi(query):
    print("Open api call")
    
# Process command
def processCommand(command):
    print(f"command: {command}")
    if "open google" in command.lower():
        speak("Opening google")
        webbrowser.open("https://google.com")
    elif "open youtube" in command.lower():
        speak("Opening youtube")
        webbrowser.open("https://youtube.com")
    elif "play" in command.lower().startswith("play"):
        song = command.lower().split(" ")[1]
        music_library.items[song]
    elif "news" in command.lower():
        # query = command.lower().startswith(" ")[1]
        fetchNews()
    else: 
        # open api call
        invokeAi(command.lower())
    

if __name__ == '__main__':
    speak("Intializing jarvis")
    while True:
        # Listen for wake word
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            try:
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
                command = r.recognize_google(audio)
                print("Google Speech Recognition thinks you said " + command)
                if(command.lower() == "hello"):
                    speak("Yes, sir")
                    # Listen for next commands
                    with sr.Microphone() as source:
                        print("Jarvis is active...")
                        audio = r.listen(source, timeout=2, phrase_time_limit=1)
                        command = r.recognize_google(audio)
                        # Process command
                        processCommand(command)
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
            except Exception as e:
                print("Error", e)
        
    
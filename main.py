import speech_recognition as sr
import webbrowser
import pyttsx3

# Initalising recognizer
recognizer = sr.Recognizer()
ttsx = pyttsx3.init()

# speak function
def speak(text):
    ttsx.say(text)
    ttsx.runAndWait()

if __name__ == '__main__':
    speak("Hey how are you!")
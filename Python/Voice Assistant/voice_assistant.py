import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random


# sapi5 to get the voices in windows(pre-existing voices in windows - 2(Male,Female))
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# print(voices[0].id)

# To get the voice from the system
engine.setProperty('voice', voices[0].id)


# To get the output audio
def speak(audio):
    '''Gives audio as output'''
    engine.say(audio)
    engine.runAndWait()


# Wish you according to current time
def wishMe():
    '''Wish you according to current time'''
    hour = int(datetime.datetime.now(
    ).hour)  # datetime module to get the current time, especifically hour in this case
    if (hour >= 0 and hour < 12):
        speak("Good Morning!")
    elif (hour >= 12 and hour < 16):
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("My name is David. How can i help you?")


def takeCommand():
    '''It takes microphone input from the user and returns string output'''

    r = sr.Recognizer()  # Helps in recognising audio
    with sr.Microphone() as source:
        print("Listening......")
        # Seconds of non-speaking audio before a phrase is considered complete
        r.pause_threshold = 1
        audio = r.listen(source)

    # If there is an error
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f'user said: {query}\n')

    except Exception as e:
        print(str(e))
        if str(e) == "recognition connection failed: [Errno 11001] getaddrinfo failed":
            speak("Please connect to the Internet!!")
        else:
            speak("Say that again please......")
        return 10
    return query


# Do not run in inherited files
if __name__ == "__main__":

    speak("Hello.")
    wishMe()
    while True:

        q = takeCommand()
        while (q == 10):
            q = takeCommand()
        query = q.lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching wikipedia.........")
            query = query.replace("wikipedia", "")
            # First 2 sentences of wikipedia
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
            break
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            break
        elif 'open google' in query:
            webbrowser.open("google.com")
            break
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            break
        elif 'play music' in query or 'play some music' in query or 'play a song' in query:
            speak("playing music")
            music_dir = 'C:\\Users\\Pranav Srivastav\\OneDrive\\Documents\\Music'
            songs = os.listdir(music_dir)
            ans = random.randrange(0, len(songs))
            os.startfile(os.path.join(music_dir, songs[ans]))
            break
        elif 'play video' in query or 'play a video' in query:
            speak("Playing video from brooklyn nine nine")
            video_dir = 'C:\\Users\\Pranav Srivastav\\Videos\\Brooklyn 99'
            videos = os.listdir(video_dir)
            ans = random.randrange(0, len(videos))
            os.startfile(os.path.join(video_dir, videos[ans]))
            break
        elif 'the time' in query or 'tell time' in query or 'tell me the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f'The time is {strTime}')
        elif 'open vs code' in query:
            speak("opening vs code")
            codePath = "C:\\Users\\Pranav Srivastav\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            break
        elif 'open browser' in query or 'open chrome' in query:
            speak("opening browser")
            browserPath = "C:\\Program Files\\Google\\Chrome\\Application\\Chrome.exe"
            os.startfile(browserPath)
            break
        elif 'open whatsapp' in query:
            speak("opening whatsapp")
            appPath = "C:\\Users\\Pranav Srivastav\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(appPath)
            break
        elif 'your name' in query:
            speak("My name is David")
        elif 'your gender' in query:
            speak("I identify myself as a Voice Assistant.")
        elif 'how are you' in query:
            speak("I am good. How are you?")
        elif 'i am good' in query or 'i am fine' in query or 'i am also good' in query or 'i am also fine' in query:
            speak("Okay, Good to hear that. How can i help you?")
        elif 'not good' in query or 'sad' in query:
            speak("Why? What happened? Can i do something for you?")
        elif 'stop' in query or 'end' in query or 'quit' in query:
            break
        elif 'thank you' in query:
            speak("You're Welcome")
            break
        elif 'hi david' in query or 'hello david' in query:
            speak("Hello there. How can i help you?")
        else:
            speak("Please try again!")

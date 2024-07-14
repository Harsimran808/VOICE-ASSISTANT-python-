# importing all the modules that we need
import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI

# Recognizer object to recognize our voice
# Recognizer() is a class that helos us to take speech_recognisation function
recognizer = sr.Recognizer()

# initialising pyttsx3 engine
engine = pyttsx3.init()
news_api = "58d4f6a3cde7408685e3331b811d007c"

# The comp will speak to our commands  and this is PYTTSX3 documentation
# runAndWait command helps to wait the func until the commond is not spkoen
def speak(text):
    engine.say(text)
    engine.runAndWait()


# function to process commands using ai
def aiprocess(command):
    client = OpenAI(
        api_key="sk-proj-7OoBvhfnUa8eWzABSPsDT3BlbkFJxBsM46VebfTmVYMwokJb",
    )

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud",
            },
            {"role": "user", "content": command},
        ],
    )

    return completion.choices[0].message.content


# making function to run our commands after activating Jarvis
def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open X" in c.lower():
        webbrowser.open("https://X.com")
    elif "open chatgpt" in c.lower():
        webbrowser.open("https://chatgpt.com")

    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]  # if we said play believer then ["play","believer"]
        link = musicLibrary.my_music[song]
        webbrowser.open(link)

    elif "news" in c.lower():  # use news word in your comand like "Tell me the news"
        r = requests.get(
            f"https://newsapi.org/v2/top-headlines?country=in&apiKey={news_api}"
        )

        if r.status_code == 200:  # check whether http request was successfull
            data = (
                r.json()
            )  # JSON is used for getting data as text and stor it in data dictionary

            # extract the articles
            articles = data.get("articles", [])  # to extract data from dictionary

            # speak as well as print the headlines of top INDIAN news
            for article in articles:
                speak(article["title"])
                print(article["title"])

    # use of else to integrate with openAI, so openAI can handle given command
    else:
        output = aiprocess(c)
        speak(output)


# if the file is running on actual prog
if __name__ == "__main__":

    # Speech_recognition documentation
    speak("Jarvis is ready to Launch....")
    while True:
        # listen for the wake word "Jarvis"
        # obtain audio from microphone
        r = sr.Recognizer()

        print("Recognizing....")

        # try is used to run code wheteher it gets an error
        try:

            # sr.microphone is used to get audio in real-time
            with sr.Microphone() as source:
                print("Jarvis is Listening....")
                audio = r.listen(
                    source, timeout=2, phrase_time_limit=1
                ) 
                # timeout is used for time limit to speak of 2 sec
                # and phrase_time_limit is used for one word to wake up jarvis
            word = r.recognize_google(audio)

            # to activate jarvis if user spoke "jarvis"
            if word.lower() == "jarvis":
                speak("Yes Iron man")

                # listen for command
                with sr.Microphone() as source:
                    print("Jarvis is Active")
                    audio = r.listen(source)
                    
                    # to recognize further commands
                    command = r.recognize_google(audio)

                    processcommand(command)

        except Exception as e:
            print("Error; {0}".format(e))

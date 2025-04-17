import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary


activation_words = ["jarvis", "jarvish", "jaarvish", "jervis", "gervis"]


recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    """Function to convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def processcommand(c):
    if "open google" in c.lower():
        speak("opening")
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        speak("opening")
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        speak("opening")
        webbrowser.open("https://youtube.com")
    elif "open linkdin" in c.lower():
        speak("opening")
        webbrowser.open("https://linkdin.com")
    elif "open gpt" in c.lower():
        speak("opening")
        webbrowser.open("https://chatgpt.com/?model=auto")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link=musicLibrary.music[song]
        webbrowser.open(link)
    pass

if __name__ == "__main__":
    speak("hello, i am jaarvish, your virtual assistance!")
    while True:
        # create a reconizer instence 
        r = sr.Recognizer()
        print("Recognition...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source)
            word = r.recognize_google(audio).lower()

            if word in activation_words:
                speak("Yes, how can I assist?")

                # this is leasten for command 
                with sr.Microphone() as source:
                    print("Jarvis activated...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processcommand(command)

        except sr.UnknownValueError:
            print("Could not understand the audio.")
        except sr.RequestError as e:
            print(f"Recognition error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

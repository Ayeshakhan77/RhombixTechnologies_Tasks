import speech_recognition as sr
import datetime
import subprocess
import pywhatkit
import pyttsx3
import webbrowser

# Initialize the text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 0 for male voice, 1 for female voice

# Initialize the recognizer
recognizer = sr.Recognizer()

def speak(text):
    """Function to speak the given text"""
    engine.say(text)
    engine.runAndWait()

def cmd():
    with sr.Microphone() as source:
        print("Clearing the background noises... Please wait")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print("Ask me anything...")
        recordedaudio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(recordedaudio)
            print("You said: " + format(command))
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that. Could you please repeat?")
            return None
        except sr.RequestError:
            speak("Sorry, my speech service is down. Please try again later.")
            return None

def run_assistant():
    while True:
        command = cmd()
        if command:
            if 'play' in command:
                song = command.replace('play', '')
                speak('Playing ' + song)
                pywhatkit.playonyt(song)
            elif 'time' in command:
                time = datetime.datetime.now().strftime('%I:%M %p')
                speak('The current time is ' + time)
            elif 'open' in command:
                website = command.replace('open', '').strip()
                url = 'https://www.' + website + '.com'
                webbrowser.open(url)
                speak('Opening ' + website)
            elif 'exit' in command or 'stop' in command:
                speak('Goodbye!')
                break
            else:
                speak("I'm sorry, I don't know how to do that.")

if __name__ == "__main__":
    speak("Hello, I am your voice assistant. How can I help you today?")
    run_assistant()
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print('recoginizing..')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
                print(command)

    except:
        pass
    return command

def run_alia():
    talk('welcome sir')
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is' + time)
    elif 'he is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person,5)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry I have some work')
        print(command)
    elif 'love' in command:
        talk('Yeah I do')
        print(command)
    elif 'hi' in command:
        talk('I am jarvis. I am the famous artificial intelligence voice assistant ')
    elif 'where are you living' in command:
        talk('I am living in internet')
        print(command)
    elif 'who invented you' in command:
        talk('I am invented by kishore')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
        print(talk)
    elif 'siri' in command:
        talk('Sorry, Not recognized ')
        talk('sorry boss')
        command = command.replace('welcome boss', '')
    else:
        talk('Hey repeat that again')
while True:

   run_alia()

import speech_recognition as sr 
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)
engine.say('Hello Anirban Sir, i am ready to service you')
engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('Your Alexa is listening....')
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if 'alexa' in command:
                command=command.replace('alexa','')
                print(command)
    except:
        pass
    return command

def run_alexa():
    command=take_command()
    if 'play' in command:
        song=command.replace('play','')
        print('playing'+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%H:%M %p')
        print('current time is: '+time)
    elif 'who is' in command:
        person=command.replace('who is','')
        info=wikipedia.summary(person,1)
        print('Here are the details------'+info)
    elif 'date' in command:
        print('No please keep distance')
    elif 'are you single' in command:
        print('I am in a relationship')
    elif 'having fun' in command:
        print('Yes njoying with 6 others like nabarun bhunia')
    elif 'joke' in command:
        print(pyjokes.get_joke())
    else:
        print('Please say the command again!!')

while True:        
    run_alexa()
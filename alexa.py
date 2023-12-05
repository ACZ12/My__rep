import speech_recognition as sr,pyttsx3,pywhatkit,datetime,wikipedia,pyjokes
listener=sr.Recognizer()
engine=pyttsx3.init()
engine.say("i am alexa")
engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if "alexa" in command:
                command=command.replace("alexa","")
                print (command)
    except:
        pass
    return command


def run_alexa():
    command=take_command()
    print(command)
    if "repeat" in command:
        command=command.replace("repeat","")
        engine.say(command)
        engine.runAndWait()
    elif "play" in command:
        song=command.replace("play","")
        print(command)
        engine.say("playing"+song)
        engine.runAndWait()
        pywhatkit.playonyt(song)
    elif "time" in command:
        time=datetime.datetime.now().strftime("%H:%M:%S")
        engine.say("the current time is"+time)
        engine.runAndWait()
    elif "wikipedia" in command:
        command=command.replace("wikipedia","")
        print(command)
        info=wikipedia.summary(command,3)
        print(info)
        engine.say(info)
        engine.runAndWait()
    elif "joke" in command:
        engine.say(pyjokes.get_joke())
        engine.runAndWait()
    else:
        engine.say("please repeat your command")
        engine.runAndWait()

while 1:
    run_alexa()
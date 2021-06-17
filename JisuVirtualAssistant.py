import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser

listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 125)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('I am listening...')
            voice = listener.listen(source, phrase_time_limit=6, timeout=3600)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jisu' in command:
                command = command.replace('jisu', '')
                print(command)
            if 'hey jisu' in command:
                command = command.replace('hey jisu', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'Take me' or 'navigate me' in command:
        if 'fess' or "payment" in command:
            webbrowser.open(
                "http://122.252.249.26:88/Forms/welcomejisu.html", new=1)
        elif 'result' in command:
            webbrowser.open(
                "http://jisexams.in/JISEXAMS/StudentServices/frmViewStudentGradeCardResult.aspx", new=1)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'thank you' in command:
        talk('you are most welcome')
    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'who' in command:
        if 'saikat maity' in command:
            talk('Dr. Saikat Maity is the Head of The Department of Computer Science and Engineering in J I S UNIVERSITY')
        elif 'kamalika datta' in command:
            talk('Dr. Kamalika Datta is a Asosiate Professor Of Department of Computer Science in J I S UNIVERSITY')
        elif 'mainak biswas' in command:
            talk('Dr.Mainak Biswas is a Asosiate Professor Of Department of Computer Science in J I S UNIVERSITY')
        elif 'indranil sengupta' in command:
            talk('Dr.Indranil Sengupta is the Vice Chancellor of J I S University')
    else:
        talk('Please say the command again.')


while True:
    run_alexa()

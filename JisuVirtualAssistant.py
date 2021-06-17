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


def run_jisu():
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
        elif 'notice' in command:
            webbrowser.open(
                "https://www.jisuniversity.ac.in/notice-board.php", new=1)
        elif 'admission' in command:
            webbrowser.open(
                "http://122.252.249.26:148/Forms/frmRegistration.aspx", new=1)
        elif 'JIS UNIVERSITY' in command:
            webbrowser.open(
                "https://www.google.com/maps?saddr=My+Location&daddr=JIS+UNIVERSITY,+Jis+University,+Nilgunj+Road,+Jagarata+Pally,+Deshpriya+Nagar,+Agarpara,+Kolkata,+West+Bengal", new=1)
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
        elif 'Nilanjan Day' in command:
            talk('Dr. Nilanjan Dey is a Asosiate Professor Of Department of Computer Science in J I S UNIVERSITY')
        elif 'indranil sengupta' in command:
            talk('Dr.Indranil Sengupta is the Vice Chancellor of J I S University')
    elif 'what' in command:
        if 'address' in command:
            talk('The Address of JIS UNIVERSITY is Agarpara Campus, Kolkata 81,Nilgunj Road,Agarpara, Kolkata-700109.')
        if 'mail' in command:
            talk('the Mail id of JISU UNIVERSITY is admission@jisuniversity.ac.in  for  Admission related Queries and  info@jisuniversity.ac.in for any Other Queries ')

    else:
        talk('Please say the command again.')


while True:
    run_jisu()

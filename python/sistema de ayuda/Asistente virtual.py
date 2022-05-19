import speech_recognition as sr
import pyttsx3
import Config

listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            pc = listener.listen(source)
            rec = listener.recognize_google(pc)
            rec = rec.lower()

            if Config.name in rec:
                rec = rec.replace(Config.name,'')

    except:
        pass
    return rec


def run():
    rec = listen()
    if 'reproduce' in rec:
        yotube = rec.replace('reproduce','')
        print("Reproducinedo" + yotube)
        talk("Reproduciendo")

if __name__ == '__main__':
    run()
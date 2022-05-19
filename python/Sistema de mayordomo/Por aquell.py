import speech_recognition as sr
import pyttsx3
#import pywhatkit
#import Config

# r = sr.Recognizer()
# mic = sr.Microphone()

# with mic as source:
#     print("Escuchando..")
#     r.adjust_for_ambient_noise(source)
#     audio = r.listen(source)   
#     rec = r.recognize_google(audio,language="Spanish",show_all=True)
#     print(rec)


listener = sr.Recognizer()

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

try:
    with sr.Microphone() as source:
        print("Escuchando...")
        listener.adjust_for_ambient_noise(source)
        voice = listener.listen(source)
        rec = listener.recognize_google(voice,language="es")
        print(rec)

except:
    pass
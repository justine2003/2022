from asyncore import write
from re import I
import speech_recognition as sr
import subprocess as sub
import pyttsx3,pywhatkit , re
import Config, Otros 

Exit = False

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
            print("Escuchando")
            listener.adjust_for_ambient_noise(source)
            pc = listener.listen(source)
            rec = listener.recognize_google(pc,language="es")
            print(rec)
            
    except:
        pass
    return rec

def run():
 try:
      global Exit
      while Exit == False:
          rec = listen()
        
          if 'Reproduce' in rec:
             music = rec.replace('Reproduce','')
             print("Reproduciendo"+music)
             talk("Reproduciendo"+music)
             pywhatkit.playonyt(music)

          elif 'Abrir' in rec or 'abrir' in rec :
            rec = rec.lstrip('Abrir')
            rec = rec.lstrip('abrir')
            print(rec)
            Otros.llamarRuta(rec)
            
                    
          elif 'Cerrar' in rec:
           for app in  Config.programs:
             if app in rec:
               talk(f'Abriendo {app}')
               sub.Pclose(Config.programs[app])

          elif 'Buscar' in rec:
            for site in Config.sites:
             if site in rec:
               sub.call(f'start brave.exe {Config.sites[site]}',shell=True)
               talk(f'Buscnado {site}')

#         elif 'Dictado' in rec:


          elif 'salir' in rec:
             Exit=True
             talk("Asta pronto")
        
 except:
     print("Repita lo que dijo")

if __name__ == '__main__':
    run()
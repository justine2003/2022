from aifc import Error
from tkinter import E
import speech_recognition as sr
import subprocess as sub
import pyttsx3,pywhatkit
import Config, os

Exit = False
atp = None

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
            talk("Escuchando")
            listener.adjust_for_ambient_noise(source)
            pc = listener.listen(source)
            rec = listener.recognize_google(pc,language="es")
            print(rec)
            
    except:
        pass
    
    try:
      return rec
    except:
      rec = ""
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
            app = rec.replace('Abrir','')
            app = rec.replace('abrir','')
            print(app)
            talk('Abriendo'+app)
            llamarRuta(app,1)
            
                    
          elif 'Cerrar' in rec or 'cerrar' in rec:
           for app in  Config.programs:
             if app in rec:
               talk(f'Cerrando {app}')
               llamarRuta(app,0)

          elif 'Buscar' in rec:
            for site in Config.sites:
             if site in rec:
               sub.call(f'start brave.exe {Config.sites[site]}',shell=True)
               talk(f'Buscando {site}')

         
          elif 'Dictado' in rec:

            r = sr.Recognizer()          

            with sr.Microphone() as source:
              print("listo para escribir")
              audio = r.listen(source)

              try:
                text = r.recognize_google(audio,language="es-ES")
                print("What did you say: {}".format(text))
              except:
                print("Sorry")


          elif 'salir' in rec:
             Exit=True
             talk("Asta pronto")
        
 except Error:
     Exit=True
     talk("Asta pronto")


def llamarRuta(app,numm):
  global atp

  num = 0

  if numm == 1:
      app = app.lstrip()  
      
      for ap in Config.programs:
        if ap in app:
          atp = sub.Popen(Config.programs[app])
        else:
          num += 1

      while num == len(Config.programs):
        target = app+".exe"
        initial_dir = 'C:\\'
        path_list = [os.path.join(root, target) for root, _, files in os.walk(initial_dir)
                                                                       if target in files]

        sub.Popen(path_list)
        num = 0
  
  else:
    atp.terminate()

def Ayuda():
    run()

if __name__ == "__main__":
    Ayuda()
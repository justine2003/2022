import speech_recognition as sr

nameUser = "Justin"
name = "computadora"

programs = {
    'WhatsApp':r"C:\Users\justi\AppData\Local\WhatsApp\WhatsApp.exe",
    'visual':r"C:\Users\justi\AppData\Local\Programs\Microsoft VS Code\Code.exe",
    'navegador':r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe",
    'Excel':r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE",
    'Word':r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE",
    'Powerpoint':r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE",
    'Adobe':r"C:\Program Files\Adobe\Adobe Illustrator 2021\Support Files\Contents\Windows\Illustrator.exe"
}

sites = {
   'universidad':"https://www.fidelitasvirtual.org/moodle3/login/index.php",
   'Discord':"https://discord.com/channels/@me",
   'yotube':'yotube.com',
   'YouTube':'yotube.com',
   'Telegram':"https://web.telegram.org/k/",
   'Khan Academy':"https://khanacademy.org/",
   'khanacademy':"https://khanacademy.org/",
   'can academic':"https://khanacademy.org/",
   'correo':"https://gmail.com/"
}

r = sr.Recognizer()         

with sr.Microphone() as source:
    print("listo para escribir")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio,language="es-ES")
        print("What did you say: {}".format(text))
    except:
        print("Sorry")
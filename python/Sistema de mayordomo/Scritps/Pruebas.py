import os
import pathlib
from tkinter import Tk, Tcl
from tkinter.filedialog import askdirectory

def Prueba():
   Tk().withdraw()
   filename = askdirectory(initialdir="C://")
   path = pathlib.Path(filename).absolute()
   
   videos = list(filter(lambda name: ".exe" in name,videos))

   for index, content in enumerate(videos):
       print(f"video{index}:{content}")


def find_files(filename, search_path):
   result = []

# Wlaking top-down from the root
   for root, dir, files in os.walk(search_path):
      if filename in files:
         result.append(os.path.join(root, filename))
   return result

print(find_files("Brave.exe","C:"))
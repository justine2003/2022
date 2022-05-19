import subprocess as sub
import Config
import fnmatch
import os


def llamarRuta(ap):   
   num = 0

   for app in Config.programs:
    if app in ap:
       sub.Popen(Config.programs[app])
    else:
       num += 1
   
   while num == len(Config.programs):
      try:
         target = app+".EXE*"
         initial_dir = 'C:\\'
         path_list = [os.path.join(root, file) for root, _, files in os.walk(initial_dir)
                                                for file in fnmatch.filter(files, target)]
         sub.Popen(path_list[0])
      
      except:
         print("Esto es lo que entendi",ap)

llamarRuta("brave")

"""""
def prueba():

   if app in Config.programs:
      sub.Popen(Config.programs[app])
   else:
         dir_base = 'C:\\'
         fichero_requerido = 'Excel.EXE'
         for root, folders, files in os.walk(dir_base):
            for file in files:
               if file == fichero_requerido: 
                  print('Encontrado '+file+' en '+os.path.join(root, file))
                  sub.Popen(os.path.join(root))
                  break

"""


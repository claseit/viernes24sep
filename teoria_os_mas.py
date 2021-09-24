import os
import sys
import shutil
import time
import subprocess

"""
● os.listdir() #retorna una lista de archivos
● os.getcwd() #retorna el dicterio actual
● os.mkdir() # crea una carpeta, no retorna nada
● os.path.exists() # existe un directorio? Retorna True or False
● os.rename() # cambia el nombre de cualquier archivo, sin retorno
● os.remove() # sirve para eliminar un archivo, sin retorno
● os.rmdir() # eliminar un directorio vacio, sin retorno

● os.system() # como escribir  en la consola del so 
● os.name # ver sistema operativo, retorna el nombre del so lo mismo con sys.platform

● shutil.copy() # copia archivos, sin retorno
● shutil.move() # mueve archivos, sin retorno
● shutil.rmtree() # elimina directorios con archivos, sin retorno


"""

p = subprocess.run(["pip","list"], capture_output=True, encoding="cp850")
# p.stdout contiene el resultado del comando como una cadena.
datos = p.stdout

elementos = datos.split()

final = elementos[4::2]

f = open("modulos.txt","w")
for n in final:
    f.write(n+"\n")
f.close()
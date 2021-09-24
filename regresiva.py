import sys
import time


ayuda = """
Ayuda del programa:
Este es un programa que permite realizar una cuenta regresiva
Se puede pasar un argumento numerico "ENTERO", para realizar
la cuenta atras desde ese argumento hasta cero.
Ejemplo:
regresiva.py 5
5
4
3
2
1
0

Tambien si no se pasa el argumento y se llama al programa sin el mismo
se toma automaticamente como 10 el mismo. 

"""

argumentos = sys.argv

try:
    primero = argumentos[1]
    if primero.lower() == "-h" or  primero.lower() == "-help":
        print(ayuda)
        sys.exit()
    else:
        try:
            numero = int(primero)
        except ValueError:
            print("Solo argumentos enteros")
            sys.exit()
except IndexError:
    numero = 10


for n in range(numero,-1,-1):
    print(n)
    time.sleep(1)
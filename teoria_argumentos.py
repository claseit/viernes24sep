import sys


argumentos = sys.argv

try:
    print("Hola",argumentos[1])
except IndexError:
    print("Falta argumento")
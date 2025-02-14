from os import system
import sys

def XScreen():

    if sys.platform == "linux" or sys.platform == "darwin":
        system("clear")
    else:
        system("cls")

def LLScreen():
    if sys.platform == "linux" or sys.platform == "darwin":
        input("Presione una tecla para continuar")
    else:
        system("pause")
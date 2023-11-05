# Programul FizzBuzz
"""Scrieti un program care printeaza in consola numerele de la 1 la 100.
La multiplu de 3 scrieti “Fizz” in locul numarului, la multiplu de 5 scrieti “Buzz” in locul numarului.
La multiplu de 3 si 5 scrieti in consola “FizzBuzz” in locul numarulu"""

from time import sleep
import os
import sys
from generare_fisier import generare, generare_dialog


var: str = "Incepe jocul, asteapta"
print(var)
os.system('cls')
sleep(2)
for _ in range(4):
    os.system('cls')
    sleep(2)
    var = var + '.'
    print(var)
    sleep(2)
os.system('cls')

# Descrierea...
print('Scrieti un program care printeaza in consola numerele de la 1 la 100.')
sleep(2)
print('La multiplu de 3 scrieti “Fizz” in locul numarului, la multiplu de 5 scrieti “Buzz” in locul numarului.')
sleep(2)
print('La multiplu de 3 si 5 scrieti in consola “FizzBuzz” in locul numarulu')

raspuns: str = input('Apasa "Enter",fara nici un caracter in consola pt a continua: ')

# Stresarea userului v 1.1
while raspuns != '':
    raspuns: str = input('Hey!!! am zis sa apesi tasta "Enter",fara nici un caracter in consola pt a continua: ')
os.system('cls')
print('Incepe numaratoarea...')
sleep(3)

# Initierea iteratiei for....
for num in range(1, 101):
    sleep(0.3)
    if num % 3 == 0 and num % 5 == 0:
        print(f"Numarul {num} este: \"FizzBuzz\"")
    elif num % 3 == 0:
        print(f"Numarul {num} este: \"Fizz\"")
    elif num % 5 == 0:
        print(f"Numarul {num} este: \"Buzz\"")
    else:
        print(num)
# stresarea userului v 1.2
var1: str = input("Apasa \"Enter\" pentru a iesi din program ")
while var1 != '':
    var1: str = input("Hey!!! am zis sa apesi tasta \"Enter\"!!! pentru a iesi din program ")
else:
    os.system('cls')
    print("Bine....ies din program...")
    sleep(3)
    generare()
    generare_dialog()
    sys.exit()

# 2. Convertir Grados Celsius a Grados Fahrenheit.

import os
os.system('clear')

print("Convertir grados Celsius a Farenheit!")
a=float(input("ingrese la temperatura: " ))
c=input("ingrese la 'c' si quiere convertir a celsius o f a farenheit: ")

def temperaturas(temp,conv):
    if conv=="c":
        res=(temp*1.8)+32
        calc=print("Los "+str(temp)+" grados celcius, son "+str(res)+" grados farenheit")
    elif conv=="f":
        res=(temp-32)*(5/9)
        calc=print("Los "+str(temp)+" grados farenheit, son "+str(res)+" grados celsius")
    return calc

print(temperaturas(a,c))
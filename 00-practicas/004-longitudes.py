# 4. Hacer un Programa que calcule longitudes de Circunferencia.

import os
import math

os.system("clear")

print("Longitudes de las circunferencias")
d=float(input("Escriba el diametro: "))

def longitudes(diametro):
    longitud=math.pi*diametro
    respuesta=print("La longitud es de: "+str(longitud))
    return respuesta

longitudes(d)
print("fin")
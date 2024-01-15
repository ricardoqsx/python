# 5. Hacer un Programa que calcule áreas de trapecios. 

import os

print("Area de los trapecios!")
a=float(input("Escriba el valor de un lado paralelo: "))
b=float(input("Escriba el valor del otro lado paralelo: "))
c=float(input("Escriba el valor de la altura: "))

def trapecios(a,b,h):
    A=(a+b)*h/2
    res=print("El area del trapecio es de: "+str(A))
    return res

trapecios(a,b,c)
print("fin")
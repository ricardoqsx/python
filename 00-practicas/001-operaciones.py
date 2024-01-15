# 1. Pedir 2 números al usuario y sumarlos, restarlos, multiplicarlos y dividirlos. 

import os
os.system('clear')

a=int(input("Escriba el 1er valor: "))
b=int(input("Escriba el 2ndo valor: "))
c=input("escriba el simbolo (+, -, * o /: ): ")

def operaciones(valor1,valor2,simbolo):
    d=0
    if c =="+":
        d=a+b
    elif c=="-":
        d=a-b
    elif c=="*":
        d=a*b
    elif c=="/":
        d=a/b
    else:
        d="El simbolo descrito no es correcto"
    return d

print(operaciones(a,b,c)) # los nombres de las variables no necesariamente 
                        # tienen que ser los mismos que sean datos de entrada
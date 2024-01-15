# 6. Calcule la media aritmética de 3 números cualesquiera.
import os
os.system("clear")
print("Media aritmetica!")

def media():
    a=float(input("Escriba el primer valor: "))
    b=float(input("Escriba el segundo valor: "))
    c=float(input("Escriba el tercer valor: "))
    d=(a+b+c)/3
    print("la media es: "+str(d))

media()
print("fin")
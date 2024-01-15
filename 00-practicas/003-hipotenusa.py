#3. Sacar la hipotenusa de un triángulo rectángulo, pidiendo al usuario el valor de los 2 catetos. 


import os

os.system("clear")
print("Cual es la hipotenusa?")

v1=float(input("Escriba el valor de un cateto: "))
v2=float(input("Escriba el valor del otro cateto: "))

def hipotenusa(a,b):
    c=a**2+b**2
    d=print("el valor de la hipotenusa es: "+str(c))
    return d

hipotenusa(v1,v2)
print("fin")
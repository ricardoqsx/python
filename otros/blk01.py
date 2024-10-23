import os
os.system('clear')
print("Bienvenido al bloque 1!!!")
a=float(input("escriba el primer valor: "))
b=float(input("Escriba el segundo valor: "))
c=float(input("Escriba un tercer valor: "))
print("\n")

def mi_info():
    nombre: str = "Ricardo"
    edad: int = 33
    peso: int = 190
    altura: float = 1.75
    print("hola "+nombre+"\n"+ \
          "tienes "+str(edad)+"\n"+ \
          "un peso de "+str(peso)+"\n"+\
          "y una altura de "+str(altura))
mi_info()

def operaciones(a,b):
    print("Vamos a realizar operaciones!")
    c=a+b
    d=a-b
    e=a*b
    f=a/b
    g=a%b
    print("La suma de "+str(a)+" y "+str(b)+" es igual a "+str(c)+"\n"+\
          "La resta de "+str(a)+" y "+str(b)+" es igual a "+str(d)+"\n"+\
          "La multiplicacion de "+str(a)+" y "+str(b)+" es igual a "+str(e)+"\n"+\
          "La division de "+str(a)+" y "+str(b)+" es igual a "+str(f)+"\n"+\
          "El modulo de "+str(a)+" y "+str(b)+" es igual a "+str(g))
operaciones(a,b)

def logica(n1, n2):
    igual=n1==n2
    dif=n1!=n2
    may=n1>n2
    men=n1<n2
    mayig=n1>=n2
    menig=n1<=n2

    print(f"""¿el primer numero es igual al segundo? {igual}
    ¿el primer numero es diferente al segundo? {dif}
    ¿el primer numero es mayor al segundo? {may}
    ¿el primer numero es menor al segundo? {men}
    ¿el primer numero es mayor o igual al segundo? {mayig}
    ¿el primer numero es menor igual al segundo? {menig}""")
    print("\n")
logica(a,b)

def oplogic(b1,b2,b3):
    op_and = (b1==b2) and (b3>0)     # si b1 es igual a b2 y b3 es mayor a cero
    op_or = (b1!=b2) or (b3>0)       # si b1 es diferente a b2 o b3 sea mayor a cero 
    op_not = (b3>=b1) or not (b2!=0) # si b3 es mayor o igual o b2 no es distinto a cero

    print(f"si b1 es igual a b2 y b3 es mayor a cero? = {op_and}")
    print(f"si b1 es diferente a b2 o b3 sea mayor a cero? = {op_or}")
    print(f"si b3 es mayor o igual o b2 no es distinto a cero? = {op_not}")
oplogic(a,b,c)

def light():
    LIGHT = 299792458
    print(f"el valor de la velocidad de la luz es {LIGHT} m/s")
light()

def concatenacion():
    nombre = "Ricardo "
    apellido = "Quiroz"
    nombre_completo=nombre+apellido
    print(f"Hola {nombre_completo} espero estes bien")
concatenacion()

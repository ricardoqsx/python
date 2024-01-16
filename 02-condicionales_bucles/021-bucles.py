import math

# Bucles
# existen 2 tipos

# bucle determinado
# se sabe cuantas veces se ejecutara

# bucle indeterminado
# dependera de las circunstancias durante la ejecucion del programa

# ejemplo: 
# while condicion:
#     print("cuerpo del bucle")

# c=0 

"""while c<10:
    print("Hola")
    c=c+1
print("afuera del bucle") """

cc=1
edad=(int(input("Escribe tu edad por favor: ")))

while edad<0 or edad>100 :
    print("Edad no valida")
    edad=(int(input("Escribe tu edad: ")))
    cc+=1
    if cc==4:
        print("numero maximo de intentos")  # aqui define una cantidad maximo de intentos en un bucle indeterminado ya que se anida el while con el if
        break                               # break permite que si la condicion se cumple, el programa termina en ese momento
print("gracias, puedes pasar")
print("edad del usuario "+str(edad ))

# otro problema

print("Este programa halla la raiz cuadrada de un valor numerico")

num=int(input("Escribe un numero: "))

intentos=0

while num<0:
    print("el valor numerico no puede ser negativo")
    num=int(input("introduce un numero: "))
    intentos=intentos+1
    if intentos==5:
        break

if intentos==5:
    print("Lo siento, no puedo realizar el calculo")
else:
    print(math.sqrt(num))
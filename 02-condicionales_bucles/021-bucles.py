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
edad=(int(input("Escribe tu edad: ")))

while edad<0 or edad>100 :
    print("Edad negativa, no valida")
    edad=(int(input("Escribe tu edad: ")))
    cc+=1
    if cc==4:
        print("numero maximo de intentos")
        break                               # break permite que si la condicion se cumple, el programa termina en ese momento
print("gracias, puedes pasar")
print("edad del usuario "+str(edad ))

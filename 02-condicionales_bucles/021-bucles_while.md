`import math`

# Bucles

- existen 2 tipos

#Bucle While
	# bucle indeterminado
	# dependera de las circunstancias durante la ejecucion del programa

### ejemplo: 

```
while condicion:
    print("cuerpo del bucle")
```

### otro ejemplo:

```
c=0 

while c<10:
    print("Hola")
    c=c+1
print("afuera del bucle")

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
```

### otro problema

```
print("Este programa halla la raiz cuadrada de un valor numerico")

num=int(input("Escribe un numero: "))

intentos=0

while num<0:
    print("el valor numerico no puede ser negativo")
    num=int(input("introduce un numero: "))
    intentos=intentos+1
    if intentos==5:
        break
```

- aqui se toma en cuenta q mientras el numero sea menor que cero
- este bucle se ejecutara, y adicional en la variable intentos
- se guardaran la cantidad de veces que se repita el bucle
- adicional el break cierra el bucle en cuanto intentos sea igual a 5

```
if intentos==5:
    print("Lo siento, no puedo realizar el calculo")
else:
    print(math.sqrt(num))
```

y aqui agrega un condicional que si se cumple, que intentos sea
igual a 5, envia el mensaje de error, de lo contrario
no se cumplira el bucle y pasara a ejecutar la raiz cuadrada del numero
mediante la funcion math.sqrt

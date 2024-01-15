# HINT: python es case sensitive
# significa que distingue entre mayusculas y minusculas
# ejemplo, no es lo mismo Msg a msg, aunque sean las mismas variables

# se inicia una variable cuando se le asigna un valor
msg="Hola Python" # esta es una variable de tipo texto/string

print(msg)

msg="adios python"

print(msg)

n1=4
n2=6
# identaciones: sirven para decirle a python que el codigo identado, va dentro del codigo superior
# ejemplo:

# linea 1
#   linea 2

# esto python lo interpreta como que la linea 2 es parte de la linea 1

print(n1+n2)

# para el tema de constantes se escriben todas en mayusculas y se agregan en un archivo independiente, 
# para luego agregarse en mediante modulos (se vera mas adelante)

# Concatenar

# se hace de la siguiente forma
nombre="Ricardo"

print("mi nombre es "+nombre)

# Funcion Predefinida

# se trata de una pieza de codigo con determinada utilidad, ejemplo

edad = 18
print("tengo "+str(edad)+" años") # esto dara error, por tanto estos valores deben convertirse a un formato compatible
# con una funcion predefinida, en este caso str que convierte lo que tiene dentro en un string
# en un print, al usar el simbolo + con strings, concatena, si se usa con valores numericos, suma
# por defecto python no permite concatenar strings con valores de otros tipos

# otro ejemplo:

salario=1500

descuento=80

print("el descuento es de "+str(salario-descuento))

#datitos
# strings largos de varias lineas deben encerrarse bajo comillas dobles triples """ejemplo""" ò '''ejemplo'''
# se pueden usar comillas simples o dobles, pero en el caso de anidar comillas hay que tener muy claro
# las comillas padres de las hijas
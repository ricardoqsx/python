# las tuplas
    # son elementos inmutables, es decir que no admiten cambios
    # no admite uso de append, extend, remove, index
#ventajas
    # son mas rapidas
    # ocupan menos espacio
    # pueden usarse como claves en un diccionario (las listas no)
# son similares en su forma de declaracion a las listas, salvo que usa parentesis en lugar de corchetes
# se pueden omitir los parentesis pero por buenas practicas es mejor usarla

misDatos=("Ricardo",32,1991)
print(misDatos)
# para convertir una tupla a lista en caso q se necesite
data=list(misDatos)

data.append("Quiroz")

print(data)
# aqui se convirtio una lista en tupla
datatup=tuple(data)

print(datatup)

print(32 in datatup) # con la palabra reservada in revisa si el valor 32 esta o no en la tupla, 
# si es cierto devuelve true, sino false 

# para ver cuantas veces se repite un valor se hace uso del metodo count
print(datatup.count("Ricardo"))
# otro es el metodo len para ver su longitud
print(len(datatup))
# desempaquetado de tupla
# aqui respetando el orden
nombre, edad, anio, apellido=datatup
# bucle for

- bucle determinado
- se sabe cuantas veces se ejecutara ya que hay algo que lo delimite
- ya sea una lista, una cadena de caracteres, lo que sea segun el caso

```
meses = ["ene","feb","mar"]                 # se crea lista meses para recorrerlo, es una forma de recorrer listas

for i in meses:                             # en este caso el bucle for con la variable i recorre la lista meses
    print("hola a todos")
    print(meses)

for mes in [1,2,3]:                         # en este caso los valores de mes son la lista dada a continuacion
    print(mes)                              # e imprime los valores de mes 1 por 1
```

### con rangos especificos

```
for i in range (1,20):                      # aqui se especifica un rango con la palabra reservada range, y adicional se
    print("hola mundo "+str(i))             # establece el inicio y el final
```

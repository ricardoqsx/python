# diccionarios

- estructuras de datos que nos permite almacenar valores de
- diferente tipo (enteros, cadenas, decimales, listas e
- incluso otros diccionarios

### ejemplo

```
capitales={"España":"Madrid","Francia":"Tolousse","UK":"Londres"}
print(capitales)
```

### agregar valores al diccionario

```
capitales["Colombia"]="Bogota"
print(capitales)
```

- se pueden reescribir para corregir

```
capitales["Francia"]="Paris"
print(capitales)
```

### para usar tuplas en un diccionario
1. creo la tupla

```countries=("España","UK","Colombia","Portugal")```

2. asignamos los valores dentro de un diccionario de esta forma

```dic={countries[0]:"Madrid",countries[1]:"Londres",countries[2]:"Bogota",countries[3]:"Lisboa"}
print(dic)```

3. para acceder a un valor en concreto se puede usar su clave en el diccionario

```print(dic[countries[2]])```

4. para imprimir las llaves

```print(dic.keys())```

5. para conocer los valores

```print(dic.values())```

6. con el metodo len se pueden ver la cantidad de valores

```print(len(dic))```

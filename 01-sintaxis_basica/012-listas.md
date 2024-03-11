# listas en python

- son parecidos a los arrays en otros lenguajes
- permiten guardar distintos tipos de datos
- se pueden expandir dinamicamente añadiendo elementos nuevos

# sintaxis

```
nombreLista = [e1,e2,e3]
```


- para trabajar con estas listas existen las funciones o metodos
- aqui se declara una lista, se usan corchetes

```
trabajadores=["ana","maria","miguel"]

print(trabajadores)

print(len(trabajadores)) # <-- metodo len permite ver la cantidad de valores en una lista
```

- metodo append agrega un valor a una lista

```
trabajadores.append("juan")
trabajadores.append("pablo")
trabajadores.append("yeisuri")

print(trabajadores)
print(len(trabajadores))
```

- para imprimir un elemento en concreto

```
print(trabajadores[1])
```

- para imprimir un rango

```
print(trabajadores[1:4])
```

- el primer valor dice desde donde empezar, 
- el 2ndo, habla de la cantidad de valores a imprimir

"""
7. Una  tienda  ofrece  un  descuento  del  15%  sobre el  total  de  la  compra  y  un  cliente 
desea saber cuánto deberá pagar finalmente por su compra. 
8. Dadas las horas trabajadas de una persona y el valor por hora. Calcular su salario 
e imprimirlo. 
9. Calcular el nuevo salario de un obrero, si obtuvo un incremento del 25% sobre su salario anterior. 
10. Un alumno desea saber cuál será su calificación final en la materia de Algoritmos. 
Dicha calificación se compone de los siguientes porcentajes: 
• 55% del promedio de sus tres calificaciones parciales. 
• 30% de la calificación del examen final. 
• 15% de la calificación de un trabajo final. 11. Calcular  la  cantidad  de  segundos  que  están  incluidos  en  el  número  de  horas, 
minutos y segundos ingresados por el usuario.
"""

import os

os.system("clear")

print("Tiendita!")

def descuento():
    a=[]
    res="si"
    while res=="si":
        a.append(float(input("Escriba el precio del articulo: ")))
        res=(input("desea agregar otro articulo? si/no: "))

descuento()
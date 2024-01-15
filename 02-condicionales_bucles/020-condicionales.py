# Condicionales: if
import os

os.system('clear')
print("programa de evaluacion")             # Titulo del programa
nota_alum=int(input("Escribe una nota: "))  # Solicitud de datos por teclado, importante destacar que todo lo q entre por input, sera considerado texto
                                            # notese la conversion de datos en el input con la funcion int

def eval(nota):                         # Definiendo una nueva funcion, def, nombre evaluacion y dato de entrada
    val="desconocido"                   # valor por defecto, fuera de la funcion no puede leerse
    if nota<5:                          # Abre sentencia if, se hace comparacion de valores
        val="suspendido"                # de cumplirse condicion, cambia valor
    elif nota<=10:                      # elif es igual a un else if, con lo cual seria "de otro modo, si..."
        val="sobresaliente"
    else:
        val="incorrecto" 
    return val                          # retorna valor

print(eval(int(nota_alum)))             # imprime y ejecuta funcion evaluacion
                                        # notese que se puede hacer la conversion al capturar datos con input 
                                        # o pasar el valor al llamar a la funcion
                                        # para al final el valor retornado imprimirlo

# if salarios admin<jefe<director<presi <<= concatenacion de valores, aqui se evaluan 2 condiciones
# si los salarios van en escala (osea, cada uno mayor que otro)

# if asignatura in (1, 2, 3): <<= aqui se compara la variable con los valores "en", cuando son
# strings se pone entre comillado separado por comas

# otro ejemplo:
# con operadores and y or

print("obtencion de licencia de conducir")

edad=int(input("escriba su edad: "))
vision=input("Tu vision esta bien?: ")

if 18<edad<90 and vision=="si": # Aqui se deben cumplir todas las condiciones
    # otra forma de expresarlo: "if edad >=18 and edad<=90:"
    print("pilla tu licencia")
else:
    print("on boy, no vas")

# operadores not y in

trabajadores=["Paula","Manuel","Pedro","Ana","Sandra"]

if "Pedro" in trabajadores:             # sirve para hacer busquedas en una lista, el IN se traduciria como EN
    print("Si, Pedro esta en la lista") # si se cumple, devuelve este mensaje
else:
    print("Pedro no esta en la lista")

# tambien se puede buscar en una cadena de texto, si trabajadores
# fuese una sola cadena corrida

# otro operador es NOT el cual se debe combinar con IN, ejemplo
# en este ejemplo se va a la inversa, si sql no esta imprime mensaje
leng="Java, Python, PHP"

if "SQL" not in leng:
    print("Falta SQL en la lista")
else:
    print("SQL esta en la lista")
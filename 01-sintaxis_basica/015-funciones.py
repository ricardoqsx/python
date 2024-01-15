# Funciones
    # es un cojunto de lineas de codigo agrupadas que funcionan como una
    # unidad realizando una tarea especifica

    # pueden devolver valores
    # pueden tener parametros/argumentos
    # tambien se les denomina "metodos"

# Utilidad
    # Reutilizar codigo en caso necesario
    # dividir el codigo en bloques logicos
    # simplificar el codigo

# tipos de funciones
    # predefinidas (ejemplo: print, len, str, etc)
    # propias

# sintaxis

def nombre_funcion():       # def para definir, nombre de la funcion, parentesis y 2 puntos
    mensaje="hola mundo"    # instrucciones de la funcion, varia segun la complejidad
    print(mensaje)
    return (mensaje)        # si retorna o no un valor

def funcion():
    print("prueba 1")
    print("prueba 2")

print("finalizado")

funcion()                   # solo se ejecutara la funcion al momento de ser llamada

# en casos de que reciben parametros o return

def func2(parametro): 
    parametro = "mensaje de la funcion"
    return parametro # esta funcion solo retorna la string

# por defecto esto no imprimiria nada ya que no tiene la funcion print 
# para imprimir el mnsaje en pantalla hay varias formas
print(func2())
# o la otra forma
valor=func2()
print(valor)

# cuando reciben parametros
def msgpers(msg): # el parametro msg significa que cuando se invoque o ejecute
                  # hay que darle un valor a msg, en este caso los 2 que se imprimen

    return msg + ". termina la funcion aqui" # aqui se concateno el valor devuelto con un string

print(msgpers("hola 1"))
print(msgpers("hola bobo 2"))

# otro ejemplo

def suma(mensaje,v1,v2):
    return mensaje + str((v1+v2))

print(suma("la suma es ",5,7)) # aqui los parametros entran en orden de llamada

# IMPORTANTE: cuando la funcion recibe parametros, se le debe dar la cantidad exacta
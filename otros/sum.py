import os
os.system('clear')

a=int(input("Escriba el 1er valor: "))
b=int(input("Escriba el 2ndo valor: "))
c=input("escriba el simbolo (+, -, * o /: ): ")

def op(a,b,c):
    if c =='+':
        d=a+b
    elif c =='-':
        d=a-b
    elif c=='*':
        d=a*b
    elif c=='/':
        d=a/b
    else:
        print("No ha ingresado una operacion valida")

    return d

print(op(a,b,c))
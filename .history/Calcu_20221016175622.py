import re
import xdrlib

print("   Calculadora.py")
print("OPERACIONES ARIMETICAS")

X=input(" Ingrese el primer numero:->>")
#verifica si (x) es numero entero o decimal
if (not re.match('^-?[0-9]+[0-9]*$',X)):
    print("Formato invalido. Debe ingresar un numero entero o decimal:->>")
    exit()

oper=input("Ingrese la operacion a relizar (+,-,*,/,^):->>")
#verifica  si la operacion es valida
if (not re.match('^[\+\-\*\/\^]$',oper)):
    print("Operacion Invalida debe ingresar (+,-,*,/,^):-->")
    exit()

y=input("Ingrese e; segundo valor de la operacion:->>")
#verifica si (y) es numero entero o decimal
if (not re.match('^-?[0-9]+[0-9]*$', y)):
    print("Formato invalido. Debe ingresar un numero entero o decimal:->>")
    exit()

#Converted el str a un numero entero o decimal
if (x.find('.')>-1 or x.find(',')>-1):
    



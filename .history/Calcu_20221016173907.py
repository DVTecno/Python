import re

print("   Calculadora.py")
print("OPERACIONES ARIMETICAS")

X=input(" Ingrese el primer numero:->>")

#verifica si x es numero entero o decimal
if (not re.match('^-?[0-9]+[0-9]*$',X)):
    print("Formato invalido. Debe ingresar un numero entero o decimal")

oper=input("Ingrese la operacion a relizar (+,-,*,/,^):->>")

#verifica  si la operacion es valida
if (not re.match('^[\+\-\*\/\^]$',oper)):
    print("Operacion Invalida debe ingresar (+,-,*,/,^):-->")
    exit()
    
# converted el str a un numero entero o decimal



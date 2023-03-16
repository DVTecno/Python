import re
import xdrlib

print("   Calculadora.py")
print("OPERACIONES ARIMETICAS")

x = input("Ingrese el primer valor de la operacion:->>")
#verifica si (x) es numero entero o decimal
if (not re.match('^-?[0-9]+[0-9]*$', x)):
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
if (x.find('.') > -1 or x.find(',')):
    x = float(y.replace(',', '.'))
else:
    x = int(x)

if (y.find('.')>-1 or y.find(',')):
    y=float(y.replace(',','.'))
else:
    y=int(y)

#Realize y muestra el resulted de la operacion
if (oper=='+'):
    print(f"{x} {oper} {y} = {x+y}")
elif(oper=='-'):
    print(f"{x} {oper} {y} = {x-y}")
elif (oper=='*'):
    print(f"{x} {oper} {y} = {x*y}")
elif (oper=='/'):
    print(f"{x} {oper} {y} = {x/y}")
elif (oper=='^'):
    print(f"{x} {oper} {y} = {x^y}")


from ast import If
from datetime import datetime
print("******************************************************")
print("         ************BIENVENIDOS************")
print("******************************************************")
cripto1 = input("      Ingrese el Nombre de la Criptomoneda:")
cantidad1 = float(input("        Ingrese la cantidad de su Criptomoneda ("+cripto1.upper()+"):"))
cripto2 = input("      Ingrese el Nombre de la Criptomoneda:")
cantidad2 = float(input("        Ingrese la cantidad de su Criptomoneda ("+cripto2.upper()+"):"))
cripto3 = input("      Ingrese el Nombre de la Criptomoneda:")
cantidad3 = float(input("        Ingrese la cantidad de su Criptomoneda ("+cripto3.upper()+"):"))
hora = datetime.now()
print("******************************************************")
print("           ************INFORME************")
print("******************************************************")
print("Dia y hora, en la que se realizo ordenamiento descendente ")
print("      ______________________________________")
print(hora.strftime("      B%A %d/%B/%Y %I:%M:%S:%p"))
print("      ______________________________________")
print("******************************************************")
if cantidad1>cantidad2 and cantidad1>cantidad3:
    print(cantidad1,cripto1)
    if cantidad2>cantidad3:
        print(cantidad2,cripto2)
        print(cantidad3,cripto3)
    else:
        print(cantidad3,cripto3)
        print(cantidad2,cripto2)
elif cantidad2 > cantidad1 and cantidad2 > cantidad3:
    print(cantidad2,cripto2)
    if cantidad1 > cantidad3:
        print(cantidad1,cripto1)
        print(cantidad3,cripto3)
    else:
        print(cantidad3,cripto3)
        print(cantidad1,cripto1)
else:
    print(cantidad3,cripto3)
    if cantidad1 > cantidad2:
        print(cantidad1,cripto1)
        print(cantidad2,cripto2)
        
    else:
        print(cantidad2,cripto2)
        print(cantidad1,cripto1)
print("******************************************************")
print("")
n = int(input("Valor a calcular el factorial: "))
fact = 1
for elem in range(1,n+1):
    fact = elem * fact
print("El factorial de",n,"es",fact)

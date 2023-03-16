numero=int(input("Indique un valor entero: "))
salida=""
if numero%3==0:
    salida+="Fizz"
if numero%5==0:
    salida+="Buzz"
if salida=="":
    salida=str(numero)
print(salida)
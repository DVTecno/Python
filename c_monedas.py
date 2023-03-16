from datetime import datetime
print("********************************************************")
print("          ************BIENVENIDOS************")
print("********************************************************")
cripto1 = input("Ingrese el Nombre de la Primera Criptomoneda: ")
cripto2 = input("Ingrese el Nombre de la Segunda Criptomoneda: ")
cripto3 = input("Ingrese el Nombre de la Tercera Criptomoneda: ")
valor_cripto1 = float(
    input("Ingrese el valor de la Primera Criptomoneda: US$"))
valor_cripto2 = float(
    input("Ingrese el valor de la Segunda Criptomoneda: US$"))
valor_cripto3 = float(
    input("Ingrese el valor de la Tercera Criptomoneda: US$"))
hora=datetime.now()
print("********************************************************")
print("              ************INFORME************")
print("********************************************************")
print("Dia y hora, en la que se realizo la consulta")
print("      ______________________________________")
print(hora.strftime("      B%A %d/%B/%Y %I:%M:%S:%p"))
print("      ______________________________________")
print("")
if valor_cripto1 > valor_cripto2 and valor_cripto1 > valor_cripto3:
    print(      cripto1+":"+str(valor_cripto1))
    if valor_cripto2 > valor_cripto3:
        print(      cripto2+":"+str(valor_cripto2))
        print(      cripto3 + ":"+str(valor_cripto3))
    else:
        print(      cripto3+":"+str(valor_cripto3))
        print(      cripto2+":"+str(valor_cripto2))

elif valor_cripto2 > valor_cripto1 and valor_cripto2 > valor_cripto3:
    print(      cripto2+":"+str(valor_cripto2))
    if valor_cripto1 > valor_cripto3:
        print(      cripto1+":"+str(valor_cripto1))
        print(      cripto3+":"+str(valor_cripto3))
    else:
        print(      cripto3+":"+str(valor_cripto3))
        print(      cripto1+":"+str(valor_cripto1))

else:
    print(      cripto3+":"+str(valor_cripto3))
    if valor_cripto1 > valor_cripto2:
        print(      cripto1+":"+str(valor_cripto1))
        print(      cripto2+":"+str(valor_cripto2))
    else:
        print(      cripto2+":"+str(valor_cripto2))
        print(      cripto1+":"+str(valor_cripto1))
print("")
print("********************************************************")
print("")



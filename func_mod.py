from datetime import datetime
print("************************************************************")
print("            ************BIENVENIDOS************")
print("************************************************************")
cripto_mon=input("Nombre de la Criptomoneda: ")
cant_cripto=float(input("Cantidad acumulada de la Criptomoneda: "))
cotizacion = float(input("Cotización por US$ del día de su : "+cripto_mon.upper()+" "))
hora = datetime.now()
print("************************************************************")
print("              ************INFORME************")
print("************************************************************")
print("Dia y hora, en la que se realizo la consulta")
print("      ______________________________________")
print(hora.strftime("      B%A %d/%B/%Y %I:%M:%S:%p"))
print("      ______________________________________")
porcentaje = cotizacion * 0.05  
porc_sem=(porcentaje*cant_cripto) * 7
billetera = cant_cripto * cotizacion
valor_total= porc_sem + billetera 
print("Ud. Tiene un total de US$ "+str(billetera))
ganancia= valor_total-billetera
print("Ganacia, luego de 7 dias es: US$"+str(ganancia))
print("************************************************************")
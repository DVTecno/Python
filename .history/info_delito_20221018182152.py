print("Consulter delicto, Sacramento Jan2006")
delitos={}

#Se cargan los datos
with open("Sacramento_crime_Jan2006.txt") as delitos_file:
    print("Cargando datos del archivo...")
    for delito in delitos_file:
        delito=delito.replace('\n','')
        delito=delito.split(',')
        delito_dup=delitos.get(delito[5])
        if delito_dup and delito_dup.count(delito)==0:
            delito_dup.append(delito)
            delitos[delito[5]]=delito_dup
        else:
            delitos[delito[5]]=[delito]
#Se muestra menu
print("MENU DE OPCIONES")
print("1. Mostrar Nombre de delitos:")
print("2. Mostrar los diez delitos más ocurridos:")
print("Salir del programa:->>")
print("")

opcion=input("Selections la option que desea aplicar:")
if (opcion=="1"):
    print("Procesando el archivo:")
    total=len(delitos)
    for delito_name,delito in delitos.items():
        delito_dup=len(delito)
        if delito_dup==1:
            print(f"{delito_name}, {delito[0][5]}")
elif (opcion=="2"):
    delitos_rep={}
    for delito_name, delito in delitos.items():
        repeticiones=len(delito)
        delito_rep = delitos_rep.get(repeticiones)
        if (delito_rep):
            delitos_rep[repeticiones]=delitos_rep
        else:
            delitos_rep[repeticiones]=[delito_name]
else:
    exit()


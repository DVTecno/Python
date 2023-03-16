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
print("1. Mostrar Nombre de delitos:->>")
print("Mostrar los diez delitos más ocurridos:->>")
print("Salir del programa:->>")

opcion=input("Selections la option que desea aplicar:->>")
if (opcion=="1"):
    print("Procesando el archivo:")
    total=len(delitos)
    for delito_name,delito in delitos.items():
        
elif (opcion=="2"):
    delitos_rep={}
    for delito_dup
else:
    exit()


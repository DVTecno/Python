print("Consulter delicto, Sacramento Jan2006")
#Se muestra menu
print("MENU DE OPCIONES")
print("1. Mostrar Nombre de delitos:")
print("2. Mostrar los diez delitos más ocurridos:")
print("Salir del programa:->>")
print("")



while True:
    opcion = input("Seleccione la opción que desea aplicar:")
    if opcion in ['1', '2', '3']:
        break
delitos={}
uniq_delito = set()
delitos_count = dict()
#Se cargan los datos
with open("Sacramento_crime_Jan2006.txt") as delitos_file:
    print("Cargando datos del archivo...")
    for delito in delitos_file:
        delito=delito.split(sep=',')
        delito_nom = delito[5].replace('\n', '')
        uniq_delito = uniq_delito | {delito_nom}
        delito_count = delitos_count.get(delito_nom)
        if delito_count:
            delitos_count[delito_nom] = delito_count+1
        else:
            delitos_count[delito_nom]=1
delito_count_ordered=sorted(((value,key) for (key,value) in delitos_count.item()),reverse=True)



if (opcion=='1'):
    for delito in uniq_delito:
        print(delito)
elif (opcion=='2'):
    i=0
    for delito in delito_count_ordered:
        i=+1
        print(delito)
        if i>10:
            break   
else:
    exit()


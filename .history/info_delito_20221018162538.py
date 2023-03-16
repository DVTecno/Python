print("Consulter delicto, Sacramento Jan2006")
delictos={}

#Se cargan los datos
with open("Sacramento_crime_Jan2006.txt") as delitos_file:
    print("Cargando datos del archivo...")
    for delicto in delitos_file:
        delito=delito.replace('\n','')
        delito=delito.replace(',')
        delito_dup=delitos.get()
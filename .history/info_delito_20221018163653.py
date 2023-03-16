print("Consulter delicto, Sacramento Jan2006")
delitos={}

#Se cargan los datos
with open("Sacramento_crime_Jan2006.txt") as delitos_file:
    print("Cargando datos del archivo...")
    for delito in delitos_file:
        delito=delito.replace('\n','')
        delito=delito.replace(',','')
        delito_dup=delitos.get(delito[6])
        if delito_dup and delitos_file(delito)==0:
            delito_dup.append(delito)
            delitos[delito[6]]=delito_dup
        else:
            delitos[delito[6]]=[delito]

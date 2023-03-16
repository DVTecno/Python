#Procesamiento del primer archivo
with open("Glosario.txt","r") as file1:
    print(f"A continuacion el contenido del archivo {file1.name.upper()}")
    print(f"""
        ***************** Inicio del archivo *****************\n{file1.read()}\n
        ******************* Fin del archivo ******************""")
    #procesamiento del archivo por lineas
    with open("Glosario.txt",) as file1:
        linea=file1.readline()
        print("Muestra el archivo linea por linea")
        print("")
        print(f"Linea 1: {linea}")
        linea=file1.readline()
        print(f"Linea 2: {linea}")
        print(f"Linea 3: {file1.readline()}")
        print(f"Linea 4: {file1.readline()}")
        print(f"Linea 5: {file1.readline()}")
        print("Muestra todas las lineas del archivo")
        
        
        
        
        

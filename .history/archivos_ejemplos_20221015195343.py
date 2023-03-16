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
    file1.seek(0)
    print(file1.readlines())
    print(f"Se puede escribir el archivo? {file1.writable()}")
print("")
#Escritura en archivos   si hay contenido se borra todo     
with open("Glosario.txt","w") as file1:
    print(f"Ahora se escribe una nueva linea en el archivo {file1.name.upper()}")
    print(f"Se puede escribir en archivo? {file1.writable()}")
    file1.write(f"Nueva linea en el archivo {file1.name.upper()}")
with open("Glosario.txt","r+") as file1:
    print(f"A continuacion el contenido del archivo {file1.name.upper()} ")
    print("")
    print(f"""
          ************* Inicio del archivo *************\n{file1.read()}\n
          *************** Fin del archivo **************""")
print("")
#Agregar contenido a archivos
with open("Glosario.txt","a") as file1:
    print(f"Ahora se agregara una nueva linea en el archivo {file1.name.upper()}")
    print(f"Se puede escribir en el archivo? {file1.writable()}")
    file1.write(f"\nSe ha agregaro una Nueva linea en el archivo {file1.name.upper()}")
with open("Glosario.txt","r+") as file1:
    print(f"A continuacion el contenido de archivo {file1.name.upper()}")
    print(f"""
          ************* Inicio del archivo *************\n{file1.read()}\n
          ************** Fin del archivo ***************""")
print("")


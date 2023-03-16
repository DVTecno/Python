#Procesamiento del primer archivo
with open("Glosario.txt","r") as file1:
    print(f"A continuacion el contenido del archivo {file1.name.upper()}")
    print(f"""
        ***************** Inicio del archivo *****************\n{file1.read()}\n
        ******************* Fin del archivo ******************""")
    #procesamiento del archivo por lineas
    with 

nombre_archivo=input("Ingrese nombre del archivo")
archivo=open(nombre_archivo,"r")

texto=archivo.read()
archivo.close()
lineas=texto.splitlines()



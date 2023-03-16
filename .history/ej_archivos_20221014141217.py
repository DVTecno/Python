nombre_archivo=input("Ingrese nombre del archivo")
archivo=open(nombre_archivo,"r")

texto=archivo.read()
archivo.close()
lineas=texto.splitlines()
terminos=texto.split(":")
diccionario={}
for linea in lineas:
    termino=linea.split(":")
    diccionario[termino[0]]=termino[1]


nombre_archivo=input("Ingrese nombre del archivo:->>")
archivo=open(nombre_archivo,"r")

texto=archivo.read()
archivo.close()
lineas=texto.splitlines()
terminos=texto.split(":")
diccionario={}
for linea in lineas:
    termino=linea.split(":")
    diccionario[termino[0]]=termino[1]

buscar=input("Indique el termino a buscar en el diccionario:->>")
encontrado=diccionario.get(buscar)
if encontrado:
    print(buscar+":"+" "+encontrado)
else:
    print("El termino buscado no esta en el glosario")
    ingresar_termino=input("Desea ingresar el termino (n/s):->>")
    if ingresar_termino == "s":
        archivo=open(nombre_archivo,"a")
        nuevo_termino=input("Ingrese la description del nuevo termino:->>")
        archivo.write(""+buscar+":"+nuevo_termino)
        archivo.close()
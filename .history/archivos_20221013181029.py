nombre_archivo=input("Ingrese el nombre del archivo que contiene las palabras:->>")
ocurrencia = open(nombre_archivo, "r")

texto = ocurrencia.read()
palabras=texto.split()
ocurrencias={}

for palabra in palabras:
    if ocurrencias.get(palabras):
        ocurrencias[palabra]+=1
    else:
        ocurrencias[palabra]=1
    
maxpar=None, 0
for palabras, cantidad in ocurrencias.items():
    if maxpar[1]<cantidad:
        maxpar=palabras,cantidad
        
print("Laa palabras con mayor cantidad de repeticion es",maxpar[0],"repetida",maxpar[1],"veces")
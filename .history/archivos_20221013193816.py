"""nombre_archivo=input("Ingrese el nombre del archivo que contiene las palabras:->>")"""
nombre_archivo = "Glosario.txt"
archivo = open(nombre_archivo, "r")

texto = archivo.read()
palabras=texto.split()
ocurrencias={}

for palabra in palabras:
    if ocurrencias.get(palabra):
        ocurrencias[palabra]+=1
    else:
        ocurrencias[palabra]=1
    
maxpar=None, 0
for palabras, cantidad in ocurrencias.items():
    if maxpar[1]<cantidad:
        maxpar=palabras,cantidad
        
print("Laa palabras con mayor cantidad de repeticion es",maxpar[0],"repetida",maxpar[1],"veces")
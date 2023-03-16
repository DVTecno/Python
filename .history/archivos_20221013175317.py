nombre_archivo=input("Ingrese el nombre del archivo que contiene las palabras:->>")
archivo=open(nombre_archivo,"r")

tecto=archivo.read()
palabras=texto.split()
ocurrencias={}

for palabras in palabras:
    if ocurrencias.get(palabras):
        ocurrencias[palabras]+=1
    else:
        ocurrencias[palabras]=1
    
maxpar=None, 0
for palabras, cantidad in ocurrencias.items():
    if maxpar[1]<cantidad:
        maxpar=palabras,cantidad
        
print("Laa palabras con mayor cantidad de repeticion es",maxpar[0],"repetida",maxpar[1],"veces")
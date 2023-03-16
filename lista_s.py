cripto=[]
cant=[]
cotiz=[]
i=0
while i<5:
    cripto.append(input("Ingrese el nombre de la moneda:->>").upper())
    cant.append(float(input("Ingrese la cantidad de ("+cripto[i]+"):->>")))
    cotiz.append(float(input("Ingrese la Cotizacion en USD de ("+cripto[i]+"):->>")))
    i+=1
i=0
while i<5:
    print("MONEDA: (",cripto[i],"), CANTIDAD: ",cant[i],", COTIZACIÓN: ",cotiz[i])
    i+=1
i=0    


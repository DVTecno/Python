cripto=[5]
cant=[5]
cotiz=[5]
i=0
while i<5:
    cripto=input("Ingrese el Nombre de la Moneda:->>").upper()
    cant=float(input("Ingrese la Cantidad de ("+cripto+"):->>"))
    cotiz=float(input("Ingrese la cotización en USD de ("+cripto+"):->>"))
    i+=1
i=0
while i<5:
    print("MONEDA: "+cripto[i]+", CANTIDAD: ",str(cant[i]),",PRECIO: USD$",str(cotiz[i]))
    i+=1
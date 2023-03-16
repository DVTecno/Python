l_inferior=int(input("Ingrese el valor inferior ->>"))
l_superior=int(input("Ingrese el valor superior ->>"))
print("Los entre ",l_inferior," y ",l_superior," son Primos")
for n in range(l_inferior,l_superior+1):
    es_primo=True
    i=2
    while (es_primo and i<n):
        es_primo=(n%i)!=0
        i+=1
    if es_primo :
        print("[",n,end=' ]')
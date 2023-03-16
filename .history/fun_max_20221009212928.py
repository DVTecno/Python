x=int( input("Ingrese el primer valor"))
y=int( input("Ingrese el segundo valor"))
z=int( input("Ingrese el tercer valor"))
print("",max(max(x,y),z))
def max(x,y):
    if x>y:
        maximo=x
    else:
        maximo=y
    return maximo
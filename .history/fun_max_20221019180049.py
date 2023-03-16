from time import sleep

print("")
x=int( input("Ingrese el primer valor:->>"))
y=int( input("Ingrese el segundo valor:->>"))
z=int( input("Ingrese el tercer valor:->>"))
print("")

def max(x,y):
    if x>y:
        maximo=x
    else:
        maximo=y
    return maximo


for i in range(0, 6):
    print(f'Esperando para actualizar... {5-i:02d} seg', end='\r')
    sleep(1)
    print('\n')
print("   ************ RESULTADO ************")
print("                 *******")
print("                 ", max(max(x, y), z))
print("                 *******")

from time import sleep
print("")
print("******** VALOR MAXIMO ********")

x = int(input("Enter the first value:->>"))
y = int(input("Enter the second value:->>"))
z=int( input("Ingrese el tercer valor:->>"))
print("")

def max(x,y):
    if x>y:
        maximo=x
    else:
        maximo=y
    return maximo


for i in range(0, 4):
    print(f'processing... {3-i:02d} seg', end='\r')
    sleep(1)
print('\n')
print("********** RESULTADO **********")
print("            *******")
print("            ", max(max(x, y), z))
print("            *******")

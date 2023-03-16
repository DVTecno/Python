cities=[]
eliminados=0
with open("US_Cities.txt","r") as cities_file:
    print("Cargando datos del archivo...")
    for city in cities_file:
        city=city.replace('\n','')
        city=city.split('|')
        cities.append(city)

print("MENU DE OPERACIONES")
print("1. Eliminar duplicator")
print("2. Ordenar las ciudades")
print("Salir del programa")

while True:
    option=input("Ingrese una Operacion")
    if option in ['1','2','3']:
        break
    if (option=='1'):
        print("Eliminando duplicados...")
        total=len(cities)
        proc=1
        
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
print("3. Salir del programa")

while True:
    option=input("Ingrese una Operacion")
    if option in ['1','2','3']:
        break
if (option=='1'):
    print("Eliminando duplicados...")
    total=len(cities)
    proc=1
    for city in cities:
        print(round((proc/total)*100,2),"%",end='\r')
        city_count=cities.count(city)
        if (city_count>1):
            i=1
            total=len(cities)
            while  (i < city_count):
                cities.remove(city)
                eliminados+=1
                i+=1
        proc+=1
elif (option=='2'):
    cities.sort()
elif (option=='3'):
    exit()


for city in cities:
    print(city)
print(f"Se han encontrado {len(cities)} ciudades")

if (option=='1'):
    print(f"Se han eliminado {eliminados} registros repetidos")
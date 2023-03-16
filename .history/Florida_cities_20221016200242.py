import csv
import math
from ssl import CHANNEL_BINDING_TYPES
_EARTH_RADIO=6371
d=0
#Apertura del archivo
with open("Florida Cities.csv") as cities_file:
    ciudad1=input("ingrese el nombre de la primera ciudad:->>")
    ciudad2=input("ingrese el nombre de la segunda ciudad:->>")

    #Carga el csv en el programa
    cities=csv.DictReader(cities_file,['name','state','lat','lng'])
    found=0
    for city in cities:
        if (ciudad1.lower()==city['name'].lower() or ciudad2.lower()==city['name'].lower()):
            if (found==0):
                lat1=float(city['lat'])*math.pi/180
                lng1=float(city['name'])*math.pi/180
                found+=1
                print(f"Ciudad: {city['name']} Lat: {city['lat']} Lng: {city['lng']}")
            else:
                found+=1
                lat2=float(city['lat'])*math.pi/180
                lng2=float(city['lng'])*math.pi/180
                print(f"Ciudad: {city['name']} Lat: {city['lat']} Lng: {city['lng']}")   
                delta_lat=lat2-lat1
                delta_long=lng2-lng1
                a=math.sin(delta_lat/2)**2+math.cos(lat1)*math.cos(lat2)*math.sin(delta_long/2)**2
                c=2*math.atan2(math.sqrt(a),math.sqrt(1-a))
                d=_EARTH_RADIO*c
                print(f"La distancia entre la {ciudad1} y la {ciudad2} es de {d:1.2f} km")
                break
    #Verification de la ciudad
    if (found<2 and d==0):
        print("Verifique el nombre de las ciudades, las ciudades disponibles son de la Florida.")
        listar=input("Quiere Listar las ciudades disponibles? (s/n):->>")
        if (listar=="s"):
            cities_file.seek(0)
            for city in cities:
                print(city['name'])
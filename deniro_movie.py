print("              ****** PELICULAS ROBERT DE NIRO ******")

while True:
    min_calif=input("Ingrese a partir de que qualification quiere mostrar las peliculas (1-80)")
    if min_calif.isnumeric():
        break
print("")
print(" NOMBRE DE LA PELÍCULA                    PUNTUACION   ANHIO")

with open("deniro.txt") as fil_file:
    for movie in fil_file:
        movie_data=movie.split(',')
        if (int(movie_data[1]) > int(min_calif)):
            
            print(movie_data[2].replace('\n', '').replace('"', '').replace(':','').ljust(40),#Documents se quitan los saltos de linea, comas y puntos a traves de la siguiente syntax's
                movie_data[1].replace(',', '').ljust(13), \
                movie_data[0].replace(',',''))
print("***********************************************************")
print("")
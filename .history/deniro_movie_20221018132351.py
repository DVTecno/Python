print("              ****** PELICULAS ROBERT DE NIRO ******")

while True:
    min_calif=input("Ingrese a partir de que qualification quiere mostrar las peliculas (1-80)")
    if min_calif.isnumeric():
        break
print("")
print("PUNTUACION  NOMBRE DE LA PELÍCULA                     ANHIO")

with open("deniro.txt") as fil_file:
    for movie in fil_file:
        movie_data=movie.split(',')
        if (int(movie_data[1]) > int(min_calif)):
            
            print(movie_data[2].replace('\n', '').replace('"', "").ljust(40),
                movie_data[0].replace(',', '').ljust(10), \
                movie_data[1].replace(',',''))
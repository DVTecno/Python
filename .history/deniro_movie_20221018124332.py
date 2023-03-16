from dataclasses import replace


print("****** PELICULAS ROBERT DE NIRO ******")
while True:
    min_calif=input("Ingrese a partir de que qualification quiere mostrar las peliculas (1-80)")
    if min_calif.isnumeric():
        break

with open("deniro.txt") as fil_file:
    for movie in fil_file:
        movie_data=movie.split(',')
        if (int(movie_data[1]) > int(min_calif)):
            print(movie_data[1].replace('\n','').replace('"','').ljust(40), \
                  movie_data[2].replace(',','').ljust(6), \
                  movie_data[0].replace(',',''))
print("PELICULAS DE ROBERT DENIRO")

while True:
    min_score=input("Ingrese a partir de que puntuacion quiere ver la pelicula (1-99):")
    if min_score.isnumeric():
        break

with open('deniro.txt') as deniro_file:
    for movie in deniro_file:
        movie_data=movie.split(',')
        if (int(movie_data[1])>int(min_score)):
            print(movie_data[2].replace('\n','').replace('"','').ljust(40), \
                  movie_data[1].replace(',','').ljust(6), \
                  movie_data[0].replace(',',''))


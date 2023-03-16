movies = []
# Class Movie

# The class Movie has a constructor that takes a line from the movies.csv file and parses it into the
# movie's id, name, year, and genres
class Movie:
    def __init__(self, movie_line):
        size = None
        movie_dat = movie_line.split(sep=',')
        self.id = movie_dat[0]
        size = movie_dat[1].index('(')
        self.name = movie_dat[1][0:size]
        self.year = int(movie_dat[1][size+1:size+5])
        self.generos = movie_dat[2].replace('\n', '').split('|')

    def show(self):
        print(self.name)
        print(self.year)
        print(self.generos)

def procesar_archivos():
    with open('movies.csv', 'r', encoding="utf8") as movies_file:
        for movie_line in movies_file:
            movies.append(Movie(movie_line))

def menu():
    print("Opciones")
    print("1. Buscar peliculas por anhio")
    print("2. Salir")
    return input("Ingresa la opcion a ejecutar:")

def buscar_por_year(year):
    for movie in movies:
        if movie.year == int(year):
            movie.show()
            print("\n")

print("Cargando peliculas...")
procesar_archivos()
print(f"Se han cargado {len(movies)} peliculas")
while True:
    opcion = menu()
    if opcion == '1':
        buscar_por_year(input("Ingrese el anhio:"))
    elif opcion == '2':
        exit()


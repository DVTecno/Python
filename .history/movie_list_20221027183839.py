movies = []
# Class Movie

# The class Movie has a constructor that takes a line from the movies.csv file and parses it into the
# movie's id, name, year, and genres
# La clase Movie tiene un constructor que toma una línea del archivo movies.csv y la analiza en el
# ID, nombre, año y géneros de la película
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


"""
     Abre el archivo movies.csv, lee cada línea y crea un objeto Movie para cada línea.
     """
def procesar_archivos():
    """
    It opens the movies.csv file, reads each line, and creates a Movie object for each line
    """
    with open('movies.csv', 'r', encoding="utf8") as movies_file:
        for movie_line in movies_file:
            movies.append(Movie(movie_line))

def menu():
    """
    It prints a menu and returns the user's input
    :return: The input of the user
    """
    print("Opciones")
    print("1. Buscar peliculas por anhio")
    print("2. Salir")
    return input("Ingresa la opcion a ejecutar:")
"""
     Recorre la lista de películas e imprime el objeto de la película si el año de la película es igual al
     año pasado como argumento
     :param year: El año de la película que quieres buscar
     """
def buscar_por_year(year):
    """
    It loops through the movies list and prints the movie object if the movie's year is equal to the
    year passed as an argument
    :param year: The year of the movie you want to search for
    """
    for movie in movies:
        if movie.year == int(year):
            movie.show()
            print("\n")

# A loop that prints a menu and asks the user for an option. If the user enters 1, it asks for a year
# and calls the buscar_por_year function. If the user enters 2, it exits the program.
# Un bucle que imprime un menú y le pide al usuario una opción. Si el usuario ingresa 1, pide un año
# y llama a la función buscar_por_año. Si el usuario ingresa 2, sale del programa.
print("Cargando peliculas...")
procesar_archivos()
print(f"Se han cargado {len(movies)} peliculas")
while True:
    opcion = menu()
    if opcion == '1':
        buscar_por_year(input("Ingrese el anhio:"))
    elif opcion == '2':
        exit()


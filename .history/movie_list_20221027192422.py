movies = []
# Class Movie
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
    with open('movies.csv', 'r', encoding="utf8") as movies_file:
        for movie_line in movies_file:
            movies.append(Movie(movie_line))
"""
     Imprime un menú y devuelve la entrada del usuario.
     :return: La entrada del usuario
     """
def menu():
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
    for movie in movies:
        if movie.year == int(year):
            movie.show()
            print("\n")

# Un bucle que imprime un menú y le pide al usuario una opción. Si el usuario ingresa 1, pide un año
# y llama a la función buscar_por_año. Si el usuario ingresa 2, sale del programa.
print("Cargando peliculas...")
procesar_archivos()
print(f"Se han cargado {len(movies)} peliculas")
while True:
    opcion = menu()
    if opcion == '1':
        buscar_por_year(
            input("Ingrese el año de la película que quieres buscar:"))
    elif opcion == '2':
        exit()
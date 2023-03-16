"""
Desarrolla un programa en Python que lea la información de películas de un archivo csv, llamado movies.csv,
procese todas las líneas del archivo y para cada película (Línea del archivo), genere un objeto con toda la información de la película. 
El programa debe satisfacer los siguientes requerimientos:
Para cada película es necesario registrar:
-Nombre de la película
-Fecha de la película
-Género de la película
La película puede tener varios géneros.
La información de cada película debe estar almacenada o registrada en objetos, un objeto por película.
El programa debe mostrar un menú, en el cual el usuario puede seleccionar dos opciones:
Buscar películas por año, en esta opción se le debe solicitar al usuario que indique el año del cual quiere mostrar las películas registradas. 
Luego que el usuario indique el año, se le deben mostrar todas las películas que tengan ese año.
Salir. Esta opción le permite al usuario salir del programa
El programa siempre debe mostrar el menú, a menos que el usuario seleccione la opción de Salir del programa.
"""
movies = []


class Movie:
  def __init__(self, movie_line):
    size = None
    movie_data = movie_line.split(sep=',')
    self.id = movie_data[0]
    size = movie_data[1].index('(')
    self.name = movie_data[1][0:size]
    self.year = int(movie_data[1][size+1:size+5])
    self.generos = movie_data[2].replace('\n', '').split('|')

  def show(self):
    print(self.name)
    print(self.year)
    print(self.generos)


def procesar_archivo():
    with open('movies.csv', 'r', encoding="utf8") as movies_file:
        for movie_line in movies_file:
            movies.append(Movie(movie_line))


def menu():
    print("Opciones")
    print("1. Buscar películas por año")
    print("2. Salir")
    return input("Indica la opción a ejecutar: ")


def buscar_por_year(year):
    for movie in movies:
        if movie.year == int(year):
            movie.show()
    print("\n")


print('Cargando películas...')
procesar_archivo()
print(f"Se han cargado {len(movies)} películas")
while True:
        opcion = menu()
        if opcion == '1':
            buscar_por_year(input("Indique el año: "))
        elif opcion == '2':
            exit()

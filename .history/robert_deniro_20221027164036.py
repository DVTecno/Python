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
# 554,Trial by Jury (1994),Crime|Drama|Thriller
from movie_list import procesar_archivos


''' movies = []
class Movie:
    def __init__(self,movie_line):#aqui le damos el nombre con el que va a trabajar la clase
        size=None
        movie_data=movie_line.split(',')#guardamos todo en movie_data

        print(f"{movie_data}") '''



    
procesar=procesar_archivos()



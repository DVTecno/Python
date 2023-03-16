# Desarrolla un programa en Python que calcule el tiempo, en días, que el usuario estará de vacaciones.
# Para ello debes solicitar la fecha de inicio y fin de las vacaciones, y a partir de esas fechas, calcula el tiempo.
#Adicionalmente, debes indicar al usuario cuántos días faltan para tomar sus vacaciones.
from ast import parse
from datetime import date, datetime
from dateutil.parser import parser
from dateutil.relativedelta import relativedelta
hoy=datetime.now()
fecha_incio=parse(input("Ingrese la Fecha de Inicio de sus Vacaciones (DD/MM/YYYY):"),dayfirst=True) 
fecha_termino=parse(input("Ingrese Fecha de fin de Vacaciones (DD/MM/YYYY):"),dayfirst=True)
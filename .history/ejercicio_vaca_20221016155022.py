# Desarrolla un programa en Python que calcule el tiempo, en días, que el usuario estará de vacaciones.
# Para ello debes solicitar la fecha de inicio y fin de las vacaciones, y a partir de esas fechas, calcula el tiempo.
#Adicionalmente, debes indicar al usuario cuántos días faltan para tomar sus vacaciones.
from datetime import date, datetime
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
hoy=datetime.now()
incio=parse(input("Ingrese la Fecha de Inicio de sus Vacaciones (DD/MM/YYYY):"),dayfirst=True) 
fin=parse(input("Ingrese Fecha de fin de Vacaciones (DD/MM/YYYY):"),dayfirst=True)





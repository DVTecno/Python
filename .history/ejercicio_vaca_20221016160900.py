"""# Desarrolla un programa en Python que calcule el tiempo, en días, que el usuario estará de vacaciones.
# Para ello debes solicitar la fecha de inicio y fin de las vacaciones, y a partir de esas fechas, calcula el tiempo.
#Adicionalmente, debes indicar al usuario cuántos días faltan para tomar sus vacaciones.
from datetime import datetime
from datetime import date, datetime
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
hoy=datetime.now()
inicio=parse(input("Ingrese la Fecha de Inicio de sus Vacaciones (DD/MM/YYYY):"),dayfirst=True) 
fin=parse(input("Ingrese Fecha de fin de Vacaciones (DD/MM/YYYY):"),dayfirst=True)
vacaciones=relativedelta(inicio,fin)
print(f"Usted tiene {abs(vacaciones.days)} dias de Vacaciones")
d_faltante=hoy-hoy.replace(hoy,inicio)
print(f"Faltan {abs(d_faltante)}")"""


salida = parse(input(
    "Indique la fecha en la que saldrÃ¡ de vacaciones (DD/MM/YYYY): "), dayfirst=True)
regreso = parse(input(
    "Indique la fecha en la que regresarÃ¡ de vacaciones (DD/MM/YYYY): "), dayfirst=True)
vacaciones = relativedelta(regreso, salida)
print(f"EstarÃ¡ {vacaciones.days} dÃ­as de vacaciones")
falta = relativedelta(salida, datetime.now())
print(f"Faltan {falta.months} meses y {falta.days} dÃ­as para las vacaciones")

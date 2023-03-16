from datetime import date,datetime
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
fecha=date.today()
fecha_hora=datetime.now()
print("Formato de fechas")
print("Fecha:",fecha)
print("Fecha y Hora",fecha_hora)
print("Fecha y Hora (Formato ctime):",fecha_hora.ctime())
print("Fecha Formato 1:")

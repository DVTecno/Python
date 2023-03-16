from datetime import date,datetime
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta

fecha=date.today()
fecha_hora=datetime.now()
print("Formato de fechas")
print("Fecha:",fecha)
print("Fecha y Hora",fecha_hora)
print("Fecha y Hora (Formato ctime):",fecha_hora.ctime())
print("Fecha Formato 1:",fecha_hora.strftime("%d/%m/%y"))
print("Fecha Formato 2:",fecha_hora.strftime("%d/%m/%y %H:%M:%S"))
print("fECHA fORMATO 3:",fecha_hora.strftime("%A %d/%m/%y %I:%M:%S%p"))
print("Calculos con fechas")
hoy=datetime.now()
fecha_nac=parse(input("Ingrese Fecha de Nacimiento (DD/MM/YYYY):",dayfirst=True))


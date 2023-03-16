from datetime import date,datetime
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta

fecha=date.today()
fecha_hora=datetime.now()
print("Formato de fechas")
print("Fecha:",fecha)
print("Fecha y Hora",fecha_hora)
#ctime muestra la fecha en orden dia/mes/anhio
print("Fecha y Hora (Formato ctime):",fecha_hora.ctime())
#FECHA DEL SISTEMA DE 3 DIFERENTES FORMATOS
print("Fecha Formato 1:",fecha_hora.strftime("%d/%m/%y"))
print("Fecha Formato 2:",fecha_hora.strftime("%d/%m/%y %H:%M:%S"))
print("fECHA fORMATO 3:",fecha_hora.strftime("%A %d/%m/%y %I:%M:%S%p"))
print("Calculos con fechas")
hoy=datetime.now()
fecha_nac=parse(input("Ingrese Fecha de Nacimiento (DD/MM/YYYY):"),dayfirst=True)
edad=relativedelta(hoy,fecha_nac)
print(f"Usted tiene {edad.years} anhios, {edad.months} meses y {edad.days}dias")
nochevieja_days=hoy-hoy.replace(day=31,month=12)
navidad_days=hoy-hoy.replace(day=24,month=12)
print(f"faltan {abs(navidad_days.days)} dias para navidad")
print(f"faltan {abs(nochevieja_days.days)} dias para fin de anhio")
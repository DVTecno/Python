from datetime import datetime
from datetime import date
d = date.today()

d.strftime("%d/%m%y")
d.strftime("%d/%m/%y")
d.strftime("%A %d/%m/%Y")
d.strftime("%A %d/%m/%Y %H:%M:%S")
dt = datetime.now()

dt.strftime("%d/%m/%y")
dt.strftime("%H:%M:%S")
dt.strftime("%A %d/%m/%Y %H:%M:%S:%p")
dt.strftime("%A %d/%m/%Y %H:%M:%S:%p")
dt.strftime("%A %d/%B/%Y %H:%M:%S:%p")
dt.strftime("%A %d/%B/%Y %I:%M:%S:%p")
print(dt.strftime("%A %d/%B/%Y %I:%M:%S:%p"))




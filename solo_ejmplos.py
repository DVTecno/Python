import random
from werkzeug.security import generate_password_hash

minus = "abcdefghijklmnopqrstwxyz"
mayus = minus.upper()
números = "0123456789"
símbolos = "@()[]{}*,:/-_?.$!$<#&+%="

base = minus+mayus+números+símbolos
longitud = 12

for _ in range(10):
    muestra = random.sample(base,longitud)
    password = "".join(muestra)
    password_encriptado=generate_password_hash(password)
    print("{} => {}".format(password,password_encriptado))
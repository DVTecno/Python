import locale
import string
import secrets
import random
import re



def check_password(password):
    password_pattern = "(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&/_=;:<>|#,\*\'\"\-\+\[\]])[A-Za-z\d@$!%*?&/_=;:<>|#,\*\'\"\-\+\[\]]{8,}$"
    return re.fullmatch(password_pattern, password) != None

locale.setlocale(locale.LC_ALL,'')
pass_characters = string.ascii_lowercase +\
                  string.ascii_uppercase +\
                  string.digits +\
                  string.punctuation

while True:
    try:
        cantidad=int(input("ingrese la cantidad de Passwords a generar"))
    except ValueError:
        print(f"El valor ingresado es invalido. debe ingresar un numero entero")
    else:
        break

print(f"Generando {locale.format_string('%2d',cantidad,grouping=True)} password")
for i in range(1,cantidad):
    password=''.join(secrets.choice(pass_characters) for i in range(0,random.randint(6,16)))
    try:
        with open('random_passwords.txt', 'a') as pass_file:
            pass_file.write(password+'\n')
    except PermissionError as error:
        print('Falla de acceso al archivo random_password.txt, verifique que este cerrado')
        print(f"Error: {error} ")
        exit()

import locale
import random
import re
import secrets
import string


print("Política de Contraseñas")
print("1. Tamaño mínimo:")
print("2.Tamaño máximo:")
print("3.Número mínimo de números:")
print("4.Número mínimo de minúsculas:")
print("5.Número mínimo de mayúsculas:")
print("6.Número mínimo de caracteres especiales:")
print("7.Caracteres especiales permitidos:")
print("8.Validación de diccionarios:")
print("9.Validación de la cantidad de caracteres repetidos consecutivos:")
print("10.Guardar cambios de la política:")
print("Para modificar algun parametro indique el numero correspondiente. Para salir 0:")


def menu():
    print("1. Configurar política de contraseña")
    print("2. Mostrar diccionario")
    print("3. Generar contraseña")
    print("4. Salir")
    return input("Ingresa la opcion a ejecutar:")


def check_password(password):
    password_pattern = "(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&/_=;:<>|#,\*\'\"\-\+\[\]])[A-Za-z\d@$!%*?&/_=;:<>|#,\*\'\"\-\+\[\]]{8,}$"
    return re.fullmatch(password_pattern, password) != None


# Asking the user to input a number and if the input is not a number it will ask again.
while True:
    try:
        cantidad = int(input("ingrese la cantidad de Passwords a generar"))
    except ValueError:
        print(f"El valor ingresado es invalido. debe ingresar un numero entero")
    else:
        break

# Setting the locale to the default locale.
locale.setlocale(locale.LC_ALL, '')
pass_characters = string.ascii_lowercase +\
    string.ascii_uppercase +\
    string.digits +\
    string.punctuation
    
print(
    f"Generando {locale.format_string('%2d',cantidad,grouping=True)} password")
for i in range(1, cantidad):
    password = ''.join(secrets.choice(pass_characters)
                       for i in range(0, random.randint(6, 16)))
    try:
        with open('random_password.txt', 'a') as pass_file:
            pass_file.write(password+'\n')
    except PermissionError as error:
        print('Falla de acceso al archivo random_password.txt, verifique que este cerrado')
        print(f"Error: {error} ")
        exit()

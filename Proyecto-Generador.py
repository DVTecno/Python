import locale
import random
import re
import secrets
import string


print("Política de Contraseñas")
print("1.Tamaño mínimo:")
print("2.Tamaño máximo:")
print("3.Número mínimo de números:")
print("4.Número mínimo de minúsculas:")
print("5.Número mínimo de mayúsculas:")
print("6.Número mínimo de caracteres especiales:")
print("7.Caracteres especiales permitidos: \.,-_+\*@$#%&")
print("8.Validación de diccionarios:")
print("9.Validación de la cantidad de caracteres repetidos consecutivos:")
print("10.Guardar cambios de la política:")
print("Para modificar algún parámetro indique el numero correspondiente. Para salir 0:")


def menu():
    print("1. Configurar política de contraseña")
    print("2. Mostrar diccionario")
    print("3. Generar contraseña")
    print("4. Salir")
    return input("Ingresa la opción a ejecutar:")

"""
    Comprueba si la contraseña tiene al menos 8 caracteres, contiene al menos una letra minúscula, una
    letra mayúscula, un dígito y un carácter especial
    :param contraseña: La contraseña para comprobar
    :return: Un valor booleano.
    """
def tamaño(tan_1,tan_2):
    tam_1=int(input("Indique tamaño mínimo que desea asignar"))
    tam_2=int(input("Indique tamaño máximo que desea asignar"))
    return tamaño
    
    
    
            
        
    

def check_password(password):
    
    password_pattern = "(?=.*[a-z])(?=.*[A-Z]){}(?=.*\d)(?=.*[@$#%&\.,-_+\*])[A-Za-z\d@$@$#%&|\.,-_+\*]{8,}$"
    return re.fullmatch(password_pattern, password) != None


# Solicitar al usuario que ingrese un número y si la entrada no es un número, volverá a preguntar.
while True:
    try:
        cantidad = int(input("ingrese la cantidad de Passwords a generar"))
    except ValueError:
        print(f"El valor ingresado es invalido. debe ingresar un número entero")
    else:
        break

# Establecer la configuración regional en la configuración regional predeterminada.
locale.setlocale(locale.LC_ALL, '')
pass_characters = string.ascii_lowercase +\
    string.ascii_uppercase +\
    string.digits +\
    string.punctuation
    
# Generar contraseñas aleatorias y guardarlas en un archivo.
print(
    f"Generando {locale.format_string('%2d',cantidad,grouping=True)} password")
for i in range(0, cantidad):
    password = ''.join(secrets.choice(pass_characters)
                       for i in range(0, random.randint(6, 16)))
    print(password)
    try:
        with open('random_password.txt', 'a') as pass_file:
            pass_file.write(password+'\n')
           
    except PermissionError as error:
        print('Falla de acceso al archivo random_password.txt, verifique que este cerrado')
        print(f"Error: {error} ")
        exit()


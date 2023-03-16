import curses
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
        with open('random_password.txt', 'a') as pass_file:
            pass_file.write(password+'\n')
    except PermissionError as error:
        print('Falla de acceso al archivo random_password.txt, verifique que este cerrado')
        print(f"Error: {error} ")
        exit()


screen = curses.initscr()
screen.clear()
curses.start_color()
curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_WHITE)
curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_MAGENTA)
screen.addstr(0, 0, "TEXTO EN DIFERENTES COLORES", curses.A_UNDERLINE)
screen.addstr(2, 0, "Texto Rojo!", curses.color_pair(1))
screen.addstr(3, 2, "Texto Azul!", curses.color_pair(2))
screen.addstr(4, 4, "Texto Amarillo!", curses.color_pair(3))
screen.addstr(5, 6, "Texto Verde!", curses.color_pair(4))
screen.addstr(7, 0, 'Pulse Enter para continuar...', curses.A_BOLD)
screen.refresh()
curses.noecho()
screen.getstr()

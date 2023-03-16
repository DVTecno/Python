import curses



screen = curses.initscr()  # type: ignore
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

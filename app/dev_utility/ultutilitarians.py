from os import system, name, environ


def clear():
    if name == 'nt':
        system('cls')
    else:
        environ['TERM'] = 'xterm'  # Define a variável de ambiente TERM
        system('clear')
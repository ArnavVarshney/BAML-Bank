import getpass

from pyfiglet import Figlet

from database import check_auth
from utility import print_name, clear_console


def existing_user():
    clear_console()
    print_name()
    print(Figlet('small').renderText('Login'))
    username = input('Username: ')
    password = getpass.getpass()
    role = int(input('Role [1. Employee, 2. Customer]: '))
    if check_auth(username, password, role):
        print('Logged in successfully!')
        return role, username
    else:
        print('Invalid credentials!')


def new_user():
    # TODO: New user implementation
    print('Welcome new user')

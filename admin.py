import os

from pyfiglet import Figlet
from termcolor import colored

import main
from database import retrieve_employee
from def_customers import customers
from def_employees import employees
from def_branches import branches
from utility import clear_console, print_name, get_current_time, pause, about


def intro():
    username = os.getenv('loggedin')
    branch = retrieve_employee(username)[6]
    try:
        main_menu = ['1. My Account', '2. Employees', '3. Customers', '4. Branches', '5. About Us', '6. Logout',
                     '7. Exit',
                     'Press Ctrl + C to Force Exit']
        login_time = get_current_time()
        for counter in range(5):
            clear_console()
            print_name()
            print(Figlet('small').renderText('Admin Menu'))
            print(colored('Hello ' + retrieve_employee(username)[3], 'blue'))
            print('Login time: ' + login_time + '\n')
            print('Choose an option: \n')
            for i in main_menu:
                print('\t' + i)
            print()
            inp = input('Command: ')
            print()
            if inp == '1':
                print('Coming soon!')
            elif inp == '2':
                employees()
            elif inp == '3':
                customers()
            elif inp == '4':
                branches()
                print('Coming soon!')
            elif inp == '5':
                about()
            elif inp == '6':
                print('Logged out!')
                main.intro()
            elif inp == '7':
                print('Goodbye!\nLogout time: ', get_current_time())
                break
            else:
                print("Invalid entry!")
            pause()
    except KeyboardInterrupt:
        print('\nForce exit encountered!')


if __name__ == '__main__':
    print('Log in first\nAbort!')

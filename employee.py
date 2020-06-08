import os

from pyfiglet import Figlet
from termcolor import colored

import main
from database import retrieve_employee
from def_customers import customers
from def_employees import view_employee_info
from utility import clear_console, print_name, get_current_time, pause, about


def intro():
    username = os.getenv('loggedin')
    try:
        main_menu = ['1. My Account', '2. Customers', '3. About Us', '4. Logout',
                     '5. Exit', 'Press Ctrl + C to Force Exit']
        login_time = get_current_time()
        while True:
            clear_console()
            print_name()
            print(Figlet('small').renderText('Employee Menu'))
            print(colored('Hello ' + retrieve_employee(username)[3], 'blue'))
            print('Login time: ' + login_time + '\n')
            print('Choose an option: \n')
            for i in main_menu:
                print('\t' + i)
            print()
            inp = input('Command: ')
            print()
            if inp == '1':
                view_employee_info(employee_user_name=username)
            elif inp == '2':
                customers()
            elif inp == '3':
                about()
            elif inp == '4':
                print('Logged out!')
                main.intro()
            elif inp == '5':
                print('Goodbye!\nLogout time: ', get_current_time())
                break
            else:
                print("Invalid entry!")
            pause()
    except KeyboardInterrupt:
        print('\nForce exit encountered!')


if __name__ == '__main__':
    print('Log in first\nAbort!')

import getpass
import os

import main
from database import retrieve_employee, retrieve_all_employees, register_employee, delete_employee, make_admin, \
    retrieve_all_customers, retrieve_customer, get_id_customer, register_customer, delete_customer, update_customer
from def_customers import customers
from def_employees import employees
from pyfiglet import Figlet
from termcolor import colored
from utility import clear_console, print_name, get_current_time, pause, about, validate_email, validate_phone, \
    send_message, generate_otp


def branches():
    branch_list = []


def intro():
    username = os.getenv('loggedin')

    try:
        main_menu = ['1. Employees', '2. Customers', '3. Branches', '4. About Us', '5. Logout', '6. Exit',
                     'Press Ctrl + C to Force Exit']
        login_time = get_current_time()
        while True:
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
                employees()
            elif inp == '2':
                customers()
            elif inp == '3':
                branches()
                # TODO: Implement Branches
            elif inp == '4':
                about()
            elif inp == '5':
                print('Logged out!')
                main.intro()
            elif inp == '6':
                print('Goodbye!\nLogout time: ', get_current_time())
                break
            else:
                print("Invalid entry!")
            pause()
    except KeyboardInterrupt:
        print('\nForce exit encountered!')


if __name__ == '__main__':
    print('Log in first\nAbort!')

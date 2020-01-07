import os

from pyfiglet import Figlet
from termcolor import colored

import main
from database import retrieve_employee, retrieve_all_employees, register_employee
from utility import clear_console, print_name, get_current_time, pause, about


def employees():
    employees_list = ['1. View All Employees', '2. Register New Employee', '3. Edit Employee Info']
    clear_console()
    print_name()
    print(Figlet('small').renderText('Employees'))
    print('Choose an option: \n')
    for i in employees_list:
        print('\t' + i)
    print()
    inp = input('Command: ')
    if inp == '1':
        print(76 * '-' + '\n' + '| {:^10s} | {:^13} | {:^20} | {:^20} |'.format('Username', 'Employee ID', 'First Name',
                                                                                'Last Name'))
        all_employees = retrieve_all_employees()
        if all_employees:
            for i in all_employees:
                print(76 * '-' + '\n' + '| {:^10s} | {:^13} | {:^20} | {:^20} |'.format(i[0], i[1], i[2], i[3]))
            print(76 * '-')
        else:
            print('No registered employees found!')
    elif inp == '2':
        while True:
            clear_console()
            print_name()
            print(Figlet('small').renderText('Register Employee'))
            user_name = input('Username: ')
            if retrieve_employee(user_name):
                print('\nUsername already in use!\n')
                pause()
            else:
                break
        first_name = input('First Name: ')
        last_name = input('Last Name: ')
        register_employee(user_name, first_name, last_name)
        print('Employee registered successfully!\nEmployee Number: ' + str(retrieve_employee(user_name)[1]))


def customers():
    customers_list = []


def branches():
    branches_list = []


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
            print(colored('Hello ' + retrieve_employee(username)[2], 'blue'))
            print('Login time: ' + login_time + '\n')
            print('Choose an option: \n')
            for i in main_menu:
                print('\t' + i)
            print()
            inp = input('Command: ')
            print()
            if inp == '1':
                employees()
                # TODO: Implement Employees
            elif inp == '2':
                customers()
                # TODO: Implement Customers
            elif inp == '3':
                branches()
                # TODO: Implement Branches
            elif inp == '4':
                about()
            elif inp == '5':
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

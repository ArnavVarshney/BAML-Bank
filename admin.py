import os

from pyfiglet import Figlet
from termcolor import colored

import main
from database import retrieve_employee, retrieve_all_employees, register_employee
from utility import clear_console, print_name, get_current_time, pause, about


def employees():
    employees_list = ['1. View All Employees', '2. Register New Employee', '3. Modify Employee',
                      '#. Return to Previous Menu']
    while True:
        clear_console()
        print_name()
        print(Figlet('small').renderText('Employees'))
        print('Choose an option: \n')
        for i in employees_list:
            print('\t' + i)
        print()
        inp = input('Command: ')
        if inp == '1':
            print(
                103 * '-' + '\n' + '| {:^13s} | {:^10s} | {:^15s} | {:^6s} | {:^20s} | {:^20s} |'.format('Employee ID',
                                                                                                         'Username',
                                                                                                         'Password',
                                                                                                         'Role',
                                                                                                         'First Name',
                                                                                                         'Last Name'))
            all_employees = retrieve_all_employees()
            if all_employees:
                for i in all_employees:
                    print(
                        103 * '-' + '\n' + '| {:^13s} | {:^10s} | {:^15s} | {:^6s} | {:^20s} | {:^20s} |'.format(
                            str(i[0]), i[1],
                            i[2], str(i[5]),
                            i[3], i[4]))
                print(103 * '-')
            else:
                print('No registered employees found!')
            break
        elif inp == '2':
            clear_console()
            print_name()
            print(Figlet('small').renderText('Register Employee'))
            while True:
                user_name = input('Username: ')
                if retrieve_employee(user_name):
                    print('\nUsername already in use!\n')
                else:
                    break
            first_name = input('First Name: ')
            last_name = input('Last Name: ')
            while True:
                password = input('Password: ')
                if len(password) == 0:
                    print('\nInvalid password!\n')
                else:
                    break
            while True:
                role = input('Role [1. Employee, 2. Customer]: ')
                if role not in ['0', '1', '2']:
                    print('\nInvalid role!\n')
                else:
                    break
            register_employee(user_name, first_name, last_name, password, role)
            print('Employee registered successfully!\nEmployee Number: ' + str(retrieve_employee(user_name)[0]))
            break
        elif inp == '3':
            clear_console()
            print_name()
            print(Figlet('small').renderText('Modify Employee'))
            print('Choose an option: \n')
            modify_employee_list = ['1. Delete Employee', '2. Edit Employee Info', '#. Return to Previous Menu']
            for i in modify_employee_list:
                print('\t' + i)
            print()
            inp1 = input('Command: ')
            if inp1 == '1':
                employee_user_name = input('Employee Username: ')
                # if retrieve_employee(employee_user_name):



        elif inp == '#':
            break
        else:
            print('Invalid entry!')
            pause()


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
                print('Logged out!')
                pause()
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

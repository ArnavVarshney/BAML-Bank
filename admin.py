import os

from pyfiglet import Figlet
from termcolor import colored

import main
from database import *
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
            modify_employee_list = ['1. Delete Employee', '2. Promote Employee', '#. Return to Previous Menu']
            for i in modify_employee_list:
                print('\t' + i)
            print()
            inp1 = input('Command: ')
            if inp1 == '1':
                while True:
                    employee_user_name = input('Employee Username: ')
                    if retrieve_employee(employee_user_name):
                        ch = input('Confirm? (Y/N): ')
                        if ch == 'Y':
                            delete_employee(employee_user_name)
                        break
                    else:
                        print('Employee Not Found!')
            elif inp1 == '2':
                while True:
                    employee_user_name = input('Employee Username: ')
                    if retrieve_employee(employee_user_name):
                        ch = input('Confirm? (Y/N): ')
                        if ch == 'Y':
                            make_admin(employee_user_name)
                        break
                    else:
                        print('Employee Not Found!')

        elif inp == '#':
            break
        else:
            print('Invalid entry!')
            pause()


def customers():
    customers_list = ['1. View All Customers', '2. Register New Customer', '3. Modify Customer',
                      '#. Return to Previous Menu']
    while True:
        clear_console()
        print_name()
        print(Figlet('small').renderText('Customers'))
        print('Choose an option: \n')
        for i in customers_list:
            print('\t' + i)
        print()
        inp = input('Command: ')
        if inp == '1':
            print(
                103 * '-' + '\n' + '| {:^13s} | {:^10s} | {:^15s} | {:^6s} | {:^20s} | {:^20s} | {:^20s} |'.format(
                    'Customer ID',
                    'Username',
                    'Password',
                    'First Name',
                    'Last Name',
                    'Phone Number',
                    'Email ID'))
            all_customers = retrieve_all_customers()
            if all_customers:
                for i in all_customers:
                    print(
                        103 * '-' + '\n' + '| {:^13s} | {:^10s} | {:^15s} | {:^6s} | {:^20s} | {:^20s} | {:^20s} |'.format(
                            str(i[12]), i[13],
                            i[14], i[0],
                            i[1],
                            str(i[10]), i[11]))
                print(103 * '-')
            else:
                print('No registered customers found!')
            break
        elif inp == '2':
            clear_console()
            print_name()
            print(Figlet('small').renderText('Register Customer'))
            while True:
                user_name = input('Username: ')
                if retrieve_customer(user_name):
                    print('\nUsername already in use!\n')
                else:
                    break
            first_name = input('First Name: ')
            last_name = input('Last Name: ')
            building = input('Building: ')
            street_name = input('Street Name: ')
            locality =input('Locality: ')
            landmark =input('Landmark: ')
            city = input('City: ')
            state = input('State: ')
            country = input('Country: ')
            zip_code = input('Zip code: ')
            phone_number = input('Phone Number: ')
            email_id = input('Email ID: ')
            customer_id = id_customer()
            while True:
                password = input('Password: ')
                if len(password) == 0:
                    print('\nInvalid password!\n')
                else:
                    break
            register_customer(first_name, last_name, building, street_name, locality, landmark, city, state,country, zip_code, phone_number, email_id, customer_id, user_name,password)
            print('Customer registered successfully!\nCustomer ID: ' + str(retrieve_customer(user_name)[12]))
            break
        elif inp == '3':
            clear_console()
            print_name()
            print(Figlet('small').renderText('Modify Customer'))
            print('Choose an option: \n')
            modify_customer_list = ['1. Delete Customer', '#. Return to Previous Menu']
            for i in modify_customer_list:
                print('\t' + i)
            print()
            inp1 = input('Command: ')
            if inp1 == '1':
                while True:
                    customer_user_name = input('Customer Username: ')
                    if retrieve_customer(customer_user_name):
                        ch = input('Confirm? (Y/N): ')
                        if ch == 'Y':
                            delete_customer(customer_user_name)
                        break
                    else:
                        print('Customer Not Found!')
        elif inp == '#':
            break
        else:
            print('Invalid entry!')
            pause()


def branches():
    branches_list = ['1. View all Branches','2. Create a new branch', '3. Add/Remove Customer from Branch', '4. Modify Branch',
                      '#. Return to Previous Menu', ]
    while True:
        clear_console()
        print_name()
        print(Figlet('small').renderText('Branches'))
        print('Choose an option: \n')
        for i in branches_list:
            print('\t' + i)
        print()
        inp = input('Command: ')
        if inp == '1':
            print(
                198 * '-' + '\n' + '| {:^13s} | {:^10s} | {:^15s} | {:^20s} | {:^20s} | {:^20s} | {:^20s} | {:^20s} | {:^20s} | {:^20s} |'.format(
                    'Branch Code',
                    'Branch Name',
                    'Building',
                    'Street Name',
                    'Locality',
                    'Landmark',
                    'City',
                    'State',
                    'Country',
                    'Zip Code'))
            all_branches = retrieve_all_branches()
            if all_branches:
                for i in all_branches:
                    print(
                        198 * '-' + '\n' + '| {:^13s} | {:^10s} | {:^15s} | {:^20s} | {:^20s} | {:^20s} | {:^20s} | {:^20s} | {:^20s} | {:^20s} |'.format(
                            str(i[0]), i[1],
                            str(i[2]), i[3],
                            i[4], i[5],
                            i[6], i[7],
                            i[8],str(i[9])))
                print(198 * '-')
                pause()
            else:
                print('No registered branches found!')
            break
        elif inp == '2':
            clear_console()
            print_name()
            print(Figlet('small').renderText('Register Branch'))
            branch_code = id_branch()
            branch_name = input('Branch Name: ')
            building = input('Building: ')
            street_name = input('Street Name: ')
            locality = input('Locality: ')
            landmark = input('Landmark: ')
            city = input('City: ')
            state = input('State: ')
            country = input('Country: ')
            zip_code = input('Zip Code: ')
            register_branch(branch_code , branch_name , building , street_name , locality , landmark , city , state , country , zip_code)
            print('Branch registered successfully!\nBranch Code: ' + str(branch_code))
            break
        elif inp == '3':
            branches_list = ['1. Add a Customer', '2. Remove a Customer',
                             '#. Return to Previous Menu' ]
            clear_console()
            print_name()
            print(Figlet('small').renderText('Associated Customers'))
            branch_code = input('Branch Code: ')
            print(
                60 * '-' + '\n' + '| {:^15s} | {:^10s} | {:^10s} |'.format(
                    'Branch Code',
                    'Customer ID',
                    'Account Number',))
            result = retrieve_accounts(branch_code)
            if result:
                for i in result:
                    print(
                        60 * '-' + '\n' + '| {:^15s} | {:^10s} | {:^10s} |'.format(
                            str(i[0]), str(i[1]),
                            i[4]))
                print(60 * '-')
                pause()
                for i in branches_list:
                    print('\t' + i)
                print()
                inp_1 = input('Command: ')
                if inp_1 == '1':
                    customer_id = input("Customer ID: ")

            else:
                print("No associated Customers")


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

from pyfiglet import Figlet

from database import *
from utility import clear_console, print_name, pause


def view_all_branches():
    all_branches = retrieve_all_branches()
    if all_branches:
        print(
            155 * '-' + '\n' + '| {:^13s} | {:^15s} | {:^15s} | {:^20s} | {:^10s} | {:^10s} | {:^10s} | {:^10s} | {:^10s} | {:^10s} |'.format(
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
        for i in all_branches:
            print(
                155 * '-' + '\n' + '| {:^13s} | {:^15s} | {:^15s} | {:^20s} | {:^10s} | {:^10s} | {:^10s} | {:^10s} | {:^10s} | {:^10s} |'.format(
                    str(i[0]), str(i[1]),
                    str(i[2]), i[3],
                    i[4], i[5],
                    i[6], i[7],
                    i[8],str(i[9])))
        print(155 * '-')
    else:
        print('No registered branches found!')


def branches():
    branches_list = ['1. View all Branches','2. Create a new branch', '3. Add/Remove customers from Branch ', '4. View Transaction details',
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
            view_all_branches()
            pause()
        elif inp == '2':
            clear_console()
            print_name()
            print(Figlet('small').renderText('Register Branch'))
            branch_name = input('Branch Name: ')
            building = input('Building: ')
            street_name = input('Street Name: ')
            locality = input('Locality: ')
            landmark = input('Landmark: ')
            city = input('City: ')
            state = input('State: ')
            country = input('Country: ')
            while True:
                zip_code = input('Zip Code: ')
                if zip_code.isnumeric() and len(zip_code) == 6:
                    break
                else:
                    print('\nInvalid Zip Code\n')
            register_branch(branch_name , building , street_name , locality , landmark , city , state , country , zip_code)
            connection = connect('db.sqlite')
            crsr = connection.cursor()
            crsr.execute("SELECT * FROM branch WHERE branch_name = ?", (branch_name,))
            rows = crsr.fetchone()
            connection.close()
            print('Branch registered successfully!\nBranch Code: ' + str(rows[0]))
            pause()
            break

        elif inp == '3':
            branch_list = ['1. Add a Customer', '2. Remove a Customer',
                             '#. Return to Previous Menu' ]
            clear_console()
            print_name()
            print(Figlet('small').renderText('Associated Customers'))
            view_all_branches()
            retrieve_all_accounts()
            for i in branch_list:
                print('\t' + i)
            print()
            inp_1 = input('Command: ')
            if inp_1 == '1':
                customer_id = input("Customer ID: ")
                connection = connect('db.sqlite')
                crsr = connection.cursor()
                select_customer = "SELECT * FROM customer WHERE customer_id = ?"
                crsr.execute(select_customer, (customer_id,))
                result = crsr.fetchone()
                print(result)
                connection.close()
                if result:
                    num = id_account()
                    branch_code = input("Branch Code: ")
                    add_customer(customer_id, branch_code, num)
                    pause()
                else:
                    print('Invalid entry!')
                    break
            elif inp_1 == '2':
                customer_id = input("Customer ID: ")
                remove_customer(customer_id)
            elif inp == '#':
                break
            else:
                print('Invalid entry!')
                pause()
                break

        elif inp == '4':
            clear_console()
            print_name()
            print('\n'"Filter by:")
            branch_list = ['1. Customer ID ', '2. Branch ID',
                             '#. Return to Previous Menu']
            print(Figlet('small').renderText('Transaction Details'))
            for i in branch_list:
                print('\t' + i)
            print()
            inp_1 = input('Command: ')
            if inp_1 == '1':
                customer_id = input("Customer ID: ")
                result = retrieve_accounts_customer(customer_id)
                if len(result) != 0:
                    print(
                        165 * '-' + '\n' + '| {:^13s} | {:^15s} | {:^15s} | {:^20s} | {:^10s} | {:^10s} | {:^20s} | {:^20s} | {:^15s} |'.format(
                            'Customer ID',
                            'Account Number',
                            'Branch ID',
                            'Date',
                            'Time',
                            'Amount',
                            'Opening Balance',
                            'Closing Balance',
                            'Remarks'))
                    for i in result:
                        if i[2] is not None:
                            print(
                                165 * '-' + '\n' + '| {:^13s} | {:^15s} | {:^15s} | {:^20s} | {:^10s} | {:^10s} | {:^20s} | {:^20s} | {:^15s} |'.format(
                                    str(i[0]), str(i[1]),
                                    str(i[4]), i[2],
                                    i[3], str(i[5]),
                                    str(i[6]), str(i[7]),
                                    str(i[8])))
                    print(165 * '-')
                else:
                    print('No records found!')
                pause()
            elif inp_1 == '2':
                branch_code = input("Branch ID: ")
                result = retrieve_accounts(branch_code)
                if len(result) != 0:
                    print(
                        165 * '-' + '\n' + '| {:^13s} | {:^15s} | {:^15s} | {:^20s} | {:^10s} | {:^10s} | {:^20s} | {:^20s} | {:^15s} |'.format(
                            'Customer ID',
                            'Account Number',
                            'Branch ID',
                            'Date',
                            'Time',
                            'Amount',
                            'Opening Balance',
                            'Closing Balance',
                            'Remarks'))
                    for i in result:
                        if i[2] is not None:
                            print(
                                165 * '-' + '\n' + '| {:^13s} | {:^15s} | {:^15s} | {:^20s} | {:^10s} | {:^10s} | {:^20s} | {:^20s} | {:^15s} |'.format(
                                    str(i[0]), str(i[1]),
                                    str(i[4]), i[2],
                                    i[3], str(i[5]),
                                    str(i[6]), str(i[7]),
                                    str(i[8])))
                    print(165 * '-')
                else:
                    print('No records found!')
                pause()
                pause()
            elif inp == '#':
                break
            else:
                print('Invalid entry!')
                pause()
        elif inp == '#':
            break
        else:
            print('Invalid entry!')

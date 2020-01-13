'''from pyfiglet import Figlet

from database import retrieve_all_branches
from utility import clear_console, print_name, pause


def branches():
    branches_list = ['1. View all Branches','2. Create a new branch', '3. Add/Remove Customer from Branch', '4. View transaction details',
                      '#. Return to Previous Menu', ]
    for counter in range(5):
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
                198 * '-' + '\n' + '| {:^13s} | {:^10s} | {:^15s} | {:^10s} | {:^10s} | {:^10s} | {:^10s} | {:^10s} | {:^10s} | {:^10s} |'.format(
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
                print(
                    198 * '-' + '\n' + '| {:^13s} | {:^10s} | {:^15s} | {:^10s} | {:^10s} | {:^10s} | {:^10s} | {:^10s} | {:^10s} | {:^10s} |'.format(
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
                        198 * '-' + '\n' + '| {:^13s} | {:^10s} | {:^15s} | {:^10s} | {:^10s} | {:^10s} | {:^10s} | {:^10s} | {:^10s} | {:^10s} |'.format(
                            str(i[0]), i[1],
                            str(i[2]), i[3],
                            i[4], i[5],
                            i[6], i[7],
                            i[8],str(i[9])))
                print(198 * '-')
                pause()
            else:
                print('No registered branches found!')
                pause()
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
            pause()
            break

        elif inp == '3':
            branches_list = ['1. Add a Customer', '2. Remove a Customer',
                             '#. Return to Previous Menu' ]
            clear_console()
            print_name()
            print(Figlet('small').renderText('Associated Customers'))
            result = retrieve_all_accounts()
            print(
                100 * '-' + '\n' + '| {:^15s} | {:^15s} | {:^20s} | {:^20s} | {:^20s} |'.format(
                    'Branch Code',
                    'Customer ID',
                    'First Name',
                    'Last Name',
                    'Account Number', ))
            if result:
                for i in result:
                    print(
                        100 * '-' + '\n' + '| {:^15s} | {:^15s} | {:^20s} | {:^20s} | {:^20s} |'.format(
                            str(i[4]), str(i[0]),
                            i[10], i[11],
                            str(i[2])))
                            str(i[1])))
                print(100 * '-')
                branch_code = input('Branch Code: ')
                result = retrieve_branch(branch_code)
                if result:
                    for i in branches_list:
                        print('\t' + i)
                    print()
                    inp_1 = input('Command: ')
                    if inp_1 == '1':
                        customer_id = input("Customer ID: ")
                        connection = connect('db.sqlite')
                        crsr = connection.cursor()
                        select_customer = "SELECT * FROM customer WHERE customer_id = ?"
                        crsr.execute(select_customer, (customer_id,))
                        connection.close()
                        if result:
                            num = id_account()
                            add_customer(customer_id,branch_code,num)
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
                else:
                    print('Invalid entry!')
                    break
        elif inp == '4':
            clear_console()
            print_name()
            print('\n'"Filter by:")
            branches_list = ['1.Customer ID ', '2. Branch ID',
                             '#. Return to Previous Menu']
            print(Figlet('small').renderText('Transaction Details'))
            for i in branches_list:
                print('\t' + i)
            print()
            inp_1 = input('Command: ')
            if inp_1 == '1':
                customer_id = input("Customer ID: ")
                result = retrieve_accounts_customer(customer_id)
                print (result)
                pause()
            elif inp_1 == '2':
                branch_code = input("Branch ID: ")
                result = retrieve_accounts(branch_code)
                print(result)
                pause()
            elif inp == '#':
                break
            else:
                print('Invalid entry!')
                pause()
        elif inp == '#':
            break
        else:
            print('Invalid entry!')'''

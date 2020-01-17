from database import *
from def_customers import *
from utility import clear_console, print_name, get_current_time, pause

def intro():
    c = 1
    username = os.getenv('loggedin')
    all_accounts = list_all_account(username)
    while c == 1:
        for i in all_accounts:
            print(i[1])
        choice = input("Which account would you like to login to? ")
        for i in all_accounts:
            if choice == i[1]:
                account = choice
                c = 0
    try:
        main_menu = ['1. Deposit', '2. Transact', '3. Transfer to another account',
                     '4. View your Balance/Transaction details', '5. Register a new account', '6. Logout',
                     'Press Ctrl + C to Force Exit']
        login_time = get_current_time()
        while True:
            clear_console()
            print_name()
            print(Figlet('small').renderText('Customer Menu'))
            print(colored('Hello ' + retrieve_customer(username)[0], 'blue'))
            print('Login time: ' + login_time + '\n')
            print("Account number:" + account)
            print('Choose an option: \n')
            for i in main_menu:
                print('\t' + i)
            print()
            inp = input('Command: ')
            print()
            if inp == '1':
                result = retrieve_customer(username)
                if result[16] is None:
                    print("Please register your account at one of our branches.")
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
                        for i in all_branches:
                            print(
                                198 * '-' + '\n' + '| {:^13s} | {:^10s} | {:^15s} | {:^10s} | {:^10s} | {:^10s} | {:^10s} | {:^10s} | {:^10s} | {:^10s} |'.format(
                                    str(i[0]), i[1],
                                    str(i[2]), i[3],
                                    i[4], i[5],
                                    i[6], i[7],
                                    i[8], str(i[9])))
                        print(198 * '-')
                        pause()
                    else:
                        print('No registered branches found!')
                        pause()
                    break
                else:
                    deposit_amount = int(input("Deposit Amount: "))
                    deposit(deposit_amount, username)

            elif inp == '2':
                result = retrieve_customer(username)
                if result[16] is None:
                    print("Please register your account at one of our branches.")
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
                        for i in all_branches:
                            print(
                                198 * '-' + '\n' + '| {:^13s} | {:^10s} | {:^15s} | {:^10s} | {:^10s} | {:^10s} | {:^10s} | {:^10s} | {:^10s} | {:^10s} |'.format(
                                    str(i[0]), i[1],
                                    str(i[2]), i[3],
                                    i[4], i[5],
                                    i[6], i[7],
                                    i[8], str(i[9])))
                        print(198 * '-')
                        pause()
                    else:
                        print('No registered branches found!')
                        pause()
                    break
                else:
                    transact_amount = int(input("Transaction Amount: "))
                    transact(transact_amount, username)

            elif inp == '3':
                result = retrieve_customer(username)
                if result[16] is None:
                    print("Please register your account at one of our branches.")
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
                        for i in all_branches:
                            print(
                                198 * '-' + '\n' + '| {:^13s} | {:^10s} | {:^15s} | {:^10s} | {:^10s} | {:^10s} | {:^10s} | {:^10s} | {:^10s} | {:^10s} |'.format(
                                    str(i[0]), i[1],
                                    str(i[2]), i[3],
                                    i[4], i[5],
                                    i[6], i[7],
                                    i[8], str(i[9])))
                        print(198 * '-')
                        pause()
                    else:
                        print('No registered branches found!')
                        pause()
                    break
                else:
                    acc = input("Target Account: ")
                    transfer_amount = int(input("Transfer Amount: "))
                    transfer(transfer_amount, username, (acc,))

            elif inp == '4':
                result = str(view_balance(username))
                print("Your account balance is: $ " + result)
            elif inp == '5':
                connection = connect('db.sqlite')
                crsr = connection.cursor()
                crsr.execute('SELECT * FROM customer WHERE user_name = ?', (username,))
                temp = crsr.fetchone()
                register_account(temp[12], temp[15])
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

from pyfiglet import Figlet
from termcolor import colored

from utility import clear_console, print_name, get_current_time, pause, about


def employees():
    employees_list = []


def customers():
    customers_list = []


def branches():
    branches_list = []


def intro(username):
    """
    Prints the main menu and forwards to respective functions
    """
    try:
        main_menu = ['1. Employees', '2. Customers', '3. Branches', '4. About Us', '5. Exit',
                     'Press Ctrl + C to Force Exit']
        login_time = get_current_time()
        while True:
            clear_console()
            print_name()
            print(Figlet('small').renderText('Admin Menu'))
            print(colored('Hello ' + username, 'blue'))
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
                print('Goodbye!\nLogout time: ', get_current_time())
                break
            else:
                print("Invalid entry!")
            # Pause before printing the menu again
            pause()
    except KeyboardInterrupt:
        print('Exiting!')

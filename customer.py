'''import os

from pyfiglet import Figlet
from termcolor import colored

import main
from database import retrieve_all_customers, retrieve_customer, register_customer, delete_customer, id_customer
from utility import clear_console, print_name, get_current_time, pause, about
def intro():
    username = os.getenv('loggedin')
    try:
        main_menu = ['1. Deposit', '2. Transact', '3. Transfer to another account', '4. Logout'
                     'Press Ctrl + C to Force Exit']
        login_time = get_current_time()
        while True:
            clear_console()
            print_name()
            print(Figlet('small').renderText('Customer Menu'))
            print(colored('Hello ' + retrieve_customer(username)[3], 'blue'))
            print('Login time: ' + login_time + '\n')
            print('Choose an option: \n')
            for i in main_menu:
                print('\t' + i)
            print()
            inp = input('Command: ')
            print()
            if inp == '1':
                
            elif inp == '2':

            elif inp == '3':

            elif inp == '4':
                print('Goodbye!\nLogout time: ', get_current_time())
                break
            else:
                print("Invalid entry!")
            pause()
    except KeyboardInterrupt:
        print('\nForce exit encountered!')


    if __name__ == '__main__':
        print('Log in first\nAbort!')'''
import os

from pyfiglet import Figlet

import admin
import customer
import employee
from authentication import existing_user
from database import sql_setup
from utility import print_name, clear_console, pause, about

sql_setup()

os.environ['loggedin'] = ''

def intro():
    main_menu = ['1. Login', '2. About Us', '3. Exit']
    try:
        while True:
            clear_console()
            print_name()
            print(Figlet('small').renderText('Welcome'))
            print('Choose an option: \n')
            for i in main_menu:
                print('\t' + i)
            print()
            ch = input('Command: ')
            if ch == '1':
                tup = existing_user()
                if tup:
                    role = tup[0]
                    username = tup[1]
                    os.environ['loggedin'] = username
                    if role == '0':
                        admin.intro()
                    elif role == '1':
                        employee.intro()
                    elif role == '2':
                        customer.intro()
                else:
                    print('Invalid credentials!')
                    pause()
                    continue
                break
            elif ch == '2':
                print()
                about()
            elif ch == '3':
                print('Goodbye!')
                break
            else:
                print('Invalid Input!')
            pause()
    except KeyboardInterrupt:
        print('\nForce exit encountered!')


if __name__ == '__main__':
    intro()
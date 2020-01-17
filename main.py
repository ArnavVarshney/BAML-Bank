import os

from pyfiglet import Figlet

import admin
import customer
from authentication import existing_user
from database import sql_setup, register_employee, register_branch, register_customer, register_account
from utility import print_name, clear_console, pause, about

sql_setup()
# Demo Data

try:
    register_employee('admin', 'Arnav', 'Varshney', 'admin', 0, 1, '29/12/2003', 'M', '27', 'Punggol Field Walk',
                      'Punggol', '', 'Singapore', 'Singapore', 'Singapore', '828649', '+919662364695',
                      'varshney.arnav@gmail.com')
except:
    print('Couldn\'t register admin. Check if value already exists!')

try:
    register_branch('HQ', '27', 'Punggol Field Walk', 'Punggol', '', 'Singapore', 'Singapore', 'Singapore', '828649')
except:
    print('Couldn\'t register HQ. Check if value already exists!')

try:
    register_customer('Arnav', 'HQ', '27', 'Punggol Field Walk', 'Punggol', '', 'Singapore', 'Singapore', 'Singapore',
                      '828649', '+919662364695', 'varshney.arnav@gmail.com', 'arnavvarshney', 'arnav29', 1,
                      '29/12/2003', 'M', 0)
except:
    print('Couldn\'t register customer. Check if value already exists!')

register_account(1,1)


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
                    if role == '2':
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

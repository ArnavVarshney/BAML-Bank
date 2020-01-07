import os

from pyfiglet import Figlet

import admin
from authentication import existing_user, new_user
from database import sql_setup
from utility import print_name, clear_console, pause

sql_setup()
os.environ['loggedin'] = ''


def intro():
    main_menu = ['1. Existing User', '2. New User', '3. About Us', '4. Exit']

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
            else:
                print('Invalid credentials!')
                pause()
                continue
            break
        elif ch == '2':
            new_user()
        elif ch == '4':
            print('Goodbye!')
            break
        else:
            print('Invalid Input!')
        pause()


if __name__ == '__main__':
    intro()

import os

from pyfiglet import Figlet
from database import sql_setup

sql_setup()
import admin
from authentication import existing_user
from utility import print_name, clear_console, pause, about

sql_setup()
os.environ['loggedin'] = ''


def intro():
    main_menu = ['1. Login', '2. About Us', '3. Exit']
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
            about()
        elif ch == '3':
            print('Goodbye!')
            break
        else:
            print('Invalid Input!')
        pause()

if __name__ == '__main__':
    intro()
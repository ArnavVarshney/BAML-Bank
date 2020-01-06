import admin
from authentication import existing_user, new_user
from database import sql_setup
from utility import print_name, clear_console, pause

sql_setup()

main_menu = ['1. Existing User', '2. New User', '3. About Us', '4. Exit']

while True:
    clear_console()
    print_name()
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
            if role == 0:
                admin.intro(username)
        else:
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

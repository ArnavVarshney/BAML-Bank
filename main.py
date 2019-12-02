from datetime import datetime
from time import sleep


def intro():
    menu_list = ['1. Open Account', '2. Close Account', '3. Modify Account', '4. Deposit/Withdraw',
                 '5. Generate Report',
                 '6. About Us', '7. Exit']
    inp = ''
    while True:
        print(27 * '=')
        print(1 * '\t' + 'Welcome to Bank XXX')
        print(27 * '=')
        print()
        for i in menu_list:
            print('\t' + i)
        print()
        inp = input('Command: ')
        print()
        if inp == '7':
            print('Goodbye!\nLogout time: ', datetime.now().strftime("%H:%M:%S"))
            break
        elif inp == '1':
            createAccount()
        elif inp == '6':
            about()
        else:
            print("Invalid entry!")


def createAccount():
    accNo = input("Account number: ")
    name = input("Account holder's name: ")
    balance = input("Initial balance: ")
    addressStreet = input("Street: ")
    addressCity = input("City: ")
    addressState = input("State: ")
    addressCountry = input("Country: ")


def about():
    str = 'Team XXX *dab*\n\tMembers:\n\t\t1. Arnav\n\t\t2. Pradyumn\n\t\t3. Aditi\n\t\t4. Mihir\n\t\t5. Shishir\n\n'
    for char in str:
        sleep(0.1)
        print(char, end='', flush=True)
    sleep(1)
    intro()


if __name__ == "__main__":
    intro()

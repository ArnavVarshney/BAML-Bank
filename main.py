from datetime import datetime


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


def aboutUs():
    print('Team XXX')
    print('Members:')
    print('\t1. Arnav\n\t2. Pradyumn\n\t3. Aditi\n\t4. Mihir\n\t5. Shishir\n')
    intro()


if __name__ == "__main__":
    intro()

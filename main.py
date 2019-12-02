def intro():
    ch = ''
    while True:
        print('\t  Welcome to XXX')
        print('\t\tMAIN MENU')
        print('1. Create Account')
        print('#. About')
        print('*. Exit')
        ch = input('Enter your choice: ')
        if ch == '#':
            aboutUs()
        elif ch == 1:
            createAccount()
        elif ch == '*':
            print("Goodbye!")
            break


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

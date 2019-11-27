"""Git test"""

def intro():
    ch = ''
    while True:
        print('\t  Welcome to XXX')
        print('\t\tMAIN MENU')
        print('#. About')
        print('*. Exit')
        ch = input('Enter your choice: ')
        if ch == '#':
            aboutUs()
        elif ch == '*':
            print("Goodbye!")
            break


def aboutUs():
    print('Team XXX')
    print('Members:')
    print('\tArnav\n\tPradyumn\n\tAditi\n\tMihir\n\tShishir\n')
    intro()


if __name__ == "__main__":
    intro()

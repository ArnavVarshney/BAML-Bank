from datetime import datetime
from time import sleep

global_account_number = 1


class Address(object):
    def __init__(self, building, street_name, landmark, city, state, country, zip_code):
        self.zip_code = zip_code
        self.street_name = street_name
        self.city = city
        self.state = state
        self.country = country
        self.landmark = landmark
        self.building = building

    def __str__(self):
        return 'Address\n\n' + self.building + self.street_name + self.landmark + self.city + self.state + self.country + self.zip_code


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
            create_account()
        elif inp == '6':
            about()
        else:
            print("Invalid entry!")


def input_address():
    loc_building = input('Building: ')
    loc_street_name = input('Street Name: ')
    loc_landmark = input('Landmark: ')
    loc_city = input('City: ')
    loc_state = input('State: ')
    loc_country = input('Country: ')
    loc_zip_code = input('Zip Code: ')
    return Address(loc_building, loc_street_name, loc_landmark, loc_city, loc_state, loc_country, loc_zip_code)


def create_account():
    global global_account_number
    account_address = input_address()
    account_number = global_account_number
    global_account_number += 1


def about():
    str = 'Team XXX *dab*\n\tMembers:\n\t\t1. Arnav Varshney\n\t\t2. Pradyumn Mishra\n\t\t3. Aditi Prasad\n\t\t4. Mihir Ghonge\n\t\t5. Shishir\n\n'
    for char in str:
        sleep(0.1)
        print(char, end='', flush=True)
    sleep(1)
    intro()


if __name__ == "__main__":
    intro()

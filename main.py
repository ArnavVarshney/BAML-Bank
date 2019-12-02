from datetime import datetime
from time import sleep

global_customer_id = 1


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
        return str(
            self.building + '\n' + self.street_name + '\n' + self.landmark + '\n' + self.city + '\n' + self.state + '\n' + self.country + '\n' + self.zip_code)

    def input_address(self):
        self.building = input('Building: ')
        self.street_name = input('Street Name: ')
        self.landmark = input('Landmark: ')
        self.city = input('City: ')
        self.state = input('State: ')
        self.country = input('Country: ')
        self.zip_code = input('Zip Code: ')


class Customer(object):
    def __init__(self, first_name, last_name, address, phone_number, email, active_accounts, customer_id):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.active_accounts = active_accounts
        self.customer_id = customer_id

    def __str__(self):
        return str(self.customer_id + '\n' + self.first_name + ' ' + self.last_name + '\n' + str(
            self.address) + '\n' + self.phone_number + '\n' + self.email + '\n' + self.active_accounts)


class Account(object):
    def __init__(self, account_number, balance, customer, max_transaction_amount):
        self.account_number = account_number
        self.balance = balance
        self.customer = customer
        self.max_transaction_amount = max_transaction_amount

    def __str__(self):
        return str(
            self.account_number + '\n' + 'Owner ID: ' + self.customer.customer_id + '\n' + self.balance + '\n' + self.max_transaction_amount)

    def deposit(self, amount):
        if amount <= 0:
            print('Invalid amount. Please enter positive values.\nTransaction aborted!')
        elif amount > self.max_transaction_amount:
            print('Amount entered is more than the maximum.\nTransaction aborted!')
        else:
            self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            print('Invalid amount. Please enter positive values.\nTransaction aborted!')
        elif amount > self.max_transaction_amount:
            print('Amount entered is more than the maximum.\nTransaction aborted!')
        elif amount > self.balance:
            print('Amount entered is more than balance.\nTransaction aborted')
        else:
            self.balance -= amount


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
        elif inp == '6':
            about()
        else:
            print("Invalid entry!")


def about():
    about_str = 'Team XXX *dab*\n\tMembers:\n\t\t1. Arnav Varshney\n\t\t2. Pradyumn Mishra\n\t\t3. Aditi Prasad\n\t\t4. Mihir Ghonge\n\t\t5. Shishir\n\n'
    for char in about_str:
        sleep(0.1)
        print(char, end='', flush=True)
    sleep(5)
    intro()


if __name__ == "__main__":
    intro()

from datetime import datetime
from time import sleep

global_customer_id = 0
global_customer_map = {}


class Address(object):
    def __init__(self):
        self.zip_code = 0
        self.street_name = ''
        self.city = ''
        self.state = ''
        self.country = ''
        self.landmark = ''
        self.building = ''

    def __str__(self):
        return str(
            'Building: ' + self.building + '\n' + 'Street: ' + self.street_name + '\n' + 'Landmark: ' + self.landmark + '\n' + 'City: ' + self.city + '\n' + 'State: ' + self.state + '\n' + 'Country: ' + self.country + '\n' + 'Zip Code: ' + str(
                self.zip_code))

    def input_address(self):
        self.building = input('Building: ')
        self.street_name = input('Street Name: ')
        self.landmark = input('Landmark: ')
        self.city = input('City: ')
        self.state = input('State: ')
        self.country = input('Country: ')
        self.zip_code = input('Zip Code: ')


class Customer(object):
    def __init__(self):
        self.first_name = ''
        self.last_name = ''
        self.address = ''
        self.phone_number = 0
        self.email = ''
        self.active_accounts = 0
        self.customer_id = ''

    def __str__(self):
        return str(
            'Customer ID: ' + self.customer_id + '\n' + 'Full Name: ' + self.first_name + ' ' + self.last_name + '\n' + str(
                self.address) + '\n' + str(
                self.phone_number) + '\n' + 'Email ID: ' + self.email + '\n' + 'Active accounts: ' + str(
                self.active_accounts))

    def input_customer(self):
        global global_customer_id
        self.first_name = input('First Name: ')
        self.last_name = input('Last Name: ')
        self.address = Address()
        self.address.input_address()
        self.phone_number = input('Phone Number: ')
        self.email = input('Email: ')
        global_customer_id += 1
        self.customer_id = ("%04d" % global_customer_id)
        global_customer_map[self.customer_id] = self
        print('Customer created successfully! Customer ID: ' + self.customer_id)


class Account(object):
    def __init__(self):
        self.account_number = ''
        self.balance = 0
        self.customer = Customer()
        self.max_transaction_amount = 0
        self.branch_code = 0

    def __str__(self):
        return str(
            'Account Number: ' + self.account_number + '\n' + 'Customer ID: ' + self.customer.customer_id + '\n' + 'Balance' + str(
                self.balance) + '\n' + 'Maximum Transaction Amount' + str(
                self.max_transaction_amount) + '\n' + 'Branch Code' + str(self.branch_code))

    def input_account(self):
        while True:
            ch = input('Existing customer? (Y/N): ')
            if ch.upper() == 'Y':
                existing_customer_id = input('Existing Customer ID: ')
                if existing_customer_id in global_customer_map:
                    self.customer = global_customer_map[existing_customer_id]
                    self.customer.active_accounts += 1
                    break
                else:
                    print('Customer ID does not exist. Recheck ID or register as a new customer.')
            else:
                self.customer = Customer()
                self.customer.input_customer()
                break
        self.max_transaction_amount = input('Maximum Transaction Amount: ')
        self.balance = input('Initial Balance: ')
        branch_code = input('Branch Code: ')
        self.account_number = str(
            self.customer.customer_id + branch_code + str("%02d" % self.customer.active_accounts))
        print('Account created successfully! Account ID: ' + self.account_number)

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

# TODO: Pause program execution at appropriate points. Almost done ig.
# TODO: Possibly add file IO to save current state
# TODO: Possibly add user-side to the bank
# TODO: Add to the already existing shit-loads of documentation
# Imported modules:
import os  # os - for providing PAUSE functionality
import platform  # platform - for determining the execution platform
from datetime import datetime  # datetime - for getting current system date and time,
from time import sleep  # sleep - pausing execution for a few seconds

#  Global variables:
global_customer_id = 0  # holds currently issued account number
global_customer_map = {}  # maps customer_id to customer
global_transactions = []  # global transaction log


def get_current_date():
    """
        Returns:
        string: current system date from the datetime module in DD/MM/YYYY format
    """
    return datetime.today().strftime('%d/%m/%Y')


def get_current_time():
    """
        Returns:
        string: current system time from the datetime module in HH:MM:SS format
    """
    return datetime.now().strftime("%H:%M:%S")


def get_customer_id(account_number):
    """
        Returns:
        string: customer_id of the account, substring[0:4]
    """
    return account_number[0:4]


def pause():
    """
    Function to pause program execution. Gives user time to interpret the output
    """
    if platform.system() == 'Linux':
        # For UNIX based systems
        lol = ''
        print('\nEnter any character to continue: ', end='')
        while lol == '':
            lol = input()
    elif platform.system() == 'Windows':
        # For Windows systems
        os.system('PAUSE')


class Transaction(object):
    """
    Transaction class: Maintains a structure for all transactions going into log
    Parameters:
        date: date of transaction, retrieved from get_current_date()
        time: time of transaction, retrieved from get_current_time()
        customer_id: customer_id of the customer involved
        account_number: account_number of involved account
        branch: branch associated to transaction, retrieved from Account.get_branch_code()
        amount: net amount involved
        opening_balance: initial balance
        closing_balance: final_balance
        remarks: notes for opening/closing of customers/accounts
    """

    def __init__(self, customer_id, account_number, date, time, branch, amount, opening_balance, closing_balance,
                 remarks):
        """
        Initialisation function for Transaction class
        """
        self.date = date
        self.time = time
        self.customer_id = customer_id
        self.account_number = account_number
        self.branch = branch
        self.amount = amount
        self.opening_balance = opening_balance
        self.closing_balance = closing_balance
        self.remarks = remarks

    def __str__(self):
        """
        Returns:
        string: printable string for an object of Customer class
        """
        return str(self.customer_id) + ' | ' + str(
            self.account_number) + ' | ' + self.date + ' | ' + self.time + ' | ' + str(self.branch) + ' | ' + str(
            self.amount) + ' | ' + str(self.opening_balance) + ' | ' + str(self.closing_balance) + ' | ' + self.remarks


class Address(object):
    """
    Address class: Maintains a structure for all addresses
    Parameters:
        building: Address line 1
        street_name: Address line 2
        landmark: Address line 3
        city: city of the address
        state: state of the address
        country: country of the address
        zip_code: postal code of the address
    """

    def __init__(self):
        """
        Initialisation function for Address class
        """
        self.zip_code = 0
        self.street_name = ''
        self.city = ''
        self.state = ''
        self.country = ''
        self.landmark = ''
        self.building = ''

    def __str__(self):
        """
        Returns:
        string: printable string for an object of Address class
        """
        return str(
            'Building: ' + self.building + '\n' + 'Street: ' + self.street_name + '\n' + 'Landmark: ' + self.landmark +
            '\n' + 'City: ' + self.city + '\n' + 'State: ' + self.state + '\n' + 'Country: ' + self.country + '\n' +
            'Zip Code: ' + str(self.zip_code))

    # TODO: Add validation rules for inputted values
    def input_address(self):
        """
        Input function to take values from the user and assign it to an object of Address class
        """
        self.building = input('Building: ')
        self.street_name = input('Street Name: ')
        self.landmark = input('Landmark: ')
        self.city = input('City: ')
        self.state = input('State: ')
        self.country = input('Country: ')
        self.zip_code = input('Zip Code: ')


class Customer(object):
    """
    Customer class: Maintains a structure for all customers
    Parameters:
        first_name: first name of customer
        last_name: last name of customer
        address: object of the Address class
        phone_number: phone number of the customer
        email: email of the customer
        active_accounts_number: number of currently active accounts assigned to the customer
        customer_id: automatically incremented number, taken from global_customer_id
        active_accounts: dictionary mapping account_ids to objects from the Account class
    """

    def __init__(self):
        """
        Initialisation function for Customer class
        """
        self.first_name = ''
        self.last_name = ''
        self.address = ''
        self.phone_number = 0
        self.email = ''
        self.active_accounts_number = 0
        self.customer_id = ''
        self.active_accounts = {}

    def __str__(self):
        """
        Returns:
        string: printable string for an object of Customer class
        """
        active_accounts = ''
        for i in self.active_accounts:
            active_accounts += ('\n' + '\t' + self.active_accounts[i].account_number)
        return str(
            'Customer ID: ' + self.customer_id + '\n' + 'Full Name: ' + self.first_name + ' ' + self.last_name + '\n' + str(
                self.address) + '\n' + str(
                self.phone_number) + '\n' + 'Email ID: ' + self.email + '\n' + 'Active accounts: ' + str(
                self.active_accounts_number) + '\n' + active_accounts)

    # TODO: Add validation rules for inputted values
    def input_customer(self):
        """
        Input function to take values from the user and assign it to an object of Customer class
        """
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
        # Add creation of customer to transactions log
        global_transactions.append(
            Transaction(self.customer_id, None, get_current_date(), get_current_time(), None, None, None, None,
                        'Customer created successfully!'))

    def delete_customer(self):
        """
        Delete function to delete an object of Customer class
        """
        # Add deletion of customer to transactions log
        global_transactions.append(
            Transaction(self.customer_id, None, get_current_date(), get_current_time(), None, None, None, None,
                        'Customer deleted successfully!'))
        # Delete individual accounts
        for i in self.active_accounts:
            self.active_accounts[i].delete_account()
        global_customer_map.pop(self.customer_id)
        print('Sorry to see you go!')


class Account(object):
    def __init__(self):
        """
        Initialisation function for Account class
        """
        self.account_number = ''
        self.balance = 0
        self.customer = Customer()
        self.max_transaction_amount = 0
        self.branch_code = 0

    def __str__(self):
        """
        Returns:
        string: printable string for an object of Account class
        """
        return str(
            'Account Number: ' + self.account_number + '\n' + 'Customer ID: ' + self.customer.customer_id + '\n' + 'Balance' + str(
                self.balance) + '\n' + 'Maximum Transaction Amount' + str(
                self.max_transaction_amount) + '\n' + 'Branch Code' + str(self.branch_code))

    # TODO: Add validation rules for inputted values
    def input_account(self):
        """
        Input function to take values from the user and assign it to an object of Account class
        """
        while True:
            ch = input('Existing customer? (Y/N): ')
            # For existing customers, adds a new account to the customer.active_accounts dictionary
            if ch.upper() == 'Y':
                existing_customer_id = input('Existing Customer ID: ')
                if existing_customer_id in global_customer_map:
                    print('Customer found. Adding account to customer ID #' + existing_customer_id)
                    self.customer = global_customer_map[existing_customer_id]
                    self.customer.active_accounts_number += 1
                    break
                else:
                    print('Customer ID does not exist. Recheck ID or register as a new customer.')
            elif ch.upper() == 'N':
                # For new customers, creates a new customer then adds a new account to the customer.active_accounts dictionary
                self.customer = Customer()
                self.customer.input_customer()
                break
        self.max_transaction_amount = input('Maximum Transaction Amount: ')
        self.balance = input('Initial Balance: ')
        branch_code = input('Branch Code: ')
        self.account_number = str(
            self.customer.customer_id + branch_code + str("%02d" % self.customer.active_accounts_number))
        self.customer.active_accounts[self.account_number] = self
        print('Account created successfully! Account ID: ' + self.account_number)
        # Add creation of account to transactions log
        global_transactions.append(
            Transaction(self.customer.customer_id, self.account_number, get_current_date(), get_current_time(),
                        self.get_branch_code(), None, self.balance, self.balance, 'Account created successfully!'))

    def delete_account(self):
        """
        Delete function to delete an object of Account class
        """
        # Add deletion of account to transactions log
        global_transactions.append(
            Transaction(self.customer.customer_id, self.account_number, get_current_date(), get_current_time(),
                        self.get_branch_code(), None, self.balance, 0, 'Account deleted successfully!'))
        self.customer.active_accounts_number -= 1
        self.customer.active_accounts.pop(self.account_number)
        print('Account ' + str(self.account_number) + ' deleted successfully! Closing Balance: ' + str(self.balance))

    def deposit(self, amount):
        """
        Deposit function to deposit money into account
        """
        if amount <= 0:
            # Validation rule: Amount is negative
            print('Invalid amount. Please enter positive values.\nTransaction aborted!')
        elif amount > self.max_transaction_amount:
            # Validation rule: Amount is more than maximum set by the customer
            print('Amount entered is more than the maximum.\nTransaction aborted!')
        else:
            self.balance += amount
            # Add deposit transaction to transactions log
            global_transactions.append(
                Transaction(self.customer.customer_id, self.account_number, get_current_date(), get_current_time(),
                            self.get_branch_code(), amount, self.balance - amount, self.balance,
                            str(amount) + ' deposited successfully!'))

    def withdraw(self, amount):
        """
        Withdraw function to withdraw money from account
        """
        if amount <= 0:
            # Validation rule: Amount is negative
            print('Invalid amount. Please enter positive values.\nTransaction aborted!')
        elif amount > self.max_transaction_amount:
            # Validation rule: Amount is more than maximum set by the customer
            print('Amount entered is more than the maximum.\nTransaction aborted!')
        elif amount > self.balance:
            # Validation rule: Amount is more than current balance
            print('Amount entered is more than balance.\nTransaction aborted!')
        else:
            self.balance -= amount
            # Add withdrawal transaction to transactions log
            global_transactions.append(
                Transaction(self.customer.customer_id, self.account_number, get_current_date(), get_current_time(),
                            self.get_branch_code(), amount, self.balance + amount, self.balance,
                            str(amount) + ' withdrawn successfully!'))

    def get_branch_code(self):
        """
        Returns:
        string: branch_code of the account, substring[4:8]
        """
        return self.account_number[4:8]


def intro():
    """
    A very short function. Isn't it?
    """
    # TODO: Add options to view customer/account details
    # TODO: Add option to modify customer/account details
    main_menu_list = ['1. Create Customer', '2. Delete Customer', '3. Open Account', '4. Close Account',
                      '5. Transact',
                      '6. Generate Report',
                      '7. About Us', '8. Exit']
    transact_menu_list = ['1. Deposit', '2.Withdraw', '3. Account to Account transfer']

    # TODO: Refine log by date (bisect module)
    report_menu_list = ['1. View all transactions', '2. View transactions by Branch',
                        '3. View transactions by Customer', '4. View transactions by Account',
                        '5. Generate Customer Report', '6. Generate Account Report']
    while True:
        print()
        print(27 * '=')
        print(1 * '\t' + 'Welcome to Bank XXX')
        print(27 * '=')
        print('\nLogin time: ' + get_current_time() + '\n')
        for i in main_menu_list:
            print('\t' + i)
        print()
        inp = input('Command: ')
        print()
        if inp == '8':
            print('Goodbye!\nLogout time: ', get_current_time())
            break
        elif inp == '7':
            about()
            pause()
        elif inp == '1':
            c = Customer()
            c.input_customer()
            pause()
        elif inp == '2':
            customer_id = input('Customer ID: ')
            if customer_id in global_customer_map:
                global_customer_map[customer_id].delete_customer()
            else:
                print('Customer does not exist!')
            pause()
        elif inp == '3':
            a = Account()
            a.input_account()
            pause()
        elif inp == '4':
            customer_id = input('Customer ID: ')
            if customer_id in global_customer_map:
                account_id = input('Account ID: ')
                if account_id in global_customer_map[customer_id].active_accounts:
                    global_customer_map[customer_id].active_accounts[account_id].delete_account()
                else:
                    print('Account does not exist!')
            else:
                print('Customer does not exist!')
            pause()
        elif inp == '5':
            for i in transact_menu_list:
                print('\t\t' + i)
            print()
            ch = input('Command: ')
            if ch == '1':
                bal = input('Amount to Deposit: ')
                customer_id = input('Customer ID: ')
                if customer_id in global_customer_map:
                    account_id = input('Account ID: ')
                    if account_id in global_customer_map[customer_id].active_accounts:
                        global_customer_map[customer_id].active_accounts[account_id].deposit(bal)
                    else:
                        print('Account does not exist!')
                else:
                    print('Customer does not exist!')
            elif ch == '2':
                bal = input('Amount to Withdraw: ')
                customer_id = input('Customer ID: ')
                if customer_id in global_customer_map:
                    account_id = input('Account ID: ')
                    if account_id in global_customer_map[customer_id].active_accounts:
                        global_customer_map[customer_id].active_accounts[account_id].withdraw(bal)
                    else:
                        print('Account does not exist!')
                else:
                    print('Customer does not exist!')
            else:
                account_id1 = input('Account to Withdraw from: ')
                customer_id1 = get_customer_id(account_id1)
                account_id2 = input('Account to Deposit to: ')
                customer_id2 = get_customer_id(account_id2)
                if account_id1 not in global_customer_map[customer_id1].active_accounts or account_id2 not in \
                        global_customer_map[customer_id2].active_accounts:
                    print('Account(s) not found!')
                else:
                    transfer_amount = input('Amount to transfer: ')
                    global_customer_map[customer_id1].active_accounts[account_id1].withdraw(transfer_amount)
                    global_customer_map[customer_id2].active_accounts[account_id2].deposit(transfer_amount)
            pause()
        elif inp == '6':
            # TODO: Give heading to outputted values
            for i in report_menu_list:
                print('\t\t' + i)
            print()
            ch = input('Command: ')
            if ch == '1':
                if len(global_transactions) > 0:
                    for i in global_transactions:
                        print(i)
                else:
                    print('No transactions found!')
            elif ch == '2':
                branch_code = input('Branch code: ')
                ls = list(filter(lambda x: x.branch == branch_code, global_transactions))
                if len(ls) == 0:
                    print('No transactions found!')
                else:
                    for i in ls:
                        print(i)
            elif ch == '3':
                customer_id = input('Customer ID: ')
                ls = list(filter(lambda x: x.customer_id == customer_id, global_transactions))
                if len(ls) == 0:
                    print('No transactions found!')
                else:
                    for i in ls:
                        print(i)
            elif ch == '4':
                account_number = input('Account Number: ')
                ls = list(filter(lambda x: x.account_number == account_number, global_transactions))
                if len(ls) == 0:
                    print('No transactions found!')
                else:
                    for i in ls:
                        print(i)
            elif ch == '5':
                customer_id = input('Customer ID: ')
                if customer_id in global_customer_map:
                    print(global_customer_map[customer_id])
                else:
                    print('Customer does not exist!')
            elif ch == '6':
                customer_id = input('Customer ID: ')
                if customer_id in global_customer_map:
                    account_number = input('Account Number: ')
                    if account_number in global_customer_map[customer_id].active_accounts:
                        print(global_customer_map[customer_id].active_accounts[account_number])
                    else:
                        print('Account does not exist!')
                else:
                    print('Customer does not exist!')
            else:
                print("Invalid entry!")
            pause()
        else:
            print("Invalid entry!")
            pause()


def about():
    """
    Prints the team info with a not-so-typewriter-ish effect
    """
    about_str = 'Team XXX *dab*\n\tMembers:\n\t\t1. Arnav Varshney\n\t\t2. Pradyumn Mishra\n\t\t3. Aditi Prasad\n\t\t4. Mihir Ghonge\n\t\t5. Shishir Balasubramanian\n\n'
    for char in about_str:
        sleep(0.1)
        print(char, end='', flush=True)


# How do I document this? xD
if __name__ == "__main__":
    intro()

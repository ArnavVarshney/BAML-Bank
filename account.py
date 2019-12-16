from address import Address
from customer import Customer
from transaction import Transaction
from utility import get_current_date, get_current_time, global_customer_map, global_transactions


class Account(object):
    """
    Maintains a structure for all accounts
    :param str account_number: account_number of account
    :param int balance: starting balance of account
    :param Customer customer: associated customer
    :param int max_transaction_amount: maximum transaction amount allowed
    :param str branch_code: branch associated with account
    """

    def __init__(self, account_number, balance, customer, max_transaction_amount, branch_code):
        """
        Initialisation function for Account class
        """
        self.account_number = account_number
        self.balance = balance
        self.customer = customer
        self.max_transaction_amount = max_transaction_amount
        self.branch_code = branch_code

    def __str__(self):
        """
        :return printable string for an object of Account class
        :rtype str
        """
        return str(
            f'Account Number: {self.account_number}\nCustomer ID: {self.customer.customer_id}\nBalance'
            f'{str(self.balance)}\nMaximum Transaction Amount{str(self.max_transaction_amount)}\nBranch Code'
            f'{self.branch_code}')

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
                    print(f'Customer found. Adding account to customer ID #{existing_customer_id}')
                    self.customer = global_customer_map[existing_customer_id]
                    self.customer.active_accounts_number += 1
                    break
                else:
                    print('Customer ID does not exist. Recheck ID or register as a new customer.')
            elif ch.upper() == 'N':
                # For new customers, creates a new customer then adds a new account to the customer.active_accounts
                # dictionary
                self.customer = Customer('', '', Address('', '', '', '', '', '', '', ''), '', '', 0, '', {})
                self.customer.input_customer()
                self.customer.active_accounts_number += 1
                break
        while True:
            try:
                self.max_transaction_amount = int(input('Maximum Transaction Amount: '))
                break
            except ValueError:
                print('\nInvalid Value\n')
        while True:
            try:
                self.balance = int(input('Initial Balance: '))
                break
            except ValueError:
                print('\nInvalid Value\n')
        branch_code = input('Branch Code: ')
        self.account_number = str(
            self.customer.customer_id + branch_code + str("%02d" % self.customer.active_accounts_number))
        self.customer.active_accounts[self.account_number] = self
        print(f'Account created successfully! Account ID: {self.account_number}')
        # Add creation of account to transactions log
        global_transactions.append(
            Transaction(self.customer.customer_id, self.account_number, get_current_date(), get_current_time(),
                        self.get_branch_code(), 'NA', 0, self.balance,
                        f'Account {self.account_number} created successfully!'))

    def delete_account(self, pop_from_list):
        """
        Delete function to delete an object of Account class
        """
        # Add deletion of account to transactions log
        global_transactions.append(
            Transaction(self.customer.customer_id, self.account_number, get_current_date(), get_current_time(),
                        self.get_branch_code(), 'NA', self.balance, 0,
                        f'Account {self.account_number} deleted successfully!'))
        self.customer.active_accounts_number -= 1
        if pop_from_list:
            self.customer.active_accounts.pop(self.account_number)
        print(f'Account {str(self.account_number)} deleted successfully! Closing Balance: {str(self.balance)}')

    def modify_account(self):
        """
        Modify function to modify an object of Account class
        """
        modify_account_list = ['1. Modify Maximum Transaction Amount']
        for i in modify_account_list:
            print('\t' + i)
        print()
        ch = input('Command: ')
        if ch == '1':
            while True:
                try:
                    self.max_transaction_amount = int(input('New Maximum Transaction Amount: '))
                    break
                except ValueError:
                    print('\nInvalid Value\n')
            global_transactions.append(
                Transaction(self.customer.customer_id, self.account_number, get_current_date(), get_current_time(),
                            self.get_branch_code(), 0, self.balance, self.balance,
                            'Maximum Transaction Amount modified successfully!'))

    def deposit(self, amount):
        """
        Deposit function to deposit money into account
        """
        if int(amount) <= 0:
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
                            self.get_branch_code(), amount, str(int(self.balance) - int(amount)), self.balance,
                            f'{str(amount)} deposited successfully!'))

    def withdraw(self, amount):
        """
        Withdraw function to withdraw money from account
        """
        if int(amount) <= 0:
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
                            self.get_branch_code(), amount, str(int(self.balance) + int(amount)), str(self.balance),
                            f'{str(amount)} withdrawn successfully!'))

    def get_branch_code(self):
        """
        :return branch_code of the account, substring[4:8]
        :rtype str
        """
        return self.account_number[4:8]

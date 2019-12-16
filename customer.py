import utility
from transaction import Transaction
from utility import get_current_date, get_current_time, global_customer_map, global_transactions


class Customer(object):
    """
    Maintains a structure for all customers
    :param str first_name: first name of customer
    :param str last_name: last name of customer
    :param Address address: object of the Address class
    :param str phone_number: phone number of the customer
    :param str email: email of the customer
    :param int active_accounts_number: number of currently active accounts assigned to the customer
    :param str customer_id: automatically incremented number, taken from global_customer_id
    :param dict active_accounts: dictionary mapping account_ids to objects from the Account class
    """

    def __init__(self, first_name, last_name, address, phone_number, email, active_accounts_number, customer_id,
                 active_accounts):
        """
        Initialisation function for Customer class
        """
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.active_accounts_number = active_accounts_number
        self.customer_id = customer_id
        self.active_accounts = active_accounts

    def __str__(self):
        """
        :return string for an object of Customer class
        :rtype str
        """
        active_accounts = ''
        for i in self.active_accounts:
            active_accounts += ('\n' + '\t' + self.active_accounts[i].account_number)
        return str(
            f'Customer ID: {self.customer_id}\nFull Name: {self.first_name} {self.last_name}\n{str(self.address)}\n'
            f'{str(self.phone_number)}\nEmail ID: {self.email}\nActive accounts: {str(self.active_accounts_number)}\n'
            f'{active_accounts}')

    def input_customer(self):
        """
        Input function to take values from the user and assign it to an object of Customer class
        """
        self.first_name = input('First Name: ')
        self.last_name = input('Last Name: ')
        self.address.input_address()
        while True:
            self.phone_number = input('Phone Number: ')
            if self.phone_number.isnumeric() and len(self.phone_number) == 10:
                break
            else:
                print('\nInvalid Phone Number\n')
        while True:
            self.email = input('Email: ')
            if self.email.__contains__('@'):
                break
            else:
                print('\nInvalid Email ID\n')
        self.customer_id = utility.global_customer_id
        utility.global_customer_id = str(int(utility.global_customer_id) + 1)
        utility.global_customer_id = '0' * (4 - len(utility.global_customer_id)) + utility.global_customer_id
        global_customer_map[self.customer_id] = self
        # Add creation of customer to transactions log
        global_transactions.append(
            Transaction(self.customer_id, 'NA', get_current_date(), get_current_time(), 'NA', 'NA', 'NA', 'NA',
                        f'Customer {self.customer_id} created successfully!'))
        print(f'Customer created successfully! Customer ID: {self.customer_id}')

    def delete_customer(self):
        """
        Delete function to delete an object of Customer class
        """
        # Add deletion of customer to transactions log
        global_transactions.append(
            Transaction(self.customer_id, 'NA', get_current_date(), get_current_time(), 'NA', 'NA', 'NA', 'NA',
                        f'Customer {self.customer_id} deleted successfully!'))
        # Delete individual accounts
        for i in self.active_accounts:
            self.active_accounts[i].delete_account(False)
        self.active_accounts.clear()
        print('Customer deleted successfully!')
        return True

    def modify_customer(self):
        """
        Modify function to modify an object of Customer class
        """
        modify_customer_list = ['1. First Name', '2. Last Name', '3. Address', '4. Phone Number', '5. Email']
        print('\n\tWhich parameter do you want to modify?')
        for i in modify_customer_list:
            print('\t' + i)
        print()
        ch = input('Command: ')
        if ch == '1':
            self.first_name = input('New First Name: ')
            global_transactions.append(
                Transaction(self.customer_id, 'NA', get_current_date(), get_current_time(), 'NA', 'NA', 'NA', 'NA',
                            'First name modified successfully!'))
        elif ch == '2':
            self.last_name = input('New Last Name: ')
            global_transactions.append(
                Transaction(self.customer_id, 'NA', get_current_date(), get_current_time(), 'NA', 'NA', 'NA', 'NA',
                            'Last name modified successfully!'))
        elif ch == '3':
            self.address.modify_address()
            global_transactions.append(
                Transaction(self.customer_id, 'NA', get_current_date(), get_current_time(), 'NA', 'NA', 'NA', 'NA',
                            'Address modified successfully!'))
        elif ch == '4':
            while True:
                self.phone_number = input('New Phone Number: ')
                if self.phone_number.isnumeric() and len(self.phone_number) == 10:
                    break
                else:
                    print('\nInvalid Phone Number\n')
            global_transactions.append(
                Transaction(self.customer_id, 'NA', get_current_date(), get_current_time(), 'NA', 'NA', 'NA', 'NA',
                            'Phone number modified successfully!'))
        elif ch == '5':
            while True:
                self.email = input('Email: ')
                if self.email.__contains__('@'):
                    break
                else:
                    print('\nInvalid Email ID\n')
            global_transactions.append(
                Transaction(self.customer_id, 'NA', get_current_date(), get_current_time(), 'NA', 'NA', 'NA', 'NA',
                            'Email modified successfully!'))

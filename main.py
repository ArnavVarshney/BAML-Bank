# TODO: Fix view branch output
# TODO: Fix report menu output

# Menu functions


def create_customer():
    """
    Menu entry 1: Create Customer
    """
    c = Customer('', '', Address('', '', '', '', '', '', '', ''), '', '', 0, '', {})
    c.input_customer()


def modify_customer():
    """
    Menu entry 2: Modify Customer
    """
    customer_id = input('Customer ID: ')
    if customer_id in global_customer_map:
        global_customer_map[customer_id].modify_customer()
    else:
        print('Customer does not exist!')


def delete_customer():
    """
    Menu entry 3: Delete Customer
    """
    customer_id = input('Customer ID: ')
    if customer_id in global_customer_map:
        global_customer_map[customer_id].delete_customer()
    else:
        print('Customer does not exist!')


def open_account():
    """
    Menu entry 4: Open Account
    """
    a = Account('', 0,
                Customer('', '', Address('', '', '', '', '', '', '', ''), '', '', 0, '', {}),
                0, '')
    a.input_account()


def modify_account():
    """
    Menu entry 5: Modify Account
    """
    customer_id = input('Customer ID: ')
    if customer_id in global_customer_map:
        account_id = input('Account ID: ')
        if account_id in global_customer_map[customer_id].active_accounts:
            global_customer_map[customer_id].active_accounts[account_id].modify_account()
        else:
            print('Account does not exist!')
    else:
        print('Customer does not exist!')


def close_account():
    """
    Menu entry 6: Close Account
    """
    customer_id = input('Customer ID: ')
    if customer_id in global_customer_map:
        account_id = input('Account ID: ')
        if account_id in global_customer_map[customer_id].active_accounts:
            global_customer_map[customer_id].active_accounts[account_id].delete_account()
        else:
            print('Account does not exist!')
    else:
        print('Customer does not exist!')


def transact():
    """
    Menu entry 7: Transact
    """
    transact_menu_list = ['1. Deposit', '2. Withdraw', '3. Account to Account transfer']
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


def print_report(ls):
    """
    Utility function for generate_report
    :param ls: list containing items to be printed
    """
    report_headings = ['Customer ID', 'Account', 'Date', 'Time', 'Branch', 'Amount', 'Opening Balance',
                       'Closing  Balance', 'Remarks']
    print(168 * '-')
    print('| {:^13s} | {:^12} | {:^12} | {:^10} | {:^8} | {:^10s} | {:^17s} | {:^18s} | {:^40s} |'.format(
        report_headings[0],
        report_headings[1],
        report_headings[2],
        report_headings[3],
        report_headings[4],
        report_headings[5],
        report_headings[6],
        report_headings[7],
        report_headings[8]))
    print(168 * '-')
    if len(ls) == 0:
        print('No transactions found!')
    else:
        for i in ls:
            print(i)
            print(168 * '-')


def generate_report():
    """
    Menu entry 8: Generate Report
    """
    report_menu_list = ['1. View all transactions', '2. View transactions by Branch',
                        '3. View transactions by Customer', '4. View transactions by Account',
                        '5. Generate Customer Report', '6. Generate Account Report']
    for i in report_menu_list:
        print('\t\t' + i)
    print()
    ch = input('Command: ')
    if ch == '1':
        print_report(global_transactions)
    elif ch == '2':
        branch_code = input('Branch code: ')
        lower_bound = input('Date From (DD/MM/YYYY): ')
        upper_bound = input('Date To (DD/MM/YYYY): ')
        d1 = datetime.strptime(lower_bound, '%d/%m/%y')
        d2 = datetime.strptime(upper_bound, '%d/%m/%y')
        ls = list(filter(lambda x: x.branch == branch_code and (d1 <= datetime.strptime(x.date, '%d/%m/%y') <= d2),
                         global_transactions))
        print_report(ls)
    elif ch == '3':
        customer_id = input('Customer ID: ')
        lower_bound = input('Date From (DD/MM/YYYY): ')
        upper_bound = input('Date To (DD/MM/YYYY): ')
        d1 = datetime.strptime(lower_bound, '%d/%m/%y')
        d2 = datetime.strptime(upper_bound, '%d/%m/%y')
        ls = list(filter(lambda x: x.customer_id == customer_id and (d1 <= datetime.strptime(x.date, '%d/%m/%y') <= d2),
                         global_transactions))
        print_report(ls)
    elif ch == '4':
        account_number = input('Account Number: ')
        lower_bound = input('Date From (DD/MM/YYYY): ')
        upper_bound = input('Date To (DD/MM/YYYY): ')
        d1 = datetime.strptime(lower_bound, '%d/%m/%y')
        d2 = datetime.strptime(upper_bound, '%d/%m/%y')
        ls = list(
            filter(lambda x: x.account_number == account_number and (d1 <= datetime.strptime(x.date, '%d/%m/%y') <= d2),
                   global_transactions))
        print_report(ls)
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


def create_branch():
    branch_name = input('Branch Name: ')
    branch_code = input('Branch Code: ')
    address = Address('', '', '', '', '', '', '', '')
    address.input_address()
    b = Branch(branch_code, branch_name, address)
    global_branches[b.branch_code] = b
    print('Branch created successfully!')


def view_branches():
    for i in global_branches:
        print(global_branches[i])


def about():
    """
    Menu entry 11: About Us
    Prints the team info with a not-so-typewriter-ish effect
    """
    about_str = 'Team XXX *dab*\n\tMembers:\n\t\t1. Arnav Varshney\n\t\t2. Pradyumn Mishra\n\t\t3. Aditi Prasad\n\t\t' \
                '4. Mihir Ghonge\n\t\t5. Shishir Balasubramanian\n\n'
    for char in about_str:
        sleep(0.1)
        print(char, end='', flush=True)


def print_name():
    """
    Beauty Mode: On
    """
    print('$$$$$$$\\                      $$\\             $$\\   $$\\ $$\\   $$\\ $$\\   $$\\ ')
    print('$$  __$$\\                     $$ |            $$ |  $$ |$$ |  $$ |$$ |  $$ |')
    print('$$ |  $$ | $$$$$$\\  $$$$$$$\\  $$ |  $$\\       \\$$\\ $$  |\\$$\\ $$  |\\$$\\ $$  |')
    print('$$$$$$$\\ | \\____$$\\ $$  __$$\\ $$ | $$  |       \\$$$$  /  \\$$$$  /  \\$$$$  /')
    print('$$  __$$\\  $$$$$$$ |$$ |  $$ |$$$$$$  /        $$  $$<   $$  $$<   $$  $$< ')
    print('$$ |  $$ |$$  __$$ |$$ |  $$ |$$  _$$<        $$  /\\$$\\ $$  /\\$$\\ $$  /$$\\')
    print('$$$$$$$  |\\$$$$$$$ |$$ |  $$ |$$ | \\$$\\       $$ /  $$ |$$ /  $$ |$$ /  $$ |')
    print('\\_______/  \\_______|\\__|  \\__|\\__|  \\__|      \\__|  \\__|\\__|  \\__|\\__|  \\__|')


def intro():
    """
    Prints the main menu and forwards to respective functions
    """
    main_menu_list = ['1. Create Customer', '2. Modify Customer', '3. Delete Customer', '4. Open Account',
                      '5. Modify Account', '6. Close Account', '7. Transact', '8. Generate Report', '9. Add Branch',
                      '10. View Branches', '11. About Us', '12. Exit']
    login_time = get_current_time()
    while True:
        clear_console()
        print_name()
        print()
        print('Login time: ' + login_time)
        print()
        print(27 * '=')
        print()
        for i in main_menu_list:
            print('\t' + i)
        print()
        inp = input('Command: ')
        print()
        if inp == '1':
            create_customer()
        elif inp == '2':
            modify_customer()
        elif inp == '3':
            delete_customer()
        elif inp == '4':
            open_account()
        elif inp == '5':
            modify_account()
        elif inp == '6':
            close_account()
        elif inp == '7':
            transact()
        elif inp == '8':
            generate_report()
        elif inp == '9':
            create_branch()
        elif inp == '10':
            view_branches()
        elif inp == '11':
            about()
        elif inp == '12':
            print('Goodbye!\nLogout time: ', get_current_time())
            break
        else:
            print("Invalid entry!")
        # Pause before printing the menu again
        pause()


# How do I document this? xD
if __name__ == "__main__":
    # Imported modules:
    from datetime import datetime  # datetime - for getting current system date and time
    from time import sleep  # sleep - pausing execution until interrupted by keyboard input (Windows)

    # Imported files:
    from account import Account
    from address import Address
    from branch import Branch
    from customer import Customer
    from utility import get_customer_id, get_current_time, pause, global_customer_map, global_transactions, \
        global_branches, clear_console

    intro()

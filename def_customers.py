import datetime
import getpass

from dateutil.relativedelta import *
from pyfiglet import Figlet

from database import retrieve_all_customers, retrieve_customer, get_id_customer, register_customer, delete_customer, \
    update_customer
from utility import pause, clear_console, print_name, validate_phone, generate_otp, validate_email, send_message


def view_all_customers():
    clear_console()
    print_name()
    print(Figlet('small').renderText('All Customers'))
    print(
        159 * '-' + '\n' + '| {:^13s} | {:^20s} | {:^20s} | {:^20s} | {:^20} | {:^14s} | {:^30s} |'.format(
            'Customer ID',
            'Username',
            'Password',
            'First Name',
            'Last Name',
            'Phone Number',
            'Email ID'))
    print(112 * '-')
    all_customers = retrieve_all_customers()
    if all_customers:
        for i in all_customers:
            print(
                '| {:^13s} | {:^20s} | {:^20s} | {:^20s} | {:^20} | {:^14s} | {:^30s} |'.format(
                    str(i[12]), i[13],
                    i[14], i[0],
                    i[1],
                    str(i[10]), i[11]))
        print(159 * '-')
    else:
        print('No registered customers found!')


def view_customer_info():
    clear_console()
    print_name()
    print(Figlet('small').renderText('Customer Info'))
    for counter in range(5):
        customer_user_name = input('Customer Username: ')
        cust = retrieve_customer(customer_user_name)
        if cust:
            print()
            print(f'Customer ID: {cust[12]}')
            print(f'Username: {cust[13]}')
            print(f'Password: {cust[14]}')
            print(f'Branch: {cust[15]}')
            print(f'Balance: {cust[16]}')
            print()
            print('Personal Info:')
            print(f'First Name: {cust[0]}')
            print(f'Last Name: {cust[1]}')
            print(f'Date of Birth: {cust[18]}')
            print(f'Gender: {cust[17]}')
            print(f'Phone Number: {cust[10]}')
            print(f'Email ID: {cust[11]}')
            print()
            print('Address Info:')
            print(f'{cust[2]}\n{cust[3]}\n{cust[4]}\n{cust[5]}\n{cust[6]}\n{cust[7]}\n{cust[8]}\n{cust[9]}')
            print()
            break
        else:
            print('Customer Not Found!')


def register_new_customer():
    clear_console()
    print_name()
    print(Figlet('small').renderText('Register Customer'))
    first_name = input('First Name: ')
    last_name = input('Last Name: ')
    for counter in range(5):
        date_of_birth = input('Date of Birth (DD/MM/YYYY): ')
        try:
            day, month, year = date_of_birth.split('/')
            d1 = datetime.datetime(int(year), int(month), int(day))
            d2 = datetime.datetime.today()
            if abs(relativedelta(d2, d1).years) >= 16:
                break
            else:
                print('\nMinimum age should be 16 years!\n')
        except ValueError:
            print('\nInvalid value!\n')
    for counter in range(5):
        gender = input('Gender (M/F): ')
        if gender in ['M', 'F']:
            break
        else:
            print('\nInvalid gender value!\n')
    building = input('Building: ')
    street_name = input('Street Name: ')
    locality = input('Locality: ')
    landmark = input('Landmark: ')
    city = input('City: ')
    state = input('State: ')
    country = input('Country: ')
    for counter in range(5):
        zip_code = input('Zip Code: ')
        if zip_code.isnumeric() and len(zip_code) == 6:
            break
        else:
            print('\nInvalid Zip Code\n')
    for counter in range(5):
        phone_number = input('Phone Number (+<Country Code><Phone Number>): ')
        if validate_phone(phone_number):
            otp = generate_otp(phone_number)
            flag = False
            while not flag:
                otp_input = input(f'OTP sent on {phone_number}: ')
                if str(otp_input) == str(otp):
                    flag = True
            if flag:
                break
        else:
            print('\nInvalid Phone Number. Phone Numbers should follow +<Country Code><Phone Number>\n')
    for counter in range(5):
        email = input('Email: ')
        if validate_email(email):
            break
        else:
            print('\nInvalid Email ID\n')
    for counter in range(5):
        user_name = input('Username: ')
        if retrieve_customer(user_name):
            print('\nUsername already in use!\n')
        else:
            break
    for counter in range(5):
        password = getpass.getpass()
        re_password = getpass.getpass(prompt='Re-enter Password: ')
        if len(password) == 0:
            print('\nInvalid password\n')
        elif password != re_password:
            print('\nPasswords don\'t match\n')
        else:
            break
    customer_id = str(get_id_customer(user_name)[12])
    send_message(
        f'Greetings from Bank SPAAM!\nWelcome {first_name} {last_name}!\nYour Customer ID '
        f'{customer_id}.', phone_number)
    register_customer(first_name, last_name, building, street_name, locality, landmark, city, state, country,
                      zip_code, phone_number, email, user_name, password, 1, date_of_birth, gender, 0)
    print('Customer registered successfully!\nCustomer ID: ' + customer_id)


def modify_customer():
    clear_console()
    print_name()
    print(Figlet('small').renderText('Modify Customer'))
    print('Choose an option: \n')
    modify_customer_list = ['1. Delete Customer', '2. Edit Customer', '#. Return to Previous Menu']
    for i in modify_customer_list:
        print('\t' + i)
    print()
    inp1 = input('Command: ')
    if inp1 == '1':
        for counter in range(5):
            clear_console()
            print_name()
            print(Figlet('small').renderText('Delete Customer'))
            customer_user_name = input('Customer Username: ')
            if retrieve_customer(customer_user_name):
                ch = input('Confirm? (Y/N): ')
                if ch == 'Y':
                    delete_customer(customer_user_name)
                break
            else:
                print('Customer Not Found!')
                pause()
    elif inp1 == '2':
        for counter in range(5):
            clear_console()
            print_name()
            print(Figlet('small').renderText('Edit Customer'))
            customer_user_name = input('Customer Username: ')
            cust = retrieve_customer(customer_user_name)
            if cust:
                phone_number = cust[10]
                customer_id = cust[12]
                modify_customer_list = ['1. First Name', '2. Last Name', '3. Address', '4. Phone Number',
                                        '5. Email', '#. Return to Previous Menu']
                print('\nWhich parameter do you want to modify?')
                print('Choose an option: \n')
                for i in modify_customer_list:
                    print('\t' + i)
                print()
                ch = input('Command: ')
                if ch == '1':
                    clear_console()
                    print_name()
                    print(Figlet('small').renderText('Edit Customer'))
                    first_name = input('New First Name: ')
                    update_customer('first_name', first_name, customer_user_name)
                    send_message(
                        f'Greetings from Bank SPAAM!\nYour Customer ID {customer_id}.\nYour account has been modified '
                        f'successfully.', phone_number)
                    break
                elif ch == '2':
                    clear_console()
                    print_name()
                    print(Figlet('small').renderText('Edit Customer'))
                    last_name = input('New Last Name: ')
                    update_customer('last_name', last_name, customer_user_name)
                    send_message(
                        f'Greetings from Bank SPAAM!\nYour Customer ID {customer_id}.\nYour account has been modified '
                        f'successfully.', phone_number)
                    break
                elif ch == '3':
                    clear_console()
                    print_name()
                    print(Figlet('small').renderText('Edit Customer'))
                    building = input('Building: ')
                    update_customer('building', building, customer_user_name)
                    street_name = input('Street Name: ')
                    update_customer('street_name', street_name, customer_user_name)
                    locality = input('Locality: ')
                    update_customer('locality', locality, customer_user_name)
                    landmark = input('Landmark: ')
                    update_customer('landmark', landmark, customer_user_name)
                    city = input('City: ')
                    update_customer('city', city, customer_user_name)
                    state = input('State: ')
                    update_customer('state', state, customer_user_name)
                    country = input('Country: ')
                    update_customer('country', country, customer_user_name)
                    for counter in range(5):
                        zip_code = input('Zip Code: ')
                        if zip_code.isnumeric() and len(zip_code) == 6:
                            update_customer('zip_code', zip_code, customer_user_name)
                            break
                        else:
                            print('\nInvalid Zip Code\n')
                    send_message(
                        f'Greetings from Bank SPAAM!\nYour Customer ID {customer_id}.\nYour account has been modified '
                        f'successfully.', phone_number)
                    break
                elif ch == '4':
                    clear_console()
                    print_name()
                    print(Figlet('small').renderText('Edit Customer'))
                    for counter in range(5):
                        phone_number = input('New Phone Number (+<Country Code><Phone Number>): ')
                        if validate_phone(phone_number):
                            otp = generate_otp(phone_number)
                            flag = False
                            while not flag:
                                otp_input = input(f'OTP sent on {phone_number}: ')
                                if str(otp_input) == str(otp):
                                    flag = True
                            if flag:
                                update_customer('phone_number', phone_number, customer_user_name)
                                break
                        else:
                            print(
                                '\nInvalid Phone Number. Phone Numbers should follow +<Country Code><Phone Number>\n')
                    send_message(
                        f'Greetings from Bank SPAAM!\nYour Customer ID {customer_id}.\nYour account has been modified '
                        f'successfully.', phone_number)
                    break
                elif ch == '5':
                    clear_console()
                    print_name()
                    print(Figlet('small').renderText('Edit Customer'))
                    for counter in range(5):
                        email = input('Email: ')
                        if validate_email(email):
                            update_customer('email_id', email, customer_user_name)
                            break
                        else:
                            print('\nInvalid Email ID\n')
                    send_message(
                        f'Greetings from Bank SPAAM!\nYour Customer ID {customer_id}.\nYour account has been modified '
                        f'successfully.', phone_number)
                elif ch == '#':
                    break
                else:
                    print('Invalid entry!')
            else:
                print('Customer Not Found!')
                pause()


def customers():
    customers_list = ['1. View All Customers', '2. View Customer Info', '3. Register New Customer',
                      '4. Modify Customer', '#. Return to Previous Menu']
    for counter in range(5):
        clear_console()
        print_name()
        print(Figlet('small').renderText('Customers'))
        print('Choose an option: \n')
        for i in customers_list:
            print('\t' + i)
        print()
        inp = input('Command: ')
        if inp == '1':
            view_all_customers()
            break
        elif inp == '2':
            view_customer_info()
            break
        elif inp == '3':
            register_new_customer()
            break
        elif inp == '4':
            modify_customer()
            break
        elif inp == '#':
            break
        else:
            print('Invalid entry!')
            pause()


if __name__ == '__main__':
    print('Log in first\nAbort!')

import datetime

from dateutil.relativedelta import relativedelta
from pyfiglet import Figlet

from database import retrieve_all_employees, retrieve_employee, register_employee, delete_employee, make_admin
from utility import clear_console, print_name, pause, validate_email, validate_phone


def view_all_employees():
    print(
        140 * '-' + '\n' + '| {:^13s} | {:^10s} | {:^15s} | {:^6s} | {:^8s} | {:^20s} | {:^20s} | {:^12s} | {:^8s} |'.format(
            'Employee ID',
            'Username',
            'Password',
            'Role',
            'Branch',
            'First Name',
            'Last Name',
            'DOB',
            'Gender'))
    all_employees = retrieve_all_employees()
    if all_employees:
        for i in all_employees:
            print(
                140 * '-' + '\n' + '| {:^13s} | {:^10s} | {:^15s} | {:^6s} | {:^8s} | {:^20s} | {:^20s} | {:^12s} | {:^8s} |'.format(
                    str(i[0]), i[1],
                    i[2], str(i[5]), str(i[6]),
                    i[3], i[4], i[8], i[7]))
        print(140 * '-')
    else:
        print('No registered employees found!')


def view_employee_info():
    clear_console()
    print_name()
    print(Figlet('small').renderText('Employee Info'))
    while True:
        employee_user_name = input('Employee Username: ')
        emp = retrieve_employee(employee_user_name)
        if emp:
            print()
            print(f'Employee ID: {emp[0]}')
            print(f'Username: {emp[1]}')
            print(f'Password: {emp[2]}')
            print(f'Role: {emp[5]}')
            print(f'Branch: {emp[6]}')
            print()
            print('Personal Info:')
            print(f'First Name: {emp[3]}')
            print(f'Last Name: {emp[4]}')
            print(f'Date of Birth: {emp[8]}')
            print(f'Gender: {emp[7]}')
            print(f'Phone Number: {emp[17]}')
            print(f'Email ID: {emp[18]}')
            print()
            print('Address Info:')
            print(f'{emp[9]}\n{emp[10]}\n{emp[11]}\n{emp[12]}\n{emp[13]}\n{emp[14]}\n{emp[15]}\n{emp[16]}')
            print()
            break
        else:
            print('Employee Not Found!')


def register_new_employee():
    clear_console()
    print_name()
    print(Figlet('small').renderText('Register Employee'))
    while True:
        user_name = input('Username: ')
        if retrieve_employee(user_name):
            print('\nUsername already in use!\n')
        else:
            break
    first_name = input('First Name: ')
    last_name = input('Last Name: ')
    while True:
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
    while True:
        gender = input('Gender (M/F): ')
        if gender in ['M', 'F']:
            break
        else:
            print('\nInvalid gender value!\n')
    while True:
        password = input('Password: ')
        if len(password) == 0:
            print('\nInvalid password!\n')
        else:
            break
    building = input('Building: ')
    street_name = input('Street Name: ')
    locality = input('Locality: ')
    landmark = input('Landmark: ')
    city = input('City: ')
    state = input('State: ')
    country = input('Country: ')
    while True:
        zip_code = input('Zip Code: ')
        if zip_code.isnumeric() and len(zip_code) == 6:
            break
        else:
            print('\nInvalid Zip Code\n')
    while True:
        phone_number = input('Phone Number (+<Country Code><Phone Number>): ')
        if validate_phone(phone_number):
            break
        else:
            print('\nInvalid Phone Number. Phone Numbers should follow +<Country Code><Phone Number>\n')
    while True:
        email = input('Email: ')
        if validate_email(email):
            break
        else:
            print('\nInvalid Email ID\n')
    register_employee(user_name, first_name, last_name, password, 0, 1, date_of_birth,
                      gender, building, street_name, locality, landmark, city, state, country,
                      zip_code, phone_number, email)
    print('Employee registered successfully!\nEmployee Number: ' + str(retrieve_employee(user_name)[0]))


def modify_employee():
    clear_console()
    print_name()
    print(Figlet('small').renderText('Modify Employee'))
    print('Choose an option: \n')
    modify_employee_list = ['1. Delete Employee', '2. Promote Employee', '#. Return to Previous Menu']
    for i in modify_employee_list:
        print('\t' + i)
    print()
    inp1 = input('Command: ')
    if inp1 == '1':
        while True:
            employee_user_name = input('Employee Username: ')
            if retrieve_employee(employee_user_name):
                ch = input('Confirm? (Y/N): ')
                if ch == 'Y':
                    delete_employee(employee_user_name)
                break
            else:
                print('Employee Not Found!')
    elif inp1 == '2':
        while True:
            employee_user_name = input('Employee Username: ')
            if retrieve_employee(employee_user_name):
                ch = input('Confirm? (Y/N): ')
                if ch == 'Y':
                    make_admin(employee_user_name)
                break
            else:
                print('Employee Not Found!')


def employees():
    employees_list = ['1. View All Employees', '2. View Employee Info', '3. Register New Employee',
                      '4. Modify Employee',
                      '#. Return to Previous Menu']
    while True:
        clear_console()
        print_name()
        print(Figlet('small').renderText('Employees'))
        print('Choose an option: \n')
        for i in employees_list:
            print('\t' + i)
        print()
        inp = input('Command: ')
        if inp == '1':
            view_all_employees()
            break
        elif inp == '2':
            view_employee_info()
            break
        elif inp == '3':
            register_new_employee()
            break
        elif inp == '4':
            modify_employee()
            break
        elif inp == '#':
            break
        else:
            print('Invalid entry!')
            pause()

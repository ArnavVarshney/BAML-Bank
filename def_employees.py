def employees():
    employees_list = ['1. View All Employees', '2. Register New Employee', '3. Modify Employee',
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
            print(
                103 * '-' + '\n' + '| {:^13s} | {:^10s} | {:^15s} | {:^6s} | {:^8s} | {:^20s} | {:^20s} |'.format(
                    'Employee ID',
                    'Username',
                    'Password',
                    'Role',
                    'Branch',
                    'First Name',
                    'Last Name'))
            all_employees = retrieve_all_employees()
            if all_employees:
                for i in all_employees:
                    print(
                        103 * '-' + '\n' + '| {:^13s} | {:^10s} | {:^15s} | {:^6s} | {:^8s} | {:^20s} | {:^20s} |'.format(
                            str(i[0]), i[1],
                            i[2], str(i[5]), str(i[6]),
                            i[3], i[4]))
                print(103 * '-')
            else:
                print('No registered employees found!')
            break
        elif inp == '2':
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
                day,month,year = date_of_birth.split('/')
                try:
                    datetime.datetime(int(year), int(month), int(day))
                    break
                except ValueError:
                    print('\nInvalid value!\n
            while not isValidGender:
                gender = input('Gender (M/F): ')
                if gender in ['M','F']:
                    break
                else:
                    print('\nInvalid gender value!\n')
            while True:
                password = input('Password: ')
                if len(password) == 0:
                    print('\nInvalid password!\n')
                else:
                    break
            while True:
                role = input('Role [1. Employee, 2. Customer]: ')
                if role not in ['0', '1', '2']:
                    print('\nInvalid role!\n')
                else:
                    break
            register_employee(user_name, first_name, last_name, password, role)
            print('Employee registered successfully!\nEmployee Number: ' + str(retrieve_employee(user_name)[0]))
            break
        elif inp == '3':
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

        elif inp == '#':
            break
        else:
            print('Invalid entry!')
            pause()

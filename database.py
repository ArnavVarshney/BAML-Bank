import random
import sqlite3  # sqlite3 - provides functionality to deal with SQL database

from utility import *


def connect(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except:
        print('Connection failed!')


def sql_setup():
    """
    Sets up all the required databases/tables/connections required during execution
    """
    connection = connect('db.sqlite')
    crsr = connection.cursor()

    try:
        crsr.execute("CREATE TABLE IF NOT EXISTS transaction_log(customer_id INTEGER, account_number varchar(10),"
                     "    date varchar(10), time varchar(8), branch int, amount int, opening_balance int, "
                     "closing_balance int, remarks varchar(255), first_name varchar(20), last_name varchar(20))")
    except sqlite3.OperationalError:
        print('Table transaction_log could not be created')

    try:
        crsr.execute(
            "CREATE TABLE IF NOT EXISTS branch(branch_code INTEGER primary key AUTOINCREMENT,branch_name varchar(255), "
            "building varchar(255), "
            "street_name varchar(255), locality varchar(255), landmark varchar(255), city varchar(255), state varchar(255), "
            "country varchar(255), zip_code varchar(6))")
    except sqlite3.OperationalError:
        print('Table branch could not be created')

    try:
        crsr.execute(
            "CREATE TABLE IF NOT EXISTS customer(first_name varchar(255), last_name varchar(255), building varchar(255), "
            "street_name varchar(255), locality varchar(255), landmark varchar(255), city varchar(255), state varchar(255),"
            "    country varchar(255), zip_code varchar(6), phone_number varchar(15), email_id varchar(255), "
            "customer_id INTEGER primary key AUTOINCREMENT, user_name varchar(255), password varchar(255), branch int, balance int, "
            "gender varchar(1), date_of_birth varchar(10))")
    except sqlite3.OperationalError:
        print('Table customer could not be created')

    try:
        crsr.execute(
            "CREATE TABLE IF NOT EXISTS account(balance int, account_number varchar(10), "
            "branch int, customer_id int)")
    except sqlite3.OperationalError:
        print('Table account could not be created')

    try:
        crsr.execute(
            "CREATE TABLE IF NOT EXISTS employee(employee_id INTEGER primary key AUTOINCREMENT, user_name varchar(255), "
            "password varchar(255), first_name varchar(255), last_name varchar(255), role int, branch int, gender varchar(1), "
            "date_of_birth varchar(10), building varchar(255), "
            "street_name varchar(255), locality varchar(255), landmark varchar(255), city varchar(255), state varchar(255),"
            "    country varchar(255), zip_code varchar(6), phone_number varchar(15), email_id varchar(255))")
    except sqlite3.OperationalError:
        print('Table employee could not be created')
    connection.commit()
    connection.close()


def check_auth(user, password, role):
    connection = connect('db.sqlite')
    crsr = connection.cursor()
    if role == '0' or role == '1':
        crsr.execute("SELECT * FROM employee WHERE user_name = ? AND password = ?", (user, password,))
    else:
        crsr.execute("SELECT * FROM customer WHERE user_name = ? AND password = ?", (user, password,))
    rows = crsr.fetchone()
    connection.close()
    if rows:
        return True
    return False


def retrieve_employee(user):
    connection = connect('db.sqlite')
    crsr = connection.cursor()
    crsr.execute("SELECT * FROM employee WHERE user_name = ?", (user,))
    rows = crsr.fetchone()
    connection.close()
    if rows:
        '''employee_info = {'first_name':rows[0], 'last_name':rows[1], 'building':rows[2], 'street_name':rows[3], 'locality':rows[4], 'landmark':rows[5], 'city':rows[6],
        'state':rows[7], 'country':rows[8], 'zip_code':rows[9], 'phone_number':rows[10], 'email_id':rows[11], 'customer_id':rows[12], 'user_name':rows[13], 'password':rows[14],
        'branch':rows[15], 'balance':rows[16], 'gender':rows[17], 'date_of_birth':rows[18]}
        return employee_info'''
        return rows
    else:
        return False


def retrieve_all_employees():
    connection = connect('db.sqlite')
    crsr = connection.cursor()
    crsr.execute("SELECT * FROM employee")
    rows = crsr.fetchall()
    connection.close()
    return rows


def register_employee(user_name, first_name, last_name, password, role, branch, date_of_birth, gender, building,
                      street_name, locality, landmark, city, state, country, zip_code,
                      phone_number, email_id):
    connection = connect('db.sqlite')
    crsr = connection.cursor()
    crsr.execute(
        "INSERT INTO employee(user_name, first_name, last_name, password, role, "
        "branch, date_of_birth, gender, building, street_name, locality, landmark, city, "
        "state, country, zip_code, phone_number, email_id) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
        (user_name, first_name, last_name, password, role, branch, date_of_birth, gender, building, street_name,
         locality, landmark, city, state, country, zip_code,
         phone_number, email_id))
    connection.commit()
    connection.close()


def delete_employee(user_name):
    connection = connect('db.sqlite')
    crsr = connection.cursor()
    crsr.execute("DELETE FROM employee WHERE user_name = ?", (user_name,))
    connection.commit()
    connection.close()


def make_admin(user_name):
    connection = connect('db.sqlite')
    crsr = connection.cursor()
    crsr.execute("UPDATE employee SET role = 0 WHERE user_name = ?", (user_name,))
    connection.commit()
    connection.close()


def retrieve_customer(user):
    connection = connect('db.sqlite')
    crsr = connection.cursor()
    crsr.execute("SELECT * FROM customer WHERE user_name = ?", (user,))
    rows = crsr.fetchone()
    connection.close()
    if rows:
        return rows
    else:
        return False


def retrieve_all_customers():
    connection = connect('db.sqlite')
    crsr = connection.cursor()
    crsr.execute("SELECT * FROM customer")
    rows = crsr.fetchall()
    connection.close()
    return rows


def register_customer(first_name, last_name, building, street_name, locality, landmark, city, state, country, zip_code,
                      phone_number, email_id, user_name, password, branch, date_of_birth, gender, balance):
    connection = connect('db.sqlite')
    crsr = connection.cursor()
    crsr.execute(
        "INSERT INTO customer(first_name, last_name, building, street_name, locality, landmark, city, state, country, "
        "zip_code, phone_number, email_id, user_name, password, branch, date_of_birth, gender, balance) VALUES"
        "(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (
            first_name, last_name, building, street_name, locality, landmark, city, state, country, zip_code,
            phone_number, email_id, user_name, password, branch, date_of_birth, gender, balance))
    connection.commit()
    connection.close()


def delete_customer(user_name):
    connection = connect('db.sqlite')
    crsr = connection.cursor()
    crsr.execute("DELETE FROM customer WHERE user_name = ?", (user_name,))
    connection.commit()
    connection.close()


def get_id_customer(user_name):
    connection = connect('db.sqlite')
    crsr = connection.cursor()
    crsr.execute('SELECT * FROM customer WHERE user_name = ?', (user_name,))
    rows = crsr.fetchone()
    connection.commit()
    connection.close()
    return rows


def update_customer(field, value, user_name):
    connection = connect('db.sqlite')
    crsr = connection.cursor()
    crsr.execute(str("UPDATE customer SET " + field + " = '" + value + "' WHERE user_name = ?"), (user_name,))
    connection.commit()
    connection.close()


def retrieve_branch(branch_code):
    connection = connect('db.sqlite')
    crsr = connection.cursor()
    crsr.execute("SELECT * FROM branch WHERE branch_code = ?", (branch_code,))
    rows = crsr.fetchone()
    connection.close()
    if len(rows) != 0:
        return rows[0]
    else:
        return False


def retrieve_all_branches():
    connection = connect('db.sqlite')
    crsr = connection.cursor()
    crsr.execute("SELECT * FROM branch")
    rows = crsr.fetchall()
    connection.close()
    return rows


def register_branch(branch_name, building, street_name, locality, landmark, city, state, country,
                    zip_code):
    connection = connect('db.sqlite')
    crsr = connection.cursor()
    crsr.execute(
        "INSERT INTO branch(branch_name , building , street_name , locality , landmark , city , state , country , zip_code) VALUES(?,?,?,?,?,?,?,?,?)",
        (branch_name, building, street_name, locality, landmark, city, state, country, zip_code))
    connection.commit()
    connection.close()


def delete_branch(user_name):
    connection = connect('db.sqlite')
    crsr = connection.cursor()
    crsr.execute("DELETE FROM branch WHERE branch_name = ?", (user_name,))
    connection.commit()
    connection.close()


def retrieve_accounts(branch_code):
    connection = connect('db.sqlite')
    crsr = connection.cursor()
    crsr.execute("SELECT * FROM transaction_log WHERE branch = ?", (branch_code,))
    rows = crsr.fetchall()
    connection.close()
    return rows


def retrieve_accounts_customer(customer_id):
    connection = connect('db.sqlite')
    crsr = connection.cursor()
    crsr.execute("SELECT * FROM transaction_log WHERE customer_id = ?", (customer_id,))
    rows = crsr.fetchall()
    connection.close()
    return rows


def retrieve_all_accounts():
    connection = connect('db.sqlite')
    crsr = connection.cursor()
    crsr.execute("SELECT * FROM transaction_log")
    rows = crsr.fetchall()
    connection.close()
    if len(rows) != 0:
        return rows
    else:
        return False


def id_account():
    connection = connect('db.sqlite')
    crsr = connection.cursor()
    while True:
        num = random.randint(1000000000, 9999999999)
        crsr.execute("SELECT * FROM transaction_log WHERE account_number = ?", (num,))
        rows = crsr.fetchall()
        connection.close()
        if len(rows) == 0:
            return num
        else:
            return False


def add_customer(customer_id, branch_code, num):
    connection = connect('db.sqlite')
    crsr = connection.cursor()
    crsr.execute('INSERT into account(branch ,account_number ,customer_id) VALUES(?,?,?)',
                 (branch_code, num, customer_id))
    connection.commit()
    crsr.execute('UPDATE customer SET branch = ? WHERE customer_id = ?',
                 (branch_code, customer_id))
    print("Your Account Number: " + str(num))
    connection.commit()
    connection.close()


def retrieve_all_accounts_customer(customer_id):
    connection = connect('db.sqlite')
    crsr = connection.cursor()
    acc = "SELECT * FROM account WHERE customer_id = ?"
    crsr.execute(acc, (customer_id,))
    connection.commit()
    rows = crsr.fetchall()
    connection.close()
    return len(rows)


def register_account(customer_id, branch_code):
    connection = connect('db.sqlite')
    crsr = connection.cursor()
    account_number = ""
    account_number += '0'*(4-len(str(customer_id))) + str(customer_id) + '0'*(4-len(str(branch_code))) + \
                      str(branch_code) + str(retrieve_all_accounts_customer(customer_id)+1)
    crsr.execute('INSERT into account(branch ,account_number ,customer_id, balance) VALUES(?,?,?,?)',
                 (branch_code, account_number, customer_id, 0))
    print("Your account number is " + account_number)
    connection.commit()
    connection.close()
    return account_number


def remove_customer(customer_id):
    connection = connect('db.sqlite')
    crsr = connection.cursor()
    delete_branch_ = "DELETE FROM transaction_log WHERE customer_id = ?"
    crsr.execute(delete_branch_, (customer_id,))
    crsr.execute("DELETE FROM transaction_log WHERE customer_id = ?", customer_id)
    connection.commit()
    connection.close()


def deposit(deposit, user):
    connection = connect('db.sqlite')
    crsr = connection.cursor()
    crsr.execute('SELECT * FROM customer WHERE user_name = ?', (user,))
    temp = crsr.fetchone()
    crsr.execute("SELECT account_number FROM account WHERE customer_id = ?", (temp[12],))
    temp_1 = (crsr.fetchone())[0]
    crsr.execute(
        "INSERT INTO transaction_log(customer_id, account_number, date , time , "
        "branch , amount , opening_balance , "
        "closing_balance , remarks ) VALUES(?,?,?,?,?,?,?,?,?)",
        (temp[12], temp_1, get_current_date(), get_current_time(), temp[15], deposit, temp[16], temp[16] + deposit,
         'Deposit'))

    temp_2 = temp[16]
    crsr.execute(
        "UPDATE account SET balance = ? WHERE account_number = ?",
        (temp_2 + deposit, temp_1)
    )
    temp_2 = temp_2 + deposit
    crsr.execute('UPDATE customer SET balance = ?  WHERE user_name = ?',
                 (temp_2, user))
    connection.commit()
    connection.close()


def list_all_account(username):
    connection = connect('db.sqlite')
    crsr = connection.cursor()
    crsr.execute('SELECT * FROM customer WHERE user_name = ?', (username,))
    temp = crsr.fetchone()
    temp = temp[16]
    crsr.execute('SELECT * FROM account WHERE customer_id = ?', (temp,))
    temp = crsr.fetchall()
    connection.close()
    return temp


def transact(transact, user):
    connection = connect('db.sqlite')
    crsr = connection.cursor()
    crsr.execute('SELECT * FROM customer WHERE user_name = ?', (user,))
    temp = crsr.fetchone()
    crsr.execute("SELECT account_number FROM account WHERE customer_id = ?", (temp[12],))
    temp_1 = (crsr.fetchone())[0]
    crsr.execute(
        "INSERT INTO transaction_log(customer_id, account_number, date , time , "
        "branch , amount , opening_balance , "
        "closing_balance , remarks ) VALUES(?,?,?,?,?,?,?,?,?)",
        (temp[16], temp_1, get_current_date(), get_current_time(), temp[15], transact, temp[16], temp[16] + transact,
         'Transact'))
    crsr.execute(
        "UPDATE account SET balance = ? WHERE customer_id = ?",
        (temp[16] + transact, temp[12])
    )
    temp = temp[16]
    if temp is None or temp < transact:
        print("You do not have enough funds to complete your transaction")
    else:
        temp = temp - transact
        crsr.execute('UPDATE customer SET balance = ?  WHERE user_name = ?',
                     (temp, user))
    connection.commit()
    connection.close()


def transfer(transfer, user_1, acc):
    connection = connect('db.sqlite')
    crsr = connection.cursor()
    crsr.execute('SELECT * FROM customer WHERE user_name = ?', (user_1,))
    temp = crsr.fetchone()
    temp = temp[16]
    if temp is None or temp < transfer:
        print("You do not have enough funds to complete your transfer")
    else:
        crsr.execute('SELECT customer_id FROM transaction_log WHERE account_number = ?', acc)
        temp = crsr.fetchone()
        if temp is not None:
            crsr.execute('SELECT balance FROM customer WHERE customer_id = ?', temp)
            if crsr.fetchone() is not None:
                crsr.execute('SELECT user_name FROM customer WHERE customer_id = ?', temp)
                temp_2 = str((crsr.fetchone())[0])
                deposit(transfer, temp_2)
                transact(transfer, user_1)
            else:
                print("User does not exist")
        else:
            print("Account does not exist")
    connection.commit()
    connection.close()


def view_balance(user_name):
    connection = connect('db.sqlite')
    crsr = connection.cursor()
    crsr.execute('SELECT balance FROM customer WHERE user_name = ?', (user_name,))
    temp = crsr.fetchone()
    connection.commit()
    connection.close()
    return temp[0]


def deltable():
    connection = connect('db.sqlite')
    crsr = connection.cursor()
    crsr.execute("DROP TABLE transaction_log")
    crsr.execute("DROP TABLE branch")
    crsr.execute("DROP TABLE customer")
    connection.commit()

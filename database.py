import sqlite3  # sqlite3 - provides functionality to deal with SQL database

import random

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
    create_transaction_log = (
        "CREATE TABLE IF NOT EXISTS transaction_log(customer_id varchar(4), account_number varchar(10),"
        "    date varchar(10), time varchar(8), branch varchar(4), credit int,debit int, opening_balance int, "
        "closing_balance int, remarks varchar(255))")
    try:
        crsr.execute(create_transaction_log)
    except sqlite3.OperationalError:
        print('Table transaction_log could not be created')

    create_branch = (
        "CREATE TABLE IF NOT EXISTS branch(branch_code varchar(4), branch_name varchar(255), building varchar(255), "
        "street_name varchar(255), locality varchar(255), landmark varchar(255), city varchar(255), state varchar(255), "
        "country varchar(255), zip_code varchar(6), customer_id varchar(6))")
    try:
        crsr.execute(create_branch)
    except sqlite3.OperationalError:
        print('Table branch could not be created')

    create_customer = (
        "CREATE TABLE IF NOT EXISTS customer(first_name varchar(255), last_name varchar(255), building varchar(255), "
        "street_name varchar(255), locality varchar(255), landmark varchar(255), city varchar(255), state varchar(255),"
        "    country varchar(255), zip_code varchar(6), phone_number varchar(15), email_id varchar(255), "
        "customer_id varchar(6), user_name varchar(255),password varchar(255),balance varchar(9))")
    try:
        crsr.execute(create_customer)
    except sqlite3.OperationalError:
        print('Table customer could not be created')

    create_employee = (
        "CREATE TABLE IF NOT EXISTS employee(employee_id INTEGER primary key AUTOINCREMENT, user_name varchar(255), "
        "password varchar(255), first_name varchar(255), last_name varchar(255), role int)")
    try:
        crsr.execute(create_employee)
    except sqlite3.OperationalError:
        print('Table employee could not be created')

    insert_admin()
    connection.commit()
    connection.close()


def check_auth(user, password, role):
    connection = connect('db.sqlite')
    crsr = connection.cursor()
    if role == '0' or role == '1':
        select_auth = "SELECT * FROM employee WHERE user_name = ? AND password = ?"
    else:
        select_auth = "SELECT * FROM customer WHERE user_name = ? AND password = ?"
    crsr.execute(select_auth, (user, password,))
    rows = crsr.fetchall()
    connection.close()
    if rows:
        return True
    return False


def insert_admin():
    connection = connect('db.sqlite')
    crsr = connection.cursor()
    add_admin_details = "INSERT INTO employee(user_name, first_name, last_name, password, role) VALUES('admin','Arnav'," \
                        "'Varshney', 'admin', 0)"
    if not retrieve_employee('admin'):
        try:
            crsr.execute(add_admin_details)
        except sqlite3.IntegrityError:
            pass
    connection.commit()
    connection.close()


def retrieve_employee(user):
    connection = connect('db.sqlite')
    crsr = connection.cursor()
    select_employee = "SELECT * FROM employee WHERE user_name = ?"
    crsr.execute(select_employee, (user,))
    rows = crsr.fetchall()
    connection.close()
    if len(rows) != 0:
        return rows[0]
    else:
        return False


def retrieve_all_employees():
    connection = connect('db.sqlite')
    crsr = connection.cursor()
    select_all_employees = "SELECT * FROM employee"
    crsr.execute(select_all_employees)
    rows = crsr.fetchall()
    connection.close()
    return rows


def register_employee(user_name, first_name, last_name, password, role):
    connection = connect('db.sqlite')
    crsr = connection.cursor()
    insert_employee = "INSERT INTO employee(user_name, first_name, last_name, password, role) VALUES(?,?,?,?,?)"
    crsr.execute(insert_employee, (user_name, first_name, last_name, password, role,))
    connection.commit()
    connection.close()


def delete_employee(user_name):
    connection = connect('db.sqlite')
    crsr = connection.cursor()
    delete_employee_ = "DELETE FROM employee WHERE user_name = ?"
    crsr.execute(delete_employee_, (user_name,))
    connection.commit()
    connection.close()


def make_admin(user_name):
    connection = connect('db.sqlite')
    crsr = connection.cursor()
    make_admi = "UPDATE employee SET role = 0 WHERE user_name = ?"
    crsr.execute(make_admi, (user_name,))
    connection.commit()
    connection.close()


def retrieve_customer(user):
    connection = connect('db.sqlite')
    crsr = connection.cursor()
    select_customer = "SELECT * FROM customer WHERE user_name = ?"
    crsr.execute(select_customer, (user,))
    rows = crsr.fetchall()
    connection.close()
    if len(rows) != 0:
        return rows[0]
    else:
        return False


def retrieve_all_customers():
    connection = connect('db.sqlite')
    crsr = connection.cursor()
    select_all_customers = "SELECT * FROM customer"
    crsr.execute(select_all_customers)
    rows = crsr.fetchall()
    connection.close()
    return rows


def register_customer(first_name, last_name, building, street_name, locality, landmark, city, state,country, zip_code, phone_number, email_id, customer_id, user_name,password):
    connection = connect('db.sqlite')
    crsr = connection.cursor()
    insert_customer = "INSERT INTO customer(first_name, last_name, building, street_name, locality, landmark, city, state,country, zip_code, phone_number, email_id, customer_id, user_name,password) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
    crsr.execute(insert_customer, (first_name, last_name, building, street_name, locality, landmark, city, state,country, zip_code, phone_number, email_id, customer_id, user_name,password))
    connection.commit()
    connection.close()


def delete_customer(user_name):
    connection = connect('db.sqlite')
    crsr = connection.cursor()
    delete_customer_ = "DELETE FROM customer WHERE user_name = ?"
    crsr.execute(delete_customer_, (user_name,))
    connection.commit()
    connection.close()

def id_customer():
    connection = connect('db.sqlite')
    crsr = connection.cursor()
    while True:
        number = random.randint(100000, 999999)
        tem = (number,)
        crsr.execute('SELECT * FROM customer WHERE customer_id = ?', tem)
        if crsr.fetchone() is None:
            return number
        else:
            continue
def retrieve_branch(branch_code):
    connection = connect('db.sqlite')
    crsr = connection.cursor()
    select_branch = "SELECT * FROM branch WHERE branch_code = ?"
    crsr.execute(select_branch, (branch_code,))
    rows = crsr.fetchall()
    connection.close()
    if len(rows) != 0:
        return rows[0]
    else:
        return False


def retrieve_all_branches():
    connection = connect('db.sqlite')
    crsr = connection.cursor()
    select_all_branches = "SELECT * FROM branch"
    crsr.execute(select_all_branches)
    rows = crsr.fetchall()
    connection.close()
    return rows


def register_branch(branch_code , branch_name , building , street_name , locality , landmark , city , state , country , zip_code):
    connection = connect('db.sqlite')
    crsr = connection.cursor()
    insert_branch = "INSERT INTO branch(branch_code , branch_name , building , street_name , locality , landmark , city , state , country , zip_code) VALUES(?,?,?,?,?,?,?,?,?,?)"
    crsr.execute(insert_branch, (branch_code , branch_name , building , street_name , locality , landmark , city , state , country , zip_code))
    connection.commit()
    connection.close()


def delete_branch(user_name):
    connection = connect('db.sqlite')
    crsr = connection.cursor()
    delete_branch_ = "DELETE FROM branch WHERE branch_name = ?"
    crsr.execute(delete_branch_, (user_name,))
    connection.commit()
    connection.close()

def id_branch():
    connection = connect('db.sqlite')
    crsr = connection.cursor()
    while True:
        number = random.randint(100000, 999999)
        tem = (number,)
        crsr.execute('SELECT * FROM branch WHERE branch_code = ?', tem)
        if crsr.fetchone() is None:
            return number
        else:
            continue

def retrieve_accounts(branch_code):
    connection = connect('db.sqlite')
    crsr = connection.cursor()
    select_accounts = "SELECT * FROM transaction_log WHERE branch = ?"
    crsr.execute(select_accounts,(branch_code,))
    rows = crsr.fetchall()
    connection.close()
    return rows
def retrieve_accounts_customer(customer_id):
    connection = connect('db.sqlite')
    crsr = connection.cursor()
    select_accounts = "SELECT * FROM transaction_log WHERE customer_id = ?"
    crsr.execute(select_accounts,(customer_id,))
    rows = crsr.fetchall()
    connection.close()
    return rows

def add_customer(customer_id, branch_code):
    connection = connect('db.sqlite')
    crsr = connection.cursor()
    crsr.execute('UPDATE transaction_log SET branch = ? WHERE customer_id = ?',
        (branch_code, customer_id))
    connection.commit()
    connection.close()


def remove_customer(customer_id):
    connection = connect('db.sqlite')
    crsr = connection.cursor()
    delete_branch_ = "DELETE FROM transaction_log WHERE customer_id = ?"
    crsr.execute(delete_branch_, (customer_id,))
    connection.commit()
    connection.close()


def deltable():
    connection = connect('db.sqlite')
    crsr = connection.cursor()
    crsr.execute("DROP TABLE customer")
    crsr.execute("DROP TABLE employee")
    crsr.execute("DROP TABLE transaction_log")
    crsr.execute("DROP TABLE branch")
    connection.commit()

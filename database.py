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
        "INSERT INTO employee(user_name, first_name, last_name, password, role, branch, date_of_birth, gender, building, street_name, locality, landmark, city, "
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
    rows = crsr.fetchone()
    connection.close()
    return rows


def retrieve_accounts_customer(customer_id):
    connection = connect('db.sqlite')
    crsr = connection.cursor()
    crsr.execute("SELECT * FROM transaction_log WHERE customer_id = ?", (customer_id,))
    rows = crsr.fetchone()
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
        num = random.randint(1000000000,9999999999)
        crsr.execute("SELECT * FROM transaction_log WHERE account_number = ?",num)
        rows = crsr.fetchall()
        connection.close()
        if len(rows) == 0:
            return num
        else:
            return False


def add_customer(customer_id, branch_code,num):
    connection = connect('db.sqlite')
    crsr = connection.cursor()
    crsr.execute('UPDATE transaction_log SET branch = ? ,account_number =?  WHERE customer_id = ?',
        (branch_code, num, customer_id))
    connection.commit()
    crsr.execute('UPDATE customer SET branch = ? WHERE customer_id = ?',
        (branch_code, customer_id))
    print("Your Account Number: " + str(num))
    connection.commit()
    connection.close()


def remove_customer(customer_id):
    connection = connect('db.sqlite')
    crsr = connection.cursor()
    delete_branch_ = "DELETE FROM transaction_log WHERE customer_id = ?"
    crsr.execute(delete_branch_, (customer_id,))
    crsr.execute("DELETE FROM transaction_log WHERE customer_id = ?", customer_id)
    connection.commit()
    connection.close()

def deposit(deposit, user_name, user):
    connection = connect('db.sqlite')
    crsr = connection.cursor()
    crsr.execute('SELECT * FROM customer WHERE user_name = ?', user_name)
    temp = crsr.fetchone()
    temp = temp[16]
    if temp is None:
        crsr.execute('UPDATE customer SET balance = ?  WHERE user_name = ?',
                     (deposit, user))
    else:
        temp = temp + deposit
        crsr.execute('UPDATE customer SET balance = ?  WHERE user_name = ?',
                     (temp, user))
    connection.commit()
    connection.close()


def transact(transact, user_name, user):
    connection = connect('db.sqlite')
    crsr = connection.cursor()
    crsr.execute('SELECT * FROM customer WHERE user_name = ?', user_name)
    temp = crsr.fetchone()
    temp = temp[16]
    if temp is None or temp < transact:
        print("You do not have enough funds to complete your transaction")
    else:
        temp = temp - transact
        crsr.execute('UPDATE customer SET balance = ?  WHERE user_name = ?',
                     (temp, user))
    connection.commit()
    connection.close()


def transfer(transfer, user_1, user_2):
    connection = connect('db.sqlite')
    crsr = connection.cursor()
    crsr.execute('SELECT * FROM customer WHERE user_name = ?', user_1)
    temp = crsr.fetchone()
    temp = temp[16]
    if temp is None or temp < transfer:
        print("You do not have enough funds to complete your transfer")
    else:
        crsr.execute('SELECT branch FROM customer WHERE customer_id = ?', user_2)
        if crsr.fetchone() is not None:
            crsr.execute('SELECT user_name FROM customer WHERE customer_id = ?', user_2)
            temp_1 = crsr.fetchone()
            deposit(temp, (temp_1,), temp_1)
        else:
            print("User does not exist")
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


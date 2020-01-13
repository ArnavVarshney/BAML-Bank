import sqlite3  # sqlite3 - provides functionality to deal with SQL database


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
        "CREATE TABLE IF NOT EXISTS transaction_log(customer_id INTEGER, account_number varchar(10),"
        "    date varchar(10), time varchar(8), branch int, amount int, opening_balance int, "
        "closing_balance int, remarks varchar(255))")
    try:
        crsr.execute(create_transaction_log)
    except sqlite3.OperationalError:
        print('Table transaction_log could not be created')

    create_branch = (
        "CREATE TABLE IF NOT EXISTS branch(branch_code INTEGER primary key AUTOINCREMENT, branch_name varchar(255), "
        "building varchar(255), "
        "street_name varchar(255), locality varchar(255), landmark varchar(255), city varchar(255), state varchar(255), "
        "country varchar(255), zip_code varchar(6))")
    try:
        crsr.execute(create_branch)
    except sqlite3.OperationalError:
        print('Table branch could not be created')

    create_customer = (
        "CREATE TABLE IF NOT EXISTS customer(first_name varchar(255), last_name varchar(255), building varchar(255), "
        "street_name varchar(255), locality varchar(255), landmark varchar(255), city varchar(255), state varchar(255),"
        "    country varchar(255), zip_code varchar(6), phone_number varchar(15), email_id varchar(255), "
        "customer_id INTEGER primary key AUTOINCREMENT, user_name varchar(255), password varchar(255), branch int)")
    try:
        crsr.execute(create_customer)
    except sqlite3.OperationalError:
        print('Table customer could not be created')

    create_employee = (
        "CREATE TABLE IF NOT EXISTS employee(employee_id INTEGER primary key AUTOINCREMENT, user_name varchar(255), "
        "password varchar(255), first_name varchar(255), last_name varchar(255), role int, branch int)")
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


def register_employee(user_name, first_name, last_name, password, role, branch):
    connection = connect('db.sqlite')
    crsr = connection.cursor()
    insert_employee = "INSERT INTO employee(user_name, first_name, last_name, password, role, branch) VALUES(?,?,?,?,?,?)"
    crsr.execute(insert_employee, (user_name, first_name, last_name, password, role, branch,))
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


def register_customer(first_name, last_name, building, street_name, locality, landmark, city, state, country, zip_code,
                      phone_number, email_id, user_name, password, branch):
    connection = connect('db.sqlite')
    crsr = connection.cursor()
    insert_customer = "INSERT INTO customer(first_name, last_name, building, street_name, locality, landmark, city, " \
                      "state, country, zip_code, phone_number, email_id, user_name, password, branch) VALUES" \
                      "(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
    crsr.execute(insert_customer, (
        first_name, last_name, building, street_name, locality, landmark, city, state, country, zip_code, phone_number,
        email_id, user_name, password, branch))
    connection.commit()
    connection.close()


def delete_customer(user_name):
    connection = connect('db.sqlite')
    crsr = connection.cursor()
    delete_customer_ = "DELETE FROM customer WHERE user_name = ?"
    crsr.execute(delete_customer_, (user_name,))
    connection.commit()
    connection.close()


def get_id_customer(user_name):
    connection = connect('db.sqlite')
    crsr = connection.cursor()
    crsr.execute('SELECT * FROM customer WHERE user_name = ?', (user_name,))
    rows = crsr.fetchall()
    connection.commit()
    connection.close()
    return rows


def update_customer(field, value, user_name):
    connection = connect('db.sqlite')
    crsr = connection.cursor()
    upd_customer = str("UPDATE customer SET " + field + " = '" + value + "' WHERE user_name = ?")
    print(upd_customer)
    crsr.execute(upd_customer, (user_name,))
    connection.commit()
    connection.close()

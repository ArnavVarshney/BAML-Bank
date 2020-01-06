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
        "CREATE TABLE IF NOT EXISTS transaction_log(customer_id varchar(4), account_number varchar(10),"
        "    date varchar(10), time varchar(8), branch varchar(4), amount int, opening_balance int, "
        "closing_balance int, remarks varchar(255))")
    try:
        crsr.execute(create_transaction_log)
    except sqlite3.OperationalError:
        print('Table transaction_log could not be created')

    create_branch = (
        "CREATE TABLE IF NOT EXISTS branch(branch_code varchar(4), branch_name varchar(255), building varchar(255), "
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
        "customer_id varchar(4))")
    try:
        crsr.execute(create_customer)
    except sqlite3.OperationalError:
        print('Table customer could not be created')

    create_auth = "CREATE TABLE IF NOT EXISTS auth(user_name varchar(255) primary key , password varchar(255), " \
                  "role int)"
    try:
        crsr.execute(create_auth)
    except sqlite3.OperationalError:
        print('Table auth could not be created')

    add_admin = "INSERT INTO auth VALUES('admin', 'admin', 0)"
    try:
        crsr.execute(add_admin)
    except sqlite3.IntegrityError:
        pass

    connection.commit()
    connection.close()


def check_auth(user, passw, role):
    connection = connect('db.sqlite')
    crsr = connection.cursor()
    select_auth = "SELECT * FROM auth WHERE user_name = ? AND password = ? AND role = ?"
    crsr.execute(select_auth, (user, passw, role,))
    rows = crsr.fetchall()
    if rows:
        return True
    return False

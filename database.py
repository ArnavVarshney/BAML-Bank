import sqlite3  # sqlite3 - provides functionality to deal with SQL database

connection = sqlite3.connect("db.sqlite")
crsr = connection.cursor()


def sql_setup():
    """
    Sets up all the required databases/tables/connections required during execution
    """
    create_transaction_log = """CREATE TABLE transaction_log(customer_id varchar(4), account_number varchar(10), 
    date varchar(10), time varchar(8), branch varchar(4), amount int, opening_balance int, closing_balance int, 
    remarks varchar(255))"""
    try:
        crsr.execute(create_transaction_log)
    except sqlite3.OperationalError:
        print('Table transaction_log could not be created/already exists')
    create_branch = """CREATE TABLE branch(branch_code varchar(4), branch_name varchar(255), building varchar(255), 
    street_name varchar(255), locality varchar(255), landmark varchar(255), city varchar(255), state varchar(255),
    country varchar(255), zip_code varchar(6))"""
    try:
        crsr.execute(create_branch)
    except sqlite3.OperationalError:
        print('Table branch could not be created/already exists')
    create_customer = """CREATE TABLE customer(first_name varchar(255), last_name varchar(255), building varchar(255), 
    street_name varchar(255), locality varchar(255), landmark varchar(255), city varchar(255), state varchar(255),
    country varchar(255), zip_code varchar(6), phone_number varchar(15), email_id varchar(255), 
    customer_id varchar(4))"""

connection.commit()
connection.close()

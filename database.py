import sqlite3  # sqlite3 - provides functionality to deal with SQL database

connection = sqlite3.connect("BAMLBank")
# noinspection SpellCheckingInspection
crsr = connection.cursor()


def sql_setup():
    """
    Sets up all the required databases/tables/connections required during execution
    """
    transaction_log_table_command = """CREATE TABLE transaction_log(customer_id varchar(4), account_number varchar(10), 
    date varchar(10), time varchar(8), branch varchar(4), amount int, opening_balance int, closing_balance int, 
    remarks varchar(255))"""
    try:
        crsr.execute(transaction_log_table_command)
    except sqlite3.OperationalError:
        print('Table transaction_log could not be created')


print('Committing to database!')
connection.commit()
connection.close()

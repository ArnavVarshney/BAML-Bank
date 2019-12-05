import sqlite3

connection = sqlite3.connect("BAMLBank")

crsr = connection.cursor()

sql_command = """CREATE TABLE transaction_log(customer_id varchar(4))"""

crsr.execute(sql_command)

connection.commit()
connection.close()

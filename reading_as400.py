import pyodbc
import csv
import sys

#server = '127.0.0.1'     # Striker(a.k.a. localhost) server
server = '192.168.1.21' # Castit server
database = 'Castit'
username = 'prog_jdbc'
password = 'Pr0gIt!'

# list configured drivers
# pyodbc.drivers()


#Castit Connection
#castit_cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';PORT=1433;DATABASE=' + database+';UID=' + username + ';PWD=' + password)
#castit_cursor = castit_cnxn.cursor()
#castit_Customer_Numbers = castit_cursor.execute('select as400_custno, cust_name from as400_to_Castit_Customer').fetchall()

# AS400 connection
as400_cnxn = pyodbc.connect('DSN=as400')
as400_cursor = as400_cnxn.cursor()
as400_parts = as400_cursor.execute("SELECT * FROM UNIDATA.UNPARTMF where pdpart = 'A3052'").fetchall()

for as400_part in as400_parts:
	print(as400_part)



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

# AS400 connection
#cnxn = pyodbc.connect('DSN=as400')

# striker Castit connection
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';PORT=1433;DATABASE=' + database+';UID=' + username + ';PWD=' + password)

# get cursor
castit_cursor = cnxn.cursor()

rows = castit_cursor.execute('select ppcn.customerno, cust.company, cust.customerno, ppcn.partno from Customer cust  inner join Part_Number_by_Customer_Number ppcn on cust.customerno = ppcn.customerno').fetchall()

#for row in rows
#   print(row[3],row[0], row[1])

file = csv.writer(open('Part_Price_by_Customer_Name.csv', 'w'))
for row in rows:
    file.writerow(row)

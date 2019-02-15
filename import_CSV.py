import pyodbc
import csv

#server = '127.0.0.1'     # Striker(a.k.a. localhost) server
server = '192.168.1.21' # Castit server
database = 'Castit'
username = 'prog_jdbc'
password = 'Pr0gIt!'

# striker Castit connection
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';PORT=1433;DATABASE=' + database+';UID=' + username + ';PWD=' + password)

#get cursor
castit_cursor = cnxn.cursor()
'''
f = open('Part_Price_by_Customer_Name.csv', 'r')
next(f, None)
reader = csv.reader(f)

castit_cursor.execute('create table Part_Price_by_Customer_Name (pdpart char(20), pdcsno int)')

for row in reader:
    castit_cursor.execute('insert into Part_Price_Translation values (?, ?)', row)
'''

f = open('Part_Price_by_Customer_Name.csv', 'r')
next(f, None)
reader = csv.reader(f)

castit_cursor.execute('create table Part_Number_by_Customer_Name (customerno char(10), company char(30), part_number char(20))')

for row in reader:
    castit_cursor.execute('insert into Part_Number_by_Customer_Name values (?, ?, ?)', row)

f.close()
cnxn.commit()
cnxn.close()


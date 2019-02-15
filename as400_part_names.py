import pyodbc

server = '127.0.0.1'     # Striker(a.k.a. localhost) server
#server = '192.168.1.21' # Castit server
database = 'Castit'
username = 'prog_jdbc'
password = 'Pr0gIt!'

# list configured drivers
# pyodbc.drivers()

 AS400 connection
cnxn_as400 = pyodbc.connect('DSN=as400')

# striker Castit connection
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';PORT=1433;DATABASE=' + database+';UID=' + username + ';PWD=' + password)

# get cursor
as400_cursor = cnxn_as400.cursor()
castit_cursor = cnxn.cursor()

names_from_as400 = as400_cursor.execute('select pdpart, pdabbr from unpartmf')
names_from_castit = castit_cursor.execute('select part_number from part_price')

for name_from_castit in names_from_castit:
    castit_cursor.execute('update part_price set part_name = ? where part_number = ?', names_from_as400[1], names_from_as400[0])

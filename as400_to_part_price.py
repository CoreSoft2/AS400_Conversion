import pyodbc

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

rows = castit_cursor.execute('select conv.as400_custno, conv.castit_custno, ppt.pdcsno, ppt.pdpart from AS400_to_Castit_Customer conv inner join Part_Price_Translation ppt on conv.as400_custno = ppt.pdcsno').fetchall()

for row in rows:
    print(row[0], row[1], row[3])



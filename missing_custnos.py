import pyodbc

#server = '127.0.0.1'     # Striker(a.k.a. localhost) server
server = '192.168.1.21' # Castit server
database = 'Castit'
username = 'prog_jdbc'
password = 'Pr0gIt!'

# list configured drivers
# pyodbc.drivers()


#Castit Connection
castit_cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';PORT=1433;DATABASE=' + database+';UID=' + username + ';PWD=' + password)
castit_cursor = castit_cnxn.cursor()

parts_in_both = castit_cursor.execute("select pp.part_number, ppt.pdpart from part_price pp inner join Part_Price_Translation ppt on pp.part_number = ppt.pdpart").fetchall()
parts_in_pncn = castit_cursor.execute("select pdpart from Part_Price_Translation").fetchall()

#parts_in_part_price = castit_cursor.execute("select distinct part_number from part_price").fetchall()

count = 1
'''
for part_in_pncn in parts_in_pncn:
    if part_in_pncn[0] not in parts_in_part_price[0]:
        print(count, part_in_pncn[0])
        count = count + 1
'''
for part_in_both in parts_in_both:
    count = count + 1
  
print("You have ", count, "part numbers that are in both the AS400 and the Castit.")
counts = 1

for part_in_pncn in parts_in_pncn and not part_in_both:
	count = count + 1

print("You have ", count, "part numbers that are on the AS400 but not Castit.")



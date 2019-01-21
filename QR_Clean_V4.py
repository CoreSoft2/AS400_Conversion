import pyodbc


#server = '127.0.0.1'
server = '192.168.1.21'
database = 'Castit'
username = 'prog_jdbc'
password = 'Pr0gIt!'

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

castit_cursor = cnxn.cursor()
'''
def row_change(row, array_number):
        row =  = map(lambda x: str(x[array_number].encode('utf-8').rstrip()), row)
        for each_instance in row:
                each_instance = each_instance.replace("b", "")
                each_instance = each_instance.replace("'", "")
        return row[array_number]
'''
results = castit_cursor.execute("select customerno, company, address1, address2, city, state, zip, country, contact, phone, fax from Customer where mastercustomerno is null and company is not null")

company_names = map(lambda x: str(x[1].encode('utf-8').rstrip()), results)
for company_name in company_names:
        company_name = company_name.replace("b'", "")
        company_name = company_name.replace("'", "")
        orig_cust = castit_cursor.execute("select customerno, address1, address2, city, state, zip, country, contact, phone, fax from Customer where mastercustomerno is null and company = ?", company_name).fetchall()
        print(company_name, orig_cust)

        
'''
null_customer_numbers = map(lambda x: int(x[0].encode('utf-8'), results)


        
for company_name in company_names:
	new_cust = castit_cursor.execute("select customerno from Customer where company = ? and customerno <> ?", company_name, null_customer_numbers).fetch_first()
	print new_cust
        #castit_cursor.execute("update customer where customerno = ? set address1 = ?, address2 = ? where customer = ", result[1], result[3], result[4])
	#castit_cursor.execute("delete from customer where company = ? and customerno <> ?", result[2], new_cust)


cnxn.commit()
'''

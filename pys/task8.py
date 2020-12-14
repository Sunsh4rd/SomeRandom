import pyodbc

def main():
	cnxn = pyodbc.connect('Driver={SQL Server};'
						  'Server=DESKTOP-MIRUVK9\SQLEXPRESS;'
						  'Database=nbd;'
						  'Trusted_Connection=yes;')
	
	cursor = cnxn.cursor()
	cursor.execute("SELECT * FROM MASTERST4")

	n = int(input())
	d = cursor.fetchmany(n)
	for row in d:
		print(row)

if __name__ == '__main__':
	main()
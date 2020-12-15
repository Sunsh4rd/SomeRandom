import pyodbc

def main():
	cnxn = pyodbc.connect('Driver={SQL Server};'
						  'Server=DESKTOP-36HKQFT\SQLEXPRESS;'
						  'Database=Polyclinic;'
						  'Trusted_Connection=yes;')
	#DESKTOP-MIRUVK9\SQLEXPRESS
	cursor = cnxn.cursor()
	cursor.execute("SELECT * FROM MedicalHistory")

	n = int(input())
	d = cursor.fetchmany(n)
	for row in d:
		print(row)

if __name__ == '__main__':
	main()
import pyodbc

def main():
	cnxn = pyodbc.connect('Driver={SQL Server};'
						  'Server=DESKTOP-MIRUVK9\SQLEXPRESS;'
						  'Database=Polyclinic;'
						  'UID=Common_User;'
						  'PWD=user')
	#DESKTOP-MIRUVK9\SQLEXPRESS
	#DESKTOP-36HKQFT\SQLEXPRESS
	cursor = cnxn.cursor()
	cursor.execute("SELECT * FROM Districts")
	d = cursor.fetchall()
	for row in d:
		print(row)
	cursor.execute("SELECT SUM(DistrictPopulation) FROM Districts")
	d = cursor.fetchall()
	for row in d:
		print(row[0])

	print(bool(cnxn))

	cursor.execute("SELECT * FROM Patients WHERE PatientID = 4")
	d = cursor.fetchall()
	for row in d:
		print(row)

	
	cnxn.commit()	
	cursor.close()
	cnxn.close()

if __name__ == '__main__':
	main()

# import random

# v = ['Терапевт', 'Педиатр', 'Кардиолог', 'Ревматолог', 'Хирург', 'Невролог', 'Травматолог']

# n = ['+7' + str(i) for i in range(900000, 999999)]

# import string

# def get_random_string(length):
#     letters = string.ascii_lowercase
#     result_str = ''.join(random.choice(letters) for i in range(length))
#     return result_str + '@mail.com'

# for i in range(1, 10):
# 	print('update Patients')
# 	print('set PhoneNumber = ', f'{random.choice(n)}')
# 	print('where PatientID = ', i)
# 	print()
# 	print('update Patients')
# 	print('set Email = ', get_random_string(random.randint(4, 10)))
# 	print('where PatientID = ', i)
# 	print()
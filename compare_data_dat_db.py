#!/usr/bin/python3

import pymysql

# Open database connection
db = pymysql.connect(host="localhost", user="root", passwd="root", db="naukri")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT * FROM job_applicationform")

# Fetch all row using fetchall() method.
all_data = cursor.fetchall()

print ("Application Form : ", all_data)

# get records count
cursor.execute("SELECT count(*) FROM job_applicationform")
records_count = cursor.fetchone()




cursor.execute("SELECT * FROM job_applicationform")


# Open dat file and read line by line
with open('naukri_job_applicationform_data.dat','r') as fo:
	line_count = 0
	
	for line in fo:
		line_count += 1
		print("\n", "Row", line_count, ": ", line)
		
		tab_splitted_line = line.strip().split("\t")
		print(tab_splitted_line)
		

		# Fetch all row using fetchall() method.
		db_data = cursor.fetchone()
		print(db_data,"\n")
		
		for i in range(0,len(db_data)-1):
			# check
			if str(tab_splitted_line[i]) != str(db_data[i]):
				print("\n", tab_splitted_line, "is not matched with ", str(db_data), "\n")
			
		
# DB
print("No of records in DB: ", records_count[0])
print("DB Record column length: ", len(all_data[0]))
# DAT File
print("No of lines in the file: ", line_count)
print("line\n",len(line.split('\t')))


# Value Comparision:
# compare records count and file line count
# if count matches, compare row 1, line1, find mismatched records
# else compare row and line and find mismatched records

# disconnect from server
db.close()
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

# disconnect from server
db.close()


with open('naukri_job_applicationform.dat','r') as fo:
	row = 0
	for line in fo:
		row += 1
		print("Row ", row, ": ", line, "\n")

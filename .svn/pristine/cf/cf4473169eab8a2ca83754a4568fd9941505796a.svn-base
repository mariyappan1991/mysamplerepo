#!/usr/bin/python3

import pymysql

# Open database connection
db = pymysql.connect(host="localhost", user="root", passwd="root", db="naukri")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT * FROM job_applicationform")

# Fetch a single row using fetchone() method.
one_data = cursor.fetchone()

all_data = cursor.fetchall()

print ("Application Form: Data 1 : ", one_data)
print ("Application Form : ", all_data)

# disconnect from server
db.close()
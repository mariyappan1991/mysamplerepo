#!/usr/bin/python3

import PyMySQL

# Open database connection
db = PyMySQL.connect("localhost","naukri","root","root" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT * FROM job_applicationform")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()

print ("Application Form : %s " % data)

# disconnect from server
db.close()
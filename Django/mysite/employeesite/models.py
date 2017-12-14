from __future__ import  unicode_literals
from django.db import models,connection
from django.db import IntegrityError
from django.shortcuts import render_to_response

import MySQLdb

# CREATE models

tablename = "Employees"
url = "../../employee/selecttable/"
errormsg = None

# Crating the demo table
def create_table():    
	try:
		with connection.cursor() as cursor:
			cursor.execute("CREATE TABLE Employees (EmployeeId int NOT NULL AUTO_INCREMENT,UserId int NOT NULL,DepartmentId int NOT NULL,PRIMARY KEY (EmployeeId),FOREIGN KEY (UserId) REFERENCES Users (UserId),FOREIGN KEY (DepartmentId) REFERENCES Departments(DepartmentId));")
			cursor.close()
		return tablename + ' table created successfully'

	except Exception as inst:
		return inst
			
# Insert some records in the demo table
def insert_table():
	try:
		with connection.cursor() as cursor:
			cursor.execute("INSERT INTO Employees (`UserId`, `DepartmentId`) VALUES ('2', '1'),('5', '2');")
			cursor.close()
		return 'data inserted to ' + tablename + ' sucessfully'

	except Exception as inst:
		return inst

#Get data from demo table	
def select_table():
	try:
		global errormsg
		errormsg= None
		with connection.cursor() as cursor:
			cursor.execute("Select * FROM Employees")
			rows = cursor.fetchall()
			cursor.close()

			if len(rows) == 0:
				errormsg = "No records found"

		return rows
		
	except Exception as inst:
		errormsg = inst
		return None

# Delete the records forn the table
def delete_records_table():
	try:
		with connection.cursor() as cursor:
			cursor.execute("DELETE FROM Employees")
			cursor.close()
			return "Records deleted"
	except Exception as inst:
		return inst

# Drop the demo table	
def drop_table():
	try:
		with connection.cursor() as cursor:
			cursor.execute("drop table Employees;")
			cursor.close()
		return tablename + ' table deleted successfully'

	except Exception as inst:
		return inst
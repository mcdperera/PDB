from __future__ import  unicode_literals
from django.db import models,connection
from django.db import IntegrityError
from django.shortcuts import render_to_response

# CREATE models

tablename = "UserType"
url = "../../usertype/selecttable/"
errormsg = None


# Crating the table
def create_table():
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "CREATE TABLE UserTypes (UserTypeId int NOT NULL AUTO_INCREMENT,UserType varchar(255) NOT NULL,Description varchar(255) NOT NULL,PRIMARY KEY (UserTypeId));")
            cursor.close()
        return tablename + ' table created successfully'

    except Exception as inst:
        return inst


# Insert some records into the table
def insert_table():
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO UserTypes (UserType, Description) VALUES ('Employee', 'Employee of the shopping mart web site.'),('Customer', 'Customer of the shopping mart web site.'),('Supplier', 'Supplier of the shopping mart web site.');")
            cursor.close()
        return 'data inserted to ' + tablename + ' sucessfully'

    except Exception as inst:
        return inst


# Get data from table
def select_table():
    try:
        global errormsg
        errormsg = None
        with connection.cursor() as cursor:
            cursor.execute("Select * FROM UserTypes")
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
            cursor.execute("DELETE FROM UserTypes")
            cursor.close()
            return "Records deleted"
    except Exception as inst:
        return inst


# Drop the table
def drop_table():
    try:
        with connection.cursor() as cursor:
            cursor.execute("drop table UserTypes;")
            cursor.close()
        return tablename + ' table deleted successfully'

    except Exception as inst:
        return inst
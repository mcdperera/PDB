from __future__ import  unicode_literals
from django.db import models,connection
from django.db import IntegrityError
from django.shortcuts import render_to_response

# CREATE models

tablename = "Supplier"
url = "../../supplier/selecttable/"
errormsg = None


# Crating the table
def create_table():
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "CREATE TABLE Suppliers (  `SupplierId` int(11) NOT NULL AUTO_INCREMENT,  `UserId` int(11) NOT NULL,  `Ratings` int(11) DEFAULT NULL,"
                " `NumberofProducts` int(11) DEFAULT NULL,  `CommisionRate` double DEFAULT NULL,  PRIMARY KEY (`SupplierId`),  KEY `UserId` (`UserId`));")
            cursor.close()
        return tablename + ' table created successfully'

    except Exception as inst:
        return inst


# Insert some records into the table
def insert_table():
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO Suppliers (`UserId`, `Ratings`, `NumberofProducts`, `CommisionRate`) VALUES ('3', '2.5', '50', '2.45'),('6', '1', '2', '9.45');")
            cursor.close()
        return 'data inserted to ' + tablename + ' successfully'

    except Exception as inst:
        return inst


# Get data from table
def select_table():
    try:
        global errormsg
        errormsg = None
        with connection.cursor() as cursor:
            cursor.execute("Select * FROM Suppliers")
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
            cursor.execute("DELETE FROM Suppliers")
            cursor.close()
            return "Records deleted"
    except Exception as inst:
        return inst


# Drop the table
def drop_table():
    try:
        with connection.cursor() as cursor:
            cursor.execute("drop table Suppliers;")
            cursor.close()
        return tablename + ' table deleted successfully'

    except Exception as inst:
        return inst
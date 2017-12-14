from __future__ import  unicode_literals
from django.db import models,connection
from django.db import IntegrityError
from django.shortcuts import render_to_response

# CREATE models

tablename = "Product"
url = "../../product/selecttable/"
errormsg = None


# Crating the table
def create_table():
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "CREATE TABLE Products (ProductId int NOT NULL AUTO_INCREMENT,ProductName varchar(255) NOT NULL,ProductTypeId int NOT NULL,"
                "PRIMARY KEY (ProductId),CONSTRAINT FK_ProductProductType FOREIGN KEY (ProductTypeId) 	REFERENCES ProductTypes (ProductTypeId));")
            cursor.close()
        return tablename + ' table created successfully'

    except Exception as inst:
        return inst


# Insert some records into the table
def insert_table():
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO  Products (ProductName, ProductTypeId) VALUES ('Apple', '1'),('Carrot', '2');")
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
            cursor.execute("Select * FROM Products")
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
            cursor.execute("DELETE FROM Products")
            cursor.close()
            return "Records deleted"
    except Exception as inst:
        return inst


# Drop the table
def drop_table():
    try:
        with connection.cursor() as cursor:
            cursor.execute("drop table Products;")
            cursor.close()
        return tablename + ' table deleted successfully'

    except Exception as inst:
        return inst
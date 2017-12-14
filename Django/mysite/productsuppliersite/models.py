from __future__ import  unicode_literals
from django.db import models,connection
from django.db import IntegrityError
from django.shortcuts import render_to_response

# CREATE models

tablename = "ProductSupplier"
url = "../../productsupplier/selecttable/"
errormsg = None


# Crating the table
def create_table():
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "CREATE TABLE ProductSuppliers (ProductSupplierId int NOT NULL AUTO_INCREMENT,ProductId int NOT NULL,SupplierId int NOT NULL,PRIMARY KEY (ProductSupplierId),"
                "CONSTRAINT FK_ProductSupplier FOREIGN KEY (SupplierId)    REFERENCES Suppliers (SupplierId) ,    CONSTRAINT FK_ProductSupplierProduct FOREIGN KEY (ProductId)    REFERENCES Products (ProductId) );")
            cursor.close()
        return tablename + ' table created successfully'

    except Exception as inst:
        return inst


# Insert some records into the table
def insert_table():
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO ProductSuppliers (`ProductId`, `SupplierId`) VALUES ('1', '1'),('2', '1'),('1', '2');")
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
            cursor.execute("Select * FROM ProductSuppliers")
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
            cursor.execute("DELETE FROM ProductSuppliers")
            cursor.close()
            return "Records deleted"
    except Exception as inst:
        return inst


# Drop the table
def drop_table():
    try:
        with connection.cursor() as cursor:
            cursor.execute("drop table ProductSuppliers;")
            cursor.close()
        return tablename + ' table deleted successfully'

    except Exception as inst:
        return inst
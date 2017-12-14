from __future__ import  unicode_literals
from django.db import models,connection
from django.db import IntegrityError
from django.shortcuts import render_to_response

# CREATE models

tablename = "Orderdetail"
url = "../../orderdetail/selecttable/"
errormsg = None


# Crating the table
def create_table():
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "CREATE TABLE OrderDetails ( OrderDetailId int NOT NULL AUTO_INCREMENT, OrderId int NOT NULL,ProductSupplierId int NOT NULL,Quantity int NOT NULL, UnitPrice double NOT NULL,"
                "PRIMARY KEY (OrderDetailId),FOREIGN KEY (OrderId) REFERENCES Orders (OrderId) , FOREIGN KEY (ProductSupplierId) REFERENCES ProductSuppliers(ProductSupplierId));")
            cursor.close()
        return tablename + ' table created successfully'

    except Exception as inst:
        return inst


# Insert some records into the table
def insert_table():
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO OrderDetails (`OrderId`, `ProductSupplierId`, `Quantity`, `UnitPrice`) VALUES ('1', '1', '2', '50.5'),('1', '2', '4', '75'),('1', '3', '6', '25'),('2', '3', '2', '358'),('3', '3', '3', '77.8'),('3', '1', '5', '50');")
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
            cursor.execute("Select * FROM OrderDetails  ")
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
            cursor.execute("DELETE FROM OrderDetails  ")
            cursor.close()
            return "Records deleted"
    except Exception as inst:
        return inst


# Drop the table
def drop_table():
    try:
        with connection.cursor() as cursor:
            cursor.execute("drop table OrderDetails  ;")
            cursor.close()
        return tablename + ' table deleted successfully'

    except Exception as inst:
        return inst
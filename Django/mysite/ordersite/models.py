from __future__ import  unicode_literals
from django.db import models,connection
from django.db import IntegrityError
from django.shortcuts import render_to_response
import datetime

# CREATE models

tablename = "Order"
url = "../../order/selecttable/"
errormsg = None


# Crating the table
def create_table():
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "CREATE TABLE Orders (`OrderId` int(11) NOT NULL AUTO_INCREMENT,`OrderNumber` int(11) NOT NULL,`CustomerId` int(11) NOT NULL,`TotalPrice` double NOT NULL,`OrderDate` date NOT NULL,"
                "PRIMARY KEY (`OrderId`),  KEY `CustomerId` (`CustomerId`));")
            cursor.close()
        return tablename + ' table created successfully'

    except Exception as inst:
        return inst


# Insert some records into the table
def insert_table():
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO Orders ( OrderNumber, CustomerId , TotalPrice, OrderDate) VALUES ( 3427, 1,150.50, ' " + datetime.datetime.today().strftime('%Y-%m-%d') + "'),"
                                        "( 3428, 2,358, ' " + datetime.datetime.today().strftime('%Y-%m-%d') + "'),"
                                        "( 3429,  1,127.8,' " + datetime.datetime.today().strftime('%Y-%m-%d') + "'),"
                                        "( 3430,  1,127.8,' " + datetime.datetime.today().strftime('%Y-%m-%d') + "');")
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
            cursor.execute("Select * FROM Orders ")
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
            cursor.execute("DELETE FROM Orders ")
            cursor.close()
            return "Records deleted"
    except Exception as inst:
        return inst


# Drop the table
def drop_table():
    try:
        with connection.cursor() as cursor:
            cursor.execute("drop table Orders ;")
            cursor.close()
        return tablename + ' table deleted successfully'

    except Exception as inst:
        return inst

# Get data from table
def selectOrdersByNumber(ordernumber):
    try:
        global errormsg
        errormsg = None
        with connection.cursor() as cursor:
            cursor.execute("SELECT o.OrderNumber , count(od.UnitPrice) as ProductCount 	FROM OrderDetails od , Orders o WHERE o.OrderId = od.OrderId 	GROUP BY o.OrderId 	HAVING o.OrderNumber >  " + ordernumber )
            rows = cursor.fetchall()
            cursor.close()

            if len(rows) == 0:
                errormsg = "No records found"

        return rows

    except Exception as inst:
        errormsg = inst
        return None
from __future__ import  unicode_literals
from django.db import models,connection
from django.db import IntegrityError
from django.shortcuts import render_to_response

# CREATE models

tablename = "Multiple tables"
url = ""
errormsg = None

# Get data from user count stored procedure
def call_UserCount():
    try:
        global errormsg
        errormsg = None
        with connection.cursor() as cursor:
            cursor.execute("call userCount;")
            rows = cursor.fetchall()
            cursor.close()

            if len(rows) == 0:
                errormsg = "No records found"

        return rows

    except Exception as inst:
        errormsg = inst
        return None

# returns the employeelist
def call_EmployeeDetails():
    try:
        global errormsg
        errormsg = None
        with connection.cursor() as cursor:
            cursor.execute("call getEmployeesDetailsProc;")
            rows = cursor.fetchall()
            cursor.close()

            if len(rows) == 0:
                errormsg = "No records found"

        return rows

    except Exception as inst:
        errormsg = inst
        return None

# Returns the supplier list
def call_SupplierDetails():
    try:
        global errormsg
        errormsg = None
        with connection.cursor() as cursor:
            cursor.execute("call SupplierList;")
            rows = cursor.fetchall()
            cursor.close()

            if len(rows) == 0:
                errormsg = "No records found"

        return rows

    except Exception as inst:
        errormsg = inst
        return None

# Returns the Buying patterns
def call_BuyingPattern():
    try:
        global errormsg
        errormsg = None
        with connection.cursor() as cursor:
            cursor.execute("call BuyingPattern;")
            rows = cursor.fetchall()
            cursor.close()

            if len(rows) == 0:
                errormsg = "No records found"

        return rows

    except Exception as inst:
        errormsg = inst
        return None

# Returns the product list
def call_ProductDetails():
    try:
        global errormsg
        errormsg = None
        with connection.cursor() as cursor:
            cursor.execute("call ProductList;")
            rows = cursor.fetchall()
            cursor.close()

            if len(rows) == 0:
                errormsg = "No records found"

        return rows

    except Exception as inst:
        errormsg = inst
        return None

# get current day order details
def get_CurrentDayOrder():
    try:
        global errormsg
        errormsg = None
        with connection.cursor() as cursor:
            cursor.execute("select * FROM  CurrentDayOrders;")
            rows = cursor.fetchall()
            cursor.close()

            if len(rows) == 0:
                errormsg = "No records found"

        return rows

    except Exception as inst:
        errormsg = inst
        return None

def get_NumberofProducts():
    try:
        global errormsg
        errormsg = None
        with connection.cursor() as cursor:
            cursor.execute(" select  getNumberOfProducts(3);")
            rows = cursor.fetchall()
            cursor.close()

            if len(rows) == 0:
                errormsg = "No records found"

        return rows

    except Exception as inst:
        errormsg = inst
        return None


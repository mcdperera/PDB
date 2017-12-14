from __future__ import  unicode_literals
from django.db import models,connection
from django.db import IntegrityError
from django.shortcuts import render_to_response

# CREATE models

tablename = "User Titles"
url = "../../usertitle/selectTable/"
errormsg = None

# Create a table using stored procedure
def call_CreateTable():
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "call createUserTitleProc;")
            cursor.close()
        return tablename + ' table created successfully'

    except Exception as inst:
        return inst

# added a column to an existing table using stored procedure
def call_AddColumnToExistingTable():
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "call  addColumnUserTitleProc;")
            cursor.close()
        return ' Added column to ' + tablename + ' successfully'

    except Exception as inst:
        return inst

# added a column to an existing table using stored procedure
def drop_ColumnInExistingTable():
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "call dropColumnUserTitleProc;")
            cursor.close()
        return ' Added column to ' + tablename + ' successfully'

    except Exception as inst:
        return inst

# added a column to an existing table using stored procedure
def delete_ExistingTable():
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "call deleteUserTitleProc;")
            cursor.close()
        return ' Deleted column to ' + tablename + ' successfully'

    except Exception as inst:
        return inst

# Insert some records into the table
def insert_table():
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO UserTitles (UserTitleName, Deacription) VALUES"
                "('Mr', 'Refer to a man without a higher or honorific'),"
                "('Mrs', 'Refer to a married woman,'),"
                "('Ms', 'Refer  woman regardless of her marital status')")
            cursor.execute(
                "UPDATE Users SET UserTitleId =1")
            cursor.close()
        return 'Data inserted to ' + tablename + ' successfully'

    except Exception as inst:
        return inst

# Get data from table
def select_table():
    try:
        global errormsg
        errormsg = None
        with connection.cursor() as cursor:
            cursor.execute("Select * FROM UserTitles")
            rows = cursor.fetchall()
            cursor.close()

            if len(rows) == 0:
                errormsg = "No records found"

        return rows

    except Exception as inst:
        errormsg = inst
        return None
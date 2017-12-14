from __future__ import  unicode_literals
from django.db import models,connection
from django.db import IntegrityError
from django.shortcuts import render_to_response

# CREATE models

tablename = "Users"
url = "../../user/selecttable/"
errormsg = None


# Crating the table
def create_table():
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "CREATE TABLE Users (    UserId int NOT NULL AUTO_INCREMENT,    LastName varchar(255) NOT NULL,    FirstName varchar(255),    Email varchar(255),"
                "Username  varchar(255) NOT NULL,    Password varchar(255) NOT NULL,    Address varchar(255) ,    UserTypeId int NOT NULL,    PRIMARY KEY (UserId),    FOREIGN KEY (UserTypeId) REFERENCES UserTypes(UserTypeId));")
            cursor.close()
        return tablename + ' table created successfully'

    except Exception as inst:
        return inst


# Insert some records into the table
def insert_table():
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO Users (LastName, FirstName, Email, Username, Password, Address, UserTypeId) VALUES"
                "('Maryann', 'Justa', 'Justa@gmail.com', 'Justa', '123', '3483 N. Hefner St. #61 Toledo FL ', '2'),"
                "('Maire', 'Francesco', 'Francesco@gmail.com', 'Francesco', '123', ' 2806 W. Pine Blvd.  Harrisburg AL', '1'),"
                "('Marva', 'Kizzie', 'Kizzie@gmail.com', 'Kizzie', '321', '1850 E. Rockwell Way #96 Tulsa OK', '3'),"
                "('Lily', 'Susan', 'Susan@gmail.com', 'Susan', '123', '13222 W. Regina Way #33 Providence SC', '2'),"
                "('Shawnda', 'Annis', ' Annis@gmail.com', 'Annis', '123', ' 5931 N. Pine Blvd. #72 Las Vegas AL', '1'),"
                "('Robbie', 'Rigoberto', 'Rigoberto@gmail.com', 'Rigoberto', '123', ' 13405 N. Regina Pl. Oklahoma City  CT', '3'),"
                "(' Elda', ' Roxanna', ' Roxanna@gmail.com', ' Roxanna', '123', ' 7013 W. Rockwell Blvd. #38 Little Rock MD', '3');")
            cursor.close()
        return 'data inserted to ' + tablename + ' sucessfully'

    except Exception as inst:
        return inst


# When the form data is insertted this method triggered.
def insert_tablewithparam(lastname , firstname ,email , username , password, address , usertypeid):
        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO Users (LastName, FirstName, Email, Username, Password, Address, UserTypeId) VALUES"
                    "('" + lastname + "','" + firstname + "','" + email + "','" + username + "','" + password + "','" + address + "','" + usertypeid + "');")
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
            cursor.execute("Select * FROM Users")
            rows = cursor.fetchall()
            cursor.close()

            if len(rows) == 0:
                errormsg = "No records found"

        return rows

    except Exception as inst:
        errormsg = inst
        return None

    # Get data from table
def userTypeReport(usertypeid):
    try:
        global errormsg
        errormsg = None
        with connection.cursor() as cursor:
            cursor.execute("Select * FROM Users WHERE UserTypeId = " + usertypeid )
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
            cursor.execute("DELETE FROM Users")
            cursor.close()
            return "Records deleted"
    except Exception as inst:
        return inst


# Drop the table
def drop_table():
    try:
        with connection.cursor() as cursor:
            cursor.execute("drop table Users;")
            cursor.close()
        return tablename + ' table deleted successfully'

    except Exception as inst:
        return inst
import psycopg2
"""
This is file is used for selecting the records
from the the mystaff.employess database

- selecting employees salary > 50000
- slecting first_name starts with richard
- selecting salry bt 50k to 55k
- selecting employess from sales and IT department

"""
# Connecting to the database
try:
    connection = psycopg2.connect(database="database1", user="postgres", password="admin@123", host="127.0.0.1",
                                  port="5432")

except psycopg2.Error as err:
    print("An error was generated while connecting to the database!")

else:
    print("Connection to database was successful!\n")

# Initializing the cursor
cursor = connection.cursor()
records = []

"""
#Fetching all the rows in a query result; returns a list
records = cursor.fetchall()

#Fetching the next 2 rows in a query result; returns a list
records = cursor.fetchmany(size = 2)

#Fetching the next row in a query result; returns a tuple; returns None
when no more records are available
records = cursor.fetchone()

"""

# Iterating over the records list and, for each inner list, extracting the data associated with each of the 7 columns
# in the table using indexes and inserting the data in the table using the INSERT command
try:
    cursor.execute("select * from mystaff.employees where salary > 58000;")
    records = cursor.fetchall()

    for record in records:
        print(record)


except psycopg2.Error as err:
    print("An error was generated while inserting the records! %s", err)

else:
    print("Successfully selected the records from database!\n")

try:
    print("Selecting last name starts with Richard")
    print()

    cursor.execute("select * from mystaff.employees where first_name like '%Richard%';")
    records = cursor.fetchall()

    for record in records:
        print(record)


except psycopg2.Error as err:
    print("An error was generated while inserting the records! %s", err)

else:
    print("Successfully selected the records from database!\n")


try:
    print("Selecting employees salary between 50k to 55k")
    print()

    cursor.execute("select * from mystaff.employees where salary between 50000 and 55000;")
    records = cursor.fetchall()

    for record in records:
        print(record)


except psycopg2.Error as err:
    print("An error was generated while inserting the records! %s", err)

else:
    print("Successfully selected the records from database!\n")

try:
    print("Selecting employees department of IT and SALES")
    print()

    cursor.execute("select * from mystaff.employees where department in ('Sales','IT');")
    records = cursor.fetchall()

    for record in records:
        print(record)


except psycopg2.Error as err:
    print("An error was generated while inserting the records! %s", err)

else:
    print("Successfully selected the records from database!\n")

"""
#Rolling back (undoing) the changes/transactions performed since the last
commit()
connection.rollback()

"""
# Committing (saving) the changes to the database
connection.commit()

# Closing the connection to the database
connection.close()

# End of Program

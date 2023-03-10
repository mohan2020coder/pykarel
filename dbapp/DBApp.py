import psycopg2

# Opening the text file for reading
f = open("employees.txt")

"""
create table employees
(id int primary key not null,
first_name varchar(25) not null,
last_name varchar(25) not null,
department varchar(25) not null,
phone varchar(25),
address varchar(25),
salary int);
"""


""""
already inserted into 
db emplyees use this format in employees.txt file

1/ Luke/ Phillip/ Sales/ 121921900/ 1st Address, Miami/ 52000
2/ Jack/ Darren/ IT/ 12918210/ 2nd Address, Miami/ 52200
3/ Ken/ Wood/ IT/ 20192101/ 3rd Address, Miami/ 58000
4/ John/ Wilson/ Marketing/ 31312311/ 4th Address, Miami/ 58700
5/ Emily/ Larson/ Marketing/ 43423434/ 5th Address, Miami/ 60000
6/ Anna/ Sullivan/ Sales/ 323232291/ 6th Address, Miami/ 54000
7/ Richard/ Smith/ Logistics/ 1277177910/ 7th Address, Miami/ 56000
8/ Ronnie/ Moore/ Sales/ 3691919186/ 8th Address, Miami/ 49000
9/ Benjamin/ Drake/ IT/ 215557299/ 9th Address, Miami/ 53000
10/ Wayne/ Barker/ Logistics/ 3266617791/ 10th Address, Miami/ 59500
"""

# Creating an empty list for storing the records as a lis of lists
records = []

# Splitting each line in the file by the "/ " delimiter and appending each list generated by readlines() to the new
# list, records
for i in f.readlines():
    records.append(i.split("/ "))

# print(records)

# Connecting to the database
try:
    connection = psycopg2.connect(database="database1", user="postgres", password="admin@123", host="127.0.0.1", port="5432")

except psycopg2.Error as err:
    print("An error was generated while connecting to the database!")

else:
    print("Connection to database was successful!\n")

# Initializing the cursor
cursor = connection.cursor()

# Iterating over the records list and, for each inner list, extracting the data associated with each of the 7 columns
# in the table using indexes and inserting the data in the table using the INSERT command
try:
    for i in records:
        cursor.execute(
            "insert into mystaff.employees (id,first_name,last_name,department,phone,address,salary) values (%s,%s,"
            "%s,%s,%s,%s,%s);",
            (i[0], i[1], i[2], i[3], i[4], i[5], i[6]))

except psycopg2.Error as err:
    print("An error was generated while inserting the records! %s", err)

else:
    print("Records inserted successfully!\n")

# Committing (saving) the changes to the database
connection.commit()

# Closing the connection to the database
connection.close()

# End of Program

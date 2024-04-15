import sqlite3

## Connect to sqlite
connection = sqlite3.connect("student.db")

## Create a cursor object to insert record, create table, retrieve
cursor=connection.cursor()

## create the table
table_info= """

Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25), GRADES INT)

"""
cursor.execute(table_info)

## Insert some more records
cursor.execute('''Insert Into STUDENT values ('Matthew', 'Data Science', 'A', 95)''')
cursor.execute('''Insert Into STUDENT values ('Tom', 'Data Science', 'B', 100)''')
cursor.execute('''Insert Into STUDENT values ('Sarah', 'Data Science', 'A', 86)''')
cursor.execute('''Insert Into STUDENT values ('Vincent', 'DEVOPS', 'A', 50)''')
cursor.execute('''Insert Into STUDENT values ('Jessica', 'DEVOPS', 'A', 35)''')

## Display all the records
print("The inserted records are")
data=cursor.execute('''Select * FROM STUDENT''')

for row in data:
    print(row)

## Close the connection
connection.commit()
connection.close()
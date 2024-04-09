import sqlite3

# conect to sqlite
connection = sqlite3.connect("student.db")

# create a cursor object to insert record ,create table
cursor = connection.cursor()

# create a table
table_info = """
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),SECTION VARCHAR(25),MARKS VARCHAR(25));
"""

cursor.execute(table_info)


# insert some more record
cursor.execute(
    '''Insert Into STUDENT values('krish','Data Science','A','76')''')
cursor.execute(
    '''Insert Into STUDENT values('shudansu','Data Science','A','87')''')
cursor.execute(
    '''Insert Into STUDENT values('vikas','Data Science','A','57')''')
cursor.execute('''Insert Into STUDENT values('param','DevOps','A','87')''')
cursor.execute('''Insert Into STUDENT values('manav','DevOps','A','87')''')
cursor.execute(
    '''Insert Into STUDENT values('prince','Data Science','A','67')''')
cursor.execute(
    '''Insert Into STUDENT values('karan','Data Science','A','86')''')
cursor.execute(
    '''Insert Into STUDENT values('girish','Data Science','A','95')''')
cursor.execute(
    '''Insert Into STUDENT values('rita','Data Science','A','79')''')
cursor.execute(
    '''Insert Into STUDENT values('khush','Data Science','A','76')''')
cursor.execute('''Insert Into STUDENT values('ansh','','A',DevOps'69')''')


# display all the records
print("The Inserted Records are")
data = cursor.execute('''select * from STUDENT''')
for row in data:
    print(row)

# commit your change in the database
connection.commit()
connection.close()

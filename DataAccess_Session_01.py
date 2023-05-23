'''
Reference:
https://learn.microsoft.com/en-us/sql/connect/python/pyodbc/step-3-proof-of-concept-connecting-to-sql-using-pyodbc?view=sql-server-ver16
https://hevodata.com/learn/python-sql-server-integration/
'''

import pyodbc
cnxn_str = ("Driver={SQL Server Native Client 11.0};"
            "Server=BHAVIN;"
            "Database=LearningDB;"
            "Trusted_Connection=yes;")
cnxn = pyodbc.connect(cnxn_str)
cursor  =cnxn.cursor()

cursor.execute("SELECT @@version;")
row = cursor.fetchone()
while row:
    print(row[0])
    row = cursor.fetchone()
# to insert a record
cnxn.execute("Insert into Student values (201,'Taru','Satellite','15-Dec-2000','1231231231')")
cnxn.commit()
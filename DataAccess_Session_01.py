import pyodbc
cnxn_str = ("Driver={SQL Server Native Client 11.0};"
            "Server=BHAVIN;"
            "Database=LearningDB;"
            "Trusted_Connection=yes;")
cnxn = pyodbc.connect(cnxn_str)

cnxn.cursor.execute("SELECT @@version;")
row = cnxn.cursor.fetchone()
while row:
    print(row[0])
    row = cnxn.cursor.fetchone()
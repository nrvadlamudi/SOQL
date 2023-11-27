# Using pyodbc to connect to SQL Server
import pyodbc

# Connect to SQL Server
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-NCA7QV0;'
                      'Database=AdventureWorks2022;'
                      'Trusted_Connection=yes;')

# Create a cursor
cursor = conn.cursor()

# Execute an obfuscated sql query
cursor.execute('s/**/e/**/l/**/e/**/c/**/t/**/ * /**/f/**/r/**/o/**/m/**/ HumanResources.Employee')

# Fetch the data
for row in cursor:
    print(row)

# Close the connection
conn.close()

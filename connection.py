# Using pyodbc to connect to SQL Server
import pyodbc

# Connect to SQL Server
conn = pyodbc.connect(
    "Driver={SQL Server};"
    "Server=NICK;"
    "Database=AdventureWorks2022;"
    "Trusted_Connection=yes;"
)

# Create a cursor
cursor = conn.cursor()

# Execute an obfuscated sql query
cursor.execute("SELECT * FROM Person.Person")

# Fetch the data
for row in cursor:
    print(row)

# Close the connection
conn.close()

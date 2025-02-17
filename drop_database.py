import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()

# Establish a connection to MySQL
conn = mysql.connector.connect(
    host="localhost",       # Your MySQL server
    user=os.getenv('user'),            # Your MySQL username
    password=os.getenv('password')     # Your MySQL password
)

# Create a cursor object using the connection
cursor = conn.cursor()

cursor.execute("SHOW DATABASES")
for db in cursor:
    print(db)

# Drop the database
cursor.execute("DROP DATABASE Database1")

cursor.execute("SHOW DATABASES")
for db in cursor:
    print(db)

# Close the cursor and connection
cursor.close()
conn.close()

print("Database dropped successfully")
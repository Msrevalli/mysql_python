import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user=os.getenv('user'),      # Change if you have a different user
    password=os.getenv('password'),  # Replace with your MySQL password
    
)

# Create a cursor object
cursor = conn.cursor()

# Print success message
print("Connected to MySQL!")

cursor.execute("CREATE DATABASE IF NOT EXISTS Database1")

# Close the cursor and connection
cursor.close()
conn.close()

print("Database1 created successfully")
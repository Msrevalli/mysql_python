import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user=os.getenv('user'),      # Change if you have a different user
    password=os.getenv('password'),  # Replace with your MySQL password
    database="testdb"  # Replace with your database name
)

# Create a cursor object
cursor = conn.cursor()

# Print success message
print("Connected to MySQL!")

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    age INT
)
""")

print("Table created successfully!")

query = "INSERT INTO users (name, age) VALUES (%s, %s)"
values = ("Alice", 25)

cursor.execute(query, values)
conn.commit()  # Save changes

print("Data inserted successfully!")

cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
conn.close()
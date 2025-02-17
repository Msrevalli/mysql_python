import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()

# Establish a connection to MySQL
conn = mysql.connector.connect(
    host="localhost",       # Your MySQL server
    user=os.getenv('user'),            # Your MySQL username
    password=os.getenv("password"),    # Your MySQL password
    database="Database1"   # The database where the table will be created
)



# Create a cursor object
cursor = conn.cursor()

# Step 1: Create a Table
create_table_query = """
CREATE TABLE IF NOT EXISTS employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT DEFAULT NULL,
    department VARCHAR(100),
    salary DECIMAL(10,2) DEFAULT NULL
)
"""
cursor.execute(create_table_query)
conn.commit()

print("Table 'employees' created successfully.")

# Step 1: Create a table
create_table_query = """
CREATE TABLE IF NOT EXISTS employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    department VARCHAR(100)
)
"""
cursor.execute(create_table_query)

# Step 2: Insert data into the table
insert_data_query = """
INSERT INTO employees (name, age, department) 
VALUES (%s, %s, %s)
"""
data = [
    ("John Doe", 30, "HR"),
    ("Jane Smith", 25, "Finance"),
    ("Emily Johnson", 35, "IT")
]

cursor.executemany(insert_data_query, data)

# Commit the changes to the database
conn.commit()

# Step 3: Verify data insertion
cursor.execute("SELECT * FROM employees")
result = cursor.fetchall()
for row in result:
    print(row)

# Step 4: Drop the table
cursor.execute("DROP TABLE employees")

# Commit the changes to the database
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()

print("Table created, data inserted, and table dropped successfully")
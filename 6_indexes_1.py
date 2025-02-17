import mysql.connector
import os
from dotenv import load_dotenv
import time

# Load environment variables (if using .env file)
load_dotenv()

# Establish connection to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user=os.getenv("MYSQL_USER"),  # Replace with your MySQL username
    password=os.getenv("MYSQL_PASSWORD"),  # Replace with your MySQL password
    database="test_db"
)
cursor = conn.cursor()

# Step 1: Create Table with Indexes
create_table_query = """
CREATE TABLE IF NOT EXISTS employees (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- Primary Key (Auto-indexed)
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE,          -- Unique Index
    age INT,
    department VARCHAR(100),
    salary DECIMAL(10,2)
)
"""
cursor.execute(create_table_query)
print("✅ Table 'employees' created successfully.")

# Step 2: Insert Sample Data
insert_query = """
INSERT INTO employees (name, email, age, department, salary)
VALUES (%s, %s, %s, %s, %s)
"""
data = [
    ("Alice Johnson", "alice@example.com", 30, "IT", 60000),
    ("Bob Smith", "bob@example.com", 40, "HR", 55000),
    ("Charlie Brown", "charlie@example.com", 35, "Finance", 75000),
    ("David White", "david@example.com", 28, "Marketing", 48000)
]

cursor.executemany(insert_query, data)
conn.commit()
print("✅ Sample data inserted.")

# Step 3: Create Index on 'department' Column
create_index_query = "CREATE INDEX idx_department ON employees(department)"
cursor.execute(create_index_query)
print("✅ Index 'idx_department' created on department column.")

# Step 4: Measure Query Performance Before and After Index
search_query = "SELECT * FROM employees WHERE department = 'IT'"

# Without Index
cursor.execute("DROP INDEX idx_department ON employees")  # Remove Index
conn.commit()
start_time = time.time()
cursor.execute(search_query)
result = cursor.fetchall()
end_time = time.time()
print(f"⏳ Query without index took: {end_time - start_time:.5f} seconds")

# With Index
cursor.execute(create_index_query)  # Re-create Index
conn.commit()
start_time = time.time()
cursor.execute(search_query)
result = cursor.fetchall()
end_time = time.time()
print(f"🚀 Query with index took: {end_time - start_time:.5f} seconds")

# Step 5: Drop Index
drop_index_query = "DROP INDEX idx_department ON employees"
cursor.execute(drop_index_query)
conn.commit()
print("✅ Index 'idx_department' dropped.")

# Close the connection
cursor.close()
conn.close()

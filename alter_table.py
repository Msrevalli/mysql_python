import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Establish a connection to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user=os.getenv("user"),  # Corrected environment variable names
    password=os.getenv("password"),
    database="Database1"
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
print("✅ Table 'employees' created successfully.")

# Step 2: Insert Data with NULL Values
insert_null_query = """
INSERT INTO employees (name, age, department, salary) 
VALUES (%s, %s, %s, %s)
"""
data_with_null = [
    ("Alice Green", None, "Marketing", 55000.00),  # Age is NULL
    ("Bob Brown", 28, None, 62000.00)  # Department is NULL
]

cursor.executemany(insert_null_query, data_with_null)
conn.commit()
print("✅ Data with NULL values inserted.")

# Verify the results
cursor.execute("SELECT * FROM employees")
print("🔹 Employees Data After Insert:")
for row in cursor.fetchall():
    print(row)

# Step 3: UPDATE Statement (Changing department)
update_query = """
UPDATE employees 
SET department = %s 
WHERE name = %s
"""
cursor.execute(update_query, ("Sales", "Alice Green"))
conn.commit()
print("✅ Updated Alice Green’s department to 'Sales'.")

# Verify the results
cursor.execute("SELECT * FROM employees")
print("🔹 Employees Data After Update:")
for row in cursor.fetchall():
    print(row)

# Step 4: DELETE Statement (Deleting an employee)
delete_query = """
DELETE FROM employees 
WHERE name = %s
"""
cursor.execute(delete_query, ("Bob Brown",))
conn.commit()
print("✅ Deleted Bob Brown from employees.")
for row in cursor.fetchall():
    print(row)

# Verify the results
cursor.execute("SELECT * FROM employees")
print("🔹 Employees Data After Delete:")
for row in cursor.fetchall():
    print(row)

# Step 5: ALTER TABLE - Add a New Column
alter_add_column_query = """
ALTER TABLE employees 
ADD COLUMN email VARCHAR(255) DEFAULT NULL
"""
cursor.execute(alter_add_column_query)
conn.commit()
print("✅ Added 'email' column to employees table.")
for row in cursor.fetchall():
    print(row)

# Step 6: ALTER TABLE - Modify Existing Column (Change 'salary' to NOT NULL)
alter_modify_column_query = """
ALTER TABLE employees 
MODIFY COLUMN salary DECIMAL(10,2) NOT NULL
"""
cursor.execute(alter_modify_column_query)
conn.commit()
print("✅ Modified 'salary' column to NOT NULL.")
for row in cursor.fetchall():
    print(row)

# Step 7: ALTER TABLE - Drop Column
alter_drop_column_query = """
ALTER TABLE employees 
DROP COLUMN email
"""
cursor.execute(alter_drop_column_query)
conn.commit()
print("✅ Dropped 'email' column from employees table.")
for row in cursor.fetchall():
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()
print("🔚 Database connection closed.")

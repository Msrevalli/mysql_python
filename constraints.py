import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables (if using .env file)
load_dotenv()

# Establish a connection to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user=os.getenv("MYSQL_USER"),  # Replace with your MySQL username
    password=os.getenv("MYSQL_PASSWORD"),  # Replace with your MySQL password
    database="test_db"
)

# Create a cursor object
cursor = conn.cursor()

# Step 1: Create Table with All Constraints
create_table_query = """
CREATE TABLE IF NOT EXISTS employees (
    id INT AUTO_INCREMENT PRIMARY KEY,   -- PRIMARY KEY Constraint
    name VARCHAR(100) NOT NULL,          -- NOT NULL Constraint
    email VARCHAR(255) UNIQUE,           -- UNIQUE Constraint
    age INT CHECK (age >= 18),           -- CHECK Constraint (MySQL 8+)
    department VARCHAR(100) DEFAULT 'General', -- DEFAULT Constraint
    salary DECIMAL(10,2) NOT NULL CHECK (salary > 30000), -- CHECK + NOT NULL
    manager_id INT,
    FOREIGN KEY (manager_id) REFERENCES employees(id) -- FOREIGN KEY Constraint
)
"""
cursor.execute(create_table_query)
conn.commit()
print("✅ Table 'employees' created successfully.")

# Step 2: Insert Valid Data
insert_valid_query = """
INSERT INTO employees (name, email, age, department, salary, manager_id)
VALUES (%s, %s, %s, %s, %s, %s)
"""
valid_data = [
    ("John Doe", "john@example.com", 30, "IT", 50000, None),
    ("Jane Smith", "jane@example.com", 28, "HR", 60000, 1)  # Refers to John as manager
]

cursor.executemany(insert_valid_query, valid_data)
conn.commit()
print("✅ Valid data inserted successfully.")

# Step 3: Insert Invalid Data (To Test Constraints)
try:
    # 1. Violating NOT NULL (Name is NULL)
    cursor.execute("INSERT INTO employees (name, email, age, department, salary, manager_id) VALUES (%s, %s, %s, %s, %s, %s)", 
                   (None, "invalid@example.com", 25, "Marketing", 50000, None))
    conn.commit()
except mysql.connector.Error as err:
    print(f"❌ NOT NULL Constraint Violation: {err}")

try:
    # 2. Violating UNIQUE (Duplicate email)
    cursor.execute("INSERT INTO employees (name, email, age, department, salary, manager_id) VALUES (%s, %s, %s, %s, %s, %s)", 
                   ("Alice Brown", "john@example.com", 29, "Finance", 55000, None))
    conn.commit()
except mysql.connector.Error as err:
    print(f"❌ UNIQUE Constraint Violation: {err}")

try:
    # 3. Violating CHECK (Age < 18)
    cursor.execute("INSERT INTO employees (name, email, age, department, salary, manager_id) VALUES (%s, %s, %s, %s, %s, %s)", 
                   ("Bob Young", "bob@example.com", 17, "IT", 60000, None))
    conn.commit()
except mysql.connector.Error as err:
    print(f"❌ CHECK Constraint Violation (Age < 18): {err}")

try:
    # 4. Violating CHECK (Salary < 30,000)
    cursor.execute("INSERT INTO employees (name, email, age, department, salary, manager_id) VALUES (%s, %s, %s, %s, %s, %s)", 
                   ("Charlie Green", "charlie@example.com", 26, "IT", 20000, None))
    conn.commit()
except mysql.connector.Error as err:
    print(f"❌ CHECK Constraint Violation (Salary < 30,000): {err}")

try:
    # 5. Violating FOREIGN KEY (Non-existing Manager ID)
    cursor.execute("INSERT INTO employees (name, email, age, department, salary, manager_id) VALUES (%s, %s, %s, %s, %s, %s)", 
                   ("David White", "david@example.com", 32, "Sales", 70000, 999))  # No manager with ID 999
    conn.commit()
except mysql.connector.Error as err:
    print(f"❌ FOREIGN KEY Constraint Violation: {err}")

# Step 4: Fetch and Display Data
cursor.execute("SELECT * FROM employees")
employees = cursor.fetchall()
print("\n✅ Employees Table Data:")
for emp in employees:
    print(emp)

# Close Connection
cursor.close()
conn.close()
print("✅ Database connection closed.")

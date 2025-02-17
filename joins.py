import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Establish a connection to MySQL
conn = mysql.connector.connect(
    host="localhost",       # Your MySQL server
    user=os.getenv("MYSQL_USER"),  # MySQL username from .env
    password=os.getenv("MYSQL_PASSWORD"),  # MySQL password from .env
    database="Database1"    # The database you're using
)

# Create a cursor object using the connection
cursor = conn.cursor()

# 1. Create Sample Tables (if not already created)
create_employee_table = """
CREATE TABLE IF NOT EXISTS employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    department VARCHAR(100)
)
"""
create_sales_table = """
CREATE TABLE IF NOT EXISTS sales (
    employee_id INT,
    sales_amount DECIMAL(10, 2),
    FOREIGN KEY (employee_id) REFERENCES employees(id)
)
"""
cursor.execute(create_employee_table)
cursor.execute(create_sales_table)

# 2. Insert Sample Data into Tables
insert_employee_data = """
INSERT INTO employees (name, department) VALUES (%s, %s)
"""
employee_data = [
    ("John Doe", "Sales"),
    ("Jane Smith", "Marketing"),
    ("Emily Johnson", "Sales"),
    ("Michael Brown", "Marketing"),
    ("Sarah White", "HR")
]
cursor.executemany(insert_employee_data, employee_data)

insert_sales_data = """
INSERT INTO sales (employee_id, sales_amount) VALUES (%s, %s)
"""
sales_data = [
    (1, 1500.50),  # John Doe's sales
    (2, 3000.00),  # Jane Smith's sales
    (3, 1200.75)   # Emily Johnson's sales
]
cursor.executemany(insert_sales_data, sales_data)

# Commit the changes
conn.commit()

# Display the tables
print("Employees Table:")
cursor.execute("SELECT * FROM employees")
result = cursor.fetchall()
for row in result:
    print(row)

print("\nSales Table:")
cursor.execute("SELECT * FROM sales")
result = cursor.fetchall()
for row in result:
    print(row)

# 3. INNER JOIN - Fetching employees with their sales
print("INNER JOIN Result (Employees with Sales):")
cursor.execute("""
    SELECT employees.name, employees.department, sales.sales_amount
    FROM employees
    INNER JOIN sales ON employees.id = sales.employee_id
""")
result = cursor.fetchall()
for row in result:
    print(row)

# 4. LEFT JOIN - Fetching all employees and their sales (including those without sales)
print("\nLEFT JOIN Result (All Employees with Sales, including those without sales):")
cursor.execute("""
    SELECT employees.name, employees.department, sales.sales_amount
    FROM employees
    LEFT JOIN sales ON employees.id = sales.employee_id
""")
result = cursor.fetchall()
for row in result:
    print(row)

# 5. RIGHT JOIN - Fetching all sales and the corresponding employees
print("\nRIGHT JOIN Result (All Sales with Corresponding Employees):")
cursor.execute("""
    SELECT employees.name, employees.department, sales.sales_amount
    FROM employees
    RIGHT JOIN sales ON employees.id = sales.employee_id
""")
result = cursor.fetchall()
for row in result:
    print(row)

# 6. CROSS JOIN - All possible combinations of employees and sales (use carefully)
print("\nCROSS JOIN Result (All combinations of Employees and Sales):")
cursor.execute("""
    SELECT employees.name, sales.sales_amount
    FROM employees
    CROSS JOIN sales
""")
result = cursor.fetchall()
for row in result:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()

print("Operations completed successfully.")

import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables
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

# 1. Create a Sample Table (if not already created)
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
    ("Emily Johnson", "Sales")
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

# 3. Create a View (Virtual Table)
create_view_query = """
CREATE VIEW employee_sales AS
SELECT employees.name, employees.department, SUM(sales.sales_amount) AS total_sales
FROM employees
JOIN sales ON employees.id = sales.employee_id
GROUP BY employees.name, employees.department;
"""
cursor.execute(create_view_query)
conn.commit()

print("View 'employee_sales' created successfully.")

# 4. Query the View
print("\nQuerying the 'employee_sales' view:")
cursor.execute("SELECT * FROM employee_sales")
result = cursor.fetchall()
for row in result:
    print(row)

# 5. Drop the View
cursor.execute("DROP VIEW IF EXISTS employee_sales")
conn.commit()

print("\nView 'employee_sales' dropped successfully.")

# Close the cursor and connection
cursor.close()
conn.close()

print("Operations completed successfully.")
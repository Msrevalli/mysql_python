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
    salary DECIMAL(10,2),
    description TEXT,                  -- For FULLTEXT index
    INDEX idx_age_salary (age, salary) -- Composite Index on 'age' and 'salary'
)
"""
cursor.execute(create_table_query)
print("✅ Table 'employees' created successfully.")

# Step 2: Insert Sample Data
insert_query = """
INSERT INTO employees (name, email, age, department, salary, description)
VALUES (%s, %s, %s, %s, %s, %s)
"""
data = [
    ("Alice Johnson", "alice@example.com", 30, "IT", 60000, "Alice is a software engineer."),
    ("Bob Smith", "bob@example.com", 40, "HR", 55000, "Bob manages HR operations."),
    ("Charlie Brown", "charlie@example.com", 35, "Finance", 75000, "Charlie is a financial analyst."),
    ("David White", "david@example.com", 28, "Marketing", 48000, "David leads the marketing team.")
]

cursor.executemany(insert_query, data)
conn.commit()
print("✅ Sample data inserted.")

# Step 3: Create FULLTEXT Index on 'description' column
create_fulltext_index_query = "CREATE FULLTEXT INDEX idx_fulltext_description ON employees(description)"
cursor.execute(create_fulltext_index_query)
print("✅ FULLTEXT Index 'idx_fulltext_description' created on 'description' column.")

# Step 4: Measure Query Performance Before and After Index
search_query = "SELECT * FROM employees WHERE description LIKE '%engineer%'"

# Without FULLTEXT Index
cursor.execute("DROP INDEX idx_fulltext_description ON employees")  # Remove FULLTEXT Index
conn.commit()
start_time = time.time()
cursor.execute(search_query)
result = cursor.fetchall()
end_time = time.time()
print(f"⏳ Query without FULLTEXT index took: {end_time - start_time:.5f} seconds")

# With FULLTEXT Index
cursor.execute(create_fulltext_index_query)  # Re-create FULLTEXT Index
conn.commit()
start_time = time.time()
cursor.execute(search_query)
result = cursor.fetchall()
end_time = time.time()
print(f"🚀 Query with FULLTEXT index took: {end_time - start_time:.5f} seconds")

# Step 5: Using COMPOSITE INDEX on 'age' and 'salary' columns
search_composite_query = "SELECT * FROM employees WHERE age > 30 AND salary > 50000"

# Using EXPLAIN ANALYZE to analyze performance of the query
explain_query = f"EXPLAIN ANALYZE {search_composite_query}"
cursor.execute(explain_query)
explain_result = cursor.fetchall()
print("📊 EXPLAIN ANALYZE output for the composite index query:")
for row in explain_result:
    print(row)

# Step 6: Drop Indexes
cursor.execute("DROP INDEX idx_fulltext_description ON employees")  # Drop FULLTEXT index
cursor.execute("DROP INDEX idx_age_salary ON employees")  # Drop Composite index
conn.commit()
print("✅ Indexes dropped.")

# Close the connection
cursor.close()
conn.close()

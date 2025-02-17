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

# 1. Creating a stored procedure that adds an employee's details
create_procedure_query = """
DELIMITER $$

CREATE PROCEDURE AddEmployee(IN emp_name VARCHAR(100), IN emp_department VARCHAR(100), IN emp_salary DECIMAL(10,2))
BEGIN
    INSERT INTO employees (name, department, salary) 
    VALUES (emp_name, emp_department, emp_salary);
END$$

DELIMITER ;
"""
cursor.execute(create_procedure_query)

print("Stored Procedure 'AddEmployee' created successfully.")

# Commit the changes
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()

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

# 3. Drop the old stored procedure (if it exists)
cursor.execute("DROP PROCEDURE IF EXISTS AddEmployee;")

# 4. Create a new version of the stored procedure with additional functionality
create_procedure_query = """
DELIMITER $$

CREATE PROCEDURE AddEmployee(IN emp_name VARCHAR(100), IN emp_department VARCHAR(100), IN emp_salary DECIMAL(10,2), IN emp_age INT)
BEGIN
    INSERT INTO employees (name, department, salary, age) 
    VALUES (emp_name, emp_department, emp_salary, emp_age);
END$$

DELIMITER ;
"""
cursor.execute(create_procedure_query)

print("Stored Procedure 'AddEmployee' modified successfully.")

# Commit the changes
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()

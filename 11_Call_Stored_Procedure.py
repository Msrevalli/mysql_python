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

try:
    # 1. Calling the stored procedure with parameters
    call_procedure_query = """
    CALL AddEmployee('Alice Green', 'HR', 4500.00);
    CALL AddEmployee('Bob Brown', 'IT', 5000.00);
    CALL AddEmployee('Charlie White', 'HR', 6000.00);
    """
    cursor.execute(call_procedure_query)

    # 2. Consume any remaining result sets (if the stored procedure returns any result)
    while cursor.nextset():
        pass  # This ensures all result sets are consumed

    # 3. Now, commit changes (if necessary)
    conn.commit()

    # 4. Verify that the employee was added
    cursor.execute("SELECT * FROM employees")
    result = cursor.fetchall()

    if result:
        print("Employee added:")
        for row in result:
            print(row)
    else:
        print("Employee not found.")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # 5. Close the cursor and connection
    cursor.close()
    conn.close()

### Creating Database

To create a MySQL database using Python, you can use the `mysql-connector` library. Here's a simple guide on how to do that:

### Step 1: Install MySQL Connector

If you haven't installed the MySQL connector yet, you can do so by running this command:

```bash
pip install mysql-connector-python
```

### Step 2: Create a Database

Once the connector is installed, you can use the following Python code to create a database in MySQL:

```python
import mysql.connector

# Establish a connection to MySQL
conn = mysql.connector.connect(
    host="localhost",       # Your MySQL server
    user="root",            # Your MySQL username
    password="password"     # Your MySQL password
)

# Create a cursor object using the connection
cursor = conn.cursor()

# Create a new database
cursor.execute("CREATE DATABASE mydatabase")

# Close the cursor and connection
cursor.close()
conn.close()

print("Database created successfully")
```

### Step 3: Verify the Database Creation

You can verify the database by logging into MySQL using:

```bash
mysql -u root -p
```

Then, run:

```sql
SHOW DATABASES;
```

This will show the list of databases, and you should see `mydatabase` in the list.

### Step 4: Use the New Database

After creating the database, you can start using it by switching to it:

```python
# Reconnect to the MySQL server
conn = mysql.connector.connect(
    host="localhost", 
    user="root", 
    password="password", 
    database="mydatabase"
)

cursor = conn.cursor()

# Your queries to create tables, etc.
cursor.close()
conn.close()
```
# To drop (delete) a MySQL database using Python, you can use the following steps:

### Step 1: Connect to MySQL Server

You'll need to connect to your MySQL server just like when you created a database.

### Step 2: Drop the Database

Here's the code to drop a MySQL database:

```python
import mysql.connector

# Establish a connection to MySQL
conn = mysql.connector.connect(
    host="localhost",       # Your MySQL server
    user="root",            # Your MySQL username
    password="password"     # Your MySQL password
)

# Create a cursor object using the connection
cursor = conn.cursor()

# Drop the database
cursor.execute("DROP DATABASE mydatabase")

# Close the cursor and connection
cursor.close()
conn.close()

print("Database dropped successfully")
```

### Important Notes:
1. **Be Careful:** Dropping a database will delete all the data in it. Make sure you have a backup if you need the data.
2. You can also check the list of databases before dropping one by running the following SQL command in Python:

```python
cursor.execute("SHOW DATABASES")
for db in cursor:
    print(db)
```

This will print out all the databases, and you can confirm the database you want to drop.

# Here’s a full Python script that demonstrates how to create a table, insert data into the table, and drop the table using MySQL:

### Step 1: Install MySQL Connector
If you haven’t installed the MySQL connector yet, you can do it using:

```bash
pip install mysql-connector-python
```

### Step 2: Python Code to Create Table, Insert Data, and Drop Table

```python
import mysql.connector

# Establish a connection to MySQL
conn = mysql.connector.connect(
    host="localhost",       # Your MySQL server
    user="root",            # Your MySQL username
    password="password",    # Your MySQL password
    database="mydatabase"   # The database where the table will be created
)

# Create a cursor object using the connection
cursor = conn.cursor()

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
```

### Explanation:
1. **Create Table:** The `CREATE TABLE` statement creates a table called `employees` with columns `id`, `name`, `age`, and `department`.
2. **Insert Data:** The `INSERT INTO` statement is used to insert multiple rows of data into the `employees` table.
3. **Verify Data:** The `SELECT * FROM employees` query retrieves all rows from the `employees` table, and the results are printed.
4. **Drop Table:** The `DROP TABLE` statement deletes the table from the database.

### Step 3: Verify the Results
When you run this script:
- It will create the `employees` table (if it doesn't exist).
- It will insert 3 rows of data.
- It will then drop the table, so make sure you don't need the table after running the script.

# Here’s a Python script using MySQL to demonstrate how to handle **NULL values**, perform **UPDATE** and **DELETE** operations, and use **ALTER TABLE** commands to modify the structure of an existing table.


```python
import mysql.connector

# Establish a connection to MySQL
conn = mysql.connector.connect(
    host="localhost",       # Your MySQL server
    user="root",            # Your MySQL username
    password="password",    # Your MySQL password
    database="mydatabase"   # The database you're using
)

# Create a cursor object using the connection
cursor = conn.cursor()

# 1. Handling NULL Values
# Inserting NULL values into the table (for example, in the "age" column)
insert_null_query = """
INSERT INTO employees (name, age, department) 
VALUES (%s, %s, %s)
"""
data_with_null = [
    ("Alice Green", None, "Marketing")  # Age is set to NULL
]

cursor.executemany(insert_null_query, data_with_null)
conn.commit()

# 2. UPDATE Statement
# Updating data in the table (for example, changing a person's department)
update_query = """
UPDATE employees 
SET department = %s 
WHERE name = %s
"""
cursor.execute(update_query, ("Sales", "John Doe"))
conn.commit()

# 3. DELETE Statement
# Deleting data from the table (for example, deleting an employee)
delete_query = """
DELETE FROM employees 
WHERE name = %s
"""
cursor.execute(delete_query, ("Alice Green",))
conn.commit()

# 4. ALTER TABLE - Add Column
# Adding a new column (for example, adding a "salary" column)
alter_add_column_query = """
ALTER TABLE employees 
ADD COLUMN salary DECIMAL(10, 2)
"""
cursor.execute(alter_add_column_query)
conn.commit()

# 5. ALTER TABLE - Modify/Alter Column
# Modifying a column (for example, changing the "age" column to allow larger values)
alter_modify_column_query = """
ALTER TABLE employees 
MODIFY COLUMN age INT(11)
"""
cursor.execute(alter_modify_column_query)
conn.commit()

# 6. ALTER TABLE - Drop Column
# Dropping a column (for example, removing the "salary" column)
alter_drop_column_query = """
ALTER TABLE employees 
DROP COLUMN salary
"""
cursor.execute(alter_drop_column_query)
conn.commit()

# Verify the results
cursor.execute("SELECT * FROM employees")
result = cursor.fetchall()
for row in result:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()

print("Operations completed successfully.")
```

### Explanation of Operations:

1. **Handling NULL Values:**
   - You can insert `NULL` values into a column by passing `None` in the `data_with_null` list. In this example, the "age" column has a `NULL` value for Alice Green.

2. **UPDATE Statement:**
   - The `UPDATE` statement changes an existing record in the table. In this case, the department of "John Doe" is changed to "Sales".

3. **DELETE Statement:**
   - The `DELETE` statement removes a record from the table. In this case, the employee "Alice Green" is deleted.

4. **ALTER TABLE - Add Column:**
   - The `ALTER TABLE ADD COLUMN` command is used to add a new column. In this case, we add a `salary` column to the `employees` table.

5. **ALTER TABLE - Modify/Alter Column:**
   - The `ALTER TABLE MODIFY COLUMN` command modifies an existing column. In this case, the `age` column is altered to allow larger integer values.

6. **ALTER TABLE - Drop Column:**
   - The `ALTER TABLE DROP COLUMN` command removes a column from the table. In this case, the `salary` column is dropped.

### Verification:
After performing these operations, the `SELECT * FROM employees` statement will retrieve the table's current data, showing any changes made.

### Notes:
- Always make sure you back up your data before performing destructive operations like `DELETE` or `DROP COLUMN`.
- Altering the column structure, such as modifying or dropping columns, will permanently affect the table.

### **SQL Constraints in MySQL**
SQL constraints ensure the integrity and accuracy of data in a database. Below are the **common SQL constraints** and how to use them in MySQL.

---

### **1. NOT NULL Constraint**
Ensures that a column cannot store `NULL` values.

```sql
CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,  -- Name cannot be NULL
    age INT NOT NULL,            -- Age cannot be NULL
    department VARCHAR(100)
);
```

---

### **2. UNIQUE Constraint**
Ensures that all values in a column are **unique**.

```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) UNIQUE,  -- Each email must be unique
    username VARCHAR(100) UNIQUE
);
```

---

### **3. PRIMARY KEY Constraint**
- Ensures each row has a **unique identifier**.
- **Combines** `UNIQUE` and `NOT NULL` constraints.

```sql
CREATE TABLE students (
    student_id INT AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    PRIMARY KEY (student_id)  -- student_id is unique & cannot be NULL
);
```

---

### **4. FOREIGN KEY Constraint**
Ensures **referential integrity** between two tables.

```sql
CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    FOREIGN KEY (customer_id) REFERENCES customers(id)  -- References another table
);
```

---

### **5. CHECK Constraint**  
Ensures values in a column meet **a specific condition**.

```sql
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT CHECK (age >= 18)  -- Age must be at least 18
);
```
> 🛑 **Note:** `CHECK` is supported in MySQL 8.0+.

---

### **6. DEFAULT Constraint**
Assigns a **default value** to a column when no value is specified.

```sql
CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    status VARCHAR(20) DEFAULT 'Available'  -- Default value is 'Available'
);
```

---

### **7. AUTO_INCREMENT Constraint**
Automatically increases the column value **by 1** for each new row.

```sql
CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);
```

---

### **8. COMPOSITE PRIMARY KEY**  
A **primary key on multiple columns**.

```sql
CREATE TABLE enrollments (
    student_id INT,
    course_id INT,
    PRIMARY KEY (student_id, course_id)  -- Composite key
);
```

---

### **Example: Applying Multiple Constraints**
```sql
CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    age INT CHECK (age >= 18),
    department VARCHAR(100) DEFAULT 'General',
    salary DECIMAL(10,2) NOT NULL
);
```

---

### **Summary Table**
| Constraint      | Description |
|---------------|-------------|
| `NOT NULL` | Ensures a column **cannot be NULL** |
| `UNIQUE` | Ensures **unique values** in a column |
| `PRIMARY KEY` | A unique **identifier** for each row |
| `FOREIGN KEY` | Links two tables to maintain **referential integrity** |
| `CHECK` | Restricts values based on a **condition** (MySQL 8.0+) |
| `DEFAULT` | Assigns a **default value** if none is provided |
| `AUTO_INCREMENT` | Automatically **increments** a column value |
| `COMPOSITE KEY` | A primary key using **multiple columns** |


### **🔹 MySQL Indexes with Python – Full Script and Explanation**
This Python script demonstrates **MySQL indexes** using `mysql-connector-python`. It includes:  

✅ **Creating a database and table with indexes**  
✅ **Inserting sample data**  
✅ **Creating and dropping indexes dynamically**  
✅ **Checking performance with and without indexes**  

---

## **🔹 Step-by-Step Explanation**
### **1️⃣ What are MySQL Indexes?**
Indexes **speed up database queries** by allowing MySQL to find data more efficiently. They are like a book’s **table of contents**—helping locate data without scanning the entire table.

| Index Type       | Description |
|-----------------|-------------|
| **PRIMARY KEY** | Auto-indexed unique identifier for rows. |
| **UNIQUE** | Ensures all values in a column are distinct. |
| **INDEX (Normal Index)** | Speeds up searches on non-unique columns. |
| **FULLTEXT** | Optimizes text-based searches (`MATCH()` & `AGAINST()`). |
| **COMPOSITE INDEX** | Index on multiple columns for better performance. |

---

## **🔹 2️⃣ Full Python Script**
```python
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
```

-### **🚀 Conclusion**
✅ **Indexes improve query speed significantly**  
✅ **Using the right indexes reduces database load**  
✅ **Indexes should be used wisely (avoid over-indexing)**  




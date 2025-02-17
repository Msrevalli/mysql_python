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



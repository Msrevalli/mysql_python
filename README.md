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

Let me know if you need any further help!
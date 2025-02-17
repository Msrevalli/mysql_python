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



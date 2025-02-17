### **1️⃣ Install MySQL Connector**  
Before using MySQL with Python, install the MySQL connector library:  
```bash
pip install mysql-connector-python
```

---

### **2️⃣ Connect Python to MySQL**
Use the **`mysql.connector`** module to connect Python to MySQL:  

```python
import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",      # Change if you have a different user
    password="your_password",  # Replace with your MySQL password
    database="testdb"  # Replace with your database name
)

# Create a cursor object
cursor = conn.cursor()

# Print success message
print("Connected to MySQL!")
```
✅ **If no error appears, the connection is successful!**  

---

### **3️⃣ Creating a Table**
To create a table in Python, use:  
```python
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    age INT
)
""")

print("Table created successfully!")
```

---

### **4️⃣ Insert Data into MySQL**
```python
query = "INSERT INTO users (name, age) VALUES (%s, %s)"
values = ("Alice", 25)

cursor.execute(query, values)
conn.commit()  # Save changes

print("Data inserted successfully!")
```

---

### **5️⃣ Fetch Data from MySQL**
```python
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

for row in rows:
    print(row)
```

---

### **6️⃣ Close Connection**
Always close the connection after executing queries:
```python
cursor.close()
conn.close()
```

---

### **🔹 Summary of Basic MySQL Operations in Python**
| **Operation** | **Python Code** |
|--------------|----------------|
| Connect to MySQL | `mysql.connector.connect()` |
| Create Table | `cursor.execute("CREATE TABLE ...")` |
| Insert Data | `cursor.execute("INSERT INTO ...")` |
| Fetch Data | `cursor.fetchall()` |
| Close Connection | `conn.close()` |

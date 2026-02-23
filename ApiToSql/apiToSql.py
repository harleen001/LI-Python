import requests
import pandas as pd
import mysql.connector
import sys

print("--- Step 1: Script started ---")

# 1. Get API Data
url = "https://jsonplaceholder.typicode.com/users"
try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    data = response.json()
    print("--- Step 2: API Data Received ---")
except Exception as e:
    print(f"❌ API Error: {e}")
    sys.exit()

# 2. Transform Data with Pandas
try:
    df = pd.json_normalize(data)  
    df = df[['id', 'name', 'username', 'email', 'address.city']]
    df.columns = ['user_id', 'full_name', 'username', 'email', 'city'] 
    print(f"--- Step 3: Data transformed ({len(df)} rows) ---")
except KeyError as e:
    print(f"❌ Data Transformation Error: Missing column {e}")
    sys.exit()

# 3. Connect to MySQL and Push Data
db = None # Initialize for the finally block
try:
    print("--- Step 4: Attempting DB Connection... ---")
    db = mysql.connector.connect(
        host="127.0.0.1",    # Changed from localhost to 127.0.0.1
        user="root",         
        password="123456",   # Ensure this is your actual password
        database="workspace", 
        connect_timeout=3    # Fails fast if DB is not running
    )
    cursor = db.cursor()
    print("--- Step 5: Connected to Database ---")

    # Optional: Create table automatically if it's missing
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users_table (
            user_id INT PRIMARY KEY,
            full_name VARCHAR(255),
            username VARCHAR(255),
            email VARCHAR(255),
            city VARCHAR(255)
        )
    """)

    # Prepare Upsert Query
    sql = """
    INSERT INTO users_table (user_id, full_name, username, email, city) 
    VALUES (%s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE 
        full_name = VALUES(full_name),
        username = VALUES(username),
        email = VALUES(email),
        city = VALUES(city)
    """

    # Execute batch update
    for _, row in df.iterrows():
        cursor.execute(sql, tuple(row))

    db.commit()
    print(f"--- Step 6: Processed {len(df)} records (Created/Updated) ---")

    # 4. Verification Print
    print("\n--- Current Data in 'users_table': ---")
    cursor.execute("SELECT * FROM users_table LIMIT 5")
    for row in cursor.fetchall():
        print(row)

except mysql.connector.Error as err:
    print("\n❌ DATABASE ERROR:")
    if err.errno == 2003:
        print("Error: Can't connect to MySQL server. Is XAMPP/MySQL running?")
    elif err.errno == 1049:
        print("Error: Database 'workspace' does not exist. Please create it in MySQL.")
    elif err.errno == 1045:
        print("Error: Wrong Username or Password.")
    else:
        print(f"Message: {err.msg}")

finally:
    if db and db.is_connected():
        cursor.close()
        db.close()
        print("\n--- Step 7: Connection closed safely ---")
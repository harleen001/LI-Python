import requests
import pandas as pd
import mysql.connector

# Get API Data
url = "https://jsonplaceholder.typicode.com/users"
try:
    response = requests.get(url)
    response.raise_for_status() # Check if the API call was successful
    data = response.json()
except Exception as e:
    print(f"API Error: {e}")
    exit()

# Convert to Dataset (DataFrame)
df = pd.json_normalize(data)  
df = df[['id', 'name', 'username', 'email', 'address.city']]   # it tells python that i only needs these specific columns from API 
df.columns = ['user_id', 'full_name', 'username', 'email', 'city']  #In this we r just renaming the columns 

# Connect to MySQL
try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",         
        password="123456", # Double check this is correct
        database="users"
    )
    cursor = db.cursor()

    # 4. Push data into the table
    sql = """
    INSERT INTO users_table (user_id, full_name, username, email, city) 
    VALUES (%s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE 
        full_name = VALUES(full_name),
        username = VALUES(username),
        email = VALUES(email),
        city = VALUES(city)
    """

    for _, row in df.iterrows():   #iteration on each row using iterrows and temporarily store in row
        cursor.execute(sql, tuple(row))  #row sent as tuple to sql

    db.commit()   # commit is ilike save command .If you forget this line, your data will disappear the moment the script ends!
    print(f"--- Processed {len(df)} records (Created/Updated) ---")

    # 5. Print the data to VS Code console to verify
    cursor.execute("SELECT * FROM users_table")
    result = cursor.fetchall()
    
    print("\nCurrent Data in 'users_table':")
    for x in result:
        print(x)

except mysql.connector.Error as err:
    print(f"Database Error: {err}")

finally:
    # 6. Clean up connections
    if 'db' in locals() and db.is_connected():
        cursor.close()
        db.close()
        print("\nMySQL connection closed.")
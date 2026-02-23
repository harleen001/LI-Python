import requests
import pandas as pd
import mysql.connector

# 1. Get API Data
url = "https://open.er-api.com/v6/latest/USD"
try:
    response = requests.get(url)
    response.raise_for_status()  # check that is this ok 
    data = response.json()
    rates_dict = data['rates'] 
except Exception as e:
    print(f"API Error: {e}")
    exit()
       
# 2. Convert to Dataset (DataFrame)
df = pd.DataFrame(rates_dict.items(), columns=['currency_code', 'rate_value'])
    
# 3. Connect to MySQL Server
try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",         
        password="123456"
    )
    cursor = db.cursor()
    
    # --- SILENT SETUP ---
    cursor.execute("CREATE DATABASE IF NOT EXISTS currency_tracker")
    cursor.execute("USE currency_tracker")
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS exchange_rates (
            currency_code VARCHAR(10) PRIMARY KEY,
            rate_value DECIMAL(15, 6),
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
        )
    """)
    
    # 4. Push data into the table (Upsert Logic)
    sql = """
    INSERT INTO exchange_rates (currency_code, rate_value) 
    VALUES (%s, %s)
    ON DUPLICATE KEY UPDATE 
        rate_value = VALUES(rate_value)
    """
    
    for _, row in df.iterrows():
        cursor.execute(sql, tuple(row))
    
    db.commit()
       
    # 5. FINAL CLEAN OUTPUT
    print(f"--- Success: {len(df)} Currency Rates Synced ---")
    print("-" * 55)
    print(f"{'CURRENCY':<12} | {'RATE (1 USD)':<15} | {'LAST UPDATED'}")
    print("-" * 55)
       
    # Fetch data to display
    cursor.execute("SELECT currency_code, rate_value, updated_at FROM exchange_rates")
    for (code, rate, time) in cursor.fetchall():
        # Using :< and :.4f to keep columns perfectly aligned
        print(f"{code:<12} | {float(rate):<15.4f} | {time}")
    
except mysql.connector.Error as err:
    print(f"Database Error: {err}")
    
finally:
    if 'db' in locals() and db.is_connected():
        cursor.close()
        db.close()
        print("-" * 55)
        print("MySQL connection closed.")
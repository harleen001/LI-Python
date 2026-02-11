import mysql.connector
import sys

try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",         
        password="123456", 
        database="college"
    )
    # 1. Use dictionary=True to avoid record[0], record[1], etc.
    cursor = db.cursor(dictionary=True)
    
    # Get the Roll No first
    value = int(input("\nWhich Rollno you want to update: "))

    # 2. Check if the key (Roll No) exists
    cursor.execute("SELECT * FROM result WHERE rollno = %s", (value,))
    record = cursor.fetchone()

    if record is None:
        print(f"Error: Rollno {value} is not present in the system.")
        db.close()
        sys.exit() # Exit immediately if not found

    # 3. If present, display current details using keys
    print("\n--- Current Details ---")
    for key, val in record.items():
        print(f"{key}: {val}")
    
    # 4. Ask which column to update
    print("\nWhat do you want to update?")
    print("1. Name | 2. English | 3. Math | 4. Science")
    choice = input("Enter choice (1-4): ")

    cols = {"1": "name", "2": "english", "3": "math", "4": "science"}
    
    if choice in cols:
        target_col = cols[choice]
        new_val = input(f"Enter new value for {target_col}: ")
        
        # 5. Perform the update on the base table
        update_query = f"UPDATE result SET {target_col} = %s WHERE rollno = %s"
        cursor.execute(update_query, (new_val, value))
        db.commit()
        
        print(f"\nSuccessfully updated {target_col}!")
        
        # 6. Show the final updated record
        cursor.execute("SELECT * FROM result WHERE rollno = %s", (value,))
        print("Updated Record:", cursor.fetchone())
    else:
        print("Invalid choice. No changes made.")

except mysql.connector.Error as err:
    print(f"Database Error: {err}")

finally:
    if 'db' in locals() and db.is_connected():
        cursor.close()
        db.close()
        print("\nMySQL connection closed.")
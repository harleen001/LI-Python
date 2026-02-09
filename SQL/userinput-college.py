import mysql.connector

try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",         
        password="123456", 
        database="college"
    )
    cursor = db.cursor()
    
    while True:
        value = int(input("Which Rollno you want to delete : "))

        query = "DELETE FROM result WHERE rollno = %s"    
        cursor.execute(query, (value,))
        
        db.commit()

        if cursor.rowcount == 0:
            print("Not present! Please enter a valid Rollno.")
    
        else:
            print(f"Successfully deleted rollno {value}")
            break 

    cursor.execute("SELECT * FROM result")
    result = cursor.fetchall()
    print("\nRemaining Records:")
    for row in result:
        print(row)

except mysql.connector.Error as err:
    print(f"Database Error: {err}")

finally:
    if 'db' in locals() and db.is_connected():
        cursor.close()
        db.close()
        print("\nMySQL connection closed.")
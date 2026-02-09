import mysql.connector

try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",         
        password="123456", 
        database="college"
    )
    cursor = db.cursor()
    
    cursor.execute("DROP VIEW IF EXISTS PercentageView")
    query = """
    CREATE VIEW PercentageView AS
    SELECT 
        rollno, 
        name, 
        (english + math + science + hindi + punjabi) AS total,
        ((english + math + science + hindi + punjabi) / 5) AS percentage
    FROM Result 
    """
    
    cursor.execute(query)
    cursor.execute("SELECT * from PercentageView")
    result = cursor.fetchall()
    for row in result:
        print(row)

except mysql.connector.Error as err:
    print(f"Database Error: {err}")

finally:
    if 'db' in locals() and db.is_connected():
        cursor.close()
        db.close()
        print("\nMySQL connection closed.")
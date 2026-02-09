import mysql.connector

try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",         
        password="123456", 
    )
    cursor = db.cursor()
    
    cursor.execute("""
    USE college;               
    INSERT INTO Result(rollno,name,english,math,science,hindi,punjabi)
    VALUES (1,'Iman',90,34,56,76,65),
       (2,'Kartik',80,64,76,66,85),
	   (3,'Harleen',90,64,76,46,65),
       (4,'Ankit',70,34,56,76,75),
       (5,'Anuj',40,34,56,76,95),
       (6,'Kanika',60,34,56,76,05),
       (7,'Taran',90,39,86,66,25),
       (8,'Prakash',30,54,45,36,55),
       (9,'Saloni',50,34,46,26,35),
       (10,'Prangani',03,13,06,09,15)         
    """)
    db.commit()

    cursor.execute("SELECT * FROM Result")
    result = cursor.fetchall()   
    print("\nCurrent Data in 'Result' table:")
    for x in result:
        print(x)

except mysql.connector.Error as err:
    print(f"Database Error: {err}")

finally:
    if 'db' in locals() and db.is_connected():
        cursor.close()
        db.close()
        print("\nMySQL connection closed.")
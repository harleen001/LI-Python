import mysql.connector

cnx = mysql.connector.connect(user='root', password='kartik',
                              host='127.0.0.1',
                              database='company')

cursor = cnx.cursor()
print("Connected")

Empid=input("Enter your Employee Id:")
Ename=input("Enter your name:")
Job=input("Enter your Job:")
Deptno=input("Enter your Department no:")
Sal=input("Enter your Salary:")

cursor.execute("select Empid from Employee where Empid=%s", (Empid,))
data = cursor.fetchall()
if not data:
        print ('Data entered successfully')
else:
        print ('ERROR:Employee ID already exists')
        exit()
# Insert new Employee
cursor.execute("""INSERT INTO Employee(Empid,Ename,Job,Deptno,Sal)
VALUES(%s,%s,%s,%s,%s)
""",(Empid,Ename,Job,Deptno,Sal))

# Make sure data is committed to the database
cnx.commit()
cursor.close()
cnx.close()
# importing mysql connector
import mysql.connector
# making Connection
cnx=mysql.connector.connect(user='root', password='kartik',
                              host='127.0.0.1',
                              database='Company')
cursor=cnx.cursor()
# Function To Check if Employee with given Empid Exist or Not
def Check_Employee(Empid):
    # Query to select all Rows from employee Table
    Query="SELECT * FROM Employee WHERE Empid=%s"
    # making cursor buffered to make rowcount method work properly
    cursor=cnx.cursor(buffered=True)
    data=(Empid,)
    # Executing the SQL Query
    cursor.execute(Query,data)
    # rowcount method to find
    # number of rows with given values
    r=cursor.rowcount
    if r==1:
        return True
    else:
        return False

# Function to Add Employee
def Add_Employee():
    Empid = input("Enter Employee Id : ")
    #Checking if Employee with given Empid Already Exist or Not
    if (Check_Employee(Empid)==True):
        print("Employee aready exists.\nTry Again\n")
        menu()
    else:
        Ename = input("Enter Employee Name : ")
        Job=input("Enter Employee Job : ")
        Deptno=input("Enter Employee Department no. : ")
        Sal=input("Enter Employee Salary : ")
        cursor=cnx.cursor()
        # Executing the SQL Query
        cursor.execute("""INSERT INTO Employee(Empid,Ename,Job,Deptno,Sal)
                VALUES(%s,%s,%s,%s,%s)
                """, (Empid, Ename, Job, Deptno, Sal))
        # commit() method to make changes in the table
        cnx.commit()
        print("Employee Added Successfully ")
        print("-----------------------------------")
        press=input("Press ENTER to Continue")
        menu()

# Function to Remove Employee with given Empid
def Delete_Employee():
    Empid = input("Enter Employee Id : ")
    # Checking if Employee with given Empid Exist or Not
    if (Check_Employee(Empid)==False):
        print("Employee does not exists\nTry Again\n")
        menu()
    else:
        # Query to Delete Employee from Table
        Query="DELETE FROM Employee WHERE Empid=%s"
        data=(Empid,)
        cursor=cnx.cursor()
        # Executing the SQL Query
        cursor.execute(Query,data)
        # commit() method to make changes in the table
        cnx.commit()
        print("Employee Removed")
        print("-----------------------------------")
        press = input("Press ENTER to Continue")
        menu()

# Function to Update Employee
def Update_Employee():
    Empid=int(input("Enter Employee ID:"))
    # Checking if Employee with given Empid Exist or Not
    if (Check_Employee(Empid)==False):
        print("Employee does not exists\nTry Again\n")
        menu()
    else:
        print("Employee Exist.")
        cursor = cnx.cursor()
        cursor.execute("SELECT * FROM Employee")
        show = cursor.fetchall()
        for i in show:
            a = str(i[0])
        if not show:
            print("Employee not Found.")
        else:
            upd_name=input("Enter New Employee Name:")
            upd_job=input("Enter New Employee Job:")
            upd_dept=input("Enter New Employee Department no.:")
            upd_sal=input("Enter New Employee Salary:")
            cursor.execute("SELECT * FROM employee")
            result = cursor.fetchall()
            updation = """UPDATE Employee SET Ename=%s,Job=%s,Deptno=%s,Sal=%s WHERE Empid=%s"""
            updated_data = (upd_name, upd_job, upd_dept, upd_sal, Empid)
            cursor.execute(updation, updated_data)
            print('Data updated successfully')
        cnx.commit()
    print("-----------------------------------")
    press = input("Press ENTER to Continue")
    menu()

#Function to Display All Employees from Employee Table
def Show_All():
    # query to select all rows from Employee Table
    Query="SELECT * FROM Employee"
    cursor=cnx.cursor()
    # Executing the SQL Query
    cursor.execute(Query)
    # Fetching all details of all the Employees
    r=cursor.fetchall()
    for i in r:
        print("Employee ID : ", i[0])
        print("Employee NAME : ", i[1])
        print("Employee Job : ", i[2])
        print("Employee Department no. : ", i[3])
        print("Employee Salary : ", i[4])
        print("-----------------------------------")
    if not r:
        print("No Data Available.")
    press = input("Press ENTER to Continue")
    menu()

def menu():
    print("MENU:")
    print("PRESS 1 TO ADD EMPLOYEE.")
    print("PRESS 2 TO DELETE EMPLOYEE.")
    print("PRESS 3 TO UPDATE EMPLOYEE.")
    print("PRESS 4 TO SHOW ALL EMPLOYEES.")
    print("PRESS 5 TO EXIT.")
    ch=int(input("Enter you choice:"))
    if ch==1:
        Add_Employee()
    elif ch==2:
        Delete_Employee()
    elif ch==3:
        Update_Employee()
    elif ch==4:
        Show_All()
    elif ch==5:
        exit(0)
    else:
        print("Invalid Choice\nTry Again")
        menu()


print("---------------EMPLOYEE MANAGEMENT SYSTEM---------------")
username = (input('Enter your username: '))
password = (input('Enter your password: '))
if(username=="Anurag" and password=="Vaid"):
    menu()
else:
    print("Invalid Username or Password.\nTry Again.")
    menu()
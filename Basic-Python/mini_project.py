for i in range(0, 100):
    import mysql.connector

    cnx = mysql.connector.connect(user='root', password='kartik',
                                  host='127.0.0.1',
                                  database='company')
    cursor = cnx.cursor()
    print(
        """Connected\nEnter 1 to Add Employee\nEnter 2 to Delete Employee\nEnter 3 to Update Employee\nEnter 4 to Show Employees\nEnter 5 to Exit.""")
    choice = int(input("Enter your choice = "))
    if choice == 1:
        Empid = input("Enter your Employee Id:")
        Ename = input("Enter your name:")
        Job = input("Enter your Job:")
        Deptno = input("Enter your Department no:")
        Sal = input("Enter your Salary:")
        cursor.execute("SELECT Empid FROM Employee WHERE Empid=%s", (Empid,))
        data = cursor.fetchall()
        if not data:
            print('Data entered successfully')
        else:
            print('ERROR:Employee ID already exists')
        cursor.execute("""INSERT INTO Employee(Empid,Ename,Job,Deptno,Sal)
        VALUES(%s,%s,%s,%s,%s)
        """, (Empid, Ename, Job, Deptno, Sal))

        cnx.commit()
        cursor.close()
        cnx.close()

    elif choice == 2:
        cursor.execute("SELECT * FROM Employee")
        show = cursor.fetchall()
        for i in show:
            a=str(i[0])
        Del_id = input("Enter your Employee Id you want to remove:")
        if not show:
            print("Database-Empty")
        elif Del_id not in a:
            print("No Such Employee Id exists")
        else:
            result = cursor.fetchall()
            deletion = ("DELETE FROM employee WHERE empid=%s")
            empid = Del_id
            cursor.execute(deletion, (empid,))
            print('Data deleted successfully')
        cnx.commit()
        cursor.close()
        cnx.close()

    elif choice == 3:
        cursor.execute("SELECT * FROM Employee")
        show = cursor.fetchall()
        for i in show:
            a=str(i[0])
        upd_id = input("Enter your Employee Id you want to update:")
        if not show:
            print("Database Empty")

        elif upd_id not in a :
            print("There is no such Employee Registered")

        else:
            upd_name = input("Enter updated Employee name = ")
            upd_job = input("Enter updated Employee job = ")
            upd_dept = input("Enter updated Employee dept = ")
            upd_sal = input("Enter updated Employee sal = ")
            cursor.execute("SELECT * FROM employee")
            result = cursor.fetchall()
            updation = """UPDATE employee SET ename=%s,job=%s,deptno=%s,sal=%s WHERE empid=%s"""
            updated_data = (upd_name, upd_job, upd_dept, upd_sal, upd_id)
            cursor.execute(updation, updated_data)
            print('Data updated successfully')
        cnx.commit()
        cursor.close()
        cnx.close()

    elif choice == 4:
        cursor.execute("SELECT * FROM employee")
        show = cursor.fetchall()
        if not show:
            print("There is no data in your table")
        else:
            for i in show:
                print("Employee ID : ", i[0])
                print("Employee NAME : ", i[1])
                print("Employee Job : ", i[2])
                print("Employee Department no. : ", i[3])
                print("Employee Salary : ", i[4])
                print("-----------------------------------")

        cnx.commit()
        cursor.close()
        cnx.close()

    elif choice == 5:
        exit(0)
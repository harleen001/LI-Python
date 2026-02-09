import pymysql
pymysql.install_as_MySQLdb()
Con = pymysql.Connect(host="127.0.0.1", port=3306, user="root", passwd="123456", db="college")
Cursor = Con.cursor()
sql = "SELECT * FROM result"
Cursor.execute(sql)
myrecord=Cursor.fetchall()

for i in myrecord:
    print(i)
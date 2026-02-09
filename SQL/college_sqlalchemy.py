from sqlalchemy import create_engine, text

engine = create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/college")
#DIALECT+driver,root,password,localhost,port,database_name

with engine.connect() as c:    #AUTOMATICALLY MAKES CONNECTION AND CLOSES AFTER EXECUTION

    sql = text("SELECT * FROM result")   #IN TEXT WRAPS FOR SAFETY FROM DATA LEAK, NO NEED TO CLOSE c.close()
    result = c.execute(sql)
    
    for row in result:
        print(row)